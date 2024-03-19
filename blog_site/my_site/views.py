from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return HttpResponse("надає звичайний текст для користувача, що описує функції сайту django.")

def home(request):
    return render(request, 'index.html')

def article(request, article_id):
    return HttpResponse(f"Представлення деталей однієї статті. URL містить динамічну частину. Вона буде використовуватися для отримання однієї статті з бази даних #{article_id}.")

def article_comment(request, article_id):
    return HttpResponse(f"Це представлення буде використовуватися для додавання коментарів до статті. #{article_id}.")

def create(request):
    return HttpResponse("Форма створення статті.")


def article_update(request, article_id):
    return HttpResponse(f"Представлення для оновлення існуючих даних статті #{article_id}.")

def article_delete(request, article_id):
    return HttpResponse(f"Представлення для підтвердження видалення статті #{article_id}.")

def topics(request):
    return HttpResponse("Перелік доступних тем на сайті.")

def topics_add(request, topic_id):
    return HttpResponse(f"Додати обрану тему до списку обраних тем #{topic_id}.")

def topics_remove(request, topic_id):
    return HttpResponse(f"Видаляє вибрану тему з обраних #{topic_id}.")

def topics_subscribe(request, topic_id):
    return HttpResponse(f"Представлення для підписки на тему #{topic_id}.")

def topics_unsubscribe(request, topic_id):
    return HttpResponse(f"Представлення для відписки від теми #{topic_id}.")

def profile(request, username):
    return HttpResponse(f"Особиста сторінка користувача сайту #{username}.")

def set_password(request):
    return HttpResponse(f"Цей маршрут буде використовуватися для зміни облікових даних користувачів.")

def set_userdata(request):
    return HttpResponse(f"Цей маршрут буде використовуватися для зміни даних користувачів.")

def deactivate(request):
    return HttpResponse(f"Представлення для деактивації облікового запису (видалення).")

def register(request):
    return HttpResponse(f"Сторінка з формою для реєстрації нового користувача.")

def login(request):
    return HttpResponse(f"Сторінка з формою для логіна.")

def logout(request):
    return HttpResponse(f"Логаут. Має перенаправляти користувача назад на домашню сторінку..")





def test(request):
    return render(request, 'test.html')

def contacts(request):
    return render(request, 'contacts.html')
