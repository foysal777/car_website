from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from car_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.home , name= 'homepage'),
    path('account_app/' , include('account_app.urls')),
    path('car_app/' , include('car_app.urls'))
    
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)