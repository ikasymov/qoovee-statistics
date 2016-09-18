# coding: utf-8
from django.shortcuts import redirect
from apps.reports.forms import ReportForm
from django.forms import formset_factory
import datetime


def check_time(function):
    def check_for_add_report(request, *args, **kwargs):
        time = datetime.datetime.now().strftime('%H')
        hour = int(time)
        if hour >= 16 and hour <= 20:
            return function(request, *args, **kwargs)
        else:
            return redirect('accounts:guest_page')
    return check_for_add_report


def check_for_departmens(function):
    def check_departments(request, *args, **kwargs):

        if request.user.profile.department.number == 2:
            list_for_department_2 = ['Звонки', 'Коммерческое предложение', 'Контракты', 'Баланс на счете', 'Минуты разговора']
            exemple = []
            for i in list_for_department_2:
                pr = {'name': i, 'number': 0}
                exemple.append(pr)
            ReportSet = formset_factory(ReportForm, max_num=1)
            formsset = ReportSet(initial=exemple)
            form = formsset
            return function(request, form, *args, **kwargs)

        elif request.user.profile.department.number == 6:
            list_for_department_6 = ['Звонки', 'Встречи', 'Завершенные звонки', 'Предоплаты', 'Бесплатный магазин']
            exemple = []
            for i in list_for_department_6:
                pr = {'name': i, 'number': 0}
                exemple.append(pr)
            ReportSet = formset_factory(ReportForm, max_num=1)
            formsset = ReportSet(initial=exemple)
            form = formsset
            return function(request, form, *args, **kwargs)
        else:
            return redirect(request.path)

    return check_departments
