# from pynput.mouse import Listener
#
# def on_click(x, y, button, pressed):
#     if pressed:
#         print(f"Координаты: X={x}, Y={y}")
#
# with Listener(on_click=on_click) as listener:
#     listener.join()







# import pyautogui
# import time
#
#
# y_scroll= 401
# step= 4
#
# account_counter = 0
#
#
# first_acc = (1545, 394)
# second_acc= (1544, 419)
# third_acc =(1545, 445)
# firth_acc =(1545, 466)
# fifth_acc =(1548, 492)
#
#
#
#
#
# click_panel=(1688, 432)
# start_acc = (1740, 398)
# close_acc = (1742, 442)
# open_pubg = (1780, 647)
#
# while True:
#     for acc in [first_acc, second_acc, third_acc, firth_acc, fifth_acc]:
#
#         pyautogui.click(first_acc)
#         print(f"Нажали на first acc")
#         time.sleep(2)
#
#         pyautogui.click(start_acc)
#         print(f'Нажал на start acc')
#         time.sleep(30)
#
#         pyautogui.doubleClick(open_pubg)
#         print(f"Запустил pubg")
#         time.sleep(90)
#
#         pyautogui.doubleClick(click_panel)
#         print(f"Клик по панели")
#         time.sleep(3)
#
#         pyautogui.click(first_acc)
#         print(f"Нажали на first_acc")
#         time.sleep(3)
#
#         pyautogui.click(close_acc)
#         print(f"Нажали на close acc")
#         time.sleep(5)
#
#         pyautogui.click(second_acc)
#         print(f"Нажали на second acc")
#         time.sleep(1)
#
#         pyautogui.click(start_acc)
#         print(f'Нажал на start acc')
#         time.sleep(70)
#
#         pyautogui.doubleClick(open_pubg)
#         print(f"Запустил pubg")
#         time.sleep(90)
#
#         pyautogui.doubleClick(click_panel)
#         print(f"Клик по панели")
#         time.sleep(3)
#
#         pyautogui.click(second_acc)
#         print(f"Нажали на second_acc")
#         time.sleep(3)
#
#         pyautogui.click(close_acc)
#         print(f"Нажали на close acc")
#         time.sleep(5)
#
#         pyautogui.click(third_acc)
#         print(f"Нажали на third acc")
#         time.sleep(1)
#
#         pyautogui.click(start_acc)
#         print(f'Нажал на start acc')
#         time.sleep(70)
#
#         pyautogui.doubleClick(open_pubg)
#         print(f"Запустил pubg")
#         time.sleep(90)
#
#         pyautogui.doubleClick(click_panel)
#         print(f"Клик по панели")
#         time.sleep(3)
#
#         pyautogui.click(third_acc)
#         print(f"Нажали на third_acc")
#         time.sleep(3)
#
#         pyautogui.click(close_acc)
#         print(f"Нажали на close acc")
#         time.sleep(5)
#
#         pyautogui.click(firth_acc)
#         print(f"Нажали на firth acc")
#         time.sleep(1)
#
#         pyautogui.click(start_acc)
#         print(f'Нажал на start acc')
#         time.sleep(70)
#
#         pyautogui.doubleClick(open_pubg)
#         print(f"Запустил pubg")
#         time.sleep(90)
#
#         pyautogui.doubleClick(click_panel)
#         print(f"Клик по панели")
#         time.sleep(3)
#
#         pyautogui.click(firth_acc)
#         print(f"Нажали на firth_acc")
#         time.sleep(3)
#
#         pyautogui.click(close_acc)
#         print(f"Нажали на stop_coor")
#         time.sleep(5)
#
#         pyautogui.click(fifth_acc)
#         print(f"Нажали на fifth acc")
#         time.sleep(3)
#
#         pyautogui.click(start_acc)
#         print(f'Нажал на start acc')
#         time.sleep(70)
#
#         pyautogui.doubleClick(open_pubg)
#         print(f"Запустил pubg")
#         time.sleep(90)
#
#         pyautogui.doubleClick(click_panel)
#         print(f"Клик по панели")
#         time.sleep(3)
#
#         pyautogui.click(fifth_acc)
#         print(f"Нажали на fifth_acc")
#         time.sleep(1)
#
#         pyautogui.click(close_acc)
#         print(f"Нажали на close acc")
#         time.sleep(5)
#
#         account_counter += 1
#
#         print(account_counter)
#         if account_counter % 1 == 0:
#             pyautogui.click(1623, y_scroll)
#             pyautogui.scroll(-4900)
#             print(f"Нажал на корды что бы листнуть")
#             y_scroll+=step
#             time.sleep(5)


#WITH PAUSE

import pyautogui
import time
import keyboard
import threading

y_scroll= 513
step= 3

account_counter = 0

first_acc = (1465, 509)
second_acc= (1467, 540)
third_acc =(1469, 570)
firth_acc =(1471, 601)
fifth_acc =(1472, 632)

click_panel=(1776, 19)
start_acc = (1810, 518)
close_acc = (1797, 567)
open_pubg = (57, 275)
accept_terms = (1111, 917)








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
    for acc in [first_acc, second_acc, third_acc, firth_acc, fifth_acc]:
        while paused:
            time.sleep(0.1)

        pyautogui.click(first_acc)
        print(f"Нажали на first acc")
        time.sleep(2)

        while paused:
            time.sleep(0.1)
        pyautogui.click(start_acc)
        print(f'Нажал на start acc')
        time.sleep(60)

        while paused:
            time.sleep(0.1)
        pyautogui.doubleClick(open_pubg)
        print(f"Запустил pubg")
        time.sleep(10)

        while paused:
            time.sleep(0.1)
        pyautogui.click(accept_terms)
        print(f"принял соглашения")
        time.sleep(120)


        while paused:
            time.sleep(0.1)
        pyautogui.click(click_panel)
        print(f"Клик по панели")
        time.sleep(3)

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
        #
        while paused:
            time.sleep(0.1)
        pyautogui.click(second_acc)
        print(f"Нажали на second acc")
        time.sleep(3)

        while paused:
            time.sleep(0.1)
        pyautogui.click(start_acc)
        print(f'Нажал на start acc')
        time.sleep(60)

        while paused:
            time.sleep(0.1)
        pyautogui.doubleClick(open_pubg)
        print(f"Запустил pubg")
        time.sleep(10)

        while paused:
            time.sleep(0.1)
        pyautogui.click(accept_terms)
        print(f"принял соглашения")
        time.sleep(120)

        while paused:
            time.sleep(0.1)
        pyautogui.click(click_panel)
        print(f"Клик по панели")
        time.sleep(3)

        while paused:
            time.sleep(0.1)
        pyautogui.click(second_acc)
        print(f"Нажали на second_acc")
        time.sleep(3)

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
        time.sleep(60)

        while paused:
            time.sleep(0.1)
        pyautogui.doubleClick(open_pubg)
        print(f"Запустил pubg")
        time.sleep(10)

        while paused:
            time.sleep(0.1)
        pyautogui.click(accept_terms)
        print(f"принял соглашения")
        time.sleep(120)

        while paused:
            time.sleep(0.1)
        pyautogui.click(click_panel)
        print(f"Клик по панели")
        time.sleep(3)

        while paused:
            time.sleep(0.1)
        pyautogui.click(third_acc)
        print(f"Нажали на third_acc")
        time.sleep(3)

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
        time.sleep(60)

        while paused:
            time.sleep(0.1)
        pyautogui.doubleClick(open_pubg)
        print(f"Запустил pubg")
        time.sleep(10)

        while paused:
            time.sleep(0.1)
        pyautogui.click(accept_terms)
        print(f"принял соглашения")
        time.sleep(120)

        while paused:
            time.sleep(0.1)
        pyautogui.click(click_panel)
        print(f"Клик по панели")
        time.sleep(3)

        while paused:
            time.sleep(0.1)
        pyautogui.click(firth_acc)
        print(f"Нажали на firth_acc")
        time.sleep(3)

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
        time.sleep(60)

        while paused:
            time.sleep(0.1)
        pyautogui.doubleClick(open_pubg)
        print(f"Запустил pubg")
        time.sleep(10)

        while paused:
            time.sleep(0.1)
        pyautogui.click(accept_terms)
        print(f"принял соглашения")
        time.sleep(120)

        while paused:
            time.sleep(0.1)
        pyautogui.click(click_panel)
        print(f"Клик по панели")
        time.sleep(3)

        while paused:
            time.sleep(0.1)
        pyautogui.click(fifth_acc)
        print(f"Нажали на fifth_acc")
        time.sleep(3)

        while paused:
            time.sleep(0.1)
        pyautogui.click(close_acc)
        print(f"Нажали на close acc")
        time.sleep(10)

        account_counter += 1
        print(account_counter)

        while paused:
            time.sleep(0.1)
        if account_counter % 1 == 0:
            pyautogui.click(1623, y_scroll)
            pyautogui.scroll(-6000)
            print(f"Нажал на корды что бы листнуть")
            y_scroll+=step
            time.sleep(5)