from django.shortcuts import render, redirect

from users.models import Goods, Clients, Basket_items
from users.forms import BasketItemsForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.

def goods_list(request):
    goods = Goods.objects.all()
    context = {'goods': goods}
    return render(request, 'goods_list.html', context)

def good_detail(request, pk):
    goods = Goods.objects.get(pk=pk)
    context = {'goods': goods}
    return render(request, 'goods_detail.html', context)

def clients_list(request):
    clients = Clients.objects.all()
    context = {'clients': clients}
    return render(request, 'clients_list.html', context)

def client_detail(request, pk):
    clients = Clients.objects.get(pk=pk)
    context = {'clients': clients}
    return render(request, 'clients_detail.html', context)

def add_to_basket(request):
            if request.method == 'POST':
                form = BasketItemsForm(request.POST)
                if form.is_valid():
                    good = form.cleaned_data['good']
                    quantity = form.cleaned_data['quantity']
                    basket, created = Basket_items.objects.get_or_create(user=request.user)
                    basket.add_item(good, quantity)
                return redirect('basket')
            else:
                form = BasketItemsForm()
            return render(request, 'add_to_basket.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            form = UserCreationForm()
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def home_view(request):
    return render(request, 'home.html')
