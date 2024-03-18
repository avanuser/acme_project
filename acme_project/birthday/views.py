"""View-function for birthday calculation."""

from django.shortcuts import render
from .forms import BirthdayForm
from .models import Birthday


def birthday(request):
    """View-function for birthday calculation."""

    form = BirthdayForm(request.POST or None)
    # Добавляем его в словарь контекста под ключом form:
    context = {'form': form}
    if form.is_valid():
        form.save()          # save to DB
    return render(request, 'birthday/birthday.html', context=context)


def birthday_list(request):
    # Получаем все объекты модели Birthday из БД.
    birthdays = Birthday.objects.all()
    # Передаём их в контекст шаблона.
    context = {'birthdays': birthdays}
    return render(request, 'birthday/birthday_list.html', context)
