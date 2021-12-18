import numpy as np
import cv2
import pyautogui

while True:
    image = pyautogui.screenshot(region=(68, 241, 175, 200))
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    blackPixel=np.sum(image<100)
    whitePixel=np.sum(image>100)

    cv2.imshow("Target", image)

    print("Number of black pixels",blackPixel)
    print("Number of white pixels",whitePixel)
    
    if whitePixel>200 and whitePixel<30000:
        pyautogui.press("up")
    if blackPixel>200 and blackPixel<30000:
        pyautogui.press("up")

    if cv2.waitKey(25) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break
