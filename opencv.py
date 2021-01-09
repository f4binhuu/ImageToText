import cv2
import glob
import requests
import matplotlib.pyplot as plt
import pytesseract
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

for path in glob.glob("C:\\Users\\Fabio\\Desktop\\opencv\\files\\*.jpg"):
    image = cv2.imread(path)
    #ax1 = plt.subplots(figsize=(20,10))
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    bwimage = cv2.threshold(gray_image,200,255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    #cv2.imshow('teste', bwimage)
    #cv2.waitKey(0)


    custom_config = r'--oem 3 --psm 6'
    details = pytesseract.image_to_data(gray_image, output_type=Output.DICT, config=custom_config, lang='eng')
    print(details.keys())
    
    #text = pytesseract.image_to_string(gray_image)
    #print(text)