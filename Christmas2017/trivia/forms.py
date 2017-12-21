from django import forms

class CreateTriviaForm(forms.Form):
    question_number = forms.IntegerField
    question_text = forms.TextInput()
