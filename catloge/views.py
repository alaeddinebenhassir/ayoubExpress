from django.shortcuts import render ,redirect, get_object_or_404 #, render_to_request 
from .models import Item  ,Categorie
from .forms import SignUpForm
from django.contrib.auth import login, authenticate , logout
from django.http import JsonResponse
import json
# Create your views here.
def err(request):
    return render(request , 'catloge/err.html')

def index(request):
    product = Item.objects.all()
    c= Categorie.objects.all()
    if request.is_ajax() :
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            #raw_password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)
            
            data = {
                'message' : 'form is saved'      
            }
            return JsonResponse(data) ,redirect(to,url='/catloge',permanent=False)
            

        else:
            
            dataerr = {
                'message' : 'wrong'      
            }
            return JsonResponse(dataerr , safe=False)
    else:
        form = SignUpForm()

    
    return render(request, 'index.html', {'form': form , 'product':product ,'c' : c})
    

def show_categories(request):
    c = Categorie.objects.all()
    product = Item.objects.all()
    if request.is_ajax() :
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            #raw_password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)
            
            data = {
                'message' : 'form is saved'      
            }
            return JsonResponse(data)
        else:
            
            dataerr = {
                'message' : 'wrong'      
            }
            return JsonResponse(dataerr , safe=False)
    else:
        form = SignUpForm()

    return render(request ,'categories.html' ,locals())

def show_categorie(request , slug):
    c = Categorie.objects.all()
    p = get_object_or_404(Categorie ,slug=slug)
    products = Item.objects.all().filter(ctgr=p.pk)
    if request.is_ajax() :
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            #raw_password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)
            
            data = {
                'message' : 'form is saved'      
            }
            return JsonResponse(data)
        else:
            
            dataerr = {
                'message' : 'wrong'      
            }
            return JsonResponse(dataerr , safe=False)
    else:
        form = SignUpForm()

    return render(request ,'products.html' , locals() )

def show_products(request , slug ):
    c = Categorie.objects.all()

    p = get_object_or_404(Item , slug=slug)
    if request.is_ajax() :
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            #raw_password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)
            
            data = {
                'message' : 'form is saved'      
            }
            return JsonResponse(data)
        else:
            
            dataerr = {
                'message' : 'wrong'      
            }
            return JsonResponse(dataerr , safe=False)
    else:
        form = SignUpForm()

    return render(request ,'product.html' ,locals())
def test_items(request):
    p = Item.objects.all()
    return render(request , 'items.html' , locals())

def purchased(request , id , uid):
    pass

def by(request , slug):
    pro = get_object_or_404(Item ,slug=slug)
    return render(request , 'purchase.html' , locals())