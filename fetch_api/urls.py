from django.urls import path
from .views import CreateRetrieveAPIView
urlpatterns = [
    path('', CreateRetrieveAPIView.as_view(), name='create'),

]
