from django.urls import path
from . import views
urlpatterns =[
    path("",views.home,name='home'),
    path("show/",views.show,name='show'),
    path("add/",views.add,name="add"),
    path('delete/<int:pid>',views.delete,name="delete"),
    path('edit/<int:pid>',views.edit,name="edit"),
    path('loginu/',views.loginu,name="loginu"),
    path('register/',views.register,name="register"),
    path('logoutu/',views.logoutu,name="logoutu"),
    path('search/',views.search_products,name="search"),
    path('electronics/',views.electronics,name="electronics"),
    path('carandmotorbikes/',views.carandmotorbikes,name="carandmotorbikes"),
    path('fashion/',views.fashion,name="fashion"),
    path('homeandkitchen/',views.homeandkitchen,name="homeandkitchen"),
]