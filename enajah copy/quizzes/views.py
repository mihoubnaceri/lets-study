from django.shortcuts import render,get_object_or_404
from .models import Quiz
from courses.models import Palier,Module,Course,Tutorial
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def quiz_list(request):
    quizzes = Quiz.objects.all()



    paliers = Palier.objects.all()
    context = {
        #"lesson":lesson,
        #"course":course,
        #"lessons":lessons,
        #"module":module,
        #"palier":palier,
        "paliers":paliers,
        "quizzes":quizzes
    }
    return render(request,"quizzes/quiz_list.html",context)
def quiz_detail(request,quiz_slug):
    quiz = get_object_or_404(Quiz,quiz_slug=quiz_slug)
    questions = quiz.related_question.all()
    quiz_score = quiz.score
    length = len(questions)
    paginator=Paginator(questions, 1)
    page = request.GET.get('question')
    paginate_quiz = paginator.get_page(page)
    

    context = {
        "length":length,
        "paginate_quiz":paginate_quiz,
        "questions":questions,
        "quiz":quiz,
    }
    return render(request,"quizzes/quiz_detail.html",context)
