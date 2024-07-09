"""
URL configuration for employereg project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('addD',views.addD),
    # path('viewE',views.viewE),
    path('employe',views.employe),
    path('delete',views.delete),
    path('edit1',views.edit1),
    path('edit2',views.edit2),
    path('delete2',views.delete2),
    path('customer',views.customer),
    path('login/',views.loginP),
    path('custHome', views.custHome),
    path('cEdit', views.cEdit),
    path('cDele', views.cDele),
    path('empHome',views.empHome),
    path('addproduct',views.addproduct),
    path('viewproduct',views.viewproduct),
    path('sview',views.sview),
    path('buynow',views.buynow),
    path('history',views.history),
    path('deleteorder',views.deleteorder),
    path('purchased_list',views.purchased_list),
    path('changeStatus',views.changeStatus),
    path('editproduct',views.editproduct),
    path('ineditproduct',views.ineditproduct),
    path('deleteproduct',views.deleteproduct),
    path('adminHome',views.adminHome),
    path('department',views.department),
    path('viewEmp',views.viewEmp),
    path('yourC',views.yourC),
    path('activeS',views.activeS),
    path('logoutFun',views.logoutFun),
    # path('hview',views.hview),
]
