from django.shortcuts import render
from joblib import load

model = load('./savedModels/model.joblib')
# Create your views here.
def predictor (request):
    return render(request,'main.html')

def formInfo(request):
 if (request.method == 'POST'):
    symptom1 = request.POST.get('symptom1')
    symptom2 = request.POST.get('symptom2')
    symptom3 = request.POST.get('symptom3')
    symptom4 = request.POST.get('symptom4')
    symptom5 = request.POST.get('symptom5')

    y_pred  =model.predict([[symptom1, symptom2, symptom3, symptom4, symptom5]])
    print (y_pred)
    return render(request,'result.html')
   
def homepage (request):
    return render(request,'homepage.html')   