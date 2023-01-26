from django.shortcuts import render
from django.http import HttpResponse
from .models import Myfiles
from pytesseract import pytesseract
import pytesseract
from PIL import Image
import img2pdf

from langdetect import detect
from langdetect import detect_langs


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

custom_config = r'-l hin+eng --oem 3 --psm 6'


# Create your views here.

def home(request):


    return render(request,'home.html')
def imagetotext(request):
    if request.method =='POST':
        image1 = request.FILES.getlist('file')
        text = []
        count = 0
        for f in image1:
            im1 = Image.open(f)
            text1 = pytesseract.image_to_string(im1, config=custom_config)
            text.append(text1)
            Myfiles(file=f).save()

        return render(request,'image.html',{'text':text,'count':count})

    return render(request,'imagetotext.html')
def image(request):
    return render(request, 'image.html')
