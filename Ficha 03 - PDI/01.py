import cv2
import numpy as np

# path = r'C:\Users\Rebec\Projetos\Ficha 03 - PDI\Dark_Moon.jpg'
# imagem = cv2.imread('Dark_Moon.jpg') #seleciona a imagem desejado
imagem = cv2.imread('Dark_Moon.jpg')
cv2.imgshow("Original", imagem)

y=0
x=0

#cv2_imshow(im) #mostra a imagem no programa

heigth = int(input("insira o valor da altura ", ))
width = int(input("insir o valor da largura ", ))
#dimensoes = (heigth, width)

#essa parte daqui é para redimensionar a imagem mas não é oque a questao pede
#image_resize = cv2.resize(imagem, dimensoes, interpolation = cv2.INTER_AREA)
#cv2_imshow(image_resize)
 
crop = imagem[y:y+heigth, x:x+width] 
cv2.imshow(crop, 'imagem')