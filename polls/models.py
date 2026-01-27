import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin   

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    # def was_published_recently(self):
    #     from django.utils import timezone
    #     import datetime
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1) # 현재시간 - 1   

    @admin.display(
        boolean=True,
        ordering="pub_date", 
        description="Published recently?",
    )    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now 
    
    def __str__(self):
        return self.question_text


class Choice(models.Model): # 데이터를 호출할때 역참조를 해야한다. choice_set
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text