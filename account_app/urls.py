
from django.contrib import admin
from django.urls import path
from  . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('' , views.home , name= 'homepage'),
    path('profile/' , views.profile , name= 'profile'),
    path('edit_profile/' , views.edit_profile, name= 'edit_profile'),
    path('register/' , views.RegisterView.as_view() , name= 'register'),
    path('Log_out/' , views.Log_out.as_view() , name= 'Log_out'),
    path('Log_in/' , views.Log_inView.as_view() , name= 'log_in'),
]
