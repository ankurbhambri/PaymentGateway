from django.db import models

class TimeStampedModel(models.Model):

    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields.
    """
    created_at = models.DateTimeField(
        verbose_name='Created', auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(verbose_name='modified', auto_now=True)

    class Meta:
        abstract = True


# class Transaction(TimeStampedModel):

#     CARD_CHOICES = [
#         ('CREDITCARD', 'creditcard'),
#         ('DEBITCARD', 'debitcard'),
#     ]

#     CURRENCY_CHOICES = [
#         (1, 'USD'),
#         (2, 'INR'),
#         (3, 'CAD'),
#     ]

#     amount = models.FloatField()
#     currency = models.CharField(
#         max_length=10,
#         choices=CARD_CHOICES,
#         default='CREDITCARD',
#     )
#     card_type = models.CharField(
#         max_length=10,
#         choices=CURRENCY_CHOICES,
#         default=1,
#     )
#     card_number = models.CharField(max_length=20)
#     expirationMonth = models.IntegerField()
#     cvv = models.IntegerField()


class TransactionHistory(TimeStampedModel):
    history_details = models.JSONField()
