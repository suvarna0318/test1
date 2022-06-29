from django.shortcuts import render,redirect
from .models import Products
from .forms import ProductForm

def home(request):
	context={
	'products':Products.objects.all
	}
	return render(request,'home.html',context)

def grocery_list(request):
	if request.method=="POST":
		form=ProductForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')

	else:
		form=ProductForm()
	return render(request,'grocery_add.html',{'form':form})

def grocery_list_remove(request,id):	
	products=Products.objects.get(id=id)
	products.delete()
	return redirect('home')
