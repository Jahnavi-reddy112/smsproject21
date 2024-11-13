from django.urls import path, include
from . import views
app_name= 'studentapp'
urlpatterns = [
    path('NameDisplay',views.NameDisplay, name='NameDisplay'),
    path('StudentHomePage/', views.StudentHomePage, name='StudentHomePage'),
    path('view_marks/', views.view_marks, name='view_marks'),

]