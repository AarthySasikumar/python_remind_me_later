from django.shortcuts import render, redirect
from .forms import ReminderForm

def create_reminder(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reminder_created')
    else:
        form = ReminderForm()
    return render(request, 'create_reminder.html', {'form': form})

def reminder_created(request):
    return render(request, 'reminder_created.html')
