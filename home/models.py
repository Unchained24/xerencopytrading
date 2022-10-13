from unicodedata import name
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
# import uuid


class Blog(models.Model):
    author = models.ForeignKey('auth.User' , null=True, blank=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField('Tag', blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    text = RichTextField(null=True, blank=True)
    featured_image = models.ImageField(null=True , blank=True, default="assets/img/uploads/default.png")
    created_date = models.DateTimeField(default=timezone.now)
    # id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    def __str__ (self):
        return self.title


    # class Meta:
    #     ordering = ['created']


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    # id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Trader(models.Model):
    tradername = models.CharField(max_length=200)
    profile_pic =  models.ImageField( null=True , blank=True, default="assets/img/default.jpg")
    cover_photo =  models.ImageField(null=True , blank=True, default="assets/img/default.png")
    followers = models.IntegerField(default=0, null=True, blank=True)
    uppercent = models.IntegerField(default=0, null=True, blank=True)
    profit = models.DecimalField( max_digits=19, decimal_places=1,default=0.0, null=True, blank=True)

    roi= models.IntegerField(default=0, null=True, blank=True)
    roiprofit = models.DecimalField( max_digits=19, decimal_places=1,default=0.0, null=True, blank=True)

    profit_graph = models.ImageField(null=True , blank=True, default="assets/img/default.jpg")
    
    drawdown = models.IntegerField(default=0, null=True, blank=True)
    drawdown_percent = models.DecimalField( max_digits=19, decimal_places=1,default=0.0, null=True, blank=True)
    aum = models.DecimalField( max_digits=19, decimal_places=1,default=0.0, null=True, blank=True, )
    aum_percent = models.DecimalField( max_digits=19, decimal_places=1,default=0.0, null=True, blank=True)

    def __str__ (self):
        return self.tradername
