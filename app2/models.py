from django.db import models

# Create your models here.

class Logins(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=10)
    def __str__(self) -> str:
        return f"{self.username} - {self.password}"


class ContactUs(models.Model):
    c_name = models.CharField(max_length=20)
    # lastname = models.CharField(max_length=20)
    c_email = models.EmailField()
    c_mobile = models.IntegerField()
    c_message = models.CharField(max_length=500)
    def __str__(self):
        return f"{self.c_name}"

class Registration(models.Model):
    username = models.CharField(max_length=20,primary_key=True)
    firstname = models.CharField(max_length=20, )
    lastname = models.CharField(max_length=20)
    email = models.EmailField()
    mobile = models.CharField(max_length=10,null=True,blank=True)
    city = models.CharField(max_length=10)
    country = models.CharField(max_length=10)
    pswrd= models.CharField( max_length=50)
    usertype = models.CharField( max_length=20)
    def __str__(self) -> str:
        return self.firstname + "-" + self.lastname


class ProductCategory(models.Model):
    product_cid = models.IntegerField()
    product_category = models.CharField(max_length=20)
    def __str__(self) -> str:
        return str(self.product_cid) +" "+ str(self.product_category)

class Products(models.Model):
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=20,)
    product_description = models.CharField(max_length=150)
    product_price = models.IntegerField()
    # product_mfg = models.DateField(null=True,blank=True)
    image = models.ImageField(null=True,blank=True)
    # pc_id = (models.ForeignKey("ProductCategory", on_delete=models.CASCADE))
    def __str__(self) -> str:
        return f"{self.product_id} - {self.product_name} - {self.product_price}"

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''

        return url