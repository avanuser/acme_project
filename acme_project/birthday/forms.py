"""Class for web form."""

from django import forms
from .models import Birthday

"""class BirthdayForm(forms.Form):

    first_name = forms.CharField(label='Имя', max_length=20)
    last_name = forms.CharField(
        label='Фамилия', required=False, help_text='Необязательное поле'
    )
    birthday = forms.DateField(
        label='Дата рождения',
        widget=forms.DateInput(attrs={'type': 'date'})
    )"""

class BirthdayForm(forms.ModelForm):

    class Meta:
        model = Birthday     # модель, на основе которой должна строиться форма
        fields = '__all__'   # Указываем, что надо отобразить все поля.
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})    # добавляем виджет для поля, в котором будет вводиться дата
        }
