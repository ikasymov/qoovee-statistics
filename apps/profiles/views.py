# coding: utf-8
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.db.models import F, Sum
from apps.profiles.models import Profile
from apps.profiles.forms import EditProfile


@login_required
def detail_info(request, profiles_id):
    user = Profile.objects.get(id=profiles_id)
    profile_report_info = user.report.all()
    if request.GET:
        return render(request, 'detail_info.html', selected_date(request, profile_id=profiles_id))
    context = {
       'profile': user,
       'report': profile_report_info,
    }
    return render(request, 'detail_info.html', context)


@require_http_methods(["GET", "POST"])
def selected_date(request, profile_id):
    user = Profile.objects.get(id=profile_id)
    selected_dates = request.GET.get('dates')
    selected_date = request.GET.get('date')
    date_of_choice = [selected_dates, selected_date]
    profile_report_info = user.report.all()
    selected_report = user.report.filter(create_date__range=date_of_choice)
    selected_report_context = {
        'selected_report': selected_report,
        'report': profile_report_info,
    }
    return selected_report_context


@login_required
def edit_profile(request, edit_profile_id):
    profile = Profile.objects.get(pk=edit_profile_id)
    form = EditProfile(request.POST or None, request.FILES or None, instance=profile)
    if form.is_valid():
        form = form.save(commit=False)
        form.save()
        messages.success(request, 'Изменение сохранились')
        return redirect(request.path)
    return render(request, 'edit_profile.html', {'form': form})


def start(request):
    pass