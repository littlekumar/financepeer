import json

import requests
from django.shortcuts import render
from .registration_and_login_forms import Login_View, Logout_View, Signup_View

# Create your views here.

from django.contrib.auth.decorators import login_required
from .models import File, UploadFileModelForm, Files, file_Json_data, files_data
from django.db import IntegrityError
from django.contrib import messages
from django.shortcuts import render, redirect, resolve_url



login = Login_View.as_view()
logout = Logout_View.as_view()
signup = Signup_View.as_view()

@login_required()
def homepage(request):
    if request.method == 'POST':
        file_form = UploadFileModelForm(request.POST, request.FILES)
        files = request.FILES.getlist('file')
        if file_form.is_valid():
            for f in files:
                try:
                    # saving the file
                    resume = File(file=f)
                    resume.save()

                except IntegrityError:
                    messages.warning(request,'Duplicate resume found:', f.name)
                    return redirect('homepage')

            l_file = File.objects.all().last()
            l_file = l_file.file
            file_path = "http://127.0.0.1:8000/mediafiles/"+str(l_file)
            file1 = requests.get(file_path).json()
            for x in file1:
                user_id = x['userId']
                id = x['id']
                title = x['title']
                body = x['body']
                l_file = File.objects.all().last().id
                file_Json_data(user_id=user_id,u_id=id,title=title,body=body,files_id=l_file).save()

            files = File.objects.all()

            messages.success(request, 'File uploaded!')
            context = {
                'files': files,
            }
            return render(request, 'base.html', context)
    else:
        form = UploadFileModelForm()
        return render(request, 'base.html', {'form': form})

@login_required()
def files(request):
    files = File.objects.all()
    context = {
        'files': files,
    }
    return render(request, 'base.html', context)


@login_required()
def file_data(request):
    id=request.GET.get('id')
    print('--- id --',id)
    f_data = file_Json_data.objects.filter(files_id=id)
    file_ = File.objects.get(id=id).file
    context = {
        'files': f_data,
        'file_':file_
    }
    return render(request,'file_data.html',context)
