import pyautogui
import time
i = 0
# while True:
#   x, y = pyautogui.position()
#   time.sleep(2)
#   print(f"Posição do mouse: ({x}, {y})")

grayscale = 0.8  # Tolerância de cor
opacity = 0.9  # Opacidade mínima da imagem

while i <= 25:
    time.sleep(3)
    x = 133
    y = 546
    time.sleep(0.7)
    pyautogui.click(x, y)
    x = 326
    y = 499
    time.sleep(0.8)
    pyautogui.click(x, y)
    x = 687
    y = 361
    time.sleep(1.3)
    pyautogui.click(x, y)
    # localizar pixel usando imagem
    while True:
        image_pos = pyautogui.locateOnScreen('./captura.png', grayscale=grayscale, confidence=opacity)
        if image_pos:
            x, y, width, height = image_pos
            time.sleep(1)
            pyautogui.click(x, y)
            print(f"A imagem está na tela nas coordenadas ({x}, {y}), com largura {width} e altura {height}.")
            break
        else:
            print("A imagem não foi encontrada na tela.")
    x = 1027
    y = 168
    time.sleep(1.2)
    pyautogui.click(x, y)
    x = 961
    y = 637
    time.sleep(1)
    pyautogui.click(x, y)
    time.sleep(78)
    i += 1
    if i == 25:
        break



