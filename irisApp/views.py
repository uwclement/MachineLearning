from django.shortcuts import render


from joblib import load
model = load('./savedModels/model2.joblib')
model2 = load('./savedModels/model5.joblib')  
maleria_model= load('./savedModels/malariamodel.joblib')
cyberbulling_model= load('./savedModels/trained_model_syberbullying.joblib')
hate_model = load('./savedModels/trained_model_hatespeech.joblib')
hate_vectorized = load('./savedModels/hate_vectorizer.joblib')
# Load the TfidfVectorizer used during training
vectorizer = load('./savedModels/tfidf_vectorizer.joblib') 
disease_model= load('./savedModels/diseasemodel.joblib')


def heart_predictor(request):
    if request.method == 'POST':
        age = request.POST['age']
        sex = request.POST['sex']
        cp = request.POST['cp']
        trestbps = request.POST['trestbps']
        chol = request.POST['chol']
        fbs = request.POST['fbs']
        restecg = request.POST['restecg']
        thalach = request.POST['thalach']
        exang = request.POST['exang']
        oldpeak = request.POST['oldpeak']
        slope = request.POST['slope']
        ca = request.POST['ca']
        thal = request.POST['thal']
        y_pred = model2.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        if y_pred[0] == 0:
          y_pred = 'The Person does not have a Heart Disease'
        elif y_pred[0] == 1:
          y_pred = 'The Person has Heart Disease'
        else:
          y_pred = 'Error'        
        return render (request, 'main2.html', {'result': y_pred})
    return render(request, 'main2.html')


def refresh(request):
    return render( request, 'main2.html')
  
  
# def formInfo(request):
#     sepal_length = request.GET['sepal_length']
#     sepal_width = request.GET['sepal_width']
#     petal_length = request.GET['petal_length']
#     petal_width = request.GET['petal_width']
#     y_pred = model.predict([[sepal_length,sepal_width,petal_length,petal_width]])
#     if y_pred[0] == 0:
#         y_pred = 'setosa'
#     elif y_pred[0] == 1:
#         y_pred = 'Vercicolor'
#     else:
#         y_pred = 'Verginica'        
#     return render (request, 'result.html', {'result': y_pred})

def predictor(request):
    if request.method == 'POST':
        sepal_length = request.POST['sepal_length']
        sepal_width = request.POST['sepal_width']
        petal_length = request.POST['petal_length']
        petal_width = request.POST['petal_width']
        y_pred = model.predict([[sepal_length,sepal_width,petal_length,petal_width]])
        if y_pred[0] == 0:
          y_pred = 'setosa'
        elif y_pred[0] == 1:
          y_pred = 'Vercicolor'
        else:
          y_pred = 'Verginica'        
        return render (request, 'main1.html', {'result': y_pred})
    return render(request, 'main1.html')
  
  
def malatia_predictor(request):
    if request.method == 'POST':
        temperature = request.POST['temperature']
        parasite_density = request.POST['parasite_density']
        whc_count = request.POST['whc_count']
        hb_level = request.POST['hb_level']
        hematocrit = request.POST['hematocrit']
        mean_cell_volume = request.POST['mean_cell_volume']
        mean_corp_hb = request.POST['mean_corp_hb']
        mean_cell_hb_conc = request.POST['mean_cell_hb_conc']
        platelet_count = request.POST['platelet_count']
        platelet_distr_width = request.POST['platelet_distr_width']
        mean_platelet_vl = request.POST['mean_platelet_vl']
        neutrophils_percent = request.POST['neutrophils_percent']
        lymphocytes_percent = request.POST['lymphocytes_percent']
        mixed_cells_percent = request.POST['mixed_cells_percent']
        neutrophils_count = request.POST['neutrophils_count']
        lymphocytes_count = request.POST['lymphocytes_count']
        mixed_cells_count = request.POST['mixed_cells_count']
        y_pred = maleria_model.predict([[temperature,parasite_density,whc_count,hb_level,hematocrit,mean_cell_volume,mean_corp_hb,mean_cell_hb_conc,platelet_count,platelet_distr_width,mean_platelet_vl,neutrophils_percent,lymphocytes_percent,mixed_cells_percent,neutrophils_count,lymphocytes_count,mixed_cells_count]])
        # if y_pred[0] == 0:
        #   y_pred = 'The Person does not have a Heart Disease'
        # elif y_pred[0] == 1:
        #   y_pred = 'The Person has Heart Disease'
        # else:
        #   y_pred = 'Error'        
        # return render (request, 'main3.html', {'result': y_pred})
        return render(request, 'main3.html',{'result': y_pred})
    else:
      return render(request, 'main3.html',{'result':''})




# the funcyion of cyberbullying

def cyberbullying_prediction (request):
  if request.method =='POST':
    tweets = request.POST['tweets']

    # Vectorize the input text
    tweets_vectorized = vectorizer.transform([tweets])

    y_pred = cyberbulling_model.predict(tweets_vectorized)
    return render(request, 'cyberbullying.html',{'result': y_pred})
  else:
    return render(request, 'cyberbullying.html',{'result':''})
   
    
def hate_prediction (request):
  if request.method =='POST':
    tweets = request.POST['tweets']

    # Vectorize the input text
    tweets_vectorized = hate_vectorized.transform([tweets])

    y_pred = hate_model.predict(tweets_vectorized)
    return render(request, 'Hate.html',{'result': y_pred})
  else:
    return render(request, 'Hate.html',{'result':''})
    
    
    
def disease_prediction (request):
   if request.method == 'POST':
     symptom1 = request.POST['symptom1']
     symptom2 = request.POST['symptom2']
     symptom3 = request.POST['symptom3']
     symptom4 = request.POST['symptom4']
     symptom5 = request.POST['symptom5']
     y_pred = disease_model.preddict([[symptom1, symptom2, symptom3, symptom4, symptom5]])
     return render (request, 'disease.html',{'result':y_pred})
   else:
      return render (request, 'disease.html',{'result': ''})   