from django import forms
from noticeBoard.models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question #사용할 모델
        fields = ['subject', 'content'] #questionform에서 사용할 question 모델의 속성
        labels = {
            'subject' : '제목',
            'content' : '내용',
        }
