from django.db import models

class Customer(models.Model):
    c_id = models.AutoField(primary_key=True)
    v_id=models.IntegerField()
    c_name=models.CharField(max_length=40)
    c_mobile=models.TextField()
    c_address=models.TextField()

class Daily_Records(models.Model):
    m_id=models.IntegerField(primary_key=True)
    c_id=models.ForeignKey('Customer',on_delete=models.CASCADE)
    date=models.DateTimeField()

class Vehicle(models.Model):
    v_id=models.ForeignKey('Customer',on_delete=models.CASCADE,)
    reg_no=models.CharField(max_length=20)
    a_cost=models.IntegerField()
    chassis_no=models.CharField(max_length=30)
    engine_no=models.CharField(max_length=30)  
    registered_address=models.TextField()
    insurance=models.CharField(max_length=40)
    insurance_date=models.DateTimeField()







