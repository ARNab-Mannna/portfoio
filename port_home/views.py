from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def index(request):
    return render(request,'findex.html')
    
# def dex(request):
#     return render(request,'index-2.html')
def dex(request):
    return render(request,'index.html')
def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        contact= Contact(name=name,email=email,subject=subject ,message=message)
        contact.save()
        return redirect("/")

    return render (request,'contact.html')




# # Import mimetypes module
# import mimetypes
# # import os module
# import os
# # Import HttpResponse module
# from django.http.response import HttpResponse


# def download_file(request):
#     # Define Django project base directory
#     BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     # Define text file name
#     filename = 'test.txt'
#     # Define the full file path
#     filepath = BASE_DIR + '/downloadapp/Files/' + filename
#     # Open the file for reading content
#     path = open(filepath, 'r')
#     # Set the mime type
#     mime_type, _ = mimetypes.guess_type(filepath)
#     # Set the return value of the HttpResponse
#     response = HttpResponse(path, content_type=mime_type)
#     # Set the HTTP header for sending to browser
#     response['Content-Disposition'] = "attachment; filename=%s" % filename
#     # Return the response value
#     return response



