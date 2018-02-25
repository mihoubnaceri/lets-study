from django.urls import path

from . import views
app_name = "courses"
urlpatterns = [
    path("<palier_slug>/",views.palier,name="palier_detail"),
    path("<palier_slug>/<module_slug>/",views.module,name="module_detail"),
    path("<palier_slug>/<module_slug>/courses/",views.course,name="course_detail"),
    path("<palier_slug>/<module_slug>/<course_slug>/",views.tutorials,name="tutos_list"),
    path("<palier_slug>/<module_slug>/<course_slug>/<tutorial_slug>/",views.lesson,name="tutos_detail"),
    path("<palier_slug>/404/",views.four,name="404"),
    #path("<palier_slug>/<module_slug>/<course_slug>/<tutorial_slug>",views.tutorial_detail,name="tutorials"),
]
