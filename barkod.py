import cv2
import time
from pyzbar.pyzbar import decode


cap = cv2.VideoCapture(0)
cap.set(3, 640) # - width
cap.set(4, 480) # height
valid_codes = []
used_codes = []

camera = True
while camera == True:
    success, Frame = cap.read()

    for code in decode(Frame):
        if code.data.decode('utf-8') not in used_codes:
            print('Kod okundu!.'"Giri� yap�ld�")
            print(code.data.decode("utf-8"))
            used_codes.append(code.data.decode('utf-8'))
            time.sleep(2)
        elif code.data.decode('utf-8')  in used_codes: 
            print("bu kod kullan�lm��t�r.")
            time.sleep(2)
        else:
            pass

    cv2.imshow("testing-code-scan", Frame)
    cv2.waitKey(1)