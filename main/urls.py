from django.urls import path
from . import views

urlpatterns = [
    #path('<int:nu>', views.index, name='hzpage'),
    path('', views.home, name='UY')
]