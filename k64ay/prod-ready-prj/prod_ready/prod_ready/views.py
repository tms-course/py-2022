from django.shortcuts import render

def page_not_found(request, exception):
    print('hello')
    return render(request, '404.html', {'name': 'Hello world'})

def home(request):
    raise Exception('oops')
    return render(request, 'home.html', {})