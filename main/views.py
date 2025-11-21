from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def user_login(request):
    """Login page view"""
    if request.user.is_authenticated:
        return redirect('main:home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', 'main:home')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'main/login.html')


def user_logout(request):
    """Logout view - handles both manual logout and beacon logout on tab close"""
    logout(request)
    
    # If it's a beacon request (from tab close), just return success
    if request.META.get('HTTP_SEC_FETCH_DEST') == 'empty' or request.method == 'POST':
        from django.http import HttpResponse
        return HttpResponse(status=204)  # No content response
    
    # For manual logout (clicking the button), redirect to login
    return redirect('main:login')


@login_required
def home(request):
    """Home page view"""
    return render(request, 'main/home.html')


@login_required
def projects(request):
    """Projects page view"""
    return render(request, 'main/projects.html')


@login_required
def analytics_dashboard(request):
    """Analytics Dashboard view"""
    return render(request, 'main/analytics_dashboard.html')


@login_required
def rso_document_checker(request):
    """RSO Document Checker view"""
    return render(request, 'main/rso_document_checker.html')

