from django.urls import path

from .views import *
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('login/', views.user_login, name="user_login"),
    # path('register/', views.register, name="register"),
    path('logout/', views.user_logout, name="user_logout"),

    path('superindex/', views.superindex, name="superindex"),
    #superuser school control
    path('superschoollist/', AllschoolView.as_view(), name="superschoollist"),
    path('superschoollistst/<int:status>/', SchoolViewByStatus.as_view(), name="superschoollistst"),
    path('superviewschool/<int:pk>/', ViewSchool.as_view(), name="superviewschool"),
    path('superchangeschool/<int:pk>/', views.editschoolinfo, name="superchangeschool"),
    path('superschooladd/', views.superschooladd, name="superschooladd"),

    #superuser admin control
    path('superadminadd/', views.superadminadd, name="superadminadd"),
    path('superadminlist/', AlladminView.as_view(), name="superadminlist"),
    path('superviewadmin/<int:pk>/', ViewAdmin.as_view(), name="superviewadmin"),
    path('superchangeadmin/<int:pk>/', views.editadmininfo, name="superchangeadmin"),
    path('superdeladmin/<int:pk>/', views.deladmininfo, name="superdeladmin"),
    path('superadminlistst/<int:status>/', AdminViewByStatus.as_view(), name="superadminlistst"),
    path('superadminlistsc/<int:pk>/', AdminViewBySchool.as_view(), name="superadminlistsc"),


    #admin teacher control
    path('adminindex/', views.adminindex, name="adminindex"),
    path('adminteacheradd/', views.adminteacheradd, name="adminteacheradd"),
    path('adminteacherlist/', views.adminteacherlist, name="adminteacherlist"),
    path('adminviewteacher/<int:pk>/', ViewTeacher.as_view(), name="adminviewteacher"),
    path('adminteacherlistst/<int:status>/', views.adminteacherlistst, name="adminteacherlistst"),
    path('adminchangeteacher/<int:pk>/', views.editteacherinfo, name="adminchangeteacher"),
    path('admindelteacher/<int:pk>/', views.admindelteacher, name="admindelteacher"),

    #admin group control
    path('admingroupadd/', views.admingroupadd, name="admingroupadd"),
    path('adminviewgroup/<int:pk>/', ViewGroup.as_view(), name="adminviewgroup"),
    path('admingrouplist/', views.admingrouplist, name="admingrouplist"),
    path('admingrouplistst/<int:status>/', views.admingrouplistst, name="admingrouplistst"),
    path('adminchangegroup/<int:pk>/', views.adminchangegroup, name="adminchangegroup"),

    #admin student
    path('adminstudentadd/', views.adminstudentadd, name="adminstudentadd"),
    path('adminviewstudent/<int:pk>/', ViewStudent.as_view(), name="adminviewstudent"),
    path('adminchangestudent/<int:pk>/', views.editstudentinfo, name="adminchangestudent"),

    #schedule
    path('adminschedulelist/', views.adminschedulelist, name="adminschedulelist"),
    path('adminviewschedule/<int:pk>', views.adminviewschedule, name="adminviewschedule"),
    path('adminscheduleadd/<int:pk>', views.adminscheduleadd, name="adminscheduleadd"),
    path('adminchangeschedule/<int:pk>', views.adminchangeschedule, name="adminchangeschedule"),
    path('admindelschedule/<int:pk>', views.admindelschedule, name="admindelschedule"),

    #admin lessons
    path('admincurrentlessons/', views.admincurrentlessons, name="admincurrentlessons"),
    path('admininfolesson/<int:pk>', views.admininfolesson, name="admininfolesson"),




    #lessons students
    path('studenturrentlessons/', views.studenturrentlessons, name="studenturrentlessons"),
    path('studentviewschedule/', views.studentviewschedule, name="studentviewschedule"),
    path('studentinfolesson/<int:pk>', views.studentinfolesson, name="studentinfolesson"),

    path('lessonroom/<int:pk>', views.lessonroom, name="lessonroom"),
    path('lessonroomstudent/<int:pk>', views.lessonroomstudent, name="lessonroomstudent"),
    path('lessonroomteacher/<int:pk>', views.lessonroomteacher, name="lessonroomteacher"),



    #teacher control
    # group by TEACHER
    path('teacherindex/', views.teacherindex, name='teacherindex'),
    path('teachergroupadd/', views.teachergroupadd, name='teachergroupadd'),
    path('teachergrouplist/', views.teachergrouplist, name='teachergrouplist'),
    path('teachergrouplistst/<int:status>/', views.teachergrouplistst, name="teachergrouplistst"),
    path('teacherviewgroup/<int:pk>/', ViewteacherGroup.as_view(), name="teacherviewgroup"),
    path('teacherchangegroup/<int:pk>/', views.teacherchangegroup, name="teacherchangegroup"),


    #student by TEACHER
    path('teacherstudentadd/', views.teacherstudentadd, name="teacherstudentadd"),
    path('teacherviewstudent/<int:pk>/', ViewStudentteacher.as_view(), name="teacherviewstudent"),
    path('teacherchangestudent/<int:pk>/', views.editstudentinfoteacher, name="teacherchangestudent"),


    #schedule by TEACHER
    path('teacherschedulelist/', views.teacherschedulelist, name="teacherschedulelist"),
    path('teacherviewschedule/<int:pk>', views.teacherviewschedule, name="teacherviewschedule"),
    path('teacherscheduleadd/<int:pk>', views.teacherscheduleadd, name="teacherscheduleadd"),
    path('teacherchangeschedule/<int:pk>', views.teacherchangeschedule, name="teacherchangeschedule"),
    path('teacherdelschedule/<int:pk>', views.teacherdelschedule, name="teacherdelschedule"),


    #lessons by TEACHER
    path('teachercurrentlessons/', views.teachercurrentlessons, name='teachercurrentlessons'),
    path('teacherinfolesson/<int:pk>', views.teacherinfolesson, name="teacherinfolesson"),


    path('lessonroomteacher/lessonstatus/', AjaxHandler.as_view()),
    path('lessonroomteacher/finishlesson/', AjaxHandlerfinishlesson.as_view()),
    path('lessonroomteacher/chatadd/', AjaxHandlerchatadd.as_view()),
    path('lessonroomteacher/chat/', AjaxHandlerchat.as_view()),

    path('lessonroomstudent/lessonstatus/', AjaxHandler.as_view()),
    path('lessonroomstudent/chatadd/', AjaxHandlerchatadd.as_view()),
    path('lessonroomstudent/chat/', AjaxHandlerchat.as_view()),
    # path('lessonstatus/', AjaxHandler.as_view())

    path('lessonroom/lessonstatus/', AjaxHandler.as_view()),
    path('lessonroom/finishlesson/', AjaxHandlerfinishlesson.as_view()),
    path('lessonroom/chatadd/', AjaxHandlerchatadd.as_view()),
    path('lessonroom/chat/', AjaxHandlerchat.as_view()),


]