from django.shortcuts import render
from apps.profiles.models import Profile
from django.contrib.auth.decorators import login_required
from django.db.models import F, Sum
import datetime


@login_required
def index(request):
    user = Profile.objects.all()
    context = {
        'user': user,
        'time': timer_for_button_add_report(),
    }
    return render(request, 'index.html', context)


def chart_for_all_profile():
    user = Profile.objects.all()
    report = []
    for i in user:
        sum_report_values = i.report.aggregate(
            summ_all_report_values=Sum(F('calls')+F('contracts')+F('meetings')+F('prepayment')+F('standart_shop')))
        report.append(sum_report_values)
    all_list = zip(user, report)
    return all_list


def timer_for_button_add_report():
    time = datetime.datetime.now().strftime('%H')
    hour = int(time)
    return hour
