from django.contrib.auth.models import AbstractUser
from django.db import models


# 아이디, 비밀번호, 이름, 닉네임
from django import forms


class User(AbstractUser):
    class Meta:
        db_table = 'User'

    nickname = models.CharField(max_length=10, blank=False)

