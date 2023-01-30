from django.db import models

# Create your models here.

class Member(models.Model):
    f_name = models.CharField(max_length=120, default="")
    l_name = models.CharField(max_length=120, default="")
    username = models.CharField(max_length=120, default="")
    email = models.EmailField(max_length=122, default="")
    phone_no = models.CharField(max_length=20,default="")
    password = models.CharField(max_length=90)

    def __str__(self):
        return self.username

class Post(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=500, default="")
    post_desc = models.CharField(max_length=500, default="")
    post_date = models.DateField()
    image = models.ImageField(upload_to="media", default="")

    def __str__(self):
        return self.post_title


