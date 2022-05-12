from django.shortcuts import render
from django.views.generic import TemplateView


class SinovView(TemplateView):
    template_name='base.html'