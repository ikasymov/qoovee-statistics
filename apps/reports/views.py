# coding: utf-8
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from apps.reports.models import Statistic, Report
from .decorators import check_time, check_for_departmens
import datetime


@check_time
@check_for_departmens
def add_report(request, argument):
    if request.GET:
        get_and_process_list_report(request)
        return redirect(request.path)
    return render(request, 'add_report.html', {'form': argument})


def timer_for_button_add_report():
    time = datetime.datetime.now().strftime('%H')
    hour = int(time)
    return hour


def get_and_process_list_report(request):
    counter = 0
    list_of_request_method = []
    while True:
        name = request.GET.get('form-%s-name' % counter, None)
        number = request.GET.get('form-%s-number' % counter, None)

        if not name:
            break

        list_of_request_method.append({
            'name': name,
            'number': number
        })
        counter += 1
    report_create = Report.objects.create(
            user=request.user.profile, department=request.user.profile.department, edited_by=request.user)
    for i in list_of_request_method:
        number = i[u'number']
        Statistic.objects.create(name=i['name'], value=i['number'], report=report_create)
    return list_of_request_method


# asd
# asd

# asd# asd
