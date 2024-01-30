from django import forms
class CreateVotingForm(forms.Form):
    question = forms.CharField(
        label='Вопрос',
        required=True
    )
    answer1 = forms.CharField(
        label='Ответ 1',
        required=True
    )
    answer2 = forms.CharField(
        label='Ответ 2',
        required=True
    )
