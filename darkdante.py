from modules_connect import * 

logo = """

******************************************************************************************************************************
*  This tool was written by the coder comdata5                                                                               *
*  GitHub : https://github.com/comdata5                                                                                      *
*  Telegram : @oakoak_draw                                                                                                   *
*  Vkontakte : @all_of_comdata                                                                                               *
*  Xss.is : @darkdantez                                                                                                      *
*  You know, people do that sometimes.    They are trying to silence those who ask questions                                 *
******************************************************************************************************************************
"""

print(logo)

#time.sleep(3)



chooseOperations = input("\n 1. Парсинг \n 2. Сменить мак адрес \n 3. Просканировать на порты \n 4. Запустить бомбер \n 5. Взлом камер \n 6. Настройки блютуз \n 7. Выход \n Выберите операцию : ")


        
if chooseOperations == "1":
    parsing()
elif chooseOperations == "2":
    mac_changer()
elif chooseOperations == "3":
    scan_port()
elif chooseOperations == "4":
    bomber()
elif chooseOperations == "5":
    cam_hackers_country()
elif chooseOperations == "6":
    bluepup()
else:
    exit()
    
