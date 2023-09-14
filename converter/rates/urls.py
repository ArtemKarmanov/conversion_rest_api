from django.urls import path

from .views import RatesCurrencies

app_name = 'rates'

urlpatterns = [
	path('', RatesCurrencies.as_view(), name='rates'),
]