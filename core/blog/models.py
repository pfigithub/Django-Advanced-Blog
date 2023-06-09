from django.db import models

# from accounts.models import User, Profile


# Create your models here.
class Post(models.Model):
    """this is a class to define posts for blog app"""

    author = models.ForeignKey("accounts.Profile", on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=250)
    content = models.TextField()
    status = models.BooleanField()
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
    created_date = models.TimeField(auto_now_add=True)
    updated_date = models.TimeField(auto_now=True)
    published_date = models.TimeField()

    def __str__(self):
        return self.title


class Category(models.Model):
    """class for category"""

    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
