import cv2
import os

# Datos = "n"   # Negativos
Datos = "p"     # Positivos
if not os.path.exists(Datos):
    print("Carpeta creada: ", Datos)
    os.makedirs(Datos)

cap = cv2.VideoCapture(0)

x1, y1 = 190, 80
x2, y2 = 450, 398

count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    imAux = frame.copy()
    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

    objeto = imAux[y1:y2, x1:x2]
    objeto = cv2.resize(objeto, (38, 38), interpolation=cv2.INTER_CUBIC)

    k = cv2.waitKey(1)
    if k == ord("s"):
        cv2.imwrite(Datos+'/objeto_{}.jpg'.format(count), objeto)
        print('Imagen guardada:' + '/objeto_{}.jpg'.format(count))
        count = count + 1

    if k == 27:
        break

    cv2.imshow("frame", frame)
    cv2.imshow("objeto", objeto)


cap.release()
cv2.destroyAllWindows()
