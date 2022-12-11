from enum import Enum
from typing import List


class WalletType(Enum):
    KZT = 'KZT'
    USD = 'USD'
    EUR = 'EUR'


class Wallet:
    cash_amount: int
    wallet_type: WalletType

    def __init__(self, cash_amount: int, wallet_type: WalletType):
        self.wallet_type = wallet_type
        self.cash_amount = cash_amount


class User:
    username: str
    password: str
    wallets: Wallet
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.wallets = Wallet(cash_amount=0, wallet_type='KZT')

    def toString(self) -> str:
        return "Вы вошли как "+self.username

        
    

users: List[User] = []
    
def addToBankAccount(user: User, cash):
    user.wallets.cash_amount += cash
    
def substractFromBankAccount(user: User, cash):
    if user.wallets.cash_amount >= cash:
        user.wallets.cash_amount -= cash
    else:
        print("Недостаточно денег на счету")

def moneyConversion(user: User, typeOfCash: str):
    print(typeOfCash)
    match user.wallets.wallet_type, typeOfCash:
        case "USD", "KZT":
            user.wallets.cash_amount *= 470
            user.wallets.wallet_type = 'KZT'
        
        case "USD", "EUR":
            user.wallets.cash_amount /= 1.05
            user.wallets.wallet_type = 'EUR'
            
        case "KZT", "USD":
            user.wallets.cash_amount /= 470
            user.wallets.wallet_type = 'USD'
            
        case "KZT", "EUR":
            user.wallets.cash_amount /= 500
            user.wallets.wallet_type = 'EUR'
            
        case "EUR", "KZT":
            user.wallets.cash_amount *= 500
            user.wallets.wallet_type = 'KZT'
            
        case "EUR", "USD":
            user.wallets.cash_amount *= 1.05
            user.wallets.wallet_type = 'USD'
            



def create_user(username: str, password: str):
    user = User(username=username, password=password)
    users.append(user)


def get_user(self, username: str, password: str):
    user = None
    for i in range(len(users)):
        if users[i].username == username and users[i].password == password:
            user = users[i]
            break
    return user.username

def checkUser(username: str, password: str):
    user = None
    for i in range(len(users)):
        if users[i].username == username and users[i].password == password:
            user = users[i]
            break
    return user


while(True):
    print("Выберите ваше действие:")
    print("1. Создание пользователя")
    print("2. Вход в аккаунт")
    print("0. Выйти")
    action = int(input())
    print()
    if action == 1:
        username, password = input("Имя и пароль: ").split(" ")
        create_user(username=username, password=password)
        print("Пользователь "+username+" создан")
    if action == 2:
        username, password = input("Имя и пароль: ").split(" ")
        user = checkUser(username=username, password=password)
        if user == None:
            print("Такого пользователя не существует")
        else:
            print()
            print(user.toString())
            while(True):
                print(user.username+ " на вашем счету: " + str(user.wallets.cash_amount)+" "+str(user.wallets.wallet_type))
                print()
                print("Выберите ваше действие:")
                print("1. Добавить деньги в банк")
                print("2. Взять деньги с банка")
                print("3. Перевести счет на другую валюту")
                print("4. Удалить аккаунт")
                print("0. Выйти")
                deistvie =  int(input())
                if deistvie == 0:
                    break
                if deistvie == 1:
                    cash = int(input("Введите сумму которую хотите внести: "))
                    addToBankAccount(user, cash)
                if deistvie == 2:
                    cash = int(input("Введите сумму которую хотите снять: "))
                    substractFromBankAccount(user, cash)
                if deistvie == 3:
                    typeOfConv = str(input("На какую валюту хотите перевести? (USD, KZT, EUR): "))
                    moneyConversion(user, typeOfConv)
                if deistvie == 4:
                    users.remove(user)
                    break
                
                print()
    if action == 0:
        print("До свидания")
        break
    print()







