from django.urls import path
from . import views

urlpatterns = [
    path('demo', views.index, name='demo'),
    path('new_interaction', views.index, name='new_interaction'),
    path('homepage', views.home, name='homepage'),
    path('mybook', views.mybook, name='mybook'),
    path('templates', views.templates, name='templates'),
    
    # path('', views.index, name='index'),

    # 
    # path('3/', views.three, name='three'),
    # path('4/', views.four, name='four'),
    # path('5/', views.five, name='five'),
]
