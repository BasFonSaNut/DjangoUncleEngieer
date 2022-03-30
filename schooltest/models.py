from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models
from datetime import datetime 
import random

DIFF_CHOICES = (
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard'),
)    
class Quiz(models.Model):
    name = models.CharField(max_length=250)
    topic = models.CharField(max_length=250)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="duration of the quiz in minutes")
    required_score_to_pass = models.IntegerField(help_text="required score in %")
    difficulty = models.CharField(max_length=6, choices=DIFF_CHOICES)

    def __str__(self):
        return f"{self.name}-{self.topic}"

    def get_questions(self):
        questions = list(self.question_set.all())
        questions = random.sample(questions,5) ###############################แก้ไขจำนวนข้อrandom
        return questions[:self.number_of_questions]

    class Meta:
        verbose_name_plural = '3.2 Quizes Random'
        
class Question(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField(max_length=5000)
    pic_question = models.ImageField(upload_to='RandomQuestions', null=True, blank=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    answer_description = models.TextField(max_length=5000, null=True, blank=True,default='')
    pic_answer = models.ImageField(upload_to='RandomAnswers', null=True, blank=True,default='')
    created = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"id: {self.id},text: {self.text},pic_question: {self.pic_question},answer_description:{self.answer_description},pic_answer:{self.pic_answer}"
        # return str(self.text)

    def get_answers(self):
        return self.answer_set.all()
    class Meta:
        verbose_name_plural = '3.3 Questions Random'

class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=250)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(default=datetime.now)

    def __str__(self):
        # return self.question.text,self.text,self.correct,self.text_description,self.pic_answer
        return f"qid:{self.question.id},question: {self.question.text}, answer: {self.text}, correct: {self.correct}"
    class Meta:
        verbose_name_plural = 'Ans. Random'

class Result(models.Model):
    quiz =models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()
    created = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name_plural = '3.1 Results Random' 
        
# =================   school===============
	
class Profile(models.Model):
	usertypelist = (('ม.x/normal','ม.x/normal'),
	              ('ม.x/medium','ม.x/medium'),
				  ('ม.x/hard','ม.x/hard'),
				  ('ม.1/normal','ม.1/normal'),
		          ('ม.1/medium','ม.1/medium'),
				  ('ม.1/hard','ม.1/hard'),
		          ('ม.2/normal','ม.2/normal'),
		          ('ม.2/medium','ม.2/medium'),
				  ('ม.2/hard','ม.2/hard'),
		          ('ม.3/normal','ม.3/normal'),
		          ('ม.3/medium','ม.3/medium'),
				  ('ม.3/hard','ม.3/hard'),
				  ('ม.4/normal','ม.4/normal'),
		          ('ม.4/medium','ม.4/medium'),
				  ('ม.4/hard','ม.4/hard'),
		          ('ม.5/normal','ม.5/normal'),
		          ('ม.5/medium','ม.5/medium'),
				  ('ม.5/hard','ม.5/hard'),
		          ('ม.6/normal','ม.6/normal'),
		          ('ม.6/medium','ม.6/medium'),
				  ('ม.6/hard','ม.6/hard'),
                  ('คอร์สสอบ','คอร์สสอบ'),
				  ('teacher','teacher'),
		          ('admin','admin'))

	levellist = (('normal','normal'),
		          ('hard','hard'))

	user = models.OneToOneField(User,on_delete=models.CASCADE)
	photoprofile = models.ImageField(default='default.png',upload_to='photo_profile',blank=True,null=True)
	usertype = models.CharField(max_length=100,null=True,blank=True,choices=usertypelist,default='ม.x/normal')
	
	class Meta:
		verbose_name_plural = '1. Profile'

	def __str__(self):
		# return self.name
		return '{}_____{}_____{}'.format(self.user.username,self.user.first_name,self.user.last_name)
		# return f'{self.user.username,self.user.first_name,self.user.last_name} Profile'
    
class PersonalRecord(models.Model):

	
	username = models.CharField(max_length=100,null=True,unique=True)
	firstname_lastname = models.CharField(max_length=100,null=True,help_text="ตัวอย่าง  สมชาย ไทเลย")	
	idcard_citizen = models.CharField(max_length=13,null=True, unique=True,help_text="เลขบัตรประชาชน 13 หลัก")
	birthday = models.CharField(max_length=100,null=True,help_text="ตัวอย่าง  01 ม.ค. 2550")
	level = models.CharField(max_length=100,null=True,help_text="ตัวอย่าง  ม.4")
	school_name = models.CharField(max_length=100,null=True,help_text="ตัวอย่าง  เลยพิทยาคม")
	last_grade = models.CharField(max_length=100,null=True,help_text="เกรดเฉลี่ยของเทอมที่ผ่านมา",default='ม.2 เทอม 2 = 3.55')
	phone_number = models.CharField(max_length=10,null=True,help_text="ตัวอย่าง  0801234567")
	father_name = models.CharField(max_length=100,null=True,help_text="ชื่อ-สกุล บิดา")
	father_occupation = models.CharField(max_length=100,null=True,help_text="อาชีพ รับราชการ/ทหาร แม่บ้าน ค้าขาย ธุระกิจส่วนตัว เกษตรกร อื่นๆ")
	father_phone = models.CharField(max_length=10,null=True,help_text="ตัวอย่าง  0891234567")
	mother_name = models.CharField(max_length=100,null=True,help_text="ชื่อ-สกุล มารดา")
	mother_occupation = models.CharField(max_length=100,null=True,help_text="อาชีพ รับราชการ/ครู แม่บ้าน ค้าขาย ธุระกิจส่วนตัว เกษตรกร อื่นๆ")
	mother_phone2 = models.CharField(max_length=10,null=True,help_text="ตัวอย่าง  0801234567")
	address = models.TextField(max_length=800,null=True,help_text="ที่อยู่ที่สามารถติดต่อได้เร็วที่สุด")
    
	class Meta:
		verbose_name_plural = '2. PersonalRecord'

	def __str__(self):
		return self.username




class DocumentTest(models.Model):
	levellist = (('ม.1','ม.1'),
		          ('ม.2','ม.2'),
		          ('ม.3','ม.3'),
		          ('ม.4','ม.4'),
		          ('ม.5','ม.5'),
		          ('ม.6','ม.6'),
                  ('เตรียมสอบ','เตรียมสอบ'))

	level = models.CharField(max_length=100, choices=levellist, default='ม.4')  
	exam_name = models.CharField(max_length=35)
	document_exam = models.FileField(upload_to='allexam_pdf')
	answer_name = models.CharField(max_length=35)
	document_answer = models.FileField(upload_to='allanswer_pdf')
	description = models.TextField(max_length=85,blank=True,null=True)
	
	class Meta:
		verbose_name_plural = '3. DocumentTest'

	def __str__(self):
		return self.exam_name




class Exam(models.Model):

    classlist = (('ม.1','ม.1'),
		          ('ม.2','ม.2'),
		          ('ม.3','ม.3'),
		          ('ม.4','ม.4'),
		          ('ม.5','ม.5'),
		          ('ม.6','ม.6'),
                  ('เตรียมสอบอื่นๆ','เตรียมสอบอื่นๆ'))
		          

    subjectlist = (('คณิตศาสตร์','คณิตศาสตร์'),
                  ('ฟิสิกส์','ฟิสิกส์'),
                  ('เคมี','เคมี'),
                  ('ชีวะวิทยา','ชีวะวิทยา'),
		          ('ภาษาไทย','ภาษาไทย'),
		          ('ภาษาอังกฤษ','ภาษาอังกฤษ'),
		          ('สังคม','สังคม'),
                  ('วิทยาศาสตร์','วิทยาศาสตร์'),
		          ('อื่นๆ','อื่นๆ'))

    examlevellist = (('แบบฝึกเรียนรู้','แบบฝึกเรียนรู้'),
		          ('แบบฝึกความชำนาญ','แบบฝึกความชำนาญ'),
		          ('แบบฝึกระดับยาก','แบบฝึกระดับยาก'),
		          ('สอบเตรียมทหาร','สอบเตรียมทหาร'),
				  ('สอบศูนย์ฝึกพาณิชย์นาวี','สอบศูนย์ฝึกพาณิชย์นาวี'),
				  ('โรงเรียนจ่า','โรงเรียนจ่า'),
				  ('สอบวิศวะ','สอบวิศวะ'),
				  ('โรงเรียนพยาบาล','โรงเรียนพยาบาล'),
		          ('สอบแพทย์','สอบแพทย์'))

    answerlist = (('ข้อ 1. ถูกต้อง','ข้อ 1. ถูกต้อง'),
		          ('ข้อ 2. ถูกต้อง','ข้อ 2. ถูกต้อง'),
		          ('ข้อ 3. ถูกต้อง','ข้อ 3. ถูกต้อง'),
		          ('ข้อ 4. ถูกต้อง','ข้อ 4. ถูกต้อง'))
                  
                  
    class_level = models.CharField(max_length=100,choices=classlist,default='ม.4')
    subject = models.CharField(max_length=100,choices=subjectlist)
    section = models.CharField(max_length=100, unique=True) #unique=True แปลว่า โค้นนี้จะไม่ซำ้กัน
    exam_level = models.CharField(max_length=100,choices=examlevellist, default='โจทย์เรียนรู้')
    exam_number = models.IntegerField(default=1) #ตัวเต็ม
    exam = models.TextField(null=True, blank=True) #ค่าว่างหรือไม่ฐานข้อมูล null=True,ค่าว่างหรือไม่หน้าจอ blank=True
    file_exam = models.FileField(upload_to='file_exam', null=True, blank=True)
    answer1 = models.CharField(max_length=100,null=True, blank=True)
    answer2 = models.CharField(max_length=100,null=True, blank=True)
    answer3 = models.CharField(max_length=100,null=True, blank=True)
    answer4 = models.CharField(max_length=100,null=True, blank=True)    
    answerallright = models.TextField(null=True, blank=True, choices=answerlist)
    file_answer = models.FileField(upload_to='file_answer', null=True, blank=True)
    answer_description = models.TextField(null=True, blank=True)
    printed = models.BooleanField(default=False)
    
    class Meta:verbose_name_plural ='4. Exam' 
    def __str__(self):
        return '{}__{}__{}'.format(self.class_level,self.subject,self.section)




class QuizVolcab3(models.Model):
	list = (('a','a'),
		          ('b','b'),
		          ('c','c'),
		          ('d','d'))
	question = models.CharField(max_length = 500)
	option1 = models.CharField(max_length= 200)
	option2 = models.CharField(max_length= 200)
	option3 = models.CharField(max_length= 200)
	option4 = models.CharField(max_length= 200)
	answer = models.CharField(max_length = 200,choices=list,default='a')

	des = models.CharField(max_length= 200)
	class Meta:
		verbose_name_plural = '5. QuizVolcab3'

   

class QuizMath4normal(models.Model):
	list = (('a','a'),
		          ('b','b'),
		          ('c','c'),
		          ('d','d'))
	id = models.AutoField(primary_key=True)
	question = models.CharField(max_length = 500)
	pic1 = models.ImageField(upload_to='QuizMath4normal_q', null=True, blank=True)
	option1 = models.CharField(max_length= 200)
	option2 = models.CharField(max_length= 200)
	option3 = models.CharField(max_length= 200)
	option4 = models.CharField(max_length= 200)
	answer = models.CharField(max_length = 200,choices=list,default='a')
	des = models.CharField(max_length= 200)
	pic2 = models.ImageField(upload_to='QuizMath4normal_d', null=True, blank=True)
	class Meta:
		verbose_name_plural = '6. QuizMath4normal'