from order.models import Order
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

def index(request):
    import datetime
    from django.db.models import Sum
    today = datetime.datetime.today()
    orders = Order.objects\
                 .filter(create_at__gt=datetime.datetime(today.year, today.month, today.day))\
                 .annotate(total_price=Sum('fee__price'))
    return render(request, 'index.html', locals())
def register_user(request):

    from django.contrib.auth.models import User
    User.objects.create_user(username=request.POST.get('username'),
                                email=request.POST.get('email'),
                                password=request.POST.get('password')
            )
    return HttpResponse(0)

def logout_user(request):

    logout(request)
    return HttpResponse('0', status=200)

def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponse('0') 
    return HttpResponse('1')
