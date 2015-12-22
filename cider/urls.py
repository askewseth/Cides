from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /cider/question/
    url(r'^question/$', views.question, name='question'),
    # ex: /cider/question/5/
    url(r'^question/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /cider/question/5/asker/
    url(r'^question/(?P<question_id>[0-9]+)/asker/$', views.asker, name='asker'),
    # ex: /cider/question/5/answers/
    url(r'^question/(?P<question_id>[0-9]+)/answers/$', views.answers, name='answers'),
    # ex: /cider/question/5/answers/accepted/
    url(r'^question/(?P<question_id>[0-9]+)/answers/accepted/$', views.accepted, name='accepted'),
    # ex: /cider/question/user/5
    url(r'^question/user/(?P<user_id>[0-9]+)/$', views.userqs, name='userqs'),
    # ex: /cider/user/
    url(r'^user/$', views.users, name='users'),
    # ex: /cider/user/5
    url(r'^user/(?P<question_id>[0-9]+)/$', views.user, name='user'),
    # ex: /cider/answer/
    url(r'^answer/$', views.answer, name='answers'),
    # ex: /cider/answer/accepted/
    url(r'^answer/accepted/$', views.allaccepted, name='allaccepted'),
    # ex: /cider/answer/5
    url(r'^answer/(?P<answer_id>[0-9]+)/$', views.answerind, name='answerind'),
    # ex: /cider/answer/5/up
    url(r'^answer/(?P<answer_id>[0-9]+)/up/$', views.answerup, name='answerup'),
    # ex: /cider/answer/5/down
    url(r'^answer/(?P<answer_id>[0-9]+)/down/$', views.answerdown, name='answerdown'),

    #POST newUser 
    url(r'^user/new/$', views.newUser, name='newUser'),
    #POST newQuestion 
    url(r'^question/new/$', views.newQuestion, name='newQuestion'),
    #POST newAnswer
    url(r'^answer/new/$', views.newAnswer, name='newAnswer')
]
