import functions
import colorama
import importlib
functions.start()
while True:
    t = input(colorama.Fore.RESET+colorama.Style.BRIGHT+colorama.Back.RESET+"💣️H.A.C.K...S.T.A.L.K.E.R💣️ ")
    if "ddos" in t.lower():
        url = input("💣️URL💣️ ")
        functions.ddos(url)
        print()
    elif t  == "secmail" in t.lower():
        functions.secmail()
    elif "parsing" in t.lower():
        ssylka = input("💣️URL💣️ ")
        functions.parsing(ssylka)
    elif "exit" in t.lower() or "quit" in t.lower():
        exit("💣️Выход из программы...💣️")
    elif "gpt" in t.lower():
        ask = input("💣️Введите запрос💣️ ")
        functions.gpt(ask)
    elif "fork" in t.lower():
        functions.fork()
    elif "click" in t.lower():
        click = input("💣Кнопка мыши(1 - левая, 2 - правая)💣 ")
        if click == "1" or "left":
            functions.click_left()
        elif click == "2" or "right":
            functions.click_right()    
    elif "console" in t.lower():
        console = input("💣Команда💣 ")
        functions.console(console)
    elif "clear" in t.lower():
        print("\033[H\033[J", end = "")
    elif "phone" in t.lower():
        httpweb_number = functions.HttpWebNumber()
        httpweb_number.print_number_results
    elif "ip" in t.lower():
        ip_1 = input("💣️IP💣️ ")
        functions.get_info_ip(ip_1)
        functions.get_info(ip_1)
    elif "999" in t.lower():
        i = 0
        while True:
            i += 1
            print(i)
    elif "web" in t.lower():
        url = input("💣URL💣 ")
        functions.webs(url)
    elif "wifi" in t.lower():
        functions.get_wifi_info()
    elif "site" in t.lower():
        functions.get_ip_by_hostname()
    elif "reload" in t.lower():
        importlib.reload(functions)
    elif "hash" in t.lower():
        functions.hashes()
    elif "pc" in t.lower():
        functions.get_pc()
    else:
        print(f"💣Not find a command - {t}💣")
    with open("history.txt", "a+") as history:
        history.write(t+"""
""")
        history.close()