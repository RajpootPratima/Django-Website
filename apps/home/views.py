# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
import os


#@login_required(login_url="/login/")
def index(request):
    gallery_images_list = os.listdir(os.path.dirname(__file__).rsplit("/",1)[0]+'/static/assets/img/gallery')

    products = ["Matrix","Creata","Royal","Samrat","Crown","Dynamic",
                "Libra","Mahi","Dolphin","Rose","Freedom","Florentine",
                "Square","Flower","Showers","Allied","Sinks"]
    context = {'segment': 'index',
               'gallery': gallery_images_list,
               'products': products}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


#@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        if load_template.split('-')[-1]=='gallery':
            context['product'] = load_template.split('-')[0]
            context['product_gallery'] = os.listdir(os.path.dirname(__file__).rsplit("/",1)[0]+'/static/assets/img/'+context['product'])
        context['segment'] = load_template
        context['products'] = ["Matrix","Creata","Royal","Samrat","Crown","Dynamic",
                "Libra","Mahi","Dolphin","Rose","Freedom","Florentine",
                "Square","Flower","Showers","Allied","Sinks"]

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
