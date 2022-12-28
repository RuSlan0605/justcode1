from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Shop
from .models import Rubric
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import ShopForm


def index(request):
    template = loader.get_template('shop/by_index.html')
    rubrics = Rubric.objects.all()
    shops = Shop.objects.all()
    context = {
        'shops' : shops,
        'rubrics': rubrics,
    }
    return HttpResponse(template.render(context, request))

def by_rubric(request, rubric_id):
    shops = Shop.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {
        'shops' : shops,
        'rubrics': rubrics,
        'current_rubric': current_rubric
    }
    return render(request, 'shop/by_rubric.html', context)

def ShopCreate(request):
    form = ShopForm()
    if request.method == 'POST':
        form = ShopForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/shop/')
    context = {
        'form' : form
    }
    return render(request, 'shop/create.html',context)


