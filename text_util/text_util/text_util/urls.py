from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', views.index, name='index'),
   path('analyze', views.analyze, name='analyze'),
   path('fullcaps', views.analyze, name='fullcaps'),
   path('newLineRemover', views.analyze, name='newLineRemover'),
   path('extraspaceremover', views.analyze, name='extraspaceremover'),
   path('charctercount', views.analyze, name='charctercount'),





]