from django import forms
from .models import Feedback


# class FeedbackForm(forms.Form):
#     name = forms.CharField()
#     feedback = forms.CharField(widget=forms.Textarea())

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
        labels = {
            'name': 'Имя пользователя',
            'feedback': 'Отзыв',
            'rating': 'Оценка'
        }

