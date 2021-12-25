import requests
import time

def parsing():
    print("ВАЖНО!!! ФУНКЦИЯ НЕ ВЫПОЛНЯЕТ ФУНКЦЮ ПАРСИНГА!!! ВРЕМЕННО НЕ РАБОТАЕТ !!!\nСЛЕДИТЕ ЗА ОБНОВЛЕНИЯМИ")
    time.sleep(5)    
    domain = input("Введите домен: ")
    url = "https://"+domain+"/"
    response = requests.get(url)
#    time.sleep(3)
    output = input("\n 1. Вывести на экран \n 2. Сохранить данные в файл \n 3. Выход \n Выберите функцию вывода: \n  ")

    if output == "1":
        print(response.content)
    elif output == "2":
        out = open("some.txt", 'w')
        out.write(response.text)
        out.close()
    elif output == "3":
         return domain
