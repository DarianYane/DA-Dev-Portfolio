from django.shortcuts import render, redirect
from PyPDF2 import *
# In order to upload a file
from django.core.files.storage import FileSystemStorage
# In order to create the PDF file
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa #Import pisa to render the PDF
from django.views import View
from django.http import HttpResponse

# Create your views here.
def upload(request):
    """ Upload the original pdf  """
    if request.method == 'POST' and request.FILES['myfile']: # myfile is the file in the form
        myfile = request.FILES['myfile']
        fs = FileSystemStorage() # we generate the FileSystemStorage object here
        global filename # this is the variable that I am going to optimize in the other view, that's why I make it global
        filename = fs.save(myfile.name, myfile) # we save the file with the name of the file, and the second parameter is the file itself
        return redirect(f2_bolded)
        print(filename)
    return render(request, "fastReading/upload.html")

def wipuf(request):
    # TODO
    """ Upload the original pdf  
    if request.method == 'POST' and request.FILES['myfile']: # myfile is the file in the form
        myfile = request.FILES['myfile']
        fs = FileSystemStorage() # we generate the FileSystemStorage object here"""

    global filename # this is the variable that I am going to optimize in the other view, that's why I make it global
    filename = "What_Is_Python_Used_For_-_A_Beginners_Guide.pdf" # we save the file with the name of the file, and the second parameter is the file itself
    return redirect(f2_bolded)


def f2_bolded(request):
	# Optimize the uploaded PDF """
    global b_text
    b_text = ""
    count = 0
    print(filename)
    file = "media/"+filename
    print(file)
    reader = PdfReader(file)
    number_of_pages = len(reader.pages)
    text = ""
    for x in range(0,number_of_pages):
        page = reader.pages[x]
        text += page.extract_text()

	# The following process can still be optimized
    letters = "qwertyuiopasdfghjklñzxcvbnmáéíóú"
    numbers = "0123456789"
    finals = ".?!"
    n = "no"
    for i in text:
        if n == "yes":
            if i.isupper():
                b_text += "</p>"
                n = "no"
        min = i.lower()
        n = "no"
        if i == " ":
            if b_text[-1] == " ":
                continue
            else:
                if count == 1:
                    b_text += "</b>"
                b_text += i
                count = 0
                continue
        if i == "\n":
            n = "yes"
            if b_text[-1] in finals:
                b_text += "<p>"
                continue
            else:
                if b_text[-2] in finals:
                    b_text += "<p>"
                    continue
                else:
                    continue

        if i == ",":
            if b_text[-1] == " ":
                b_text = b_text[:-1]
        if min in letters or i in numbers:
            if count >= 2:
                b_text += i
                count +=1
            if count == 1:
                b_text += i
                b_text += "</b>"
                count +=1
            if count == 0:
                b_text += "<b>"
                b_text += i
                count +=1
        else:
            if count == 1:
                b_text += "</b>"
            b_text += i
            count = 0

    global context
    context = {'b_text': b_text}
    return render(request,"fastReading/optimized.html",context)


def render_to_pdf(template_src, context_dict={}):
	""" Create the optimized PDF file """
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None


class DownloadPDF(View):
	""" Automaticly downloads  the optimized text to a new PDF file """
	def get(self, request, *args, **kwargs):
		pdf = render_to_pdf("fastReading/pdf_template.html", context)
		response = HttpResponse(pdf, content_type='application/pdf') # The response is internal and then I use it to create the PDF.
		content = "attachment; filename=%s" %(filename)
		response['Content-Disposition'] = content
		return response # Here you download the PDF