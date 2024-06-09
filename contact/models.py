from django.db import models


# Newsletter model to store emails of users who subscribe to the newsletter
class Newsletter(models.Model):
    email = models.EmailField(unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


# Contact form model to store the name, email, message and
# date sent of users who contact the website
class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
