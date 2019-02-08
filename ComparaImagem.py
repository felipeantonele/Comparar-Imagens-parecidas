from skimage.measure import compare_ssim as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
import csv
import pandas
from skimage import img_as_float
from PIL import Image


def resize(link_image1, link_image2):
	# Aqui ser· redimensionado as imagens para mesmo tamanho - Distorcendo a imagem se necess·rios
	# Caso n„o queira que distorÁa, sÛ alterar o mÈtodo de calculo abaixo
    # Abrindo as imagen
    image1 = Image.open(link_image1)
    image2 = Image.open(link_image2)
    # analisando o tamanho da imagem1
    if image1.size[0] >= image2.size[0]:
        size_x = image1.size[0]
    else:
        size_x = image2.size[0]
    # analisando o tamanho da imagem1
    if image1.size[1] >= image2.size[1]:
        size_y = image1.size[1]
    else:
        size_y = image2.size[1]
    size = size_x, size_y
    image1 = image1.resize(size)
    image2 = image2.resize(size)
    return image1, image2


def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err


def compare_images(imageA, imageB,link_image1,link_image2):
    m = mse(imageA, imageB)
    s = ssim(imageA, imageB)
    with open(r'resultados.txt',
              'a') as txtfile:
        texto_write = str("\"") + str(link_image1) + str("\";\"") + str(link_image2) + str("\";\"") + str(m) + str("\";\"") + str(
            s) + str("\"")
        print(texto_write)
        txtfile.write(texto_write + "\r\n")
        txtfile.close()


pasta = str(r'C:\Users\eduardo.droubi\Desktop\Tracbel\Imagem\FUNDO BRANCO\Planilha de Cadastro')
linkcsvleva2 = pasta + str(r'\Leva2.csv')
linkcsvsb = pasta + str(r'\Compara√ß√£oSemFundoBranco.csv')
try:
    with open(linkcsvleva2, 'r', encoding='utf-8', errors='ignore') as lv2:
        reader_lv2 = csv.reader(lv2)
        for r_lv2 in reader_lv2:
            link_image1 = pasta + str(r'\Leva 2') + chr(92) + r_lv2[0]
            with open(linkcsvsb, 'r', encoding='utf-8', errors='ignore') as sb:
                reader_sb = csv.reader(sb)
                for r_sb in reader_sb:
                    link_image2 = pasta + str(r'\SEM FUNDO BRANCO') + chr(92) + r_sb[0]
                    image1, image2 = resize(link_image1,link_image2)
                    # image1 = cv2.imread(link_image1)
                    # image2 = cv2.imread(link_image2)
                    image1 = cv2.cvtColor(np.array(image1), cv2.COLOR_BGR2GRAY)
                    image2 = cv2.cvtColor(np.array(image2), cv2.COLOR_BGR2GRAY)
                    compare_images(image1, image2,link_image1,link_image2)
except:
    print("Fudeu")

