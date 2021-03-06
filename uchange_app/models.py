from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __unicode__(self):
        return self.name

class Person(models.Model):
    student_id = models.CharField(max_length=10)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    item_now = models.ForeignKey(Item,related_name='item_now')
    item_original = models.ForeignKey(Item,related_name='item_original')
    def __unicode__(self):
        return self.student_id

class Deal(models.Model):
    item = models.ForeignKey(Item)
    p1 = models.ForeignKey(Person,related_name='p1')
    p2 = models.ForeignKey(Person,related_name='p2')
    deal_time = models.DateTimeField('time of the deal')
    def __unicode__(self):
        return self.item.name+' ('+self.p1.student_id+' -> '+self.p2.student_id+')'

class Request(models.Model):
    person = models.ForeignKey(Person)
    item = models.ForeignKey(Item)
    def __unicode__(self):
        return self.person.student_id+' -> '+self.item.name

class Comment(models.Model):
    person = models.ForeignKey(Person)
    item = models.ForeignKey(Item)
    content = models.TextField()
    comment_time = models.DateTimeField('time of the comment')
    def __unicode__(self):
        return self.person.student_id+'->'+self.item.name

class Control(models.Model):
    result_switch = models.CharField(max_length=10)
    def __unicode__(self):
        return 'result_switch'