from django.contrib import admin
from django.urls import path, include, re_path
from .views import * 
from . import views

urlpatterns = [

	path('',HomePage, name='home-page'),
    ######ชื่อhtml,จากview,ลิงค์base.html
	path('register/', Register, name='register-page'),
	path('editprofile/', EditProfile, name='editprofile-page'),
	path('documentAll/', ShowDocument, name='document-page'),
	path('document_1/', ShowDocument1, name='document_1-page'),
    path('document_2/', ShowDocument2, name='document_2-page'),
    path('document_3/', ShowDocument3, name='document_3-page'),
    path('document_4/', ShowDocument4, name='document_4-page'),
	path('document_5/', ShowDocument5, name='document_5-page'),
    path('document_6/', ShowDocument6, name='document_6-page'),
	path('document_x/', ShowDocumentx, name='document_x-page'),
	path('personalrecord/', PersonalRecord_add, name='personalrecord-page'),
    path('showprofile/', ShowProfile, name='showprofile-page'),
    path('QuizVolcab3/', QuizVolcab3Page, name='quizVolcab3-page'),
	path('QuizMath4normal/', QuizMath4normalPage, name='QuizMath4normal-page'),
	path('คณิตศาสตร์4/', MathClass4, name='คณิตศาสตร์4-page'),
	re_path(r'add/$',views.PersonalRecord_add,name='PersonalRecord_add'),
    path('math_normal_pdf/', math_normal_pdf, name='math_normal_pdf-page'),
    path('index/',index,name='index-page'),
    path('report',views.report),
	
]		