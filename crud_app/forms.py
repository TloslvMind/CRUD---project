from django import forms


class UserForm(forms.Form):
    name = forms.CharField(max_length=100, label='Ваше имя',
                           widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    age = forms.IntegerField(label='Ваш возраст?', initial=18, help_text='Введите свой возраст')