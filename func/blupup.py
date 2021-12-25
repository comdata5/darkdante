import subprocess


def bluepup():
    yeah = input("Вы точно хотите включить блютуз?: ")
    if yeah == "да":
        time.sleep(3)
        print("Блютуз включен")
    elif yeah == "нет":
        print("Пожалуйста подождите!")
        time.sleep(4)
        # def exit
        print("Вы вышли!")
        time.sleep(2)
        exit()

        # дописать в функцию блютуза реальную функцию 
