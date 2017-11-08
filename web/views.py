from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from web.models import User, Token, Expense, Income
from datetime import datetime


# Create your views here.

@csrf_exempt
def submit_expense(request):
    """user submits an expense"""


    #TODO validate might be fake user might be fake, token might be fake
    this_token = request.POST['token'] if 'token' in request.POST else "1234567"
    this_user = User.objects.filter(token__token = this_token).get()
    this_amount = request.POST['amount'] if 'amount' in request.POST else "0"
    this_text = request.POST['text'] if 'text' in request.POST else ""
    if 'date' not in request.POST:
        date = datetime.now()
    Expense.objects.create(user = this_user, amount=this_amount,
        text = this_text, date=date)



    return JsonResponse({
        'status': 'ok',

    }, encoder=JSONEncoder)
