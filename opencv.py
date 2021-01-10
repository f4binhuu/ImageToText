from __future__ import print_function
import cv2
import glob
import requests
import matplotlib.pyplot as plt
import pytesseract
from pytesseract import Output
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


# for path in glob.glob(r"C:\Users\Fabio\Desktop\Dev\Python\opencv\files\*.jpg"):
#     image = cv2.imread(path)
#     #ax1 = plt.subplots(figsize=(20,10))
#     gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     bwimage = cv2.threshold(gray_image,200,255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
#     #cv2.imshow('teste', bwimage)
#     #cv2.waitKey(0)
#     custom_config = r'--oem 3 --psm 6'
#     details = pytesseract.image_to_data(gray_image, output_type=Output.DICT, config=custom_config, lang='eng')
#     print(details.keys())

alpha = 0.5

# raw_input = input
# print(type(raw_input))
# print('Enter alpha')
input_alpha = float('0.5'.strip())

if 0 <= alpha <=1:
    alpha = input_alpha

src1 = cv2.imread(cv2.samples.findFile(r"C:\Users\Fabio\Desktop\Dev\Python\opencv\pic1.jpg"))
src2 = cv2.imread(cv2.samples.findFile(r"C:\Users\Fabio\Desktop\Dev\Python\opencv\pic2.jpg"))
beta = (1.0 - alpha)
dst = cv2.addWeighted(src1, alpha, src2, beta, 0.0)
gray_image = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
bwimage = cv2.threshold(gray_image,200,255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
custom_config = r'--oem 3 --psm 11'

# cv2.imshow('teste', gray_image)
# cv2.waitKey(0)
# details = pytesseract.image_to_data(gray_image, output_type=Output.DICT, config=custom_config, lang='eng')
# print(details.keys())

text = pytesseract.image_to_string(gray_image,  config=custom_config, lang='eng')
split = text.split('\n')
maior = max(split, key=len)

print(maior)

