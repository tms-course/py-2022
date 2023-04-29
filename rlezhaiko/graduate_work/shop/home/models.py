from django.db import models
from django.contrib.auth.models import User


class CustomerReview(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_review = models.TextField(blank=False)
    admin_answer = models.TextField(blank=True)
    creation_date = models.DateField(auto_now_add=True)


    def __str__(self) -> str:
        return self.customer_review
    

    def have_admin_answer(self):  
        print(len(self.admin_answer))
        print(type(self.admin_answer))      
        return len(self.admin_answer)