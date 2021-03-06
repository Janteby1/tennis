from django.conf.urls import include, url
from django.contrib import admin
from cal import views #gets all our view functions

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^add$', views.AddScore.as_view(), name='add'),
    url(r'^top$', views.ViewTop.as_view(), name='top'),
    url(r'^all$', views.ViewAll.as_view(), name='all'),
    url(r'^edit$', views.EditScore.as_view(), name='edit'),
]