import math


class CreditCalculator:
    """
    Credit calculator computing different financial parameters.

    :ivar information: A dictionary in the form: {'principal': None, 'diff_payment': [], 'payment': None, 'n_months': None, 'interest': None}
        information['principal']: credit principal
        information['diff_payment']: differentiated payment
        information['payment']: annuity payment
        information['n_months']: repayment period in months
        information['interest']: nominal interest
    :ivar overpayment: amount to be overpaid after repaying credit
    """

    def __init__(self, information):
        self.information = information
        self.overpayment = None

    def calculate(self):
        """
        Find which is the missing info, calculate it and display info (given the rest of info are complete).
        """
        p = self.information['principal']  # credit principal
        a = self.information['payment']  # annuity payment
        i = self.information['interest'] / 1200  # nominal interest = 1/12 of annual interest (converted from percentage)
        n = self.information['n_months']  # repayment period in months
        missing_info = None
        for info, value in self.information.items():
            if value == 'target':
                missing_info = info
                break
        assert missing_info is not None
        if missing_info == 'n_months':
            self.__calc_months(p, a, i)
        elif missing_info == 'payment':
            self.__calc_annuity_payment(p, i, n)
        elif missing_info == 'principal':
            self.__calc_principal(a, i, n)
        elif missing_info == 'diff_payment':
            self.__calc_differentiated_payment(p, i, n)
    
    def __calc_months(self, p, a, i):
        """
        Helper of calculate().
        Calculate and set the repayment period in months. Print results.
        """
        n = math.ceil(math.log((a / (a - i * p)), i + 1))  # repayment period in months
        self.information['n_months'] = n
        self.overpayment = math.ceil(a * n - p)
        print('\n' + self.__human_readable_period(n))
        print(f'Overpayment = {self.overpayment}')
    
    def __calc_annuity_payment(self, p, i, n):
        """
        Helper of calculate().
        Calculate and set the annuity payment. Print results.
        """
        a = math.ceil((p * i * (1 + i)**n) / ((1 + i)**n - 1))  # annuity payment
        self.information['payment'] = a
        self.overpayment = math.ceil(a * n - p)
        print(f'\nAnnuity payment = {a}')
        print(f'Overpayment = {self.overpayment}')
    
    def __calc_principal(self, a, i, n):
        """
        Helper of calculate().
        Calculate and set the credit principal. Print results.
        """
        p = round(a / ((i * (1 + i)**n) / ((1 + i)**n - 1)))
        self.information['principal'] = p
        self.overpayment = math.ceil(a * n - p)
        print(f'\nCredit principal = {p}')
        print(f'Overpayment = {self.overpayment}')
    
    def __calc_differentiated_payment(self, p, i, n):
        """
        Helper of calculate().
        Calculate and set the differentiated payment. Print results.
        """
        dm = []  # differentiated payment (monthly list)
        for m in range(1, n + 1):  # m is current month
            amount = math.ceil(p / n + i * (p - (p * (m - 1)) / n))
            dm.append(amount)
        self.information['diff_payment'] = dm
        self.overpayment = math.ceil(sum(dm) - p)
        print()
        for m_payment in self.__human_readable_diff(dm):
            print(m_payment)
        print(f'Overpayment = {self.overpayment}')

    def __human_readable_diff(self, dm):
        """
        Helper of __calc_differentiated_payment().
        :param dm: a monthly list of differentiated payments.
        :yield: each of the payments in a human readable format.
        """
        for i in range(len(dm)):
            yield f'Month {i + 1}: paid out {dm[i]}'

    def __human_readable_period(self, months):
        """
        Helper of __calc_months(). Converts count of months to count of years and months.
        :param months: amount of months to repay credit.
        :return: a string of information
        """
        years = 0
        months = math.ceil(months)
        # 1 or more years
        if months > 12:
            years = months // 12
            months = months % 12
            if (1 < years) and (1 < months):
                return f'You need {years} years and {months} months to repay this credit!'
            elif 1 == years:
                if 0 == months:
                    return f'You need {years} years to repay this credit!'
                elif 1 == months:
                    return f'You need {years} year and {months} month to repay this credit!'
                else:
                    return f'You need {years} year and {months} months to repay this credit!'
            elif 1 == months:
                if 1 == years:
                    return f'You need {years} year and {months} month to repay this credit!'
                else:
                    return f'You need {years} years and {months} month to repay this credit!'
            else:
                return f'You need {years} years to repay this credit!'
        # 0 years, 1 month
        elif months == 1:
            return f'You need {months} month to repay this credit!'
        # 0 years
        else:
            return f'You need {months} months to repay this credit!'
