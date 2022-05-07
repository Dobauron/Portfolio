from django.db import models


# Create your models here.


class Question(models.Model):
    title = models.CharField(max_length=250)
    question = models.CharField(max_length=500)

    def __str__(self):
        return self.question


class Answer(models.Model):
    answer = models.ForeignKey(Question,
                               on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now=True)


