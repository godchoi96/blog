from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from user.forms import LoginForm, JoinForm
from user.models import User


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'user/login.html', {'form' : form})

    def post(self, request):
        form = LoginForm(request.POST)
        username = request.POST['user_name']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main:main')
        else:
            return HttpResponse('로그인 다시 시도')


class JoinView(View):
    def get(self, request):
        form = JoinForm()
        return render(request, 'user/join.html', {'form': form})

    def post(self, request):
        form = JoinForm(request.POST)

        if form.is_valid():
            if form.cleaned_data['password'] != form.cleaned_data['password2']:
                return redirect('user:join')
            else:
                obj = User()
                obj.user_account = form.cleaned_data['user_account']
                obj.password = make_password(form.cleaned_data['password'])
                obj.user_name = form.cleaned_data['user_name']
                obj.nickname = form.cleaned_data['nickname']
                obj.user_phone = form.cleaned_data['user_phone']
                obj.user_email = form.cleaned_data['user_email']
                obj.save()
                return redirect('user:login')
        else:
            return HttpResponse('회원가입 다시')