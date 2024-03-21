from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('food/', views.show_item, name='show_item'),
	path('food/<int:item_id>/',views.view_item,name='view_item'),
	path('food/add/',views.add_item,name='add_item'),
	path('food/delete/<int:id>',views.delete_item,name ='delete_item'),
	path('food/update/<int:id>',views.update_item,name='update_item')
]