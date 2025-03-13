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

tri_tochki1=(1796,119)
tri_tochki2=(1796,155)
tri_tochki3=(1796,193)
tri_tochki4=(1796,234)
tri_tochki5=(1796,269)



first_acc = (1647,115)
second_acc= (1647,154)
third_acc =(1647,195)
firth_acc =(1647,234)
fifth_acc =(1647,273)



open_steam1 = (1681, 231)
open_steam2 = (1708, 271)
open_steam3 = (1683, 309)
open_steam4 = (1687, 340)
open_steam5 = (1694, 386)


click_panel = (1897, 16)
open_pubg = (1858,442)
nextpg_coor = (1855, 70)
stop_coor = (1895, 313)

while True:
    for acc in [first_acc, second_acc, third_acc, firth_acc, fifth_acc]:

        pyautogui.click(tri_tochki1)
        print(f"Нажали на Три точки")
        time.sleep(3)

        pyautogui.click(open_steam1)
        print(f'Нажал на open_steam')
        time.sleep(90)

        pyautogui.doubleClick(open_pubg)
        print(f"Запустил pubg")
        time.sleep(120)

        pyautogui.doubleClick(click_panel)
        print(f"Клик по панели")
        time.sleep(3)

        pyautogui.click(first_acc)
        print(f"Нажали на first_acc")
        time.sleep(3)

        pyautogui.click(stop_coor)
        print(f"Нажали на stop_coor")
        time.sleep(5)

        pyautogui.click(tri_tochki2)
        print(f"Нажали на Три точки")
        time.sleep(3)

        pyautogui.click(open_steam2)
        print(f'Нажал на open_steam')
        time.sleep(90)

        pyautogui.doubleClick(open_pubg)
        print(f"Запустил pubg")
        time.sleep(120)

        pyautogui.doubleClick(click_panel)
        print(f"Клик по панели")
        time.sleep(3)

        pyautogui.click(second_acc)
        print(f"Нажали на second_acc")
        time.sleep(3)

        pyautogui.click(stop_coor)
        print(f"Нажали на stop_coor")
        time.sleep(5)

        pyautogui.click(tri_tochki3)
        print(f"Нажали на три точки")
        time.sleep(3)

        pyautogui.click(open_steam3)
        print(f'Нажал на open_steam')
        time.sleep(90)

        pyautogui.doubleClick(open_pubg)
        print(f"Запустил pubg")
        time.sleep(120)

        pyautogui.doubleClick(click_panel)
        print(f"Клик по панели")
        time.sleep(3)

        pyautogui.click(third_acc)
        print(f"Нажали на third_acc")
        time.sleep(3)

        pyautogui.click(stop_coor)
        print(f"Нажали на stop_coor")
        time.sleep(5)

        pyautogui.click(tri_tochki4)
        print(f"Нажали на Три точки")
        time.sleep(3)

        pyautogui.click(open_steam4)
        print(f'Нажал на open_steam')
        time.sleep(90)

        pyautogui.doubleClick(open_pubg)
        print(f"Запустил pubg")
        time.sleep(120)

        pyautogui.doubleClick(click_panel)
        print(f"Клик по панели")
        time.sleep(3)

        pyautogui.click(firth_acc)
        print(f"Нажали на firth_acc")
        time.sleep(3)

        pyautogui.click(stop_coor)
        print(f"Нажали на stop_coor")
        time.sleep(5)

        pyautogui.click(tri_tochki5)
        print(f"Нажали на Три точки")
        time.sleep(3)

        pyautogui.click(open_steam5)
        print(f'Нажал на open_steam')
        time.sleep(90)

        pyautogui.doubleClick(open_pubg)
        print(f"Запустил pubg")
        time.sleep(120)

        pyautogui.doubleClick(click_panel)
        print(f"Клик по панели")
        time.sleep(3)

        pyautogui.click(fifth_acc)
        print(f"Нажали на fifth_acc")
        time.sleep(3)

        pyautogui.click(stop_coor)
        print(f"Нажали на stop_coor")
        time.sleep(5)

        account_counter += 1

        print(account_counter)
        if account_counter % 1 == 0:
            pyautogui.click(nextpg_coor)
            print(f"Нажали на координаты для смены страницы: nextpg_coor")
            time.sleep(10)









