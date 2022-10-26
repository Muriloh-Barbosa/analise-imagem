import cv2

capturaimagem = cv2.VideoCapture(0)

while True:
    imagem, frame = capturaimagem.read()

    cv2.imshow("Imagem camera", frame)

    if cv2.waitkey(0) == ord("p"): #Linha para finalizar o programa, utilizando a tecla p.
        break


capturaimagem.release()
cv2.destroyAllWindows()










