from django import forms


class FeedbackForms(forms.Form):
    name = forms.CharField()
    feedback = forms.CharField(widget=forms.Textarea())
