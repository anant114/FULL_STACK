from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import upload_file, download_file


from django.urls import re_path


urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", views.index1, name='myapp'),
    path("login_page", views.login_page, name='login_page'),
    path("signup", views.signup, name='signup'),
    path("datatable", views.datatable, name='datatable'),
    path("forgot", views.forgot, name='forgot'),
    path("signout", views.signout, name='signout'),
    path("successful", views.successful, name='successful'),
    path("emailreset", views.emailreset, name='emailreset'), 
    path("userlist", views.userlist, name='userlist'), 
    path("add_market", views.add_market, name='add_market'), 
    path("edit_market", views.edit_market, name='edit_market'), 
    path("adduser", views.adduser, name='adduser'), 
    path("alarm", views.alarm, name='alarm'), 
    path("market2", views.market2, name='market2'), 
    path("dashboard", views.dashboard, name='dashboard'), 
    path("account_settings", views.account_settings, name='account_settings'), 
    path("practice", views.practice, name='practice'),
    path("rolelist", views.rolelist, name='rolelist'),
    path("companylist", views.companylist, name='companylist'),
    path("delete", views.delete, name='delete'),
    path("createactivity", views.createactivity, name='createactivity'), 
    path("activitylist", views.activitylist, name='activitylist'),    
     path('process_excel', views.process_excel, name='process_excel'),            
    path('process', views.process_form, name='process_form'),  
    path('lgfile', upload_file, name='upload_file'),
    path('download/',download_file, name='download_file'),      

   
]

if settings.DEBUG:

 urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



