from django.urls import path

from . import views

app_name = 'noticeBoard'

urlpatterns = [
    ## 게시글 불러오기
    path('', views.index, name='index'),
    ## 게시글 상세 조회
    path('<int:question_id>/', views.detail, name='detail'),
    ## 게시글 작성
    path('question/create/', views.question_create, name='question_create'),
    ## 게시글 삭제
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
    ## 댓글 작성
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),

]
