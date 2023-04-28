class Account:
    '''
    This method will initialize the Account object.

    :param name: Takes name of the user to be stored in the Account object
    '''

    def __init__(self, name: str):
        self.__account_name = name
        self.__account_balance = 0

    '''
    This method will deposit money into the account. If the amount is negative or zero, it will return False and nothing will happen.
    If the amount is greater than zero, it will add to the account balance

    :param amount: amount of money being deposited into the account
    :return: True or False of the account depending on the amount
    '''

    def deposit(self, amount: str) -> bool:
        if float(amount) > 0:
            self.__account_balance += float(amount)
            return True
        else:
            return False

    '''
    This method will withdraw money from the account. If the amount being withdrawn is negative or greater than the balance of the account then nothing will happen.
    Otherwise the amount that is being withdrawn will subtracted from the account balance.

    :param amount: amount of money being withdrawn from the account
    :return: True or False if money was withdrawn
    '''

    def withdraw(self, amount: str) -> bool:
        if float(amount) < self.__account_balance and float(amount) > 0:
            self.__account_balance -= float(amount)
            return True
        else:
            return False

    '''
    Will return the amount of money in the account

    :return: value of the account
    '''

    def get_balance(self) -> float:
        return self.__account_balance

    '''
    Will return the name in the account

    :return: name of the account
    '''

    def get_name(self) -> str:
        return self.__account_name
