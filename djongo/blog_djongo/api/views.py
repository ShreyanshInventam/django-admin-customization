from re import template
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import  Task
from django.views import View
from django.views.generic import ListView, DetailView


class ApiListView(ListView):
    model = Task
    template_name = 'api_list.html'

    def get(self, request):
        obj = self.model.objects.all()
        return render(request, template_name=self.template_name, context={'obj':obj})

class ApiDetailView(DetailView):
    model = Task
    template_name = 'api/api_detail.html'
