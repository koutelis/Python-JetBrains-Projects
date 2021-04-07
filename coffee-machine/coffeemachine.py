

class CoffeeMachine:

    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def __str__(self):
        """:return: coffee machine state of resources"""
        output = f'The coffee machine has: \n{self.water} of water \n{self.milk} of milk \n'
        output += f'{self.beans} of coffee beans \n{self.cups} of disposable cups \n{self.money} of money'
        return output

    def fill(self):
        fill_water = int(input('Write how many ml of water would you like to add: '))
        fill_milk = int(input('Write how many ml of milk would you like to add: '))
        fill_beans = int(input('Write how many grams of coffee beans would you like to add: '))
        fill_cups = int(input('Write how many disposable cups of coffee do you want to add: '))
        self.water += fill_water
        self.milk += fill_milk
        self.beans += fill_beans
        self.cups += fill_cups

    def take(self):
        """Extract all money from the coffee machine"""
        print(f'I gave you ${str(self.money)}')
        self.money = 0

    def buy(self):
        """User options are 3 types of coffee or back to main menu."""
        espresso = [250, 0, 16, 1, 4]
        latte = [350, 75, 20, 1, 7]
        capuccino = [200, 100, 12, 1, 6]
        while True:
            option = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ')
            if (option == '1'):
                if self.check_resources(espresso):
                    self.make_coffee(espresso)
                break
            elif (option == '2'):
                if self.check_resources(latte):
                    self.make_coffee(latte)
                break
            elif (option == '3'):
                if self.check_resources(capuccino):
                    self.make_coffee(capuccino)
                break
            elif (option == 'back'):
                break
            else:
                print('Invalid input...')

    def make_coffee(self, coffee):
        """Update coffee machine resources"""
        water, milk, beans, cups, money = coffee[0], coffee[1], coffee[2], coffee[3], coffee[4]
        self.water -= water
        self.milk -= milk
        self.beans -= beans
        self.cups -= cups
        self.money += money

    def check_resources(self, coffee):
        """Check if coffee machine resources are sufficient"""
        water, milk, beans, cups, money = coffee[0], coffee[1], coffee[2], coffee[3], coffee[4]
        if self.water < water:
            print('Sorry, not enough water!')
        elif self.milk < milk:
            print('Sorry, not enough milk!')
        elif self.beans < beans:
            print('Sorry, not enough coffee beans!')
        elif self.cups < cups:
            print('Sorry, not enough cups!')
        else:
            print('I have enough resources, making you a coffee!')
            return True
        return False
    
    def control(self):
        """Run this method to operate the coffee machine"""
        active = True
        while active:
            user_input = input('Write action (buy, fill, take, remaining, exit): ')
            if user_input == 'buy':
                self.buy()
            elif user_input == 'fill':
                self.fill()
            elif user_input == 'take':
                self.take()
            elif user_input == 'remaining':
                print(self)
            elif user_input == 'exit':
                active = False
            else:
                print('Invalid input...')
