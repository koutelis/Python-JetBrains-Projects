# write your code here
import argparse
import math

class Credit:

    information = {'principal': None, 'payment': None, 'diff_payment': [], 'n_months': None, 'interest': None}

    def __init__(self):
        self.information = Credit.information


    def calculate(self, info):
        P = self.information['principal']  # credit principal
        A = self.information['payment']  # annuity payment
        Dm = self.information['diff_payment']  # differentiated payment list per month
        n = self.information['n_months']  # repayment period in months
        i = self.information['interest'] / 1200  # nominal interest = 1/12 of annual interest (converted from percentage)
        if info == 'n_months':
            n = math.ceil(math.log((A / (A - i * P)), i + 1))
            self.information['n_months'] = n
            self.overpayment = math.ceil(A * n - P)
            print(self.human_readable_period(n))
        elif info == 'payment':
            A = math.ceil((P * i * (1 + i)**n) / ((1 + i)**n - 1))
            self.information['payment'] = A
            self.overpayment = math.ceil(A * n - P)
            print(f'Your annuity payment = {A}!')
        elif info == 'principal':
            P = math.ceil(A / ((i * (1 + i)**n) / ((1 + i)**n - 1)))
            self.information['principal'] = P
            self.overpayment = math.ceil(A * n - P)
            print(f'Your credit principal = {P}!')
        elif info == 'diff_payment':
            for m in range(1, n + 1):  # m = current month
                amount = math.ceil(P / n + i * (P - (P * (m - 1)) / n))
                Dm.append(amount)
            self.information['diff_payment'] = Dm
            self.overpayment = math.ceil(sum(Dm) - P)
            for m_payment in self.human_readable_diff(Dm):
                print(m_payment)
        # overpayment for all cases
        print(f'\nOverpayment = {self.overpayment}')


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


# init
credit = Credit()

# argparser reads input from terminal
parser = argparse.ArgumentParser(description='Credit calculator')
parser.add_argument('--type', type=str, help="'diff' for differential payments |'annuity' for annuity paments")  # required
parser.add_argument('--payment', type=float, default=0, help='Enter (positive) monthly payment')  # watch out for combination with diff
parser.add_argument('--principal', type=float, default=0, help='Enter (positive) principal credit value')
parser.add_argument('--periods', type=int, default=0, help='Enter number of months to repay credit')  # positive integer, number of months
parser.add_argument('--interest', type=float, default=0, help='Enter interest without the percentage sign')  # required
args = parser.parse_args()

# calculations
if (args.type == 'diff') and all(num > 0 for num in [args.principal, args.periods, args.interest]) and (args.payment == 0):
    credit.information = {'principal': args.principal, 'payment': None, 'diff_payment': [], 'n_months': args.periods, 'interest': args.interest}
    credit.calculate('diff_payment')
elif (args.type == 'annuity'):
    if all(num > 0 for num in [args.payment, args.principal, args.interest]):
        credit.information = {'principal': args.principal, 'payment': args.payment, 'diff_payment': [], 'n_months': None, 'interest': args.interest}
        credit.calculate('n_months')
    elif all(num > 0 for num in [args.payment, args.periods, args.interest]):
        credit.information = {'principal': None, 'payment': args.payment, 'diff_payment': [], 'n_months': args.periods, 'interest': args.interest}
        credit.calculate('principal')
    elif all(num > 0 for num in [args.principal, args.periods, args.interest]):
        credit.information = {'principal': args.principal, 'payment': None, 'diff_payment': [], 'n_months': args.periods, 'interest': args.interest}
        credit.calculate('payment')
    else:
        print('Incorrect parameters')
else:
    print('Incorrect parameters')
