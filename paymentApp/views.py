import random
import string
from datetime import datetime
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from paymentApp.models import TransactionHistory


def get_random_alphanumeric_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits)
                          for i in range(length)))
    return result_str


def try_or(fn, default, *args, **kwargs):
    """
    Usage: try_or(lambda: request_user.email, None, *args, **kwargs)
    """
    try:
        return fn(*args, **kwargs)
    except Exception:
        return default


class TransactionViewSet(viewsets.ViewSet):
    """
    (POST) Api for Payment Gateway
    """
    permission_classes = (AllowAny, )

    def create(self, request, pk=None):
        response = dict()
        validate_data = validate(self.request.data)
        if validate_data['status']:
            response = {
                "amount": self.request.data['amount'],
                "currency": try_or(lambda: self.request.data['amount'], 'USD'),
                "type": try_or(lambda: self.request.data['amount'], 'creditcard'),
                "card": {
                    "number": self.request.data['amount']
                },
                "status": "success",
                "authorization_code": get_random_alphanumeric_string(12).capitalize(),
                "time": str(datetime.today())
            }
            TransactionHistory.objects.create(history_details=response)
        else:
            response = {
                "amount": self.request.data['amount'],
                "currency": try_or(lambda: self.request.data['amount'], 'USD'),
                "type": try_or(lambda: self.request.data['amount'], 'creditcard'),
                "card": {
                    "number": self.request.data['amount']
                },
                "status": "error",
                "error": str(validate_data['error']) + 'was not present in the response',
                "authorization_code": get_random_alphanumeric_string(12).capitalize(),
                "time": str(datetime.today())
            }
            TransactionHistory.objects.create(history_details=response)
        return Response(response)


def validate(data):
    context = {'status': False}
    try:
        card = data['card']
        if data['amount'] and card and card['number'] \
                and card['expirationMonth'] \
        and card['expirationYear'] and card['cvv']:
            context = {'status': True}
    except Exception as e:
        context.update({'error': e})
    return context


class AllTransaction(viewsets.ViewSet):
    """
    (GET) Api for all transactions.
    """
    permission_classes = (AllowAny, )

    def list(self, request):
        response = TransactionHistory.objects.all().values_list('id', 'history_details')
        return Response(response)
