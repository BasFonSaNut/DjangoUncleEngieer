from django.shortcuts import render,redirect
from django.views.generic import ListView
from urllib import response
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required  #ล็อคอินก่อนถึงจะดูได้
from django.core.files.storage import FileSystemStorage
from .models import *
from .forms import PersonalRecordForm
import random

############reportlab###################
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
pdfmetrics.registerFont(TTFont('F1','THSarabunNew.ttf'))
pdfmetrics.registerFont(TTFont('F2','THSarabunNew Bold.ttf'))
pdfmetrics.registerFont(TTFont('F3','THSarabunNew BoldItalic.ttf'))
pdfmetrics.registerFont(TTFont('F4','THSarabunNew Italic.ttf'))
from datetime import datetime


#######fpdf2##############################################
from django.shortcuts import render
from fpdf import FPDF
from django.http import FileResponse

def HomePage(request):
    return render(request,'school/home.html')





@login_required
def Register(request):

    if request.method == 'POST':
        data = request.POST.copy()
        first_name = data.get('first_name')#เก็บค่ามาจากhtmlขอให้ชื่อเหมือนกันกับหน้าregister.html
        last_name = data.get('last_name')#เก็บค่ามาจากhtmlขอให้ชื่อเหมือนกันกับหน้าregister.html
        email = data.get('email')
        student_user = data.get('student_user')
        password = data.get('password')#เก็บค่ามาจากhtmlขอให้ชื่อเหมือนกันกับหน้าregister.html
        newuser = User()
        newuser.username = student_user
        newuser.first_name = first_name
        newuser.last_name = last_name
        newuser.email = email
        newuser.student_user = student_user
        newuser.set_password(password)
        newuser.save()
        return redirect('register-page')#ไปใส่บรรทัดที่1ด้วย

    return render(request, 'school/register.html')




@login_required
def EditProfile(request):
    
    username = request.user.username
    current = User.objects.get(username=username)
    
    if request.method == 'POST' and request.FILES['photo_profile']:
        

        data = request.POST.copy()
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        # student_user = data.get('student_user') ไม่ให้โชuserในหน้าediteprofile
        # password = data.get('password')
        idcard_citizen = data.get('idcard_citizen')
        birthday = data.get('birthday')
        level = data.get('level')
        school_name = data.get('school_name')
        phone_number = data.get('phone_number')
        parent_name1 = data.get('parent_name1')
        parent_phone1 = data.get('parent_phone1')
        parent_name2 = data.get('parent_name2')
        parent_phone2 = data.get('parent_phone2')
        address = data.get('address')

        myprofile = User.objects.get(username=username)
        
        ###file system###########################################
        try:
            setprofile = Profile.objects.get(user=myprofile)
        except:
            setprofile = Profile()
            setprofile.user = myprofile
        file_image = request.FILES['photo_profile']
        file_image_name = request.FILES['photo_profile'].name
        fs = FileSystemStorage()   #location='media/photo_profile'
        filename = fs.save(file_image_name,file_image)
        upload_file_url = fs.url(filename)
        setprofile.photoprofile = upload_file_url[6:]
        setprofile.save()
        #########################################################

        # myprofile.username = student_user ไม่ให้โชuserในหน้าediteprofile
        myprofile.first_name = first_name
        myprofile.last_name = last_name
        myprofile.email = email
        myprofile.save()
        return redirect('showprofile-page')    
    context = {'data':current}    
    return render(request, 'school/editprofile.html',context)  
    


@login_required
def ShowExam(request):
    exames = Exam.objects.all()#ดึงค่ามาจากดาต้าเบสทั้งหมด
    context = {'exames' :exames}
    return render(request,'exam/showexam.html',{'exames':exames,})  



@login_required
def ShowDocument(request):
    document = DocumentTest.objects.all() #ดึงค่ามาจาก database ทั้งหมด
    context = {'document':document}
    return render(request, 'school/All_document_test/documentAll.html', context)
@login_required
def ShowDocument1(request):
    document = DocumentTest.objects.all() #ดึงค่ามาจาก database ทั้งหมด
    context = {'document':document}
    return render(request, 'school/All_document_test/document_1.html', context)
@login_required
def ShowDocument2(request):
    document = DocumentTest.objects.all() #ดึงค่ามาจาก database ทั้งหมด
    context = {'document':document}
    return render(request, 'school/All_document_test/document_2.html', context)
@login_required
def ShowDocument3(request):
    document = DocumentTest.objects.all() #ดึงค่ามาจาก database ทั้งหมด
    context = {'document':document}
    return render(request, 'school/All_document_test/document_3.html', context)
@login_required
def ShowDocument4(request):
    document = DocumentTest.objects.all() #ดึงค่ามาจาก database ทั้งหมด
    context = {'document':document}
    return render(request, 'school/All_document_test/document_4.html', context)
@login_required
def ShowDocument5(request):
    document = DocumentTest.objects.all() #ดึงค่ามาจาก database ทั้งหมด
    context = {'document':document}
    return render(request, 'school/All_document_test/document_5.html', context)
@login_required
def ShowDocument6(request):
    document = DocumentTest.objects.all() #ดึงค่ามาจาก database ทั้งหมด
    context = {'document':document}
    return render(request, 'school/All_document_test/document_6.html', context)
@login_required
def ShowDocumentx(request):
    document = DocumentTest.objects.all() #ดึงค่ามาจาก database ทั้งหมด
    context = {'document':document}
    return render(request, 'school/All_document_test/document_x.html', context)



@login_required
def ShowProfile(request):
    show_profile = Profile.objects.all()#ดึงค่ามาจากดาต้าเบสทั้งหมด
    context = {'show_profile' :show_profile}
    return render(request,'school/showprofile.html', context)

@login_required
def PersonalRecord_add(request):
    form = PersonalRecordForm
    if request.method == 'POST':        
       form = PersonalRecordForm(request.POST)
       if form.is_valid():
           personal = form.save(commit=False)
        #    personal.slug = slugify(personal.idcard_citizen)
           personal.save()
        #    messages.success(request, 'Save success')
           return redirect('showprofile-page')
        #    messages.error(request, 'Save failed')

            
    context = {'form' :form }
    return render(request, 'school/personalrecord.html', context)


def MathClass4(request):
    return render(request,'school/4course/คณิตศาสตร์4.html')

    

#########################################################################
def QuizVolcab3Page(request):
    questions = list(QuizVolcab3.objects.all())
    questions = random.sample(questions,1) ###ตัวเลขคือจำนวนrandomมาเท่าไหร่
    context = { 'questions': questions }
    return render(request, 'school/Allquiz/eng3/QuizVolcab3.html', context )


#############################################
def QuizMath4normalPage(request):
    questions = list(QuizMath4normal.objects.all())
    questions = random.sample(questions,1) ###ตัวเลขคือจำนวนrandomมาเท่าไหร่
    context = { 'questions': questions }
    return render(request, 'school/Allquiz/math4/QuizMath4normal.html', context )

###################fpdf##########################################
def index(request):

    context = {}

    return render(request, 'school/index.html', context = context)

def report(request):
    sales = [
        {"item": "Speaker", "amount": "$120,00"},
        {"item": "UPS", "amount": "$10,00"},
        {"item": "PS5", "amount": "$1 000 000,00"},
    ]
    pdf = FPDF('L', 'mm', 'A4')
    pdf.add_font('THSarabun', '', r'C:\Windows\Fonts\THSarabun.TTF', uni=True)
    # pdf.add_font('THSarabun', '', 'THSarabun.ttf', uni=True)
    pdf.add_page()
    pdf.set_font('THSarabun', '', 50)
    pdf.cell(40, 10, 'Customer Orderกกกกก :',0,1)
    pdf.cell(40, 10, '',0,1)
    pdf.set_font('courier', '', 12)
    pdf.cell(200, 8, f"{'Item'.ljust(50)} {'Amount'.rjust(20)}", 1, 1)
    pdf.line(10, 30, 150, 30)
    pdf.line(10, 38, 150, 38)
    for line in sales:
        pdf.cell(200, 8, f"{line['item'].ljust(50)} {line['amount'].rjust(20)}", 0, 1)
    pdf.output('report.pdf', 'F')
    return FileResponse(open('report.pdf', 'rb'), as_attachment=True, content_type='application/pdf')

#################################reportlab################

def math_normal_pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=A4, bottomup=0)
    
    
    ##page1#########################################
    #สเกล+
    c.drawString(1*cm,1*cm, "+")
    c.drawString(20*cm,1*cm, "+")
    c.drawString(1*cm,29*cm, "+")
    c.drawString(20*cm,29*cm, "+")
    ########       
    questions = list(QuizVolcab3.objects.all())
    questions = random.sample(questions,3)
    dt = datetime.now().strftime('%X %A-%d-%B-%Y ')
    
    
    lines = ["แบบฝึกหัด"]
    
    for q in questions:
        
        id_str = str(q.id)
        lines.append("(คำถาม).....................................................................................................................................รหัสคำถาม = [6.Quiz] ("+ id_str+")")
        lines.append("             "+q.question)
        lines.append("                  a.) "+q.option1)
        lines.append("                  b.) "+q.option2)
        lines.append("                  c.) "+q.option3)
        lines.append("                  d.) "+q.option4)
       
        # lines.append("รหัสคำถาม = [6.Quiz] ("+ id_str+")")
    c.drawString(12*cm,29*cm, dt)
    
    textob = c.beginText()
    textob.setTextOrigin(2*cm, 1*cm)
    textob.setFont('F4',16)
    for line in lines:
        textob.textLine(line)
    c.drawText(textob)
    c.showPage()    
     ##page2##################################################
   
    c.drawString(12*cm,29*cm, dt)
    c.showPage()
    
     ##page3##################################################

    ans1 = ["เฉลยแบบฝึกหัด"]
    for n in questions :
        id_n = str(n.id)
        ans1.append("คำตอบ = "+n.answer+".) "+n.des + "................[6.Quiz ("+ id_n+")]")


    
    c.drawString(12*cm,29*cm, dt)
    tob = c.beginText()
    tob.setTextOrigin(2*cm, 1*cm)   
    tob.setFont('F3',20)
    for line in ans1: ######เฉลย
        tob.textLine(line)
    c.drawText(tob)
    c.showPage()
    ####################################
  
    c.setTitle("MOTHERSHIP Project X")
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=False, filename='Test.pdf')



class QuizListView(ListView):
    model = Quiz 
    template_name = 'quizes/main.html'

def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, 'quizes/quiz.html', {'obj': quiz})


def ShowProfile(request):
    show_profile = Profile.objects.all()#ดึงค่ามาจากดาต้าเบสทั้งหมด
    context = {'show_profile' :show_profile}
    return render(request,'quizes/quiz.html', context)

def quiz_data_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)   
    
    #new line by me########
    questionsinfo = Question.objects.filter(quiz=pk)
    questionsinfo = list(questionsinfo.all())
    questionsinfo = random.sample(questionsinfo,5)######เอาหมดตัดบบรรทัดนี้ออีก 
    
    questions = []    
    for q in questionsinfo:
        qid = q.id
        ansx = Answer.objects.filter(question_id=qid) 
        answers = []
        answers2 = []
        for a in ansx:
            ans_text    =str(a.text)
            ans_id     =str(a.id)
            q_text   =str(a.question.text)
            answers2.append({'ans_id':ans_id,'q_text':q_text,'ans_text':ans_text})
            answers.append(str(a.text))
        questions.append({
                        str(q.text):{
                            'answer':answers,
                            'answer2':answers2,
                            'pic_question':str(q.pic_question),
                            'qid':str(qid)
                            }
        })
            
    return JsonResponse({
        'data': questions,
        'time': quiz.time,
    })

def save_quiz_view(request, pk):
    if request.is_ajax():
        questions = []
        
        data = request.POST
        data_ = dict(data.lists())

        data_.pop('csrfmiddlewaretoken')

        for k in data_.keys():
            print('key: ', k)
            question = Question.objects.get(text=k)
            
            questions.append(question)
        


        user = request.user
        quiz = Quiz.objects.get(pk=pk)

        score = 0
        multiplier = 100 / quiz.number_of_questions
        results = []
        correct_answer = None

        for q in questions:
            a_selected = request.POST.get(q.text)
            picans= str(q.pic_answer)
            ansdesc = str(q.answer_description)
            
            if a_selected != "":
                question_answers = Answer.objects.filter(question=q)
                for a in question_answers:
                    if a_selected == a.text:
                        if a.correct:
                            score += 1
                            correct_answer = a.text
                    else:
                        if a.correct:
                            correct_answer = a.text
                   
                results.append({str(q.text): {'correct_answer': correct_answer, 'answered': a_selected,'ansdesc':ansdesc,'answerpic':picans}})
            else:
                results.append({str(q.text): 'not answered'})
            
        # print(results)    
        score_ = score * multiplier
        Result.objects.create(quiz=quiz, user=user, score=score_)

        if score_ >= quiz.required_score_to_pass:
            return JsonResponse({'passed': True, 'score': score_, 'results': results})
        else:
            return JsonResponse({'passed': False, 'score': score_, 'results': results})