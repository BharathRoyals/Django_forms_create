from django.db import models

# Create your models here.
class Topic(models.Model):
    tname=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.tname

class Webpages(models.Model):
    tname=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,unique=True)
    Email=models.EmailField(default='sbharath143@gmail.com')
    url=models.URLField()
    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name=models.ForeignKey(Webpages,on_delete=models.CASCADE)
    author=models.CharField(max_length=100)
    date=models.DateField()

    def __str__(self):
        return self.author
