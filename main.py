import functions
import colorama
functions.start()
while True:
    t = input(colorama.Fore.RESET+colorama.Style.BRIGHT+colorama.Back.RESET+"💣️H.A.C.K...S.T.A.L.K.E.R💣️ ")
    if "ddos" in t.lower() or "1" in t.lower():
        url = input("💣️URL💣️ ")
        functions.ddos(url)
        print()
    elif t  == "secmail" in t.lower() or "2" in t.lower():
        functions.secmail()
    elif t.lower().strip(" ") == "parsing" or t.lower().strip(" ") == "3":
        ssylka = input("💣️URL💣️ ")
        functions.parsing(ssylka)
    elif "exit" in t.lower() or "quit" in t.lower() or "4" in t.lower():
        exit("💣️Выход из программы...💣️")
    elif "gpt" in t.lower() or "5" in t.lower():
        ask = input("💣️Введите запрос💣️ ")
        functions.gpt(ask)
    elif "fork" in t.lower() or "6" in t.lower():
        functions.fork()
    elif "click" in t.lower() or "7" in t.lower():
        click = input("💣Кнопка мыши(1 - левая, 2 - правая)💣 ")
        if click == "1" or "left":
            functions.click_left()
        elif click == "2" or "right":
            functions.click_right()    
    elif "console" in t.lower() or "8" in t.lower():
        console = input("💣Команда💣 ")
        functions.console(console)
    elif "clear" in t.lower() or "9" in t.lower():
        print("\033[H\033[J", end = "")
    elif "phone" in t.lower() or "10" in t.lower():
        httpweb_number = functions.HttpWebNumber()
        httpweb_number.print_number_results
    elif "ip" in t.lower() or "11" in t.lower():
        ip_1 = input("💣️IP💣️ ")
        functions.get_info_ip(ip_1)
        functions.get_info(ip_1)
    elif "999" in t.lower() or "12" in t.lower():
        i = 0
        while True:
            i += 1
            print(i)
    elif "web" in t.lower() or "13" in t.lower():
        url = input("💣URL💣 ")
        functions.webs(url)
    elif "wifi" in t.lower() or "14" in t.lower():
        functions.get_wifi_info()
    elif "site" in t.lower() or "15" in t.lower():
        functions.get_ip_by_hostname()
    elif "hash" in t.lower() or "17" in t.lower():
        functions.hashes()
    elif "pc" in t.lower() or "18" in t.lower():
        functions.get_pc()
    elif "gut" in t.lower() or "19" in t.lower():
        print("Ну-сс...:\nНу что сказать - год прошёл не питоновски, а на все сиплюсовски!\nПока я осваивал Python до кончиков пальцев, решил расширить горизонты и теперь штурмую C++ .\nЭто как из змейки превратиться в супергероя - из Python-а в C++-er'а, и я горжусь, что сумел так языково разнообразить свой код жизни.\nЖелаю себе не останавливаться на достигнутом, продолжать программить свой опыт и превращать любой код в праздник, а в новом году пусть каждая переменная будет правильной, а баги - только кулинарными!")
    elif "author" in t.lower() or "20" in t.lower():
        functions.author()
    elif "help" in t.lower() or "21" in t.lower():
        functions.help()
    else:
        print(f"💣Не найдена команда - {t}💣")
    with open("history.txt", "a+") as history:
        history.write(t+"""
""")
        history.close()
