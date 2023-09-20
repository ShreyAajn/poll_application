# Create your models here.
import datetime
from typing import Self

from django.db import models
from django.utils import timezone
from django.contrib import admin
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
    
    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
        ) 
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    
class user_info(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    connections = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    profile_languages = models.CharField(max_length=255)
    public_profile_and_url = models.CharField(max_length=255)
    about = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class analytics(models.Model):
    user = models.ForeignKey(user_info, on_delete=models.CASCADE,null=True) 
    type = models.CharField(max_length=255)
    count = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.type

class resources(models.Model):
    user = models.ForeignKey(user_info, on_delete=models.CASCADE,null=True) 
    name = models.CharField(max_length=255)
    action = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class education(models.Model):
    user = models.ForeignKey(user_info, on_delete=models.CASCADE,null=True) 
    university = models.CharField(max_length=255)
    degree_name = models.CharField(max_length=255)
    time_period = models.CharField(max_length=255)

    def __str__(self):
        return self.university  

class experience(models.Model):
    user = models.ForeignKey(user_info, on_delete=models.CASCADE,null=True) 
    role = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    period_of_training = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.role  
    
class licenses_and_certifications(models.Model):
    user = models.ForeignKey(user_info, on_delete=models.CASCADE,null=True) 
    name = models.CharField(max_length=255)
    issuing_organization = models.CharField(max_length=255)
    issuedate = models.CharField(max_length=255)

    def __str__(self):
        return self.name  
    
class skills(models.Model):
    user = models.ForeignKey(user_info, on_delete=models.CASCADE,null=True) 
    skillset = models.CharField(max_length=255)

    def __str__(self):
        return self.skillset  
    
class languages(models.Model):
    user = models.ForeignKey(user_info, on_delete=models.CASCADE,null=True) 
    type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name  
    
class people_also_viewed(models.Model):
    user = models.ForeignKey(user_info, on_delete=models.CASCADE, null=True) 
    name = models.CharField(max_length=255)
    tagline = models.CharField(max_length=255)
    action = models.CharField(max_length=255)

    def __str__(self):
        return self.name  
    
class people_you_may_know(models.Model):
    user = models.ForeignKey(user_info, on_delete=models.CASCADE, null=True) 
    name = models.CharField(max_length=255)
    tagline = models.CharField(max_length=255)
    action = models.CharField(max_length=255)

    def __str__(self):
        return self.name  
    
class you_might_like(models.Model):
    user = models.ForeignKey(user_info, on_delete=models.CASCADE, null=True) 
    name = models.CharField(max_length=255)
    company_type = models.CharField(max_length=255)
    followers_count = models.CharField(max_length=255)
    action = models.CharField(max_length=255)

    def __str__(self):
        return self.name  