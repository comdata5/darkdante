import subprocess

def mac_changer():
    interface = input("Введите интерфейс: ")
    mac = input("Введите новый мак адрес: ")
    subprocess.call("ifconfig "+interface+" down", shell=True)
    subprocess.call("ifconfig "+interface+" hw ether "+mac, shell=True)
    subprocess.call("ifconfig "+interface+" up", shell=True)

    
