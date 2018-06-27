from django.db import models
# from pygments.lexers import get_all_lexers
# from pygments.styles import get_all_styles
# from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class Card(models.Model):
    # TODO : define true type
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    card_types = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    )
    type = models.CharField(
        max_length=2,
        choices=card_types,
        default=FRESHMAN,
    )
    # TODO : Discuss varchar or int
    width = models.CharField(max_length=20)
    height = models.CharField(max_length=20)
    score = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    create_at = models.DateTimeField('date create_at')
    update_at = models.DateTimeField('date update_at')
    enable = models.BooleanField(initial=True)


class Card_Picture(models.Model):
    Card_id = models.ForeignKey(Card, on_delete=models.CASCADE)
    is_main = models.BooleanField(initial=True)
    # TODO : Discuss varchar or text
    path = models.TextField()
    enable = models.BooleanField(initial=True)
    create_at = models.DateTimeField('date create_at')
    # votes = models.IntegerField(default=0)

class Card_Text(models.Model):
    Text = 'TX'
    Poem = 'PO'
    TextPoem = 'TP'
    Custom = 'CU'
    card_types = (
        (Text, 'Text'),
        (Poem, 'Poem'),
        (TextPoem, 'TextPoem'),
        (Custom, 'Custom'),
    )
    type = models.CharField(
        max_length=2,
        choices=card_types,
        default=Text,
    )
    Card_id = models.ForeignKey(Card, on_delete=models.CASCADE)
    is_main = models.BooleanField(initial=True)
    Text = models.TextField(null=True)
    Image_path = models.TextField(null=True)
    enable = models.BooleanField(initial=True)
    create_at = models.DateTimeField('date create_at')

class Order(models.Model):
    Card_id = models.ForeignKey(Card, on_delete=models.CASCADE)
    Text_id = models.ForeignKey(Card_Text, on_delete=models.CASCADE)
    Title = models.TextField()
    Gold = 'GL'
    Simple = 'SP'
    types = (
        (Gold, 'Gold'),
        (Simple, 'Simple'),
    )
    type = models.CharField(
        max_length=2,
        choices=types,
        default=Simple,
    )
    Image_path = models.TextField(null=True) #optional
    PhoneNumber = models.CharField(max_length=20)
    Order_info = models.TextField()
    Order_address = models.TextField()
    deadline = models.DateTimeField('date deadline')
    create_at = models.DateTimeField('date create_at')

class Order(models.Model):
    username = models.CharField(max_length=50)
    fullname = models.CharField(max_length=50)
    PhoneNumber = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    enable = models.BooleanField(initial=True)
    create_at = models.DateTimeField('date create_at')
