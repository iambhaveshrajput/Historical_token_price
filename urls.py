
from django.urls import path
from priceoracle.views import get_price

urlpatterns = [
    path('api/price/', get_price),
]
