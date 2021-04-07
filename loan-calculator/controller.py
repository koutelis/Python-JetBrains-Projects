from creditcalculator import CreditCalculator
import argparse


def menu():
    """
    Ask user which credit information needs to be calculated.
    :return: a credit target info (string)
    """
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


def input_credit_information(target_info):
    """
    Receive user input to retrieve necessary information about the credit except target_info.
    :param target_info: Information that needs to be calculated.
    :return: A CreditCalculator object.
    """
    information = {'principal': None, 'diff_payment': None, 'payment': None, 'n_months': None, 'interest': None}
    
    if target_info == 'diff_payment':
        information['payment'] = 0
    else:
        information['diff_payment'] = 0
    information[target_info] = 'target'

    if information['principal'] is None:
        print('Enter credit principal:')
        information['principal'] = float(input())
    if information['payment'] is None:
        print('Enter monthly payment:')
        information['payment'] = float(input())
    if information['n_months'] is None:
        print('Enter count of periods:')
        information['n_months'] = int(input())
    if information['interest'] is None:
        print('Enter credit interest percentage without the sign (%):')
        information['interest'] = float(input())

    return CreditCalculator(information)


def parse_credit_information():
    """
    Receive user input from terminal to retrieve necessary information about the credit.
    :return: A CreditCalculator object.

    examples:
        --type diff --principal 1000000 --period 10 --interest 10
        --type=diff --principal=500000 --periods=8 --interest=7.8
        --type=annuity --principal=1000000 --periods=60 --interest=10
        --type=annuity --payment=8722 --periods=120 --interest=5.6
        --type=annuity --principal=500000 --payment=23000 --interest=7.8
    """
    # argparser reads input from terminal
    parser = argparse.ArgumentParser(description='Credit calculator')
    parser.add_argument('--type', type=str, default=None, help="'diff' for differential payments |'annuity' for annuity paments")  # required
    parser.add_argument('--payment', type=float, default=None, help='Enter (positive) monthly payment')  # watch out for combination with diff
    parser.add_argument('--principal', type=float, default=None, help='Enter (positive) principal credit value')
    parser.add_argument('--periods', type=int, default=None, help='Enter number of months to repay credit')  # positive integer, number of months
    parser.add_argument('--interest', type=float, default=None, help='Enter interest without the percentage sign')  # required
    args = parser.parse_args()

    if args.type is None:
        return None

    information = None
    # calculations
    if (args.type == 'diff') and all(num > 0 for num in [args.principal, args.periods, args.interest]) and (args.payment == None):
        information = {'principal': args.principal, 'payment': 0, 'diff_payment': 'target', 'n_months': args.periods, 'interest': args.interest}
    elif (args.type == 'annuity'):
        if all(num > 0 for num in [args.payment, args.principal, args.interest]):
            information = {'principal': args.principal, 'payment': args.payment, 'diff_payment': 0, 'n_months': 'target', 'interest': args.interest}
        elif all(num > 0 for num in [args.payment, args.periods, args.interest]):
            information = {'principal': 'target', 'payment': args.payment, 'diff_payment': 0, 'n_months': args.periods, 'interest': args.interest}
        elif all(num > 0 for num in [args.principal, args.periods, args.interest]):
            credit.information = {'principal': args.principal, 'payment': 'target', 'diff_payment': 0, 'n_months': args.periods, 'interest': args.interest}
        else:
            print('Incorrect parameters')
    else:
        print('Incorrect parameters')
    
    if information is not None:
        return CreditCalculator(information)


def run():
    """Run this function to start a credit calculator"""
    calc = parse_credit_information()
    if calc is None:
        target_info = menu()
        calc = input_credit_information(target_info)
    calc.calculate()
