import pyautogui  # install via pip install pyautogui
import pygame  # install via pip install pygame
import threading
import queue
import os

script = 'USB Dual handle controller "support" for JR EAST Train Simulator version:'
version = '[0.5.0]'
pyautogui.PAUSE = 0  # Lowest possible delay before the game starts dropping key presses.
pygame.init()
clock = pygame.time.Clock()

joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
joystick_list = []
joyid = "joyid"
joyname = "joyname"

qMascon = queue.Queue()
qButton = queue.Queue()

for i in range(pygame.joystick.get_count()):
    jid = {joyid: i, joyname: pygame.joystick.Joystick(i).get_name()}
    joystick_list.append(jid)
mascon_select = next((i for i, item in enumerate(joystick_list) if item["joyname"] == "HID Interface"),
                     None)

if mascon_select is None:
    print('########################################################################################')
    print("# No matching controller found. Connect the correct controller and restart the script")
    print('########################################################################################')
    exit()

brake_counter = 15
power_counter = 5
pygame.event.clear()  # Clear events to remove wrong inputs.


def menu():
    clearscreen()
    print('########################################################################################')
    print(f'# {script}{version}')
    print('#')
    print('# Make sure that the power lever is in the OFF position.')
    print('# Start the game and use the EB notch to sync the controller once you are in the train.')
    print('# Do NOT use both levers at the same time when driving a single lever train.')
    print('# Press CTRL + C to end the script.')



def clearscreen():
    os.system('clear')


def brake_inc():
    pyautogui.keyDown('.')
    pyautogui.keyUp('.')


def brake_dec():
    pyautogui.keyDown(',')
    pyautogui.keyUp(',')


def brake_eb():
    pyautogui.keyDown('1')  # Set brake to EB
    pyautogui.keyUp('1')
    pyautogui.keyDown('/')  # Set brake to EB
    pyautogui.keyUp('/')


def pneutral():
    pyautogui.keyDown('s')
    pyautogui.keyUp('s')


def bneutral():
    pyautogui.keyDown('m')
    pyautogui.keyUp('m')


def power_inc():
    pyautogui.keyDown('z')  # Power up
    pyautogui.keyUp('z')


def power_dec():
    pyautogui.keyDown('a')  # Power down
    pyautogui.keyUp('a')


def button_a():
    pyautogui.keyDown('c')
    pyautogui.keyUp('c')


def button_b():
    pyautogui.keyDown('backspace')
    pyautogui.keyUp('backspace')


def button_c():
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')


def button_d():
    pyautogui.keyDown('e')


def button_select():
    pyautogui.keyDown('left')
    pyautogui.keyUp('left')


def button_start():
    pyautogui.keyDown('right')
    pyautogui.keyUp('right')


def wmascon():
    while True:
        item1 = qMascon.get()
        item1()
        qMascon.task_done()


def wbutton():
    while True:
        item2 = qButton.get()
        item2()
        qButton.task_done()

menu()

try:

    threading.Thread(target=wmascon, daemon=True).start()
    threading.Thread(target=wbutton, daemon=True).start()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                # Lever section
                mascon_axis_b = (joysticks[mascon_select].get_axis(0))
                mascon_axis_b = (round(mascon_axis_b, 2))
                mascon_axis_p = (joysticks[mascon_select].get_axis(1))
                mascon_axis_p = (round(mascon_axis_p, 2))

                if mascon_axis_p == -1.0 and power_counter != 0:
                    qMascon.put(power_inc)
                    power_counter = 0
                    
                if mascon_axis_p == -0.74 and power_counter != 1:
                    if power_counter == 2:
                        qMascon.put(power_inc)
                        power_counter = 1
                        
                    if power_counter == 0:
                        qMascon.put(power_dec)
                        power_counter = 1

                if mascon_axis_p == -0.51 and power_counter != 2:
                    if power_counter == 3:
                        qMascon.put(power_inc)
                        power_counter = 2

                    if power_counter == 1:
                        qMascon.put(power_dec)
                        power_counter = 2
                        
                if mascon_axis_p == -0.34 and power_counter != 3:
                    if power_counter == 4:
                        qMascon.put(power_inc)
                        power_counter = 3
                        
                    if power_counter == 2:
                        qMascon.put(power_dec)
                        power_counter = 3
                        
                if mascon_axis_p == -0.15 and power_counter != 4:
                    if power_counter == 5:
                        qMascon.put(power_inc)
                        power_counter = 4
                        
                    if power_counter == 3:
                        qMascon.put(power_dec)
                        power_counter = 4
                        
                if mascon_axis_p == 0.0 and power_counter != 5:
                    qMascon.put(pneutral)
                    power_counter = 5
                # ------------------Lever border------------------ #
                if mascon_axis_b == -1.0 and brake_counter != 6:
                    qMascon.put(bneutral)
                    brake_counter = 6

                if mascon_axis_b == 0.12 and brake_counter != 7:
                    if brake_counter == 6:
                        qMascon.put(brake_inc)
                        brake_counter = 7
                    if brake_counter == 8:
                        qMascon.put(brake_dec)
                        brake_counter = 7

                if mascon_axis_b == 0.2 and brake_counter != 8:
                    if brake_counter == 7:
                        qMascon.put(brake_inc)
                        brake_counter = 8
                    if brake_counter == 9:
                        qMascon.put(brake_dec)
                        brake_counter = 8

                if mascon_axis_b == 0.24 and brake_counter != 9:
                    if brake_counter == 8:
                        qMascon.put(brake_inc)
                        brake_counter = 9
                    if brake_counter == 10:
                        qMascon.put(brake_dec)
                        brake_counter = 9

                if mascon_axis_b == 0.3 and brake_counter != 10:
                    if brake_counter == 9:
                        qMascon.put(brake_inc)
                        brake_counter = 10
                    if brake_counter == 11:
                        qMascon.put(brake_dec)
                        brake_counter = 10

                if mascon_axis_b == 0.35 and brake_counter != 11:
                    if brake_counter == 10:
                        qMascon.put(brake_inc)
                        brake_counter = 11
                    if brake_counter == 12:
                        qMascon.put(brake_dec)
                        brake_counter = 11

                if mascon_axis_b == 0.4 and brake_counter != 12:
                    if brake_counter == 11:
                        qMascon.put(brake_inc)
                        brake_counter = 12
                    if brake_counter == 13:
                        qMascon.put(brake_dec)
                        brake_counter = 12

                if mascon_axis_b == 0.42 and brake_counter != 13:
                    if brake_counter == 12:
                        qMascon.put(brake_inc)
                        brake_counter = 13
                    if brake_counter == 14:
                        qMascon.put(brake_dec)
                        brake_counter = 13

                if mascon_axis_b == 0.44 and brake_counter != 14:
                    if brake_counter == 13:
                        qMascon.put(brake_inc)
                        brake_counter = 14
                    if brake_counter == 15:
                        qMascon.put(brake_dec)
                        brake_counter = 14

                if mascon_axis_b == 0.47 and brake_counter != 15:
                    qMascon.put(brake_eb)
                    brake_counter = 15

            # Button section
            if event.type == pygame.JOYBUTTONDOWN and event.button == 0:  # Back
                qButton.put(button_b)
            if event.type == pygame.JOYBUTTONDOWN and event.button == 1:  # Camera
                qButton.put(button_a)
            if event.type == pygame.JOYBUTTONDOWN and event.button == 2:  # Confirm
                qButton.put(button_c)
            if event.type == pygame.JOYBUTTONDOWN and event.button == 3:  # DMS
                qButton.put(button_d)

            if event.type == pygame.JOYBUTTONDOWN and event.button == 4:  # Left
                qButton.put(button_select)
            if event.type == pygame.JOYBUTTONDOWN and event.button == 5:  # Right
                qButton.put(button_start)

            clock.tick_busy_loop(120)
except KeyboardInterrupt:
    pass
