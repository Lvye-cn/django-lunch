import datetime

from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


from models import Order, Fee

def create_order(request):

    if request.method == "POST":
        from forms import OrderForm
        now = datetime.datetime.now()
        hour, minute = request.POST.get('expirate_at').split(':')
        data = request.POST.copy()
        data.update({'expirate_at':datetime.datetime(now.year, now.month,
                                now.day, int(hour), int(minute))})
        form = OrderForm(data, request.FILES)
        if form.is_valid():
            order = form.save(commit=False)
            order.creator = request.user
            order.save()
            from django.http import HttpResponseRedirect
            return HttpResponseRedirect('/')

def view_order(request, oid):

    order = Order.objects.get_or_404(pk=oid)

    if request.method == "GET":

        return render(request, 'view_order.html', locals())

def create_fee(request):

    if request.method == "POST":
        
        from forms import FeeForm
        data = request.POST.copy()
        form = FeeForm(data)
        if form.is_valid():
            fee = form.save(commit=False)

            fee.creator = request.user
            fee.save()
            return HttpResponse('0')
        return HttpResponse(str(form.errors))

def fee_restful(request,fee_id):

    if request.method == "DELETE":
        fee = Fee.objects.get(pk=fee_id)
        fee.delete()
        return HttpResponse('')
