import pyautogui
import keyboard


def monitor_keyboard_event(e):
    if e.name == 'p':
        x, y = pyautogui.position()
        print(f"A posição do mouse é X: {x}, Y: {y}")


# Registre a função `monitor_keyboard_event` para ser chamada quando a tecla 'p' for pressionada
keyboard.on_press(monitor_keyboard_event)

# Mantenha o programa em execução
# Aguarda a tecla "esc" ser pressionada para encerrar o programa
keyboard.wait('esc')
