from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You are not authorized to view this page. Sizga ushbu sahifa uchun ruhsat berilmagan.")
        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == "student":
            return redirect("home")

        if group == "teacher":
            return redirect("home")

        if group == "admin":
            return view_func(request, *args, **kwargs)
    return wrapper_func

def superuser_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        else:
            return redirect("home")
    return wrapper_func

def adminuser_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == "admin":
            return view_func(request, *args, **kwargs)
        else:
            return redirect("home")
    return wrapper_func

def studentuser_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == "student":
            return view_func(request, *args, **kwargs)
        else:
            return redirect("home")
    return wrapper_func

def teacheruser_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == "teacher":
            return view_func(request, *args, **kwargs)
        else:
            return redirect("home")
    return wrapper_func



def free_access(view_func):
    def wrapper_func(request, *args, **kwargs):
        return view_func(request, *args, **kwargs)
    return wrapper_func

