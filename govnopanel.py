
# import autoit
# import os
# import time
# import json
# import subprocess
# from steampy.guard import generate_one_time_code
# import threading
# import keyboard

# STEAM_PATH = r"C:\Program Files (x86)\Steam\steam.exe"
# PUBG_PATH = r"C:\Users\typoi\OneDrive\Рабочий стол\PUBG BATTLEGROUNDS.url"
# MAFILES_DIR = "MaFiles"
#
#
#
#
# paused = False
#
# def pause_listener():
#     global paused
#     while True:
#         if keyboard.is_pressed('down'):
#             paused = True
#             print("Пауза... Нажмите '⬆️' для продолжения")
#             while paused:
#                 if keyboard.is_pressed('up'):
#                     paused = False
#                     print("Продолжаем...")
#                     break
#         time.sleep(0.1)


# threading.Thread(target=pause_listener, daemon=True).start()


# def get_shared_secret(login):
#     for filename in os.listdir(MAFILES_DIR):
#         if filename.endswith(".maFile"):
#             file_path = os.path.join(MAFILES_DIR, filename)
#             with open(file_path, "r") as file:
#                 data = json.load(file)
#                 if data.get("account_name") == login:
#                     return data.get("shared_secret")
#
#
# def open_pubg():
#     os.startfile(PUBG_PATH)
#     print("PUBG запущен")
#
#
# def kill_steam():
#     subprocess.run(["taskkill", "/IM", "steam.exe", "/F"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
#     print("Steam закрыт")
#
#
# with open("logpass.txt", "r") as f:
#     accounts = [line.strip().split(":") for line in f.readlines()]
#
#
# for login, password in accounts:
#     print(f"Запуск аккаунта: {login}")
#
#     while paused:
#         time.sleep(0.1)
#     shared_secret = get_shared_secret(login)
#     if not shared_secret:
#         print(f"Ошибка: Не найден shared_secret для {login}, пропускаем аккаунт.")
#         continue
#
#     while paused:
#         time.sleep(0.1)
#     os.startfile(STEAM_PATH)
#     time.sleep(15)
#
#     while paused:
#         time.sleep(0.1)
#     autoit.send(login)
#     autoit.send("{TAB}")
#     autoit.send(password)
#     autoit.send("{ENTER}")
#     time.sleep(10)

# shared_secret="iEoZxdZvxHLubgwuI2C9ZTlbF2E="

    # while paused:
    #     time.sleep(0.1)
# guard_code = generate_one_time_code(shared_secret)
# print(f"Guard код: {guard_code}")
    # autoit.send(guard_code)
    # autoit.send("{ENTER}")
    # time.sleep(10)
    #
    # while paused:
    #     time.sleep(0.1)
    # open_pubg()
    # time.sleep(90)
    #
    # while paused:
    #     time.sleep(0.1)
    # kill_steam()
    #
    # print(f"Аккаунт {login} завершил работу")
    # time.sleep(20)










# import autoit
# import os
# import time
# import json
# import subprocess
# import threading
# import keyboard
# import pygetwindow as gw
# from steampy.guard import generate_one_time_code
#
# STEAM_PATH = r"C:\Program Files (x86)\Steam\steam.exe"
# PUBG_PATH = r"C:\Users\typoi\OneDrive\Рабочий стол\PUBG BATTLEGROUNDS.url"
# MAFILES_DIR = "MaFiles"
#
# paused = False
#
#
# def pause_listener():
#     global paused
#     while True:
#         if keyboard.is_pressed('down'):
#             paused = True
#             print("Пауза... Нажмите '⬆️' для продолжения")
#             while paused:
#                 if keyboard.is_pressed('up'):
#
#                     paused = False
#                     print("Продолжаем...")
#                     break
#         time.sleep(0.1)
#
#
# threading.Thread(target=pause_listener, daemon=True).start()
#
#
# def get_shared_secret(login):
#     for filename in os.listdir(MAFILES_DIR):
#         if filename.endswith(".maFile") or filename.endswith(".mafile"):
#             file_path = os.path.join(MAFILES_DIR, filename)
#             with open(file_path, "r") as file:
#                 data = json.load(file)
#                 if data.get("account_name") == login.lower():
#                     return data.get("shared_secret")
#
#
# def wait_for_steam_window(timeout=30):
#     start_time = time.time()
#     while time.time() - start_time < timeout:
#         windows = gw.getWindowsWithTitle("Steam")
#         time.sleep(0)
#         if windows:
#             print("Окно Steam найдено!")
#             return True
#         time.sleep(1)
#     print("Ошибка: Окно Steam не появилось.")
#     return False
#
#
# def open_pubg():
#     os.startfile(PUBG_PATH)
#     print("PUBG запущен")
#
#
# def kill_steam():
#     subprocess.run(["taskkill", "/IM", "steam.exe", "/F"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
#     print("Steam закрыт")
#
#
# with open("logpass.txt", "r") as f:
#     accounts = [line.strip().split(":") for line in f.readlines()]
#
# for login, password in accounts:
#     print(f"Запуск аккаунта: {login}")
#
#     shared_secret = get_shared_secret(login)
#     if not shared_secret:
#         print(f"Ошибка: Не найден shared_secret для {login}, пропускаем аккаунт.")
#         continue
#
#     while paused:
#         time.sleep(0.1)
#     os.startfile(STEAM_PATH)
#     time.sleep(7)
#
#     if not wait_for_steam_window():
#         print("Ошибка: Окно Steam не открылось. Пропускаем аккаунт.")
#         continue
#
#     while paused:
#         time.sleep(0.1)
#     autoit.send(login)
#     autoit.send("{TAB}")
#     autoit.send(password)
#     autoit.send("{ENTER}")
#     time.sleep(7)
#
#     while paused:
#         time.sleep(0.1)
#     guard_code = generate_one_time_code(shared_secret)
#     print(f"Guard код: {guard_code}")
#     autoit.send(guard_code)
#     autoit.send("{ENTER}")
#     time.sleep(10)
#
#     # while paused:
#     #     time.sleep(0.1)
#     # open_pubg()
#     # time.sleep(20)
#     #
#     while paused:
#         time.sleep(0.1)
#     kill_steam()
#
#     print(f"Аккаунт {login} завершил работу")
#     time.sleep(20)


import autoit
import os
import time
import json
import subprocess
# import pyautogui
import threading
import keyboard
import pygetwindow as gw
from steampy.guard import generate_one_time_code

STEAM_PATH = r"C:\Program Files (x86)\Steam\steam.exe"
PUBG_PATH = r"C:\Users\typoi\OneDrive\Рабочий стол\PUBG BATTLEGROUNDS.url"
MAFILES_DIR = "MaFiles"


COORD_MENU = (1031, 177)
COORD_OPENER = (706, 716)
COORD_MAIN_OPENER = (956, 523)
COORD_MAIN_OPENER2 =(897, 754)

paused = False

def pause_listener():
    global paused
    while True:
        if keyboard.is_pressed('ctrl+down'):
            paused = True
            print("Пауза... Нажмите 'ctrl+⬆️' для продолжения")
            while paused:
                if keyboard.is_pressed('ctrl+up'):
                    paused = False
                    print("Продолжаем...")
                    break
        time.sleep(0.1)


threading.Thread(target=pause_listener, daemon=True).start()


def get_shared_secret(login):
    for filename in os.listdir(MAFILES_DIR):
        if filename.endswith(".maFile") or filename.endswith(".mafile"):
            file_path = os.path.join(MAFILES_DIR, filename)
            with open(file_path, "r") as file:
                data = json.load(file)
                if data.get("account_name") == login.lower():
                    return data.get("shared_secret")


def wait_for_active_steam_window(timeout=30):
    keywords = ["steam", "guard", "login", "update"]
    start_time = time.time()

    while time.time() - start_time < timeout:
        active_window = gw.getActiveWindow()
        if active_window:
            title = active_window.title.lower()
            if any(word in title for word in keywords):
                print(f"✅ Steam активно: {active_window.title}")
                return True
        time.sleep(1)

    print("❌ Окно Steam не активно или не найдено.")
    return False


def open_pubg():
    os.startfile(PUBG_PATH)
    print("PUBG запущен")


def kill_steam():
    subprocess.run(["taskkill", "/IM", "steam.exe", "/F"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("Steam закрыт")


with open("logpass.txt", "r") as f:
    accounts = [line.strip().split(":") for line in f.readlines()]


print("\nСписок аккаунтов:")
for idx, (login, _) in enumerate(accounts, start=1):
    print(f"{idx}. {login}")


start_index = input("\nС какого аккаунта начать? (например, 3): ")
try:
    start_index = int(start_index) - 1
    if start_index < 0 or start_index >= len(accounts):
        raise ValueError
    accounts = accounts[start_index:]
except ValueError:
    print("Неверный ввод. Запуск с первого аккаунта.\n")

for login, password in accounts:
    print(f"\nЗапуск аккаунта: {login}")

    shared_secret = get_shared_secret(login)
    if not shared_secret:
        print(f"Ошибка: Не найден shared_secret для {login}, пропускаем аккаунт.")
        continue

    while paused:
        time.sleep(0.1)
    os.startfile(STEAM_PATH)
    time.sleep(7)

    if not wait_for_active_steam_window():
        print("Ошибка: Окно Steam не открылось. Пропускаем аккаунт.")
        kill_steam()
        time.sleep(10)
        continue

    while paused:
        time.sleep(0.1)
    autoit.send(login)
    autoit.send("{TAB}")
    autoit.send(password)
    autoit.send("{ENTER}")
    time.sleep(7)

    while paused:
        time.sleep(0.1)
    guard_code = generate_one_time_code(shared_secret)
    print(f"Guard код: {guard_code}")
    autoit.send(guard_code)
    autoit.send("{ENTER}")
    time.sleep(15)

    while paused:
        time.sleep(0.1)
    os.startfile(PUBG_PATH)
    time.sleep(80)

    # while paused:
    #     time.sleep(0.1)
    # pyautogui.moveTo(COORD_MENU, duration=0.5)
    # time.sleep(2)
    # pyautogui.click()
    # time.sleep(3)
    # pyautogui.moveTo(COORD_OPENER, duration=0.5)
    # pyautogui.click()
    # time.sleep(6)
    #
    # while paused:
    #     time.sleep(0.1)
    # for opener in range(8):
    #     pyautogui.moveTo(COORD_MAIN_OPENER, duration=0.5)
    #     pyautogui.doubleClick()
    #     time.sleep(6)
    #     pyautogui.moveTo(COORD_MAIN_OPENER2, duration=0.5)
    #     pyautogui.doubleClick()
    #     time.sleep(6)

    while paused:
        time.sleep(0.1)
    kill_steam()

    print(f"Аккаунт {login} завершил работу")

    with open("made_accs.txt", "a", encoding="UTF-8") as done_file:
        done_file.write(f"{login}:{password} СДЕЛАН! \n")
    time.sleep(20)





# COORDINAT CHECKER

# from pynput.mouse import Listener
#
# def on_click(x, y, button, pressed):
#     if pressed:
#         print(f"Координаты: X={x}, Y={y}")
#
# with Listener(on_click=on_click) as listener:
#     listener.join()
# #
#
# import pyautogui
# import time
#
# COORD_MENU = (1031, 175)
# COORD_OPENER = (706, 716)
# COORD_MAIN_OPENER = (956, 523)
# COORD_MAIN_OPENER2 =(897, 754)
#
#
# pyautogui.moveTo(COORD_MENU,duration=0.5)
# time.sleep(2)
# pyautogui.click()
# time.sleep(3)
# pyautogui.moveTo(COORD_OPENER,duration=0.5)
# pyautogui.click()
# time.sleep(6)
# for opener in range(5):
#     pyautogui.moveTo(COORD_MAIN_OPENER,duration=0.5)
#     pyautogui.doubleClick()
#     time.sleep(6)
#     pyautogui.moveTo(COORD_MAIN_OPENER2,duration=0.5)
#     pyautogui.doubleClick()
#     time.sleep(6)
# time.sleep(120)