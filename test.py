# from pynput.mouse import Listener
#
# def on_click(x, y, button, pressed):
#     if pressed:
#         print(f"Координаты: X={x}, Y={y}")
#
# with Listener(on_click=on_click) as listener:
#     listener.join()
# #

# from fileinput import close

import pyautogui
import time

account_counter = 0

first_acc = (173, 116)
second_acc = (173, 156)
third_acc = (173, 194)
firth_acc = (173, 233)
fifth_acc = (173, 273)

coor_start = (437, 316)
nextpg_coor = (1855, 70)
stop_coor = (477, 314)

while True:
    for acc in [first_acc, second_acc, third_acc, firth_acc, fifth_acc]:

        pyautogui.click(first_acc)
        print(f"Нажали на first_acc")
        time.sleep(2)

        pyautogui.click(coor_start)
        print(f'Нажал на coor_start')
        time.sleep(2)

        pyautogui.click(first_acc)
        print(f"Нажали на first_acc")
        time.sleep(2)

        pyautogui.click(stop_coor)
        print(f"Нажали на stop_coor")
        time.sleep(2)

        pyautogui.click(second_acc)
        print(f"Нажали на second_acc")
        time.sleep(2)

        pyautogui.click(coor_start)
        print(f'Нажал на coor_start')
        time.sleep(2)

        pyautogui.click(second_acc)
        print(f"Нажали на second_acc")
        time.sleep(2)

        pyautogui.click(stop_coor)
        print(f"Нажали на stop_coor")
        time.sleep(2)

        pyautogui.click(third_acc)
        print(f"Нажали на third_acc")
        time.sleep(2)

        pyautogui.click(coor_start)
        print(f'Нажал на coor_start')
        time.sleep(2)

        pyautogui.click(third_acc)
        print(f"Нажали на third_acc")
        time.sleep(2)

        pyautogui.click(stop_coor)
        print(f"Нажали на stop_coor")
        time.sleep(2)

        pyautogui.click(firth_acc)
        print(f"Нажали на firth_acc")
        time.sleep(2)

        pyautogui.click(coor_start)
        print(f'Нажал на coor_start')
        time.sleep(2)

        pyautogui.click(firth_acc)
        print(f"Нажали на firth_acc")
        time.sleep(2)

        pyautogui.click(stop_coor)
        print(f"Нажали на stop_coor")
        time.sleep(2)

        pyautogui.click(fifth_acc)
        print(f"Нажали на fifth_acc")
        time.sleep(2)

        pyautogui.click(coor_start)
        print(f'Нажал на coor_start')
        time.sleep(2)

        pyautogui.click(fifth_acc)
        print(f"Нажали на fifth_acc")
        time.sleep(2)

        pyautogui.click(stop_coor)
        print(f"Нажали на stop_coor")
        time.sleep(2)

        account_counter += 1

        print(account_counter)
        if account_counter % 1 == 0:
            pyautogui.click(nextpg_coor)
            print(f"Нажали на координаты для смены страницы: nextpg_coor")
            time.sleep(10)
