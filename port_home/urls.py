
from django.urls import path
from .views import *
from .views2 import *
urlpatterns = [
    path('',index,name='home'),
    path('dex',dex,name='dex'),
    path('contact',contact,name='contact'),
    # path('download/', download_file),
    # path('downloadpdf/', download_pdf_file, name='download_pdf_file'),
    # path('downloadpdf//',download_pdf_file, name='download_pdf_file')
]
