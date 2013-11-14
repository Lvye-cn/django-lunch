import datetime

from django.shortcuts import render

from models import Order, Fee
# Create your views here.

def index(request):

   today = datetime.datetime.today()

   orders = Order.objects.filter(expirate_at__gt=today)

   return render(request, 'index.html', locals())


def create_order(request):

    if request.method == "POST":
        from forms import OrderForm
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.creator = request.user
            order.save()

def view_order(request, oid):

    order = Order.objects.get_or_404(pk=oid)

    if request.method == "GET":

        return render(request, 'view_order.html', locals())

def fee(request):

    from forms import FeeForm
    if request.method == "GET":
        order = request.GET.get('order')
        form = FeeForm({'order': Order.objects.get(pk=order)})
        return render(request, 'fee_form.html', locals())

    if request.method == "POST":
        form = FeeForm(request.POST)
        if form.is_valid():
            fee = form.save(commit=False)

            fee.creator = request.user
            fee.save()
