from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.


class IndexView(View):

    def get(self, request):
        # <view logic>
        return HttpResponse('index view venue')
