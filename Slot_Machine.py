import random

Simbols = ['🔴', '🟢', '🟡']

Columns = []
Column_01 = []
Column_02 = []
Column_03 = []

COLUMNS_LENGTH = 3
MIN_BET_LINES = 0
MAX_BET_LINES = 4
LOSE_FRASE = "Bad Luck"
WIN_FRASE = "Winner Winner!"


def Deposet():
    Coins = input("How Much Money Would You Like to Deposet : $")
    if not Coins:
        Coins = input("You Must Type How Much Money to Deposet : $")

    if Coins.isdigit() == False:
        Coins = input("How Much Money Must be a Number : $")

    Balance = int(Coins)
    print(f'Your Balance is {Balance}')

    return Balance


def Get_Bet_Lines(Balance):
    Bet_Lines = input("How Many Lines to Bet on (1-3) : ")
    if not Bet_Lines:
        Bet_Lines = input("You Must Type How Many Lines to Bet on : ")

    if MIN_BET_LINES <= int(Bet_Lines) <= MAX_BET_LINES:
        Bet_Lines = input("You Must ")

    if Bet_Lines.isdigit() == False:
        Bet_Lines = input("How Many Bet_Lines Must be a Number : ")

    Bet_Money = input("How Much Would You Like To Bet on Each Line : $")
    if not Bet_Money:
        Bet_Money = input(
            "You Must Type How Much Would You Like To Bet on Each Line : $")

    if Bet_Money.isdigit() == False:
        Bet_Money = input("How Much Money Must be a Number : $")

    Total_Bet_Money = int(Bet_Lines) * int(Bet_Money)

    if Total_Bet_Money > int(Balance):
        print(
            f"You Don't Have Enough Money To Bet, Your Current Balance is {Balance}$")
    else:
        print(
            f"You are Betting {Bet_Money}$ on {Bet_Lines}, Total Bet is {Total_Bet_Money}$")

    return Bet_Lines, Total_Bet_Money


def Slot_Spin(Balance, Bet_Lines, Total_Bet_Money):
    for j in range(COLUMNS_LENGTH):

        for i in range(COLUMNS_LENGTH):
            number = random.choice(Simbols)
            Columns.append(number)

            if j == 0:
                Column_01.append(number)
            if j == 1:
                Column_02.append(number)
            if j == 2:
                Column_03.append(number)

            if i < COLUMNS_LENGTH - 1:
                print(Columns[i], end=' | ')
            else:
                print(Columns[i], end='')

        print()
        Columns.clear()

    Check_Winning(Balance, Bet_Lines, Total_Bet_Money)


def Check_Winning(Balance, Bet_Lines, Total_Bet_Money):
    Check_01, Check_02, Check_03 = False, False, False

    if Column_01[0] == Column_01[1] == Column_01[2]:
        Check_01 = True

    if Column_02[0] == Column_02[1] == Column_02[2]:
        Check_02 = True

    if Column_03[0] == Column_03[1] == Column_03[2]:
        Check_03 = True

    if Bet_Lines == '1':
        if Check_01 == True:
            print(WIN_FRASE)
            Balance += Total_Bet_Money
        else:
            print(LOSE_FRASE)
            Balance -= Total_Bet_Money

    if Bet_Lines == '2':
        if Check_01 == True and Check_02 == True:
            print(f"{WIN_FRASE} \n")
            Balance += Total_Bet_Money
        else:
            print(f"{LOSE_FRASE} \n")
            Balance -= Total_Bet_Money

    if Bet_Lines == '3':
        if Check_01 == True and Check_02 == True and Check_03 == True:
            print(WIN_FRASE)
            Balance += Total_Bet_Money
        else:
            print(LOSE_FRASE)
            Balance -= Total_Bet_Money

    Column_01.clear()
    Column_02.clear()
    Column_03.clear()

    print(f"Your Current Balance is {Balance}")

    Play_Again = input("Press (1) to Play Again (q)\n ")

    if Play_Again == '1':
        if Balance < Total_Bet_Money:
            print(
                f"Sorry, You Don't Have Enough Money To Bet, Your Current Balance is {Balance}$")
        else:
            Slot_Spin(Balance, Bet_Lines, Total_Bet_Money)


def Main():
    Balance = Deposet()
    Bet_Lines, Total_Bet_Money = Get_Bet_Lines(Balance)
    Slot_Spin(Balance, Bet_Lines, Total_Bet_Money)


Main()
