from django.shortcuts import render
import os
import pickle
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from lime.lime_text import LimeTextExplainer

# Create your views here.
# pages/views.py





# modelview

with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resources/rf_model.pkl'), 'rb') as f:
    model = pickle.load(f)

with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resources/tfidf_vectorizer.pkl'), 'rb') as vec:
    vectorizer = pickle.load(vec)


def my_predict_function(x):
    # Transform the text to a numerical form using your existing vectorizer
    text_vectorized = vectorizer.transform(x)  # Assuming x is a list of text inputs

    # Get prediction probabilities (two columns: [bad, good])
    prediction_probs = model.predict_proba(text_vectorized)
    return prediction_probs



def index(request):
    return render(request, "AITerror/index.html", {})

@csrf_exempt
def predict(request):
    if request.method == 'POST':
        text = request.POST.get('textarea')

         # Transform the text to a numerical form
        text_vectorized = vectorizer.transform([text])

        # Explain the instance using LIME
        explainer = LimeTextExplainer(class_names=["0", "1"])
        exp = explainer.explain_instance(text, my_predict_function, num_features=7)

        # Convert the explanation to a list of tuples
        explanation = exp.as_list()


        prediction = model.predict(text_vectorized)

         # Convert the explanation and prediction to a JSON serializable format
        response = {
            'prediction': int(prediction[0]),
            'explanation': explanation
        }
        # return render(request, "AITerror/index.html", {"text": text, "prediction": prediction, "explanation": exp.as_html()})
        return JsonResponse(response)