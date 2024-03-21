from django.shortcuts import render,redirect
from .models import Item
from django import forms
# Create your views here.

# def home(request):
# 	context = {
#
# 	}
# 	return render(request,'base.html', context)

def show_item(request):
	item_list = Item.objects.all()
	context ={
		'item_list':item_list,
	}
	return render(request,'index.html',context)

def view_item(request,item_id):
	item = Item.objects.get(pk=item_id)
	context = {
		'item':item,
	}
	return render(request,'view_item.html',context)

class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = ['item_name', 'item_desc', 'item_price', 'item_rating', 'item_image']
		widgets = {
			'item_desc': forms.Textarea(attrs={'rows': 4}),  # Customize widget if needed
		}

def add_item(request):
	# form = ItemForm(request.POST)
	# if form.is_valid():
	# 	form.save()
	# 	return redirect('food:show_item')
	# return render(request, 'add_form.html',{'form':form})
	if request.method == 'POST':
		form = ItemForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('show_item')  # Redirect to the desired URL after successful form submission
	else:
		form = ItemForm()
	return render(request, 'add_form.html', {'form': form})

def delete_item(request,id):
	item = Item.objects.get(id=id)
	if request.method == "POST":
		item.delete()
		return redirect('show_item')
	return render(request,'delete_item.html',{'item':item})

def update_item(request,id):
	item = Item.objects.get(id=id)
	form = ItemForm(request.POST or None, instance=item)
	if form.is_valid():
		form.save()
		return redirect('show_item')
	return render(request,'update_item.html',{'form':form, 'item':item})


