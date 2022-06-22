from django.db import models


class User(models.Model):
    user_account = models.CharField("유저 계정", max_length=20)
    password = models.CharField("유저 비밀번호", max_length=40)
    password2 = models.CharField("비밀번호 체크", max_length=40)
    user_name = models.CharField("유저 이름", max_length=10)
    nickname = models.CharField("유저 닉네임", max_length=10)
    user_phone = models.CharField("유저 핸드폰 번호", max_length=15)
    user_email = models.EmailField("유저 이메일", max_length=30)