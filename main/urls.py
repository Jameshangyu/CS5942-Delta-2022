from django.urls import path
from .views import *



urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('color/', ColorAnalysisView.as_view(), name="color"),
    path('result', Output.as_view(), name="result"),
]
