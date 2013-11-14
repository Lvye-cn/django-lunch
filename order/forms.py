
from django.forms import ModelForm
from models import Order, Fee


class OrderForm(ModelForm):

    class Meta:
        model = Order
        exclude = ['creator']

class FeeForm(ModelForm):

    class Meta:
        model = Fee
        exclude = ['creator']
