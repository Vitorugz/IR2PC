import pyautogui
import keyboard
import serial
import time
import os
import threading
from UI.UI import Interface

# Defining commands
commands = {
    # Movement
    'E17A38C7': 'right',
    'E17AD827': 'left',
    'E17A30CF': 'down',
    'E17AD02F': 'up',

    # Sound
    'E17AF807': 'volumemute',
    'E17A708F': 'volumedown',
    'E17AB04F': 'volumeup',

    # Shortcuts
    'E17A6897': 'shutdown',
    'E17A18E7': 'explorer',
    'E17A9C63': 'youtube',
    'E17A9867': 'email',
    'E17A48B7': 'opera',
    'E17A04FB': 'code',
    'E17A7887': 'time',

    # Keyboard
    'E17A58A7': 'shift_down',
    'E17A08F7': 'shift_up',
    'E17A8877': 'backspace',
    'E17A50AF': 'close',
    'E17AA857': 'enter',
    'E17AE817': 'win',

    # Numbers
    'E17A00FF': '0',
    'E17A807F': '1',
    'E17A40BF': '2',
    'E17AC03F': '3',
    'E17A20DF': '4',
    'E17AA05F': '5',
    'E17A609F': '6',
    'E17AE01F': '7',
    'E17A10EF': '8',
    'E17A906F': '9',

    # Alternate
    'E17AB847': 'toggle_mode',
    'FFFFFFFF': 'repeat'
}

def perform_action(action, mode):
    if action in ['up', 'down', 'left', 'right']:
        if mode == 0:
            pyautogui.press(action)
        else:
            offset = 15
            moves = {
                'up': (0, -offset),
                'down': (0, offset),
                'left': (-offset, 0),
                'right': (offset, 0)
            }
            pyautogui.moveRel(*moves[action])

    elif action in ['volumeup', 'volumedown', 'volumemute']:
        pyautogui.press(action)

    elif action == 'enter':
        pyautogui.press('enter') if mode == 0 else pyautogui.click()

    elif action == 'shift_down':
        pyautogui.keyDown('shift')
    elif action == 'shift_up':
        pyautogui.keyUp('shift')
    elif action == 'backspace':
        pyautogui.press('backspace')
    elif action == 'close':
        pyautogui.hotkey('alt', 'f4')
    elif action == 'win':
        pyautogui.press('win')

    elif action.isdigit():
        keyboard.write(action)

    elif action == 'shutdown':
        os.system('shutdown /s /t 1')
    elif action == 'explorer':
        pyautogui.hotkey('win', 'e')
    elif action == 'opera':
        os.system('start opera')
    elif action == 'youtube':
        os.system('start opera https://www.youtube.com')
    elif action == 'email':
        os.system('start opera https://www.gmail.com')
    elif action == 'time':
        os.system('start opera https://time.is')
    elif action == 'code':
        os.system('start code')

def arduino_loop():
    last_command = ''
    mode = 1  # 0 = teclado, 1 = mouse

    while True:
        try:
            data = arduino.readline().decode().strip()
            if not data:
                continue

            if data == 'E17ACC33':
                ui.close()

            if data in commands:
                command = commands[data]

                if command == 'toggle_mode':
                    mode = 1 - mode  # alterna entre 0 e 1
                    ui.var_mode.set(f"Current Mode: {['Keyboard', 'Mouse'][mode]}")
                    continue

                if command == 'repeat' and last_command:
                    perform_action(commands[last_command], mode)
                elif command != 'repeat':
                    perform_action(command, mode)
                    last_command = data
                    ui.var_last_command.set(f"Last Command: {data}")
                    ui.var_last_action.set(f"Last Action: {command}")

            time.sleep(0.05)
        except KeyboardInterrupt:
            print("\nEncerrando script.")
            break
        except Exception as e:
            print(f"Erro: {e}")

# Iniciar a interface
ui = Interface()

# Conectar ao Arduino
arduino = serial.Serial('COM3', 9600, timeout=1)

# Iniciar a thread de leitura do Arduino
arduino_thread = threading.Thread(target=arduino_loop)
arduino_thread.daemon = True
arduino_thread.start()

# Iniciar a interface (NA THREAD PRINCIPAL)
ui.run()