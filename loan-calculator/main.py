"""
This program may also be run from terminal.
examples:
    --type diff --principal 1000000 --period 10 --interest 10
    --type=diff --principal=500000 --periods=8 --interest=7.8
    --type=annuity --principal=1000000 --periods=60 --interest=10
    --type=annuity --payment=8722 --periods=120 --interest=5.6
    --type=annuity --principal=500000 --payment=23000 --interest=7.8

see controller.parse_credit_information()
"""

import controller


if __name__ == "__main__":
    introduction = '''Personal finances are an important part of life. 
Sometimes you need some extra money and decide to take a loan, or you want to buy a house using a mortgage.
To make an informed decision, you need to be able to calculate different financial parameters. 

'''
    print(introduction)
    controller.run()
