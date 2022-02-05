from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.home, name= 'blog-name'),
    path('login', views.login, name= 'blog-login'),
    path('index', views.index, name= 'blog-index'),
    path('register', views.register, name= 'blog-register'),
    path('page1', views.page1, name ='blog-page1'),
    path('contact', views.contact, name='blog-contact'),
    path('alpr' , views.alpr , name='blog-alpr'),
    path('fine_history' , views.fine_history , name= 'blog-fine_history'),
    path('current_fine', views.current_fine , name= 'blog-current_fine'),
    path('adminhome', views.adminhome , name= 'blog-adminhome'),
    path('userhome', views.userhome , name = 'blog-userhome'),
    path('current_fine1', views.current_fine1 , name= 'blog-current_fine1'),
    path('payment', views.payment , name = 'blog-payment'),
    path('upload', views.fine_upload, name= 'blog-upload'),
    path('upload1/<str:obj>', views.fine_upload1, name= 'blog-upload1')

    


]