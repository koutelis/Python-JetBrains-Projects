# write your code here
import math

class Credit:

    information = {'principal': None, 'diff_payment': [], 'payment': None, 'n_months': None, 'interest': None}

    def __init__(self):
        self.information = Credit.information

    def get_information(self, info):
        if info == 'diff_payment':
            self.information['payment'] = 0
        else:
            self.information[info] = 0

        if self.information['principal'] == None:
            print('Enter credit principal:')
            self.information['principal'] = float(input())
        if self.information['payment'] == None:
            print('Enter monthly payment:')
            self.information['payment'] = float(input())
        if self.information['n_months'] == None:
            print('Enter count of periods:')
            self.information['n_months'] = int(input())
        if self.information['interest'] == None:
            print('Enter credit interest percentage without the sign (%):')
            self.information['interest'] = float(input())

    def calculate(self, info):
        P = self.information['principal']  # credit principal
        A = self.information['payment']  # annuity payment
        Dm = self.information['diff_payment']  # differentiated payment list per month
        n = self.information['n_months']  # repayment period in months
        i = self.information['interest'] / 1200  # nominal interest = 1/12 of annual interest (converted from percentage)
        print()
        if info == 'n_months':
            n = math.ceil(math.log((A / (A - i * P)), i + 1))
            self.information['n_months'] = n
            self.overpayment = math.ceil(A * n - P)
            print(self.human_readable_period(n))
        elif info == 'payment':
            A = math.ceil((P * i * (1 + i)**n) / ((1 + i)**n - 1))
            self.information['payment'] = A
            self.overpayment = math.ceil(A * n - P)
            print(f'Annuity payment = {A}')
        elif info == 'principal':
            P = round(A / ((i * (1 + i)**n) / ((1 + i)**n - 1)))
            self.information['principal'] = P
            self.overpayment = math.ceil(A * n - P)
            print(f'Credit principal = {P}')
        elif info == 'diff_payment':
            for m in range(1, n + 1):  # m = current month
                amount = math.ceil(P / n + i * (P - (P * (m - 1)) / n))
                Dm.append(amount)
            self.information['diff_payment'] = Dm
            self.overpayment = math.ceil(sum(Dm) - P)
            for m_payment in self.human_readable_diff(Dm):
                print(m_payment)
        # overpayment for all cases
        print(f'Overpayment = {self.overpayment}')


    def human_readable_diff(self, m):
        for i in range(len(m)):
            yield f'Month {i + 1}: paid out {m[i]}'


    def human_readable_period(self, months):
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


def what_info():
    while True:
        print('What do you want to calculate?')
        print('type "d" - for differentiated monthly payment,')
        print('type "a" - for annuity monthly payment,')
        print('type "p" - for credit principal:')
        print('type "n" - for count of months,')
        user_option = input()
        if user_option == 'd':
            return 'diff_payment'
        elif user_option == 'a':
            return 'payment'
        elif user_option == 'p':
            return 'principal'
        elif user_option == 'n':
            return 'n_months'
        else:
            print('Invalid input')


# init
credit = Credit()
# calculate specified info
info = what_info()
credit.get_information(info)
credit.calculate(info)
