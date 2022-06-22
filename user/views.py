from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.views import View

from user.forms import LoginForm, JoinForm
from user.models import User


# 로그인
class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'user/login.html', {'form': form})

    def post(self, request):
        username = request.POST['user_account']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main:main')
        else:
            if username == '' or password == '':
                messages.error(request, "There is a blank space.")
            else:
                messages.error(request, 'username or password not correct')
            return redirect('user:login')


# 회원가입
class JoinView(View):
    def get(self, request):
        form = JoinForm()
        return render(request, 'user/join.html', {'form': form})

    def post(self, request):
        form = JoinForm(request.POST)

        if form.is_valid():
            if User.objects.filter(user_account=form.cleaned_data['user_account']).exists():
                messages.error(request, "Oops, Already existed.")
                return redirect('user:join')
            elif form.cleaned_data['password'] != form.cleaned_data['password2']:
                messages.error(request, "password and password_check is not same")
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
            messages.error(request, "check your input.")
            return redirect('user:join')