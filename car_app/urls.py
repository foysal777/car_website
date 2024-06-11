
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from  .import views

urlpatterns = [  
  
    path('slug/<slug:brand_slug>/' , views.home  , name= 'slug_name'),
    path('details/<int:id>/' , views.detailsView.as_view() , name= 'details'),
    path('buys/<int:id>/', views.buyView.as_view(), name='buy'),
    #  path('success/', views.success_view, name='success_page'),
 
]

if settings.DEBUG:urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)