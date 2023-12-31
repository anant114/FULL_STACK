"""
URL configuration for table project.

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from myapp import views

# from myapp import views
# from django.shortcuts import render
# from myapp.models import signup
# from django.contrib.auth.models import data
# def data_table(request):
#     data = data.objects.all('first_name','last_name','CompanyName' , 'phone_number','email')
#     return render(request, 'datatable.html', {'signups': signups})


admin.site.site_header = "Pushpendra Kumar"
admin.site.site_title = "Pushpendra Kumar Portal"
admin.site.index_title = "Welcome to Pushpendra Kumar Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
] 


