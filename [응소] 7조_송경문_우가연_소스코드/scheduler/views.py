from django.shortcuts import render, redirect, get_object_or_404
from .models import Schedule
from .forms import ScheduleForm

def schedule_list(request):
    schedules = Schedule.objects.all()
    return render(request, 'scheduler/schedule_list.html', {'schedules': schedules})

def add_schedule(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedule_list')
    else:
        form = ScheduleForm()
    return render(request, 'scheduler/add_schedule.html', {'form': form})

def edit_schedule(request, id):
    schedule = get_object_or_404(Schedule, id=id)
    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            return redirect('schedule_list')
    else:
        form = ScheduleForm(instance=schedule)
    return render(request, 'scheduler/edit_schedule.html', {'form': form})

def delete_schedule(request, id):
    schedule = get_object_or_404(Schedule, id=id)
    if request.method == 'POST':
        schedule.delete()
        return redirect('schedule_list')
    return render(request, 'scheduler/delete_schedule.html', {'schedule': schedule})
