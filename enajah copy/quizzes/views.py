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
        # lesson= get_object_or_404(Tutorial,tutorial_slug=tutorial_slug)
        # lesson_next = Tutorial.objects.filter(course=course,order__gt=lesson.order).order_by("order").first()
        #
        # lesson_prev = Tutorial.objects.filter(course=course,order__lt=lesson.order).order_by("-order").first()

    quiz = get_object_or_404(Quiz,quiz_slug=quiz_slug)
    questions = quiz.related_question.all()
    # question_next = Quiz.objects.filter(quiz=quiz,order__gt=quiz.order).order_by("order").first()
    # question_prev = Quiz.objects.filter(quiz=quiz,order__lt=quiz.order).order_by("-order").first()
    quiz_score = quiz.score
    question = quiz.related_question.all()
    first_question = question[0]
    print(first_question)
    length = len(questions)
    paginator=Paginator(questions, 1)
    page = request.GET.get('question')
    correct = None
    button = "Check"
    paginate_quiz = paginator.get_page(page)
    if request.method=="POST":
        answer_choice = request.POST.get("choice")
        for question in paginate_quiz:
            answers = question.related_answer.all()
            for answer in answers:
                if answer.correct:
                    if str(answer) == answer_choice:
                        correct  =True
                        button="Next"
                        print("correct")


    context = {

        # "question_next":question_next,
        # "question_prev":question_prev,
        "correct":correct,
        "button":button,
        "length":length,
        "paginate_quiz":paginate_quiz,
        "questions":questions,
        "quiz":quiz,
    }
    return render(request,"quizzes/quiz_detail.html",context)
