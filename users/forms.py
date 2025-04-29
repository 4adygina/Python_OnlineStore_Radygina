from django import forms
from .models import Goods, Basket

class BasketItemsForm(forms.Form):
	good = forms.ModelChoiceField(queryset=Goods.objects.all())
	quantity = forms.IntegerField()
	
class BasketForm(forms.Form):
	name = forms.CharField()
	adress = forms.CharField()
	email = forms.EmailField()
	Basket = forms.ModelChoiceField(queryset=Basket.objects.all())
