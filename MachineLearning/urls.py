
from django.contrib import admin

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
#    path('', include('basicConcepts.urls')),
    #  path('',include('PredictApp.urls')),
     path('', include('irisApp.urls')),
   
  
]
