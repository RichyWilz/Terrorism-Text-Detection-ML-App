from django.urls import path
from AITerror import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("", views.index, name='index'),
    path('predict', views.predict, name='predict')
]

urlpatterns += staticfiles_urlpatterns()