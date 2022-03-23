money = input('Please enter the money you have in account: ')
print('You have $' + str(money))

choices = input('Are you ready to play the game of choices: Y/N ')

class WM:
    def __init__(self, amount): 
        self.amount = amount
        m1 = (money - self.amount)
        print(m1)
        