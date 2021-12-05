from _imp import get_frozen_object
from gc import get_objects
from django.utils.timezone import utc

from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from datetime import date, datetime, time
from django.db.models import F
from django.views import View

from .forms import UserRegisterForm, TeacherRegisterForm, UserLoginForm, MessageForm, UserProfileForm, SchoolForm, \
    GroupForm, StudentRegisterForm, StudentProfileForm, SubjectForm, GroupteacherForm

from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404

# chek login required
from django.contrib.auth.decorators import login_required
# decoratorni import qilish
from .decorators import unauthenticated_user, allowed_users, free_access, superuser_only, adminuser_only, \
    studentuser_only, teacheruser_only

from .models import *
from django.http import JsonResponse

# Create your views here.
# @login_required(login_url='user_login')
# @allowed_users(allowed_roles=['admin', 'student'])


# if form.is_valid():
#     user = form.save()
#
#     username = form.cleaned_data.get("username")
#     password = form.cleaned_data.get('password1')
#     # admin guruhiga foydalanuvchini qo'shish
#     group = Group.objects.get(name="teacher")
#     user.groups.add(group)
#
#     profile_form = UserProfileForm()
#     profile = profile_form.save(commit=False)
#     # admin type ligini bildiruvchi belgi
#     profile.type = 2
#     profile.user = user
#     profile.password = password
#     profile.school = request.user.userprofile.school
#     profile.save()
#
#     messages.success(request, 'O\'qituvchi qo\'shildi')
# else:
#     messages.error(request, 'Saqlashda xatolik')
# @superuser_only
# def superadminupdate(request):
#     return render(request, 'super/superadminlist.html')


@superuser_only
def superschoollist(request):
    return render(request, 'super/superschoollist.html')


# @unauthenticated_user
# def register(request):
#
#     # if request.user.is_authenticated:
#     #     return redirect('home')
#     # form = UserCreationForm()
#     # return render(request, 'blog/register.html', {'form':form})
#
#
#     if request.method == "POST":
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#
#             username = form.cleaned_data.get("username")
#             group = Group.objects.get(name="student")
#             user.groups.add(group)
#             messages.success(request, 'Registration accepted')
#         else:
#             messages.error(request, 'Failed')
#     else:
#         form = UserRegisterForm()
#
#     return render(request, 'blog/register.html', {'form':form})


@unauthenticated_user
def user_login(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            # username = request.POST.get('username')
            # password = request.POST.get('password')
            # user = authenticate(request, username=username, password=password)
            # if user is not None:
            #     login(request, user)
            #     return redirect('home')
            # else:
            #     messages.info(request, "Username OR password is incorrect")
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'blog/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('user_login')


@free_access
def index(request):
    if request.method == "POST":
        form_message = MessageForm(request.POST)
        if form_message.is_valid():
            Message.objects.create(**form_message.cleaned_data)
            messages.success(request, 'Xabaringiz jo\'natildi!')
        else:
            form_message = MessageForm()
            messages.error(request, 'Xabar jo\'natilmadi')

    form_message = MessageForm()
    if request.user.is_authenticated:
        group = request.user.groups.all()[0].name
    else:
        group = "Free"

    return render(request, 'blog/index.html', {"group": group, "form_message": form_message})


@superuser_only
def superindex(request):
    return render(request, 'super/superindex.html')


@superuser_only
def superschooladd(request):
    if request.method == "POST":
        form = SchoolForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Maktab qo\'shildi')
            form = SchoolForm()
        else:
            messages.error(request, 'Failed')
    else:
        form = SchoolForm()

    return render(request, 'super/superschooladd.html', {"form": form})


class AllschoolView(ListView):
    model = School
    template_name = "super/superschoollist.html"
    context_object_name = "allschools"

    # extra_context = {"title":"Hwllo!"}
    def get_context_data(self, *, object_list=None, **kwargs):
        # context = super(HomeNews, self).get_context_data()
        context = super().get_context_data(**kwargs)
        context['title'] = "All Schools"
        return context

    def get_queryset(self):
        return School.objects.order_by('contract_finish')


class SchoolViewByStatus(ListView):
    model = School
    template_name = "super/superschoollist.html"
    context_object_name = "allschools"

    # extra_context = {"title":"Hwllo!"}
    def get_context_data(self, *, object_list=None, **kwargs):
        # context = super(HomeNews, self).get_context_data()
        context = super().get_context_data(**kwargs)
        context['title'] = "All Schools"
        return context

    def get_queryset(self):
        if self.kwargs['status'] == 1:
            return School.objects.filter(status=True)
        elif self.kwargs['status'] == 0:
            return School.objects.filter(status=False)
        else:
            return School.objects.order_by('contract_finish')


class ViewSchool(DetailView):
    model = School
    template_name = "super/superschoolone.html"
    context_object_name = "schoolinfo"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        # return News.objects.filter(category_id=self.kwargs['category_id'])
        return School.objects.filter(pk=self.kwargs['pk'])


@superuser_only
def editschoolinfo(request, pk=None):
    school = get_object_or_404(School, pk=pk)
    form = SchoolForm(request.POST or None, instance=school)
    if form.is_valid():
        school = form.save(commit=False)
        school.save()
        if school.status:
            User.objects.filter(userprofile__school_id=school.pk).update(is_active=True)
        else:
            User.objects.filter(userprofile__school_id=school.pk).update(is_active=False)

        return redirect(school)

    return render(request, 'super/superschooladd.html', {"form": form})


@superuser_only
def superadminadd(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get('password1')
            # admin guruhiga foydalanuvchini qo'shish
            group = Group.objects.get(name="admin")
            user.groups.add(group)

            profile = profile_form.save(commit=False)
            # admin type ligini bildiruvchi belgi
            profile.type = 3
            profile.user = user
            profile.password = password
            profile.save()

            messages.success(request, 'Registration accepted')
        else:
            messages.error(request, 'Saqlashda xatolik')
    else:
        form = UserRegisterForm()
        profile_form = UserProfileForm()
    return render(request, 'super/superadminadd.html', {'form': form, "profile_form": profile_form})


class AlladminView(ListView):
    model = UserProfile
    template_name = "super/superadminlist.html"
    context_object_name = "alladmins"

    # extra_context = {"title":"Hwllo!"}
    def get_context_data(self, *, object_list=None, **kwargs):
        # context = super(HomeNews, self).get_context_data()
        context = super().get_context_data(**kwargs)
        context['title'] = "All Admins"
        context['schools'] = School.objects.all()
        return context

    def get_queryset(self):
        return UserProfile.objects.filter(type=3).order_by('school')


class AdminViewByStatus(ListView):
    model = UserProfile
    template_name = "super/superadminlist.html"
    context_object_name = "alladmins"

    # extra_context = {"title":"Hwllo!"}
    def get_context_data(self, *, object_list=None, **kwargs):
        # context = super(HomeNews, self).get_context_data()
        context = super().get_context_data(**kwargs)
        context['title'] = "Admins By Status"
        context['schools'] = School.objects.all()
        return context

    def get_queryset(self):
        if self.kwargs['status'] == 1:
            return UserProfile.objects.filter(type=3, user__is_active=True).order_by('school')
        elif self.kwargs['status'] == 0:
            return UserProfile.objects.filter(type=3, user__is_active=False).order_by('school')
        else:
            UserProfile.objects.filter(type=3).order_by('school')


class AdminViewBySchool(ListView):
    model = UserProfile
    template_name = "super/superadminlist.html"
    context_object_name = "alladmins"

    # extra_context = {"title":"Hwllo!"}
    def get_context_data(self, *, object_list=None, **kwargs):
        # context = super(HomeNews, self).get_context_data()
        context = super().get_context_data(**kwargs)
        context['title'] = "Admins By School"
        context['schools'] = School.objects.all()
        return context

    def get_queryset(self):
        return UserProfile.objects.filter(type=3, school_id=self.kwargs['pk']).order_by('school')


class ViewAdmin(DetailView):
    model = UserProfile
    template_name = "super/superadminone.html"
    context_object_name = "admininfo"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return UserProfile.objects.filter(pk=self.kwargs['pk'], type=3)


@superuser_only
def editadmininfo(request, pk=None):
    # profileform uchun
    userprofile = get_object_or_404(UserProfile, pk=pk)
    profile_form = UserProfileForm(request.POST or None, instance=userprofile)

    # form uchun
    user = get_object_or_404(User, pk=userprofile.user.pk)
    form = UserRegisterForm(request.POST or None, instance=user)

    if form.is_valid() and profile_form.is_valid():
        user = form.save(commit=False)
        user.save()

        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password1')

        userprofile = profile_form.save(commit=False)
        userprofile.password = password
        userprofile.save()

        return redirect('superviewadmin', userprofile.pk)

    form.password1 = userprofile.password
    form.password2 = userprofile.password

    return render(request, 'super/superadminadd.html',
                  {"form": form, "profile_form": profile_form, "userprofile": userprofile})


@superuser_only
def deladmininfo(request, pk=None):
    admininfo = get_object_or_404(UserProfile, pk=pk)
    userkey = admininfo.user.pk
    admininfo.delete()
    user = get_object_or_404(User, pk=userkey)
    user.delete()
    return redirect('superadminlist')


# admin page uchun funksiyalar


# teacher control by ADMIN
@adminuser_only
def adminindex(request):
    title = "O'qituvchilar nazorati"
    return render(request, 'admin/adminindex.html', {"title": title})


# admin o'qituvchi qo'shish
@adminuser_only
def adminteacheradd(request):
    if request.method == "POST":
        form = TeacherRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get('password1')
            # admin guruhiga foydalanuvchini qo'shish
            group = Group.objects.get(name="teacher")
            user.groups.add(group)

            profile_form = UserProfileForm()
            profile = profile_form.save(commit=False)
            # admin type ligini bildiruvchi belgi
            profile.type = 2
            profile.user = user
            profile.password = password
            profile.school = request.user.userprofile.school
            profile.save()

            messages.success(request, 'O\'qituvchi qo\'shildi')
            return redirect('adminviewteacher', profile.pk)
        else:
            messages.error(request, 'Saqlashda xatolik')
    else:
        form = TeacherRegisterForm()
    title = "O'qituvchi qo'shish"
    return render(request, 'admin/adminteacheradd.html', {'form': form, "title": title})


@adminuser_only
def adminteacherlist(request):
    allteachers = UserProfile.objects.filter(type=2, school=request.user.userprofile.school)
    title = "O'qituvchilar ro'yhati"
    return render(request, "admin/adminteacherlist.html", {"allteachers": allteachers, "title": title})


class ViewTeacher(DetailView):
    model = UserProfile
    template_name = "admin/adminteacherone.html"
    context_object_name = "teacherinfo"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Admin::O'qitvuchi info"
        return context

    def get_queryset(self):
        return UserProfile.objects.filter(pk=self.kwargs['pk'], type=2)


@adminuser_only
def adminteacherlistst(request, status):
    if status == 1:
        allteachers = UserProfile.objects.filter(type=2, school=request.user.userprofile.school, user__is_active=True)
    elif status == 0:
        allteachers = UserProfile.objects.filter(type=2, school=request.user.userprofile.school, user__is_active=False)
    else:
        allteachers = UserProfile.objects.filter(type=2, school=request.user.userprofile.school)

    title = "O'qituvchilar ro'yhati(holati bo'yicha)"

    return render(request, "admin/adminteacherlist.html", {"allteachers": allteachers, "title": title})


@adminuser_only
def editteacherinfo(request, pk=None):
    # profileform uchun
    userprofile = get_object_or_404(UserProfile, pk=pk, type=2, school=request.user.userprofile.school)

    # form uchun
    user = get_object_or_404(User, pk=userprofile.user.pk)
    form = TeacherRegisterForm(request.POST or None, instance=user)

    if form.is_valid():
        user = form.save()
        user.save()

        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password1')

        userprofile.password = password
        userprofile.save()
        messages.success(request, "Ma'lumot o'zgartirildi")

        return redirect('adminviewteacher', userprofile.pk)

    title = "O'qituvchi qo'shish"
    return render(request, 'admin/adminteacheradd.html', {"form": form, "userprofile": userprofile, "title": title})


@adminuser_only
def admindelteacher(request, pk=None):
    teacherinfo = get_object_or_404(UserProfile, pk=pk, type=2, school=request.user.userprofile.school)
    userkey = teacherinfo.user.pk
    teacherinfo.delete()
    user = get_object_or_404(User, pk=userkey)
    user.delete()
    return redirect('adminteacherlist')


# groups by ADMIN
@adminuser_only
def admingroupadd(request):
    if request.method == "POST":
        form = GroupForm(request.POST)

        if form.is_valid():
            group = form.save(commit=False)
            group.school = request.user.userprofile.school
            group.save()
            messages.success(request, 'Guruh qo\'shildi')
            form = GroupForm()
        else:
            messages.error(request, 'Guruh qo\'shilmadi')
    else:
        teacher = UserProfile.objects.filter(type=2)
        # form = GroupForm(instance= initial={'teacher':UserProfile.objects.get(pk=24)})
        form = GroupForm()
    form.fields["teacher"].queryset = UserProfile.objects.filter(type=2, school=request.user.userprofile.school)
    title = "Guruh qo'shish"
    return render(request, 'admin/group/admingroupadd.html', {"form": form, "title": title})


@adminuser_only
def admingrouplist(request):
    allgroups = Groups.objects.filter(school=request.user.userprofile.school).order_by('-end')
    title = "Guruhlar ro'yhati"
    return render(request, "admin/group/admingrouplist.html", {"allgroups": allgroups, "title": title})


class ViewGroup(DetailView):
    model = Groups
    template_name = "admin/group/admingroupone.html"
    context_object_name = "groupinfo"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Guruh ma'lumoti"
        context['students'] = UserProfile.objects.filter(type=1, sinf_id=self.kwargs['pk'])
        return context

    def get_queryset(self):
        # return UserProfile.objects.filter(pk=self.kwargs['pk'],type=3)
        return Groups.objects.filter(pk=self.kwargs['pk'], school=self.request.user.userprofile.school)


@adminuser_only
def admingrouplistst(request, status):
    if status == 1:
        allgroups = Groups.objects.filter(school=request.user.userprofile.school, status=True).order_by('-end')
    elif status == 0:
        allgroups = Groups.objects.filter(school=request.user.userprofile.school, status=False).order_by('-end')
    else:
        allgroups = Groups.objects.filter(school=request.user.userprofile.school).order_by('-end')

    title = "Guruhlar ro'yhati(holat bo'yicha)"
    return render(request, "admin/group/admingrouplist.html", {"allgroups": allgroups, "title": title})


@adminuser_only
def adminchangegroup(request, pk):
    groupinfo = get_object_or_404(Groups, pk=pk, school=request.user.userprofile.school)
    form = GroupForm(request.POST or None, instance=groupinfo)

    if form.is_valid():
        group = form.save()

        if group.status:
            User.objects.filter(userprofile__school=group.school, userprofile__sinf=group, userprofile__type=1).update(
                is_active=True)
        else:
            User.objects.filter(userprofile__school=group.school, userprofile__sinf=group, userprofile__type=1).update(
                is_active=False)

        messages.success(request, "Ma'lumot yuklandi")
        return redirect('adminviewgroup', group.pk)

    title = "Talaba ma'lumotlari"
    form.fields["teacher"].queryset = UserProfile.objects.filter(type=2, school=request.user.userprofile.school)

    return render(request, 'admin/group/admingroupadd.html',
                  {"form": form, "title": title})


# student by ADMIN
@adminuser_only
def adminstudentadd(request):
    if request.method == "POST":
        form = StudentRegisterForm(request.POST)
        profile_form = StudentProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():

            user = form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get('password1')
            # student guruhiga foydalanuvchini qo'shish
            group = Group.objects.get(name="student")
            user.groups.add(group)

            profile = profile_form.save(commit=False)
            # student type ligini bildiruvchi belgi
            profile.type = 1
            profile.user = user
            profile.school = request.user.userprofile.school
            profile.password = password
            profile.save()

            messages.success(request, "Ma'lumotlar yuklandi")
            return redirect("adminviewgroup", profile.sinf.pk)

        else:
            messages.error(request, 'Saqlashda xatolik')
    else:
        form = StudentRegisterForm()
        profile_form = StudentProfileForm()
    title = "Talaba ma'lumotlari"
    profile_form.fields["sinf"].queryset = Groups.objects.filter(status=True, school=request.user.userprofile.school)
    return render(request, 'admin/student/adminstudentadd.html',
                  {'form': form, "profile_form": profile_form, "title": title})


class ViewStudent(DetailView):
    model = UserProfile
    template_name = "admin/student/adminstudentone.html"
    context_object_name = "studentinfo"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Talaba ma'lumoti"
        return context

    def get_queryset(self):
        # return UserProfile.objects.filter(pk=self.kwargs['pk'],type=3)
        return UserProfile.objects.filter(pk=self.kwargs['pk'], school=self.request.user.userprofile.school)


@adminuser_only
def editstudentinfo(request, pk):
    userprofile = get_object_or_404(UserProfile, pk=pk, school=request.user.userprofile.school)
    profile_form = StudentProfileForm(request.POST or None, instance=userprofile)

    # form uchun
    user = get_object_or_404(User, pk=userprofile.user.pk)
    form = StudentRegisterForm(request.POST or None, instance=user)

    if form.is_valid() and profile_form.is_valid():
        user = form.save(commit=False)
        user.save()

        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password1')

        userprofile = profile_form.save(commit=False)
        userprofile.password = password
        userprofile.save()

        return redirect('adminviewgroup', userprofile.sinf.pk)

    title = "Talaba ma'lumotlari"
    profile_form.fields["sinf"].queryset = Groups.objects.filter(status=True, school=request.user.userprofile.school)

    return render(request, 'admin/student/adminstudentadd.html',
                  {"form": form, "profile_form": profile_form, "userprofile": userprofile, "title": title})


# schedule by ADMIN
@adminuser_only
def adminschedulelist(request):
    allgroups = Groups.objects.filter(school=request.user.userprofile.school, status=True).order_by('-end')
    title = "Dars o'tish grafigi"
    return render(request, "admin/schedule/adminschedulelist.html", {"allgroups": allgroups, "title": title})


@adminuser_only
def adminviewschedule(request, pk):
    group = get_object_or_404(Groups, school=request.user.userprofile.school, pk=pk)
    title = "Darslar jadvali"

    schedulelist = Schedule.objects.filter(sinf=group, school=request.user.userprofile.school).order_by('days__pk',
                                                                                                        'begin')

    return render(request, "admin/schedule/adminschedulegroup.html",
                  {"group": group, "title": title, "schedulelist": schedulelist})


@adminuser_only
def adminscheduleadd(request, pk):
    group = get_object_or_404(Groups, school=request.user.userprofile.school, pk=pk)
    schedulelist = Schedule.objects.filter(sinf=group, school=request.user.userprofile.school).order_by('days__pk',
                                                                                                        'begin')
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():

            subject = form.save(commit=False)
            subject.sinf = group
            subject.school = request.user.userprofile.school
            subject.save()

            messages.success(request, "Ma'lumotlar yuklandi")
            return redirect("adminviewschedule", group.pk)

        else:
            messages.error(request, 'Saqlashda xatolik')
    else:
        form = SubjectForm()
    title = "Talaba ma'lumotlari"

    title = "Fan qo'shish"
    return render(request, "admin/schedule/adminscheduleadd.html",
                  {"group": group, "title": title, "form": form, "schedulelist": schedulelist})


@adminuser_only
def adminchangeschedule(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk, school=request.user.userprofile.school)
    form = SubjectForm(request.POST or None, instance=schedule)

    group = get_object_or_404(Groups, school=request.user.userprofile.school, pk=schedule.sinf.pk)
    schedulelist = Schedule.objects.filter(sinf=group, school=request.user.userprofile.school).order_by('days__pk',
                                                                                                        'begin')

    if form.is_valid():
        form.save()
        messages.success(request, "Ma'lumotlar yuklandi")

        return redirect('adminviewschedule', group.pk)

    title = "Fanni o'zgartirish"
    return render(request, "admin/schedule/adminscheduleadd.html",
                  {"group": group, "title": title, "form": form, "schedulelist": schedulelist})


@adminuser_only
def admindelschedule(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk, school=request.user.userprofile.school)
    group = schedule.sinf
    schedule.delete()
    return redirect('adminviewschedule', group.pk)


# admin lessons page
@adminuser_only
def admincurrentlessons(request):
    day = date.today()
    weekday = day.isoweekday()

    # weekday = 6

    schedule = Schedule.objects.filter(school=request.user.userprofile.school, days=weekday).order_by("begin")
    title = "Bugungi darslar ro'yhati"
    return render(request, "lessons/adminschedulelist.html",
                  {"schedule": schedule, "title": title})


@adminuser_only
def admininfolesson(request, pk):
    day = date.today()

    # schedule = Schedule.objects.get(school=request.user.userprofile.school, pk=pk)

    weekday = day.isoweekday()

    # weekday = 6

    schedule = get_object_or_404(Schedule, school=request.user.userprofile.school, pk=pk, days_id=weekday)
    lesson = Lessons.objects.filter(school=request.user.userprofile.school, group=schedule.sinf, schedule=schedule,
                                    date=day)

    if not lesson:
        lessonmodel = Lessons.objects.create(days_id=weekday, schedule=schedule, group=schedule.sinf,
                                             school=request.user.userprofile.school, start=request.user.userprofile,
                                             status=True, date=day)
        lesson = lessonmodel
    else:
        lesson = Lessons.objects.get(school=request.user.userprofile.school, group=schedule.sinf, schedule=schedule,
                                     date=day)

    title = "Online dars"

    return render(request, "lessons/admininfolesson.html",
                  {"lesson": lesson, "title": title})


@studentuser_only
def studenturrentlessons(request):
    day = date.today()
    weekday = day.isoweekday()

    # weekday = 6

    schedule = Schedule.objects.filter(sinf=request.user.userprofile.sinf, school=request.user.userprofile.school,
                                       days=weekday).order_by("begin")

    title = "Bugungi darslar ro'yhati"
    return render(request, "lessons/studentschedulelist.html",
                  {"schedule": schedule, "title": title})


@studentuser_only
def studentviewschedule(request):
    schedulelist = Schedule.objects.filter(sinf=request.user.userprofile.sinf,
                                           school=request.user.userprofile.school).order_by('days__pk',
                                                                                            'begin')
    title = "Darslar jadvali"
    return render(request, "student/info/studentviewschedule.html",
                  {"title": title, "schedulelist": schedulelist})


@studentuser_only
def studentinfolesson(request, pk):
    day = date.today()
    # schedule = Schedule.objects.get(school=request.user.userprofile.school, pk=pk)
    lesson = Lessons.objects.filter(school=request.user.userprofile.school, group=request.user.userprofile.sinf,
                                    schedule_id=pk, status=True, date=day)
    if lesson:
        lesson = Lessons.objects.get(school=request.user.userprofile.school, group=request.user.userprofile.sinf,
                                     schedule_id=pk, status=True, date=day)
    title = "Online dars"

    return render(request, "lessons/studentinfolesson.html",
                  {"lesson": lesson, "title": title})


@adminuser_only
def lessonroom(request, pk):
    lesson = Lessons.objects.get(school=request.user.userprofile.school, pk=pk)
    students = UserProfile.objects.filter(school=request.user.userprofile.school, sinf=lesson.group).order_by(
        'user__last_name')
    title = "Online Stream"
    group = request.user.groups.all()[0].name
    return render(request, "lessons/lessonroom.html",
                  {"title": title, "lesson": lesson, "group": group, "students": students})


@studentuser_only
def lessonroomstudent(request, pk):
    lesson = Lessons.objects.get(school=request.user.userprofile.school, pk=pk)

    attendance = Attendance.objects.filter(lesson=lesson, student=request.user.userprofile)
    if not attendance:
        lessonmodel = Attendance.objects.create(lesson=lesson, student=request.user.userprofile)
    else:
        attendance = Attendance.objects.get(lesson=lesson, student=request.user.userprofile)
        attendance.date = datetime.now()
        attendance.save()

    students = UserProfile.objects.filter(school=request.user.userprofile.school, sinf=lesson.group).order_by(
        'user__last_name')

    title = "Online Stream"
    group = request.user.groups.all()[0].name
    return render(request, "lessons/lessonroom.html",
                  {"title": title, "lesson": lesson, "group": group, "students": students})


@teacheruser_only
def lessonroomteacher(request, pk):
    lesson = Lessons.objects.get(school=request.user.userprofile.school, pk=pk)
    students = UserProfile.objects.filter(school=request.user.userprofile.school, sinf=lesson.group).order_by(
        'user__last_name')
    title = "Online Stream"
    group = request.user.groups.all()[0].name
    return render(request, "lessons/lessonroom.html",
                  {"title": title, "lesson": lesson, "group": group, "students": students})


# control by TEACHER
@teacheruser_only
def teacherindex(request):
    title = "O'qituvchilar nazorati"
    return render(request, 'teacher/teacherindex.html', {"title": title})


@teacheruser_only
def teachergroupadd(request):
    if request.method == "POST":
        form = GroupteacherForm(request.POST)

        if form.is_valid():
            group = form.save(commit=False)
            group.school = request.user.userprofile.school
            group.teacher = request.user.userprofile
            group.save()
            messages.success(request, 'Guruh qo\'shildi')
            form = GroupteacherForm()
        else:
            messages.error(request, 'Guruh qo\'shilmadi')
    else:
        form = GroupteacherForm()
    title = "Guruh qo'shish"
    return render(request, 'teacher/group/teachergroupadd.html', {"form": form, "title": title})


@teacheruser_only
def teachergrouplist(request):
    allgroups = Groups.objects.filter(school=request.user.userprofile.school,
                                      teacher=request.user.userprofile).order_by('-end')
    title = "Guruhlar ro'yhati"
    return render(request, "teacher/group/teachergrouplist.html", {"allgroups": allgroups, "title": title})


@teacheruser_only
def teachergrouplistst(request, status):
    if status == 1:
        allgroups = Groups.objects.filter(school=request.user.userprofile.school, status=True,
                                          teacher=request.user.userprofile).order_by('-end')
    elif status == 0:
        allgroups = Groups.objects.filter(school=request.user.userprofile.school, status=False,
                                          teacher=request.user.userprofile).order_by('-end')
    else:
        allgroups = Groups.objects.filter(school=request.user.userprofile.school,
                                          teacher=request.user.userprofile).order_by('-end')

    title = "Guruhlar ro'yhati(holat bo'yicha)"
    return render(request, "teacher/group/teachergrouplist.html", {"allgroups": allgroups, "title": title})


class ViewteacherGroup(DetailView):
    model = Groups
    template_name = "teacher/group/teachergroupone.html"
    context_object_name = "groupinfo"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Guruh ma'lumoti"
        context['students'] = UserProfile.objects.filter(type=1, sinf_id=self.kwargs['pk'])
        return context

    def get_queryset(self):
        # return UserProfile.objects.filter(pk=self.kwargs['pk'],type=3)
        return Groups.objects.filter(pk=self.kwargs['pk'], school=self.request.user.userprofile.school,
                                     teacher=self.request.user.userprofile)


@teacheruser_only
def teacherchangegroup(request, pk):
    groupinfo = get_object_or_404(Groups, pk=pk, school=request.user.userprofile.school,
                                  teacher=request.user.userprofile)
    form = GroupteacherForm(request.POST or None, instance=groupinfo)

    if form.is_valid():
        group = form.save()

        if group.status:
            User.objects.filter(userprofile__school=group.school, userprofile__sinf=group, userprofile__type=1).update(
                is_active=True)
        else:
            User.objects.filter(userprofile__school=group.school, userprofile__sinf=group, userprofile__type=1).update(
                is_active=False)

        messages.success(request, "Ma'lumot yuklandi")
        return redirect('teacherviewgroup', group.pk)

    title = "Talaba ma'lumotlari"

    return render(request, 'teacher/group/teachergroupadd.html',
                  {"form": form, "title": title})


# student by TEACHER

@teacheruser_only
def teacherstudentadd(request):
    if request.method == "POST":
        form = StudentRegisterForm(request.POST)
        profile_form = StudentProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():

            user = form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get('password1')
            # student guruhiga foydalanuvchini qo'shish
            group = Group.objects.get(name="student")
            user.groups.add(group)

            profile = profile_form.save(commit=False)
            # student type ligini bildiruvchi belgi
            profile.type = 1
            profile.user = user
            profile.school = request.user.userprofile.school
            profile.password = password
            profile.save()

            messages.success(request, "Ma'lumotlar yuklandi")
            return redirect("teacherviewgroup", profile.sinf.pk)

        else:
            messages.error(request, 'Saqlashda xatolik')
    else:
        form = StudentRegisterForm()
        profile_form = StudentProfileForm()
    title = "Talaba ma'lumotlari"
    profile_form.fields["sinf"].queryset = Groups.objects.filter(status=True, school=request.user.userprofile.school,
                                                                 teacher=request.user.userprofile)
    return render(request, 'teacher/student/teacherstudentadd.html',
                  {'form': form, "profile_form": profile_form, "title": title})


class ViewStudentteacher(DetailView):
    model = UserProfile
    template_name = "teacher/student/teacherstudentone.html"
    context_object_name = "studentinfo"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Talaba ma'lumoti"
        return context

    def get_queryset(self):
        # return UserProfile.objects.filter(pk=self.kwargs['pk'],type=3)
        return UserProfile.objects.filter(pk=self.kwargs['pk'], school=self.request.user.userprofile.school,
                                          sinf__teacher=self.request.user.userprofile)


@teacheruser_only
def editstudentinfoteacher(request, pk):
    userprofile = get_object_or_404(UserProfile, pk=pk, school=request.user.userprofile.school,
                                    sinf__teacher=request.user.userprofile)
    profile_form = StudentProfileForm(request.POST or None, instance=userprofile)

    # form uchun
    user = get_object_or_404(User, pk=userprofile.user.pk)
    form = StudentRegisterForm(request.POST or None, instance=user)

    if form.is_valid() and profile_form.is_valid():
        user = form.save(commit=False)
        user.save()

        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password1')

        userprofile = profile_form.save(commit=False)
        userprofile.password = password
        userprofile.save()

        return redirect('teacherviewgroup', userprofile.sinf.pk)

    title = "Talaba ma'lumotlari"
    profile_form.fields["sinf"].queryset = Groups.objects.filter(status=True, school=request.user.userprofile.school,
                                                                 teacher=request.user.userprofile)

    return render(request, 'teacher/student/teacherstudentadd.html',
                  {"form": form, "profile_form": profile_form, "userprofile": userprofile, "title": title})


# schedule by TEACHER
@teacheruser_only
def teacherschedulelist(request):
    allgroups = Groups.objects.filter(school=request.user.userprofile.school, teacher=request.user.userprofile,
                                      status=True).order_by('-end')
    title = "Dars o'tish grafigi"
    return render(request, "teacher/schedule/teacherschedulelist.html", {"allgroups": allgroups, "title": title})


@teacheruser_only
def teacherviewschedule(request, pk):
    group = get_object_or_404(Groups, school=request.user.userprofile.school, pk=pk, teacher=request.user.userprofile)
    title = "Darslar jadvali"

    schedulelist = Schedule.objects.filter(sinf=group, school=request.user.userprofile.school).order_by('days__pk',
                                                                                                        'begin')

    return render(request, "teacher/schedule/teacherschedulegroup.html",
                  {"group": group, "title": title, "schedulelist": schedulelist})


@teacheruser_only
def teacherscheduleadd(request, pk):
    group = get_object_or_404(Groups, school=request.user.userprofile.school, pk=pk, teacher=request.user.userprofile)
    schedulelist = Schedule.objects.filter(sinf=group, school=request.user.userprofile.school).order_by('days__pk',
                                                                                                        'begin')
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():

            subject = form.save(commit=False)
            subject.sinf = group
            subject.school = request.user.userprofile.school
            subject.save()

            messages.success(request, "Ma'lumotlar yuklandi")
            return redirect("teacherviewschedule", group.pk)

        else:
            messages.error(request, 'Saqlashda xatolik')
    else:
        form = SubjectForm()
    title = "Talaba ma'lumotlari"

    title = "Fan qo'shish"
    return render(request, "teacher/schedule/teacherscheduleadd.html",
                  {"group": group, "title": title, "form": form, "schedulelist": schedulelist})


@teacheruser_only
def teacherchangeschedule(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk, school=request.user.userprofile.school,
                                 sinf__teacher=request.user.userprofile)
    form = SubjectForm(request.POST or None, instance=schedule)

    group = get_object_or_404(Groups, school=request.user.userprofile.school, pk=schedule.sinf.pk,
                              teacher=request.user.userprofile)
    schedulelist = Schedule.objects.filter(sinf=group, school=request.user.userprofile.school).order_by('days__pk',
                                                                                                        'begin')

    if form.is_valid():
        form.save()
        messages.success(request, "Ma'lumotlar yuklandi")

        return redirect('teacherviewschedule', group.pk)

    title = "Fanni o'zgartirish"
    return render(request, "teacher/schedule/teacherscheduleadd.html",
                  {"group": group, "title": title, "form": form, "schedulelist": schedulelist})


@teacheruser_only
def teacherdelschedule(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk, school=request.user.userprofile.school,
                                 sinf__teacher=request.user.userprofile)
    group = schedule.sinf
    schedule.delete()
    return redirect('teacherviewschedule', group.pk)


# lessons by TEACHER
@teacheruser_only
def teachercurrentlessons(request):
    day = date.today()
    weekday = day.isoweekday()

    # weekday=6

    schedule = Schedule.objects.filter(school=request.user.userprofile.school, days=weekday,
                                       sinf__teacher=request.user.userprofile).order_by("begin")
    title = "Bugungi darslar ro'yhati"
    return render(request, "lessons/teacherschedulelist.html",
                  {"schedule": schedule, "title": title})


@teacheruser_only
def teacherinfolesson(request, pk):
    day = date.today()

    weekday = day.isoweekday()

    # weekday = 6

    schedule = get_object_or_404(Schedule, school=request.user.userprofile.school, pk=pk, days_id=weekday)
    lesson = Lessons.objects.filter(school=request.user.userprofile.school, group=schedule.sinf, schedule=schedule,
                                    date=day)

    if not lesson:
        lessonmodel = Lessons.objects.create(days_id=weekday, schedule=schedule, group=schedule.sinf,
                                             school=request.user.userprofile.school, start=request.user.userprofile,
                                             status=True, date=day)
        lesson = lessonmodel
    else:
        lesson = Lessons.objects.get(school=request.user.userprofile.school, group=schedule.sinf, schedule=schedule,
                                     date=day)

    title = "Online dars"

    return render(request, "lessons/teacherinfolesson.html",
                  {"lesson": lesson, "title": title})


class AjaxHandler(View):
    def get(self, request):
        text = request.GET.get('lesson')
        print()
        print(text)
        print()
        t = datetime.now()
        # return render(request, 'lessons/lessonroom.html');
        return JsonResponse({'seconds':t});
        # return render(request, 'lessons/parts/users.html', {"text":text});
    def post(self, request):
        text = request.POST.get('lesson')
        t = datetime.utcnow().replace(tzinfo=utc)
        users = Attendance.objects.filter(lesson=text)
        if request.user.userprofile.type == 1:
            attendance = Attendance.objects.get(lesson=text, student=request.user.userprofile)
            attendance.date = datetime.now()
            attendance.save()
        # users = Attendance.objects.filter(lesson=text)
        return JsonResponse(dict(users.values_list('student', 'date')));


class AjaxHandlerchatadd(View):
    def post(self, request):
        lesson = request.POST.get('lesson')
        context = request.POST.get('content')
        Chat.objects.create(lesson_id=lesson, context=context, sender=request.user.userprofile)
        return JsonResponse({"result":True});

class AjaxHandlerchat(View):
    def post(self, request):
        lesson = request.POST.get('lesson')
        chats = Chat.objects.filter(lesson=lesson).order_by('date')
        result = ""
        for chat in chats:
            if chat.sender == request.user.userprofile:
                result += "<li class='mb-4 pb-3' style='width:100%'><div class='chat-body blue text-white p-3 ml-2 z-depth-1'><div class='header'><strong class='primary-font'>"+chat.sender.user.last_name+"</strong><small class='pull-right text-muted'> <i class='far fa-clock'></i> "+chat.date.strftime("%H:%M:%S")+"</small></div><hr class='w-100'><p class='mb-0'>"+chat.context+"</p></div></li>"
            else:
                result += "<li class='mb-4' style='width:100%'><div class='chat-body p-3 ml-2 z-depth-1'><div class='header'><strong class='primary-font'>" + chat.sender.user.last_name + "</strong><small class='pull-right text-muted'> <i class='far fa-clock'></i> " + chat.date.strftime("%H:%M:%S") + "</small></div><hr class='w-100'><p class='mb-0'>" + chat.context + "</p></div></li>"
        # else:
        #     result="Empty"
        return JsonResponse({"result":result});


class AjaxHandlerfinishlesson(View):
    def post(self, request):
        lesson = request.POST.get('lesson')
        lesson = Lessons.objects.get(pk=lesson, start=request.user.userprofile)
        lesson.status = False
        lesson.save()
        return JsonResponse({"result": 1});
#
# def lessonstatus(request):
#     return 1;
#
# # @teacheruser_only
# # def teachercurrentlessons(request):
# #     pass
