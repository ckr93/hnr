from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, render_to_response
from django.db.models import Q
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponseNotFound,HttpResponseServerError

def index(request):

    return render(request, 'application/index.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                c = {}
                return render(request, 'application/logged.html', c)
            else:
                return render(request, 'application/index.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'application/index.html', {'error_message': 'Invalid login'})
    return render(request, 'application/index.html')

def home(request):
    return render(request, 'application/homepage.html')

def search(request):
    return render(request, 'application/search.html')

def last_search(request):
    return render(request, 'application/last_search.html')

def manage_recruitments(request):
    return render(request, 'application/manage_recruitments.html')


@ensure_csrf_cookie
def search_result(request):
    return render(request, 'application/search_result.html')

def custom_404(request, ):
    return render(request, 'application/404.html')

def custom_500(request, ):
    return render(request, 'application/500.html')