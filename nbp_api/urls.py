"""
URL configuration for nbp_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('api/avg_exchange_rate/<str:currency_code>/<str:date>/', views.avg_exchange_rate, name='avg_exchange_rate'),
    path('api/min_max_average/<str:currency_code>/<int:n>/', views.min_max_average, name='min_max_average'),
    path('api/buy_sell_difference/<str:currency_code>/<int:n>/', views.buy_sell_difference, name='buy_sell_difference'),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('<path:path>', TemplateView.as_view(template_name='index.html'), name='catchall'),
]
