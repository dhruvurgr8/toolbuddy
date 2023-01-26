from django.shortcuts import render,HttpResponse
from PyPDF2 import PdfMerger


# Create your views here.
merger = PdfMerger()
def pdfmerger(request):
    pdf = []
    if request.method == "POST":
        file = request.FILES.getlist('file')
        for files in file:
            pdf.append(files)
        with open('static/merge.pdf','wb')as file:
            for data in pdf:
                merger.append(data)
            merger.write(file)
        return render(request,'pdfmerger/downloadpdf.html')
    return render(request,'pdfmerger/pdfmerger.html')
