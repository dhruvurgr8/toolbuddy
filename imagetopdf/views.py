from django.shortcuts import render
import img2pdf

# Create your views here.

def image2pdf(request):
    if request.method =='POST':
        image1 = request.FILES.getlist('file')
        li = []
        for img in image1:
            li.append(img)
        img = [im for im in li]
        pdf = img2pdf.convert(img)

        with open("static/mypdf.pdf", "wb") as file:
            file.write(pdf)
        return render(request,'image2pdf/showpdf.html')
    return render(request, 'image2pdf/image2pdf.html')



