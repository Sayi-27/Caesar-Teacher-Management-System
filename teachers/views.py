from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Teacher
from .forms import TeacherForm

# Create your views here.
def index(request):
    return render(request, 'teachers/index.html',{
        'teachers': Teacher.objects.all()
    })

def view_teacher(request, id):
    teacher = Teacher.objects.get(id=pk)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
          new_TSC_Number = form.cleaned_data['TSC_Number']
          new_first_name = form.cleaned_data['first_name']
          new_last_name = form.cleaned_data['last_name']
          new_Responsibility = form.cleaned_data['Rensponsibility']
          new_Subject = form.cleaned_data['Subject']
          new_phone_number = form.cleaned_data['phone_number']

        new_teacher = Teacher(
            TSC_Number = new_TSC_Number,
            first_name = new_first_name,
            last_name = new_last_name,
            Rensponsibility = new_Responsibility,
            Subject = new_Subject,
            phone_number = new_phone_number
        )
        new_teacher.save()
        return render(request, 'teachers/add.html', {
            'form': TeacherForm(),
            'success': True
        })
    else:
        form = TeacherForm()
        return render(request, 'teachers/add.html', {
            'form': TeacherForm()
        })

def edit(request, id):
    if request.method == 'POST':
        teacher = Teacher.objects.get(pk=id)
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return render(request, 'teachers/edit.html', {
                'form': form,
                'success': True
            })
    else:
        teacher = Teacher.objects.get(pk=id)
        form = TeacherForm(instance=teacher)
    return render(request, 'teachers/edit.html', {
                'form': form
    })

def delete(request, id):
    if request.method == 'POST':
        teacher = Teacher.objects.get(pk=id)
        teacher.delete()
    return HttpResponseRedirect(reverse('index'))