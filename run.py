from check import *
from conditions import *
from options import *
import pyautogui
import time
import keyboard

# Tempo de intervalo (segundos)
intervalo = 0.53

executando = True

start_tibia_window()

while executando:
    window_check = verify_tibia_window()

    if window_check:
        hp_result_raw, mp_result_raw, not_tibia = status_check()

        if not_tibia:
            if hp_result_raw > 0:
                hp_result = hp_result_raw
            else:
                hp_result = 0

            if mp_result_raw > 0:
                mp_result = mp_result_raw
            else:
                mp_result = 0

            print("precisa de HP:", hp_result)
            print("precisa de MP:", mp_result)

            if (hp_result / hp_max) > 0.40 and (hp_result / hp_max) < 0.62:
                pyautogui.press(at_ultimate_hp)
            elif (hp_result/hp_max) > 0.62:
                pyautogui.press(at_supreme_hp)
            elif mp_result > strong_mana:
                pyautogui.press(at_strong_mana)

            if (mp_result/mp_max) < 0.75:
                if hp_result > exura_ico:
                    pyautogui.press(at_exura_ico)

    # Espera o intervalo de tempo
    time.sleep(intervalo)

    if keyboard.is_pressed('f9'):
        print("Tecla 'f9' pressionada. Parando o loop.")
        executando = False
