
from random import randint

win = "Ты Победил!"
lose = "Ты Проиграл."
rock, scissors, paper = "Камень", "Ножницы", "Бумага"
player_res, comp_res, tme = 0, 0, 0


def warning():
    return "Только цифры 1,2 и 3 !"


def rock_scissors():
    return "Камень тупит ножницы."


def rock_paper():
    return "Бумага обернет камень."


def scissors_paper():
    return "Ножницы разрезают бумагу"


while player_res != 3 and comp_res != 3:
    tme += 1
    comp = [rock, scissors, paper]
    # выбираем значение
    try:
        player_number = str(input(f"Введи цифру: \n1-{rock} \n2-{scissors} \n3-{paper}\n"))
        if int(player_number) == 0:
            print(warning())
            continue
        player = comp[int(player_number) - 1]
    except IndexError:
        print(warning())
        continue
    except ValueError:
        print(warning())
        continue

    print(f"Твой выбор: {player}")
    comp = comp[randint(0, 2)]
    print(f"Соперник выбрал: {comp}")
    if comp == player:
        print("Draw, nobody win!")
    else:
        if comp == rock:
            if comp == rock and player == scissors:
                print(f"{lose}", rock_scissors())
                comp_res += 1
            else:
                print(f"{win}", rock_paper())
                player_res += 1
        if comp == scissors:
            if comp == scissors and player == rock:
                print(f"{win}", rock_scissors())
                player_res += 1
            else:
                print(f"{lose}", scissors_paper())
                comp_res += 1

        if comp == paper:
            if comp == paper and player == rock:
                print(f"{lose}", rock_paper())
                comp_res += 1
            else:
                print(f"{win}", scissors_paper())
                player_res += 1
    print(f"Счет: Игрок - Компьютер {player_res} - {comp_res}")
    player, comp = [], []
if player_res == 3:
    print(f"Сокрушительная победа!!! Количество раундов для победы: {tme}")
else:
    print(f"Сокрушительное поражение! Попробуй еще раз. ")
