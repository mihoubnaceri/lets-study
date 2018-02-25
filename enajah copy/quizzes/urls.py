from django.urls import path

from . import views
app_name="quizzes"
urlpatterns=[
    path("",views.quiz_list,name="list_quizzes"),
    path("<quiz_slug>/",views.quiz_detail,name="quiz_detail"),
]
