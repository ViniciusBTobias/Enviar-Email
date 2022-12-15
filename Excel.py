import pyautogui
import time


    #Pagina inicial
pyautogui.hotkey('winleft','d')

    #Abrir excel
pyautogui.moveTo(128,132)
pyautogui.click()
pyautogui.click()
time.sleep(0.5)

pyautogui.PAUSE = 0.5

    #Selecionar planilha
pyautogui.moveTo(208,688)
pyautogui.click()
time.sleep(0.5)

    #Abrir printer
pyautogui.moveTo(578,740)
pyautogui.click()

pyautogui.moveTo(87,87)
pyautogui.click()

    #Cordenadas
pyautogui.moveTo(25,225)
pyautogui.mouseDown()

pyautogui.moveTo(893,677)
pyautogui.mouseUp()

    #Copiar print
time.sleep(0.5)
pyautogui.hotkey('ctrl','c')
time.sleep(0.5)

    #Fechar pagina do printer
pyautogui.moveTo(825,52)
pyautogui.click()
time.sleep(0.5)

    #Abrir Google
pyautogui.moveTo(664,743)
pyautogui.click()
time.sleep(0.5)

    #Abrir Gmail
pyautogui.moveTo(21,14)
pyautogui.click() 
time.sleep(0.5)

    #Escrever email
pyautogui.moveTo(63,158)
pyautogui.click()
time.sleep(0.5)

    #Nome do email
pyautogui.write('Email')
pyautogui.press('enter')
time.sleep(0.5)

    #Enviar email +  assunto                 
pyautogui.press('tab')
pyautogui.write('Assunto do email.')
pyautogui.press('tab')
pyautogui.write('Descrição do email')
pyautogui.press('enter')

    #Copiar print
pyautogui.hotkey('ctrl','v')
time.sleep(0.5)
                                                    
    #Enviar o email
pyautogui.moveTo(836,691)
pyautogui.click()