from django.shortcuts import render
from PyPDF2 import PdfReader
# Create your views here.
def pdf2text(request):
    if request.method == "POST":
        text = ""
        file = request.FILES.getlist('file')
        for files in file:
            reader = PdfReader(files)
            l = len(reader.pages)
            for i in range(l):
                texted = reader.pages[i].extract_text()
                text+=texted
                with open("static/mytext.txt","w",encoding="utf-8") as file:
                    file.write(text)
                    print(text)
        return render(request,'pdf2text/showtext.html',{'text':text})

    return render(request,"pdf2text/pdf2text.html")
