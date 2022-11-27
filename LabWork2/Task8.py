bank = 0
dollar = True
currency = "Dollar"


def addToBankAccount(sum: float, bank: int):
    bank += sum
    return bank


def substractFromBankAccount(sum: float, bank: int):
    bank -= sum
    return bank


def moneyConversionToTenge(bank: float, dollar: bool):
    dollar = False
    bank *= 470
    return bank, dollar


def moneyConversionToDollar(bank: float, dollar: bool):
    dollar = True
    bank /= 470
    return bank, dollar



bank = addToBankAccount(300, bank)
bank = substractFromBankAccount(200, bank)
bank = moneyConversionToTenge(bank,dollar)[0]
dollar = moneyConversionToTenge(bank,dollar)[1]
bank = substractFromBankAccount(200, bank)


if not dollar:
    currency = "Tenge"
print(f'In your bank: {bank} {currency}')
