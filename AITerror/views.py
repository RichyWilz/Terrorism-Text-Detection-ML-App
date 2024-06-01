from django.shortcuts import render

# Create your views here.
# pages/views.py

from django.shortcuts import render

def index(request):
    return render(request, "AITerror/index.html", {})

# modelview
import os
import pickle
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resources/rf_model.pkl'), 'rb') as f:
    model = pickle.load(f)

with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resources/tfidf_vectorizer.pkl'), 'rb') as vec:
    vectorizer = pickle.load(vec)

@csrf_exempt
def predict(request):
    if request.method == 'POST':
        text = request.POST.get('textarea')

         # Transform the text to a numerical form
        text_vectorized = vectorizer.transform([text])

        prediction = model.predict(text_vectorized)
        return JsonResponse({'prediction': int(prediction[0])})