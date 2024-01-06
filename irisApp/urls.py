from django.urls import path
from . import views 

urlpatterns = [
     path('',views.predictor, name='predictor'),
    # path('result',views.formInfo, name='result'),
      path('heart',views.heart_predictor, name='heart_predictor'),
      path('malaria',views.malatia_predictor, name='malatia_predictor'),
      path('cyberbullying',views.cyberbullying_prediction, name='cyberbullying'),
      path('hate',views.hate_prediction, name='hate'),
      path('disease',views.disease_prediction, name='disease_prediction')
 ]
 