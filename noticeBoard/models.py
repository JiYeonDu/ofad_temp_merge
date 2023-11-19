
# Create your models here.
from django.db import models



"""
 * MODEL No. 1
 * MODEL Name : Question
"""
class Question(models.Model):
    ##author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

"""
 * MODEL No. 2
 * MODEL Name : Answer
"""
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()