from rest_framework import serializers
from paymentApp.models import TransactionHistory
#  PayAmount, Transactions


class AllTransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = TransactionHistory
        fields = ['id', 'history_details']
