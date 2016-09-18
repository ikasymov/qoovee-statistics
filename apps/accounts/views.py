# coding: utf-8
from django.contrib import auth
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from apps.accounts.forms import Registrations
from apps.reports.models import Department
from apps.profiles.models import Profile


def register(request):
    department = Department.objects.all()
    user = Registrations(request.POST or None)
    if user.is_valid():
        obj = user.save(commit=False)
        if obj.password == request.POST['password2']:
            obj.set_password(user.cleaned_data['password'])
            obj.is_active = False
            obj.save()
            obj_department_id = Department.objects.get(pk=request.POST.get('select'))
            Profile.objects.create(user=obj, phone=request.POST.get('phone'), department=obj_department_id)
        return redirect('accounts:guest_page')
    else:
        messages.success(request, 'Введенные пароли не совпадают')

    return render(request, 'reg.html', {'form': user, 'depart': department})


def create_profile(request, user, phone):
    create = Profile.objects.create(user=user, phone=phone)
    messages.success(request, 'Пожалуйста введите личные данные')


def authentication(request):
    if request.POST:
        authenticated(request, request.POST.get('username'), request.POST.get('password'))
        return redirect('/')
    return render(request, 'signin.html', {})


def authenticated(request, username, password):
    username = username
    password = password
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)


@login_required
def auth_logout(request):
    logout(request)
    return redirect('/')


def page_for_guest(request):
    return render(request, 'page_for_guest.html', {})
