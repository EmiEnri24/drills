from django.db import models

# Create your models here.

class Expense(models.Model):
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    class Category(models.TextChoices):
        FOOD = 'F', "Food"
        TRANSPORT = 'T',"Transport"
        OTHER = "O", "Other"
    
    category= models.CharField(max_length=1,choices=Category.choices)
    
    spent_on = models.DateField("Date of expense")
    created_at = models.DateTimeField(auto_now_add =True)
    
    #class Meta:
    #    ordering = ["created"]
    
    
    