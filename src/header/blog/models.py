from django.db import models

from django.urls import reverse
from django.contrib.auth.models import User


class Message(models.Model):
    name = models.CharField(max_length=150, verbose_name='Ismingiz')
    email = models.EmailField(verbose_name='Email manzilingiz')
    content = models.TextField(blank=True, verbose_name='Sizning xabaringiz')
    status = models.BooleanField(default=True, verbose_name='Xabar holati')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Qo\'shilgan sana')
    updated_at = models.DateTimeField(auto_now=True,  verbose_name='Yangilangan sana')

    # def get_absolute_url(self):
    #     # return reverse("view_news", kwargs={'news_id':self.pk})
    #     return reverse("home", kwargs={'pk':self.pk})

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
        ordering = ['-created_at']

class School(models.Model):
    name = models.CharField(max_length=150, verbose_name='Maktab nomi')
    address = models.CharField(max_length=150, verbose_name='Maktab manzili')
    phone = models.CharField(max_length=150, verbose_name='Telefon raqam')
    contract_num = models.CharField(max_length=50, blank=True, verbose_name='Shartnoma No.')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Qo\'shilgan sana')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Yangilangan sana')
    contract_finish = models.DateField(verbose_name='Time limit')
    status = models.BooleanField(default=True, verbose_name='Maktab holati')

    def get_absolute_url(self):
        # return reverse("view_news", kwargs={'news_id':self.pk})
        return reverse("superviewschool", kwargs={'pk':self.pk})

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Maktab"
        verbose_name_plural = "Maktablar"
        ordering = ['-contract_finish']

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # user = models.OneToOneField(UserRegisterForm, on_delete=models.CASCADE)
    school = models.ForeignKey('School', on_delete=models.PROTECT, null=True, verbose_name="Maktab nomi")
    sinf = models.ForeignKey('Groups', on_delete=models.PROTECT, null=True, verbose_name="Guruh nomi")
    type = models.IntegerField(default=1, verbose_name="TypeUser")#1 student, 2teacher, 3admin
    password = models.CharField(max_length=20, null=True, verbose_name="Kirish paroli")

    # bu yerda class uchun kod yoziladi

    class Meta:
        verbose_name = "Admin & student"
        verbose_name_plural = "Admins & students"


    def __str__(self):
        if self.user.first_name:
            return self.user.first_name
        else:
            return self.user.username

class Groups(models.Model):
    name = models.CharField(max_length=150, verbose_name='Guruh nomi')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Qo\'shilgan sana')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Yangilangan sana')
    end = models.DateField(verbose_name='Tugash muddati')
    status = models.BooleanField(default=True, verbose_name='Guruh holati')
    teacher = models.ForeignKey('UserProfile', on_delete=models.PROTECT, verbose_name="O'qituvchi")

    school = models.ForeignKey('School', on_delete=models.PROTECT, verbose_name="Maktab nomi")

    def get_absolute_url(self):
        # return reverse("view_news", kwargs={'news_id':self.pk})
        return reverse("adminviewgroup", kwargs={'pk':self.pk})

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Guruh"
        verbose_name_plural = "Guruhlar"
        ordering = ['-end']

class Days(models.Model):
    name = models.CharField(max_length=20, verbose_name='Hafta kuni')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kun"
        verbose_name_plural = "Hafta kunlari"

class Schedule(models.Model):
    name = models.CharField(max_length=150, verbose_name='Fan nomi')
    sinf = models.ForeignKey(Groups, on_delete=models.PROTECT, null=True, verbose_name="Guruh nomi")
    school = models.ForeignKey(School, on_delete=models.PROTECT, null=True, verbose_name="Maktab nomi")
    begin = models.TimeField(verbose_name='Boshlanish vaqti')
    days = models.ForeignKey(Days, on_delete=models.PROTECT, verbose_name='Hafta kunlari', default=1)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Fan"
        verbose_name_plural = "Fanlar"

class Lessons(models.Model):
    days = models.ForeignKey(Days, on_delete=models.PROTECT, verbose_name='Hafta kuni')
    schedule = models.ForeignKey(Schedule, on_delete=models.PROTECT, verbose_name='Fan')
    group = models.ForeignKey(Groups, on_delete=models.PROTECT, verbose_name='Guruh')
    school = models.ForeignKey(School, on_delete=models.PROTECT, verbose_name='Maktab')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Qo\'shilgan sana')
    date = models.DateField(auto_now_add=True, verbose_name='Sana', null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Yangilangan sana')
    status = models.BooleanField(default=True, verbose_name='Dars holati')
    start = models.ForeignKey(UserProfile, on_delete=models.PROTECT, verbose_name='Boshlagan')
    def __str__(self):
        return self.schedule.name

    class Meta:
        verbose_name = "Dars"
        verbose_name_plural = "Darslar"

class Attendance(models.Model):
    lesson = models.ForeignKey(Lessons, on_delete=models.PROTECT, verbose_name='Dars')
    student = models.ForeignKey(UserProfile, on_delete=models.PROTECT, verbose_name='Talaba')
    date = models.TimeField(auto_now_add=True, verbose_name='vaqt')

class Chat(models.Model):
    date = models.TimeField(auto_now_add=True, verbose_name='vaqt')
    lesson = models.ForeignKey(Lessons, on_delete=models.PROTECT, verbose_name='Dars')
    sender = models.ForeignKey(UserProfile, on_delete=models.PROTECT, verbose_name='Talaba')
    context = models.TextField(blank=True, verbose_name='chatmessage')