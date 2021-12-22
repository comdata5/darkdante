#      Author comdata5      # 
import requests
import time
import subprocess

chooseOperations = input("\n 1. Парсинг \n 2. Сменить мак адрес \n 3. Просканировать на порты \n 4. Выход \n Выберите операцию : ")

# Функция парсинга

def parsing():
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
    
# Функция смены мак адреса

def mac_changer():
    interface = input("Введите интерфейс: ")
    mac = input("Введите новый мак адрес: ")
    subprocess.call("ifconfig "+interface+" down", shell=True)
    subprocess.call("ifconfig "+interface+" hw ether "+mac, shell=True)
    subprocess.call("ifconfig "+interface+" up", shell=True)
    

# Функция скана портом(nmap)

def scan_port():
    opera = input(" 1. Показать всю информацию о сервере \n 2. Скан определенного порта \n 3. Сканирование списка/сетей из файла \n 4. Выход \n Выберите функцию: \n ")
    
    if opera == "1":
        ipadr = input("Введите домен/айпи цели: ")
        subprocess.call("nmap "+ipadr, shell=True)
    elif opera == "2":
        ipadr = input("Введите домен/айпи цели: ")
        port = input("Введите порт(ы): ")
        subprocess.call("nmap -p " +port + " " + ipadr, shell=True)
    elif opera == "3":
        print("Временно в разработке....")
        # fileRead = input("Укажите название файла: ")
        # roadFile = open(fileRead,"r")
        # subprocess.call("nmap -iL "+ roadFile)
    elif opera == "4":
        input("Нажмите энтер чтобы выйти......")
            
# $ nmap -iL input.txt        
    
if chooseOperations == "1":
    parsing()
elif chooseOperations == "2":
    mac_changer()
elif chooseOperations == "3":
    scan_port()
else:
    input("Чтобы выйти нажмите Enter: ")
    print("Вы вышли....")
