from django.shortcuts import render,get_object_or_404,redirect
from .models import Palier,Module,Course,Tutorial
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from accounts.models import StudentProfile
from django.views.generic import RedirectView



# Create your views here.
def palier(request,palier_slug):

    palier = get_object_or_404(Palier,palier_slug=palier_slug)
    paliers = Palier.objects.all()

    return render(request,"courses/palier_detail.html",{"palier":palier,"paliers":paliers})
def module(request,palier_slug,module_slug):
    module = get_object_or_404(Module,module_slug=module_slug)
    palier =  get_object_or_404(Palier,palier_slug=palier_slug)
    return render(request,"courses/module_detail.html",{"module":module,"palier":palier})
def course(request,palier_slug,module_slug):
    cours = get_object_or_404(Module,module_slug=module_slug)
    paliers = Palier.objects.all()
    #print(user.user.bio)
    #user.save()
    #user.save()
    palier = get_object_or_404(Palier,palier_slug=palier_slug)
    courses = Course.objects.filter(module=cours)
    c1 = courses.filter(trimestre="t1")
    c2 = courses.filter(trimestre="t2")
    c3 = courses.filter(trimestre="t3")
    context = {
        "paliers":paliers,
        "palier":palier,
        "cours":cours,
        "c1":c1,
        "c2":c2,
        "c3":c3,
    }
    return render(request,"courses/course_detail.html",context)

def tutorials(request,palier_slug,module_slug,course_slug):
    tutorials = get_object_or_404(Course,course_slug=course_slug) # course object example equations
    module = get_object_or_404(Module,module_slug=module_slug) # what module
    palier = get_object_or_404(Palier,palier_slug=palier_slug) #what bac is it or what year is it
    paliers = Palier.objects.all() # list of all classes this is mostly for the navigation
    tutos = Tutorial.objects.filter(course = tutorials) # get all the tutorials that correspons to cours

    #issue = get_object_or_404(Tutorial,tutorial_slug=tutos.tutorial_slug)


    if len(tutos) >0:
        first_item = tutos[0]
    else:
        return redirect("courses:module_detail",palier_slug=palier.palier_slug,module_slug=module.module_slug)
    quizzes = []
    videos = []
    counter=0
    counter_video=0
    for tuto in tutos:
        if tuto.quiz:
            quizzes.append(tuto)
            counter+=1
        else:
            videos.append(tuto)
            counter_video+=1

    # prev_course = tutos.filter("order__lte=tutos.order").order_by("-order",)[0:1]
    # next_course = tutos.filter("order__gte=tutos.order").order_by("order",)[0:1]
    #print(prev_course.title)
    context = {
        #"quizzes":quizzes,
        #"correct":correct,
        "first_item":first_item,
        "paliers":paliers,
        "counter_video":counter_video,
        "counter":counter,
        #"lessons":lessons,
        "tutorials":tutorials,
        "module":module,
        "palier":palier,
        "tutos":tutos,
        "quizzes":quizzes,
        "videos":videos,
    }
    return render(request,"courses/tutorial_list.html",context)
def lesson(request,palier_slug,module_slug,course_slug,tutorial_slug):
    module = get_object_or_404(Module,module_slug=module_slug)
    palier = get_object_or_404(Palier,palier_slug=palier_slug)
    course =get_object_or_404(Course,course_slug=course_slug)
    lesson= get_object_or_404(Tutorial,tutorial_slug=tutorial_slug)
    lesson_next = Tutorial.objects.filter(course=course,order__gt=lesson.order).order_by("order").first()
    lesson_prev = Tutorial.objects.filter(course=course,order__lt=lesson.order).order_by("-order").first()
    course_next = Course.objects.filter(module=module,order__gt=course.order).order_by("order").first()
    #print(course_next.title)

    lessons = Tutorial.objects.filter(course=course)

    paliers = Palier.objects.all()
    quiz_questions = []
    counter=0
    questions=None
    if lesson.quiz:
        questions = lesson.quiz.related_question.all()
        for question in questions:
            counter +=1
            quiz_questions.append(question)

    paginator=Paginator(quiz_questions, 1)
    page = request.GET.get('question')
    paginate_quiz = paginator.get_page(page)
    context = {
        "course_next":course_next,
        "lesson_next":lesson_next,
        "lesson_prev":lesson_prev,
        "counter":counter,
        "quiz_questions":quiz_questions,
        "questions":questions,
        "paginate_quiz":paginate_quiz,
        "lessons":lessons,
        "course":course,
        "paliers":paliers,
        "lesson":lesson,
        #"tutorials":tutorials,
        "module":module,
        "palier":palier,
        #"tutos":tutos,
    }
    return render(request,"courses/tutorial_detail.html",context)

def four(request):
    return render(request,"courses/404.html",{})
