# from pynput.mouse import Listener
#
# def on_click(x, y, button, pressed):
#     if pressed:
#         print(f"Координаты: X={x}, Y={y}")
#
# with Listener(on_click=on_click) as listener:
#     listener.join()


#WITH PAUSE

# import pyautogui
# import time
# import keyboard
# import threading
#
# y_scroll= 521
# step= 2.5
#
# account_counter = 0
#
# first_acc = (1495, 514)
# second_acc= (1495, 545)
# third_acc =(1496, 577)
# firth_acc =(1498, 604)
# fifth_acc=(1495, 636)
#
#
#
# click_panel=(1840, 19)
# start_acc = (1782, 518)
# close_acc = (1781, 571)
# open_pubg = (57, 275)
# accept_terms = (1111, 917)
#
#
#
#
#
#
#
#
# paused = False
#
# def pause_listener():
#     global paused
#     while True:
#         if keyboard.is_pressed('p'):
#             paused = True
#             print("Пауза... Нажмите 'r' для продолжения")
#             while paused:
#                 if keyboard.is_pressed('r'):
#                     paused = False
#                     print("Продолжаем...")
#                     break
#         time.sleep(0.1)
#
#
# threading.Thread(target=pause_listener, daemon=True).start()
#
#
# while True:
#     for acc in [first_acc, second_acc, third_acc, firth_acc]:
#         while paused:
#             time.sleep(0.1)
#
#         pyautogui.click(first_acc)
#         print(f"Нажали на first acc")
#         time.sleep(3)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(start_acc)
#         print(f'Нажал на start acc')
#         time.sleep(45)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.doubleClick(open_pubg)
#         print(f"Запустил pubg")
#         time.sleep(4)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(accept_terms)
#         print(f"принял соглашения")
#         time.sleep(1.5)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.doubleClick(open_pubg)
#         print(f"Запустил pubg")
#         time.sleep(80)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(click_panel)
#         print(f"Клик по панели")
#         time.sleep(4)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(first_acc)
#         print(f"Нажали на first_acc")
#         time.sleep(3)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(close_acc)
#         print(f"Нажали на close acc")
#         time.sleep(10)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(second_acc)
#         print(f"Нажали на second acc")
#         time.sleep(4)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(start_acc)
#         print(f'Нажал на start acc')
#         time.sleep(45)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.doubleClick(open_pubg)
#         print(f"Запустил pubg")
#         time.sleep(4)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(accept_terms)
#         print(f"принял соглашения")
#         time.sleep(1.5)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.doubleClick(open_pubg)
#         print(f"Запустил pubg")
#         time.sleep(80)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(click_panel)
#         print(f"Клик по панели")
#         time.sleep(4)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(second_acc)
#         print(f"Нажали на second_acc")
#         time.sleep(4)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(close_acc)
#         print(f"Нажали на close acc")
#         time.sleep(10)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(third_acc)
#         print(f"Нажали на third acc")
#         time.sleep(4)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(start_acc)
#         print(f'Нажал на start acc')
#         time.sleep(45)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.doubleClick(open_pubg)
#         print(f"Запустил pubg")
#         time.sleep(3)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(accept_terms)
#         print(f"принял соглашения")
#         time.sleep(1.5)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.doubleClick(open_pubg)
#         print(f"Запустил pubg")
#         time.sleep(80)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(click_panel)
#         print(f"Клик по панели")
#         time.sleep(4)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(third_acc)
#         print(f"Нажали на third_acc")
#         time.sleep(4)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(close_acc)
#         print(f"Нажали на close acc")
#         time.sleep(10)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(firth_acc)
#         print(f"Нажали на firth acc")
#         time.sleep(4)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(start_acc)
#         print(f'Нажал на start acc')
#         time.sleep(45)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.doubleClick(open_pubg)
#         print(f"Запустил pubg")
#         time.sleep(3)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(accept_terms)
#         print(f"принял соглашения")
#         time.sleep(1.5)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.doubleClick(open_pubg)
#         print(f"Запустил pubg")
#         time.sleep(80)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(click_panel)
#         print(f"Клик по панели")
#         time.sleep(4)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(firth_acc)
#         print(f"Нажали на firth_acc")
#         time.sleep(4)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(close_acc)
#         print(f"Нажали на stop_coor")
#         time.sleep(10)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(fifth_acc)
#         print(f"Нажали на fifth acc")
#         time.sleep(4)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(start_acc)
#         print(f'Нажал на start acc')
#         time.sleep(45)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.doubleClick(open_pubg)
#         print(f"Запустил pubg")
#         time.sleep(3)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(accept_terms)
#         print(f"принял соглашения")
#         time.sleep(1.5)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.doubleClick(open_pubg)
#         print(f"Запустил pubg")
#         time.sleep(80)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(click_panel)
#         print(f"Клик по панели")
#         time.sleep(4)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(fifth_acc)
#         print(f"Нажали на fifth_acc")
#         time.sleep(4)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(close_acc)
#         print(f"Нажали на stop_coor")
#         time.sleep(10)
#
#         account_counter += 1
#         print(account_counter)
#
#         while paused:
#             time.sleep(0.1)
#         if account_counter % 1 == 0:
#             pyautogui.click(1613, y_scroll)
#             pyautogui.scroll(-6000)
#             print(f"Нажал на корды что бы листнуть")
#             y_scroll+=step
#             time.sleep(7)





# FOR MINION ACCS

# import random
# import string
# import pyautogui
# import time
# import keyboard
# import threading
#
# y_scroll= 521
# step= 4
#
# account_counter = 0
# first_acc = (1495, 514)
# second_acc= (1495, 545)
# third_acc =(1496, 577)
# firth_acc =(1498, 604)
# fifth_acc=(1495, 636)
#
#
# click_panel=(1776, 19)
# start_acc = (1782, 518)
# close_acc = (1781, 571)
# open_pubg = (57, 275)
# accept_terms = (1111, 917)
#
# nick_click=(890, 576)
# first_terms=(670, 697)
# second_terms=(1191, 699)
# accept_all=(956, 748)
# create_bro= (444, 815)
# click_pubg=(1010, 527)
#
#
#
#
#
# def generate_nickname(length=10):
#     chars = string.ascii_letters.replace("F", "").replace("f", "") + string.digits
#     return "".join(random.choices(chars, k=length))
#
# def type_nickname(nick_click):
#     nickname = generate_nickname()
#     pyautogui.click(nick_click)
#     time.sleep(2)
#     pyautogui.typewrite(nickname)
#     time.sleep(2)
#     pyautogui.press("enter")
#
#
# paused = False
#
# def pause_listener():
#     global paused
#     while True:
#         if keyboard.is_pressed('p'):
#             paused = True
#             print("Пауза... Нажмите 'r' для продолжения")
#             while paused:
#                 if keyboard.is_pressed('r'):
#                     paused = False
#                     print("Продолжаем...")
#                     break
#         time.sleep(0.1)
#
#
# threading.Thread(target=pause_listener, daemon=True).start()
#
#
# while True:
#     for acc in [first_acc, second_acc, third_acc, firth_acc]:
#         while paused:
#             time.sleep(0.1)
#
#         pyautogui.click(first_acc)
#         print(f"Нажали на first acc")
#         time.sleep(3)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(start_acc)
#         print(f'Нажал на start acc')
#         time.sleep(40)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.doubleClick(open_pubg)
#         print(f"Запустил pubg")
#         time.sleep(3)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(accept_terms)
#         print(f"принял соглашения")
#         time.sleep(1.5)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.doubleClick(open_pubg)
#         print(f"Запустил pubg")
#         time.sleep(90)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(click_pubg)
#         print("Нажал на окно пабга")
#         time.sleep(1)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(first_terms)
#         print("Принял первые соглашения")
#         time.sleep(2)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(second_terms)
#         print("Принял вторые соглашения")
#         time.sleep(2)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(accept_all)
#         print("Подтвердил")
#         time.sleep(5)
#
#         type_nickname(nick_click)
#         print("Рандомнул ник")
#         time.sleep(8)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(create_bro)
#         print("Создал персонажа")
#         time.sleep(20)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(click_panel)
#         print(f"Клик по панели")
#         time.sleep(4)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(first_acc)
#         print(f"Нажали на first_acc")
#         time.sleep(4)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(close_acc)
#         print(f"Нажали на close acc")
#         time.sleep(11)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(second_acc)
#         print(f"Нажали на second acc")
#         time.sleep(3)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(start_acc)
#         print(f'Нажал на start acc')
#         time.sleep(40)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.doubleClick(open_pubg)
#         print(f"Запустил pubg")
#         time.sleep(3)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(accept_terms)
#         print(f"принял соглашения")
#         time.sleep(1.5)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.doubleClick(open_pubg)
#         print(f"Запустил pubg")
#         time.sleep(90)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(click_pubg)
#         print("Нажал на окно пабга")
#         time.sleep(1)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(first_terms)
#         print("Принял первые соглашения")
#         time.sleep(2)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(second_terms)
#         print("Принял вторые соглашения")
#         time.sleep(2)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(accept_all)
#         print("Подтвердил")
#         time.sleep(5)
#
#         type_nickname(nick_click)
#         print("Рандомнул ник")
#         time.sleep(8)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(create_bro)
#         print("Создал персонажа")
#         time.sleep(20)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(click_panel)
#         print(f"Клик по панели")
#         time.sleep(4)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(second_acc)
#         print(f"Нажали на second_acc")
#         time.sleep(4)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(close_acc)
#         print(f"Нажали на close acc")
#         time.sleep(11)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(third_acc)
#         print(f"Нажали на third acc")
#         time.sleep(3)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(start_acc)
#         print(f'Нажал на start acc')
#         time.sleep(40)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.doubleClick(open_pubg)
#         print(f"Запустил pubg")
#         time.sleep(3)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(accept_terms)
#         print(f"принял соглашения")
#         time.sleep(1.5)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.doubleClick(open_pubg)
#         print(f"Запустил pubg")
#         time.sleep(90)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(click_pubg)
#         print("Нажал на окно пабга")
#         time.sleep(1)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(first_terms)
#         print("Принял первые соглашения")
#         time.sleep(2)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(second_terms)
#         print("Принял вторые соглашения")
#         time.sleep(2)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(accept_all)
#         print("Подтвердил")
#         time.sleep(5)
#
#         type_nickname(nick_click)
#         print("Рандомнул ник")
#         time.sleep(8)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(create_bro)
#         print("Создал персонажа")
#         time.sleep(20)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(click_panel)
#         print(f"Клик по панели")
#         time.sleep(4)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(third_acc)
#         print(f"Нажали на third_acc")
#         time.sleep(3)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(close_acc)
#         print(f"Нажали на close acc")
#         time.sleep(11)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(firth_acc)
#         print(f"Нажали на firth acc")
#         time.sleep(3)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(start_acc)
#         print(f'Нажал на start acc')
#         time.sleep(40)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.doubleClick(open_pubg)
#         print(f"Запустил pubg")
#         time.sleep(3)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(accept_terms)
#         print(f"принял соглашения")
#         time.sleep(1.5)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.doubleClick(open_pubg)
#         print(f"Запустил pubg")
#         time.sleep(90)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(click_pubg)
#         print("Нажал на окно пабга")
#         time.sleep(1)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(first_terms)
#         print("Принял первые соглашения")
#         time.sleep(2)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(second_terms)
#         print("Принял вторые соглашения")
#         time.sleep(2)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(accept_all)
#         print("Подтвердил")
#         time.sleep(5)
#
#         type_nickname(nick_click)
#         print("Рандомнул ник")
#         time.sleep(8)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(create_bro)
#         print("Создал персонажа")
#         time.sleep(20)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(click_panel)
#         print(f"Клик по панели")
#         time.sleep(4)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(firth_acc)
#         print(f"Нажали на firth_acc")
#         time.sleep(3)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(close_acc)
#         print(f"Нажали на stop_coor")
#         time.sleep(11)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(fifth_acc)
#         print(f"Нажали на fifth acc")
#         time.sleep(3)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(start_acc)
#         print(f'Нажал на start acc')
#         time.sleep(40)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.doubleClick(open_pubg)
#         print(f"Запустил pubg")
#         time.sleep(3)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(accept_terms)
#         print(f"принял соглашения")
#         time.sleep(1.5)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.doubleClick(open_pubg)
#         print(f"Запустил pubg")
#         time.sleep(90)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(click_pubg)
#         print("Нажал на окно пабга")
#         time.sleep(1)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(first_terms)
#         print("Принял первые соглашения")
#         time.sleep(2)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(second_terms)
#         print("Принял вторые соглашения")
#         time.sleep(2)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(accept_all)
#         print("Подтвердил")
#         time.sleep(5)
#
#         type_nickname(nick_click)
#         print("Рандомнул ник")
#         time.sleep(8)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(create_bro)
#         print("Создал персонажа")
#         time.sleep(20)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(click_panel)
#         print(f"Клик по панели")
#         time.sleep(4)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(fifth_acc)
#         print(f"Нажали на fifth_acc")
#         time.sleep(3)
#
#         while paused:
#             time.sleep(0.1)
#         pyautogui.click(close_acc)
#         print(f"Нажали на stop_coor")
#         time.sleep(11)
#
#         account_counter += 1
#         print(account_counter)
#
#         while paused:
#             time.sleep(0.1)
#         if account_counter % 1 == 0:
#             pyautogui.click(1613, y_scroll)
#             pyautogui.scroll(-6000)
#             print(f"Нажал на корды что бы листнуть")
#             y_scroll+=step
#             time.sleep(10)







#KONTRABANDA


import pyautogui
import time
import keyboard
import threading

y_scroll= 521
step= 2.5

account_counter = 0

first_acc = (1495, 514)
second_acc= (1495, 545)
third_acc =(1496, 577)
firth_acc =(1498, 604)
fifth_acc=(1495, 636)



click_panel=(1840, 19)
start_acc = (1782, 518)
close_acc = (1781, 571)
open_pubg = (57, 275)
# accept_terms = (1111, 917)


BOX=(1438, 179)
GIFT_CHOOSE=(445, 533)
GIFT_COLLECT=(676, 469)
PUBG_CLICK=(676,469)




paused = False

def pause_listener():
    global paused
    while True:
        if keyboard.is_pressed('p'):
            paused = True
            print("Пауза... Нажмите 'r' для продолжения")
            while paused:
                if keyboard.is_pressed('r'):
                    paused = False
                    print("Продолжаем...")
                    break
        time.sleep(0.1)


threading.Thread(target=pause_listener, daemon=True).start()


while True:
    for acc in [first_acc, second_acc, third_acc, firth_acc]:
        while paused:
            time.sleep(0.1)

        pyautogui.click(first_acc)
        print(f"Нажали на first acc")
        time.sleep(3)

        while paused:
            time.sleep(0.1)
        pyautogui.click(start_acc)
        print(f'Нажал на start acc')
        time.sleep(45)


        while paused:
            time.sleep(0.1)
        pyautogui.doubleClick(open_pubg)
        print(f"Запустил pubg")
        time.sleep(70)

        while paused:
            time.sleep(0.1)
        pyautogui.click(BOX)
        time.sleep(1)

        while paused:
            time.sleep(0.1)
        pyautogui.click(BOX)
        time.sleep(3)

        while paused:
            time.sleep(0.1)
        pyautogui.click(GIFT_CHOOSE)
        time.sleep(3)

        while paused:
            time.sleep(0.1)
        pyautogui.click(GIFT_COLLECT)
        time.sleep(5)

        while paused:
            time.sleep(0.1)
        pyautogui.click(click_panel)
        print(f"Клик по панели")
        time.sleep(4)

        while paused:
            time.sleep(0.1)
        pyautogui.click(first_acc)
        print(f"Нажали на first_acc")
        time.sleep(3)

        while paused:
            time.sleep(0.1)
        pyautogui.click(close_acc)
        print(f"Нажали на close acc")
        time.sleep(10)

        while paused:
            time.sleep(0.1)
        pyautogui.click(second_acc)
        print(f"Нажали на second acc")
        time.sleep(3)

        while paused:
            time.sleep(0.1)
        pyautogui.click(start_acc)
        print(f'Нажал на start acc')
        time.sleep(45)

        while paused:
            time.sleep(0.1)
        pyautogui.doubleClick(open_pubg)
        print(f"Запустил pubg")
        time.sleep(70)

        while paused:
            time.sleep(0.1)
        pyautogui.click(BOX)
        time.sleep(1)

        while paused:
            time.sleep(0.1)
        pyautogui.click(BOX)
        time.sleep(3)

        while paused:
            time.sleep(0.1)
        pyautogui.click(GIFT_CHOOSE)
        time.sleep(3)

        while paused:
            time.sleep(0.1)
        pyautogui.click(GIFT_COLLECT)
        time.sleep(5)


        while paused:
            time.sleep(0.1)
        pyautogui.click(click_panel)
        print(f"Клик по панели")
        time.sleep(4)

        while paused:
            time.sleep(0.1)
        pyautogui.click(second_acc)
        print(f"Нажали на second_acc")
        time.sleep(4)

        while paused:
            time.sleep(0.1)
        pyautogui.click(close_acc)
        print(f"Нажали на close acc")
        time.sleep(10)

        while paused:
            time.sleep(0.1)
        pyautogui.click(third_acc)
        print(f"Нажали на third acc")
        time.sleep(3)

        while paused:
            time.sleep(0.1)
        pyautogui.click(start_acc)
        print(f'Нажал на start acc')
        time.sleep(45)

        while paused:
            time.sleep(0.1)
        pyautogui.doubleClick(open_pubg)
        print(f"Запустил pubg")
        time.sleep(70)

        while paused:
            time.sleep(0.1)
        pyautogui.click(BOX)
        time.sleep(1)

        while paused:
            time.sleep(0.1)
        pyautogui.click(BOX)
        time.sleep(3)

        while paused:
            time.sleep(0.1)
        pyautogui.click(GIFT_CHOOSE)
        time.sleep(3)

        while paused:
            time.sleep(0.1)
        pyautogui.click(GIFT_COLLECT)
        time.sleep(5)

        while paused:
            time.sleep(0.1)
        pyautogui.click(click_panel)
        print(f"Клик по панели")
        time.sleep(4)

        while paused:
            time.sleep(0.1)
        pyautogui.click(third_acc)
        print(f"Нажали на third_acc")
        time.sleep(4)

        while paused:
            time.sleep(0.1)
        pyautogui.click(close_acc)
        print(f"Нажали на close acc")
        time.sleep(10)

        while paused:
            time.sleep(0.1)
        pyautogui.click(firth_acc)
        print(f"Нажали на firth acc")
        time.sleep(3)

        while paused:
            time.sleep(0.1)
        pyautogui.click(start_acc)
        print(f'Нажал на start acc')
        time.sleep(45)

        while paused:
            time.sleep(0.1)
        pyautogui.doubleClick(open_pubg)
        print(f"Запустил pubg")
        time.sleep(70)

        while paused:
            time.sleep(0.1)
        pyautogui.click(BOX)
        time.sleep(1)

        while paused:
            time.sleep(0.1)
        pyautogui.click(BOX)
        time.sleep(3)

        while paused:
            time.sleep(0.1)
        pyautogui.click(GIFT_CHOOSE)
        time.sleep(3)

        while paused:
            time.sleep(0.1)
        pyautogui.click(GIFT_COLLECT)
        time.sleep(5)

        while paused:
            time.sleep(0.1)
        pyautogui.click(click_panel)
        print(f"Клик по панели")
        time.sleep(4)

        while paused:
            time.sleep(0.1)
        pyautogui.click(firth_acc)
        print(f"Нажали на firth_acc")
        time.sleep(4)

        while paused:
            time.sleep(0.1)
        pyautogui.click(close_acc)
        print(f"Нажали на stop_coor")
        time.sleep(10)

        while paused:
            time.sleep(0.1)
        pyautogui.click(fifth_acc)
        print(f"Нажали на fifth acc")
        time.sleep(3)

        while paused:
            time.sleep(0.1)
        pyautogui.click(start_acc)
        print(f'Нажал на start acc')
        time.sleep(45)

        while paused:
            time.sleep(0.1)
        pyautogui.doubleClick(open_pubg)
        print(f"Запустил pubg")
        time.sleep(70)

        while paused:
            time.sleep(0.1)
        pyautogui.click(BOX)
        time.sleep(1)

        while paused:
            time.sleep(0.1)
        pyautogui.click(BOX)
        time.sleep(3)

        while paused:
            time.sleep(0.1)
        pyautogui.click(GIFT_CHOOSE)
        time.sleep(3)

        while paused:
            time.sleep(0.1)
        pyautogui.click(GIFT_COLLECT)
        time.sleep(5)

        while paused:
            time.sleep(0.1)
        pyautogui.click(click_panel)
        print(f"Клик по панели")
        time.sleep(4)

        while paused:
            time.sleep(0.1)
        pyautogui.click(fifth_acc)
        print(f"Нажали на fifth_acc")
        time.sleep(4)

        while paused:
            time.sleep(0.1)
        pyautogui.click(close_acc)
        print(f"Нажали на stop_coor")
        time.sleep(10)

        account_counter += 1
        print(account_counter)

        while paused:
            time.sleep(0.1)
        if account_counter % 1 == 0:
            pyautogui.click(1613, y_scroll)
            pyautogui.scroll(-6000)
            print(f"Нажал на корды что бы листнуть")
            y_scroll+=step
            time.sleep(7)