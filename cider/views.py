from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from .models import *
from django.template import loader, RequestContext
from django.template.defaulttags import csrf_token
from django.views.decorators.csrf import csrf_exempt

def index(request):
    latest_question_list = Question.objects.order_by('id')
    template = loader.get_template('cider/index.html')
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
    })
    return HttpResponse(template.render(context))

def detail(request, question_id):
    q =  Question.objects.get(pk=question_id)
    dic = {
        'question_id' : question_id,
        'question_text' : q.question_text, 
        'timestamp' : q.timestamp
    }
    return JsonResponse( dic )


def asker(request, question_id):
    user_id = str(int(Question.objects.get(pk = question_id).user_id))
    dic = { 'User' : user_id }
    return JsonResponse( dic )

def answers(request, question_id):
    answer = list(Question.objects.get(pk = question_id).getAnswers())
    dic = {}
    for x, ans in enumerate(answer):
        dic[x]= {
            'answer_id' : ans.id,
            'question_id' : ans.question_id,
            'answer_text' : ans.answer_text,
            'up_votes' : ans.up_votes,
            'down_votes' : ans.down_votes
        }
    return JsonResponse( dic )
    
def user(request, question_id):
    usr = User.objects.get(pk = question_id)
    dic = {
        'user_id' : usr.id,
        'name' : usr.name,
        'email': usr.email,
        'phone_number' : usr.phone_number
    }
    return JsonResponse( dic  )

def accepted(request, question_id):
    cutoff = 5
    answer = list(Question.objects.get(pk = question_id).getAnswers())
    accepted = [x for x in answer if x.accepted(cutoff)]
    dic = {}
    for x, ans in enumerate(accepted):
        dic[x]= {
            'answer_id' : ans.id,
            'question_id' : ans.question_id,
            'answer_text' : ans.answer_text,
            'up_votes' : ans.up_votes,
            'down_votes' : ans.down_votes
        }
    return JsonResponse( dic )

def allaccepted(request):
    cutoff = 5
    answer = list(Answer.objects.all())
    accepted = [x for x in answer if x.accepted(cutoff)]
    dic = {}
    for x, ans in enumerate(accepted):
        dic[x]= {
            'answer_id' : ans.id,
            'question_id' : ans.question_id,
            'answer_text' : ans.answer_text,
            'up_votes' : ans.up_votes,
            'down_votes' : ans.down_votes
        }
    return JsonResponse( dic )

def question(request):
    questions = list(Question.objects.all().order_by('id'))
    dic = {}
    for q in questions:
        dic[q.id] = {
            'user_id' : q.user_id,
            'question_text' : q.question_text,
            'timestamp' : q.timestamp
        }
    return JsonResponse( dic )

def users(request):
    users = list(User.objects.all().order_by('id'))
    dic = {}
    for u in users:
        dic[u.id] = {
            'name' : u.name,
            'email' : u.email,
            'phone_number' : u.phone_number
            }
    return JsonResponse( dic ) 

def answer(request):
    answers = list(Answer.objects.all().order_by('id'))
    dic = {}
    for a in answers:
        dic[a.id] = {
            'question_id' : a.question_id,
            'answer_text' : a.answer_text,
            'up_votes' : a.up_votes,
            'down_votes' : a.down_votes
            }
    return JsonResponse( dic ) 

def answerind(request, answer_id): 
    a = Answer.objects.get(pk = answer_id)
    dic ={
    'question_id' : a.question_id,
    'answer_text' : a.answer_text,
    'up_votes' : a.up_votes,
    'down_votes' : a.down_votes
    }
    return JsonResponse( dic )

def answerup(response, answer_id):
    try:
        a = Answer.objects.get(pk = answer_id)
        a.upVote()
        a.save()
        worked = True
    except:
        worked = False
    dic = {'Sucessful': worked}
    return JsonResponse( dic ) 

def answerdown(response, answer_id):
    try:
        a = Answer.objects.get(pk = answer_id)
        a.downVote()
        a.save()
        worked = True
    except:
        worked = False
    dic = {'Sucessful': worked}
    return JsonResponse( dic ) 

def userqs(response, user_id):
    questions = list(Question.objects.filter(user_id=user_id))
    dic = {}
    for x,q in enumerate(questions):
        dic[x] = {
            'question_id' : q.id,
            'user_id' : q.user_id,
            'question_text' : q.question_text,
            'timestamp' : q.timestamp
        }
    return JsonResponse( dic )

@csrf_exempt
def newQuestion(request): 
    if request.method == 'POST':
        try:
            q = Question(
                user_id = request.POST.get('user_id'),
                question_text = request.POST.get('question_text')
            )
            q.save()
            dic = { 'Sucessful' : True }
        except:
            dic = { 'Sucessful' : False  }
        return JsonResponse( dic )
    else:
        return JsonResponse( {'POST': False} )

@csrf_exempt
def newAnswer(request): 
    if request.method == 'POST':
        try:
            a = Answer(
                question_id = request.POST.get('question_id'),
                answer_text = request.POST.get('answer_text'),
                up_votes = request.POST.get('up_votes', 0), 
                down_votes = request.POST.get('down_votes', 0)
            )
            a.save()
            dic = { 'Sucessful' : True }
        except:
            dic = { 'Sucessful' : False  }
        return JsonResponse( dic )
    else:
        return JsonResponse( {'POST': False} )

@csrf_exempt
def newUser(request): 
    if request.method == 'POST':
        try:
            u = User(
                name = request.POST.get('name'),
                phone_number = request.POST.get('phone_number'),
                email = request.POST.get('email')
            )
            u.save()
            dic = { 'Sucessful' : True }
        except:
            dic = { 'Sucessful' : False  }
        return JsonResponse( dic )
    else:
        return JsonResponse( {'POST': False} )
