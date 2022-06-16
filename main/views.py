from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class MainView(View):
    def get(self, request):
        return HttpResponse('Main')