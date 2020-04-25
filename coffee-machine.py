class CoffeeMachine:

    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def __str__(self):
        """prints coffee machine state of resources"""
        return ('The coffee machine has: \n{} of water \n{} of milk \n{} of coffee beans \n{} of disposable cups \n{} of money'.format(self.water, self.milk, self.beans, self.cups, self.money))

    def fill(self):
        fill_water = int(input('Write how many ml of water would you like to add:'))
        fill_milk = int(input('Write how many ml of milk would you like to add:'))
        fill_beans = int(input('Write how many grams of coffee beans would you like to add:'))
        fill_cups = int(input('Write how many disposable cups of coffee do you want to add:'))
        self.water += fill_water
        self.milk += fill_milk
        self.beans += fill_beans
        self.cups += fill_cups

    def take(self):
        """extracts all money from the coffee machine"""
        print(f'I gave you ${str(self.money)}')
        self.money = 0

    def buy(self):
        """user options are 3 types of coffee or back to main menu."""
        espresso = [250, 0, 16, 1, 4]
        latte = [350, 75, 20, 1, 7]
        capuccino = [200, 100, 12, 1, 6]
        while True:
            option = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
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
        """updates coffee machine resources"""
        water, milk, beans, cups, money = coffee[0], coffee[1], coffee[2], coffee[3], coffee[4]
        self.water -= water
        self.milk -= milk
        self.beans -= beans
        self.cups -= cups
        self.money += money

    def check_resources(self, coffee):
        """checks if coffee machine resources are sufficient"""
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


# MAIN
# instantiate
coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)

# interactive loop
while True:
    user_input = input('Write action (buy, fill, take, remaining, exit):')
    if user_input == 'buy':
        coffee_machine.buy()
    elif user_input == 'fill':
        coffee_machine.fill()
    elif user_input == 'take':
        coffee_machine.take()
    elif user_input == 'remaining':
        print(coffee_machine)
    elif user_input == 'exit':
        break
    else:
        print('Invalid input...')
