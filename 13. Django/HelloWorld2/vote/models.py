from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.TextField(max_length=200)
    create_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.question
    

class Choice(models.Model):
    question = models.ForeignKey(
        'Question',
        on_delete=models.CASCADE
    )
    choice_text = models.CharField(max_length=200)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text