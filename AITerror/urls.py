from django.urls import path
from AITerror import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("", views.index, name='index'),
    path('predict', views.predict, name='predict')
]

urlpatterns += staticfiles_urlpatterns()

# from lime.lime_text import LimeTextExplainer

# def my_predict_function(x):
#     # Preprocess the input text (similar to what you did before)
#     testing_sequences = tokenizer.texts_to_sequences(x)
#     testing_padded = tf.keras.preprocessing.sequence.pad_sequences(testing_sequences, maxlen=max_length, padding=padding_type, truncating=trunc_type)

#     # Get prediction probabilities (two columns: [bad, good])
#     prediction_probs = model.predict(testing_padded)
#     return prediction_probs

# # Explain the instance using LIME
#         explainer = LimeTextExplainer(class_names=["bad", "good"])
#         exp = explainer.explain_instance(text, my_predict_function, num_features=7)

#         # Convert prediction probabilities to class label (0 or 1)
#         prediction = int(exp.predict_proba[0][1] > 0.5)