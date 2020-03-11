import pyautogui, keyboard
import datetime

def click():
    while True:
        clock = datetime.datetime.today()
        pyautogui.mouseDown(x=960, y=540)

        try:
            if keyboard.is_pressed(stop_button):
                pyautogui.mouseUp(x=960, y=540)
                print("Время остановки программы: " + str(clock.hour) + "ч " + str(clock.minute) + "мин")
                break
        except:
            break


start_button = 'up'
stop_button = 'down'

keyboard.add_hotkey(start_button, lambda: click())

keyboard.wait('n')
