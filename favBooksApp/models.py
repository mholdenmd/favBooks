from django.db import models
from django.db.models.deletion import CASCADE

import re

class UsersMan(models.Manager):
    def i_am_the_validator(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        emlTaken = Users.objects.filter(email = postData['eml'])
        print(postData)
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['fname']) < 2:
            errors["FirstnameRequired"] = "First name must be aleast 2 characters long"
        if len(postData['lname']) < 2:
            errors["LastnameRequired"] = "Last name should be at least 3 characters long"
        if len(postData['eml']) == 0:
            errors["descriptionRequired"] = "Please add an email address"
        elif not EMAIL_REGEX.match(postData['eml']):    # test whether a field matches the pattern            
            errors['eml'] = "Invalid email address!"
        elif len(emlTaken)>0:
            errors['emlTaken'] = "This email is taken, Try again!"

        
        if len(postData['PW']) < 8:
            errors["PWRequired"] = "Password should be at least 8 characters long"
        return errors

    def loginVal(self, postData):    
        errors = {}
        emailMatch = Users.objects.filter(email = postData['eml'])
        if len(emailMatch) == 0:
            errors['emailNotfound'] = "This email address is not found"

        

        elif emailMatch[0].password != postData ['PW']:
            errors['PWwrong'] = "incorrect password"
        return errors

    def bookVal(self, postData):
        errors = {}
        if len(postData['tt']) < 5:
            errors["TitleRequired"] = "Title of book must be aleast 5 characters long"
        return errors



# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UsersMan()

    def __str__(self):
        return f"(added by: {self.first_name} {self.last_name})"


class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    uploaded_by = models.ForeignKey(Users, related_name="books_uploaded", on_delete = models.CASCADE)
    wholiked = models.ManyToManyField(Users, related_name="liked_book")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    


    def __str__(self):
        return f"<Book object: {self.title} ({self.id})>"







