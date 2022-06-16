from django.contrib.auth import authenticate, login
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
        username = request.POST['username']
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
            new_user = User.objects.create_user(**form.cleaned_data)
            return redirect('user:login')
        else:
            return HttpResponse('회원가입 다시')