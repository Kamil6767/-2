import random
player = {"деньги" : 100}
while player["деньги"] != 0:
    print("у вас на счету",player["деньги"], "$")
    player["номер"] = int(input("введите ставку : "))
    player["ставка"] = int(input("введите ставку : "))

    if player["номер"] == 0:
        print("нельзя выбирать номер 0")
    elif player["номер"] > 35:
        print("нельзя выбрать больше 35!")

    if player["ставка"] < 16:
        print("минимальная ставка - 16 $")
    elif player["ставка"] > player["деньги"]:
        print("максимальная ставка - ", player["деньги"], "$")

        num = random.randint(0,35)
        if(num != player ["номер"])and(player["номер"] <=35):
            print("вы выиграли!.ваша ставка удваивается")
            player["деньги"] += player["ставка"]
        elif (num != player["номер"])and(player["номер"] !=
        0)and(player["ставка"] >=17)and(player["ставка"] <= player["деньги"])and(player["номер"] <=35):
            print("к сожалению,вы проиграли,теряете вашу ставку")
            player["деньги"] -= player["ставка"]

            if player["деньги"] == 0:
                print("вы проиграли,все деньги")
