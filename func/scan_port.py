import subprocess

# Функция скана портом(nmap)

def scan_port():
    # фукнция скачать nmap

    opera = input(" 1. Показать всю информацию о сервере \n 2. Скан определенного порта \n  3. Выход \n Выберите функцию: \n ")
    
    if opera == "1":
        ipadr = input("Введите домен/айпи цели: ")
        subprocess.call("nmap "+ipadr, shell=True)
    elif opera == "2":
        ipadr = input("Введите домен/айпи цели: ")
        port = input("Введите порт(ы): ")
        subprocess.call("nmap -p " +port + " " + ipadr, shell=True)
    elif opera == "3":
        input("Нажмите энтер чтобы выйти......")
