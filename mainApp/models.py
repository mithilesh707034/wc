from django.db import models


class Website_Category(models.Model):
    id=models.AutoField(primary_key=True)
    category=models.CharField(max_length=200)
    def __str__(self):
        return self.category
    

class Website_Technology(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    def __str__(self):
        return str(self.name)


class Product(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_category=models.ForeignKey(Website_Category,on_delete=models.CASCADE)
    product_technology=models.ForeignKey(Website_Technology,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=100)
    product_image=models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    product_price=models.IntegerField()
    product_web_link=models.CharField(max_length=150,default='',null=True,blank=True)
   
    def __str__(self):
        return str(self.product_id)+" "+str(self.product_name)+" "+str(self.product_technology)


class Enquiry(models.Model):
    client_id=models.AutoField(primary_key=True)
    client_name=models.CharField(max_length=100)
    client_email=models.CharField(max_length=100)
    client_phone=models.CharField(max_length=100)
    client_subject=models.CharField(max_length=100,default='',null=True,blank=True)
    client_message=models.TextField(default='',null=True,blank=True)

    product_id=models.IntegerField(default=0,null=True,blank=True)
    product_name=models.CharField(max_length=100,default='',null=True,blank=True)
    product_image=models.ImageField(upload_to="uploads",default='',null=True,blank=True)
    product_price=models.IntegerField(default=0,null=True,blank=True)
    product_web_link=models.CharField(max_length=150,default='',null=True,blank=True)
    product_technology=models.CharField(max_length=100,default='',null=True,blank=True)
   
    def __str__(self):
        return str(self.client_id)+" "+self.client_name


