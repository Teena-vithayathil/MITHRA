from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=100, default='False')
    name = models.CharField(max_length=100, default='False')
    password = models.CharField(max_length=100, default='False')  # Consider using Django's built-in user model or at least its password management
    age = models.IntegerField(default=0)  # No 'max_length' for IntegerField
    city = models.CharField(max_length=100, default='False')
    phno = models.CharField(max_length=10,default='False')  # Should be CharField to accommodate leading zeroes and international formats
    occupation = models.CharField(max_length=100, default='False')
    id_proof = models.FileField(upload_to='./frontend/images/idproofs/',null=True)  # Defines the directory within MEDIA_ROOT to store these files
    driving_license = models.FileField(upload_to='./frontend/images/drivinglicenses/',null=True)
    profile_pic = models.FileField(upload_to='./frontend/images/propics/',null=True)
    verified = models.CharField(max_length=10,default=False)
    rating = models.IntegerField(default=0)
    review = models.CharField(max_length=300,default=False)
    r1 = models.IntegerField(default=0)
    r2 = models.IntegerField(default=0)
    r3 = models.IntegerField(default=0)
    r4 = models.IntegerField(default=0)
    r5 = models.IntegerField(default=0)
    driving_verified = models.CharField(max_length=10,default=False)
    def __str__(self):
        return self.name

class CreateCarpool(models.Model):
    id = models.AutoField(primary_key=True)
    userid = models.IntegerField(default=0)
    start = models.CharField(max_length=100, default='False')
    end = models.CharField(max_length=100, default='False')
    time = models.CharField(max_length=20,null=True)
    via = models.CharField(max_length=100, blank=True, null=True)  # Optional field
    date = models.CharField(max_length=20,null=True)
    TYPE_OF_VEHICLE_CHOICES = [
        ('car', 'Car'),
        ('scooter', 'Scooter'),
        ('bike', 'Bike'),
    ]
    vehicle_type = models.CharField(max_length=100, choices=TYPE_OF_VEHICLE_CHOICES, default='car')
    max_seats = models.IntegerField(default=0)
    no_of_seats = models.IntegerField(default=0)
    vehicle_model = models.CharField(max_length=100)
    vehicle_no = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    YES_NO_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    product_delivery = models.CharField(max_length=100, choices=YES_NO_CHOICES, default='no')
    delivery_price = models.IntegerField(null=True, blank=True, default='False')  # Optional, assuming it's only needed if prodelivery is 'yes'
    music = models.CharField(max_length=100, choices=YES_NO_CHOICES, default='no')
    ac = models.CharField(max_length=100, choices=YES_NO_CHOICES, default='no')
    chitchat = models.CharField(max_length=100, choices=YES_NO_CHOICES, default='no')
    pet = models.CharField(max_length=100, choices=YES_NO_CHOICES, default='no')
    smoking = models.CharField(max_length=100, choices=YES_NO_CHOICES, default='no')
    eatdrink = models.CharField(max_length=100, choices=YES_NO_CHOICES, default='no')
    search_route=models.CharField(max_length=200, choices=YES_NO_CHOICES, default='no')
    paymentpic = models.FileField(upload_to='./frontend/images/paymentpics/')

    def __str__(self):
        return f"Carpool from {self.start} to {self.end} on {self.date}"
    
class JoinCarpool(models.Model):
    id = models.AutoField(primary_key=True)
    passengerid = models.IntegerField(default=0)
    carpool_id = models.IntegerField(default=0)
    driverid = models.IntegerField(default=0)
    start = models.CharField(max_length=100, default='False')
    end = models.CharField(max_length=100, default='False')
    price = models.IntegerField(default=0)
    REQUEST_STATUS_CHOICES = [
        ('accept', 'Accept'),
        ('reject', 'Reject'),
        ('pending', 'Pending'),
    ]
    request = models.CharField(max_length=100, choices=REQUEST_STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.userid}'s request to {self.carpool_id}: {self.request}"
    
class Delivery(models.Model): #no delivery size given
    id = models.AutoField(primary_key=True)
    passengerid = models.IntegerField(default=0)
    driverid = models.IntegerField(default=0)
    carpool_id = models.IntegerField(default=0)
    start = models.CharField(max_length=100,default='False')
    end = models.CharField(max_length=100,default='False')
    price = models.IntegerField(default=0)
    pro_size = models.IntegerField(default=0)
    pro_wgt = models.IntegerField(default=0)
    pro_type = models.CharField(max_length=100,default=0)
    pro_anyother = models.CharField(max_length=100, default='False')


    REQUEST_CHOICES = [
        ('accept', 'Accept'),
        ('reject', 'Reject'),
        ('pending', 'Pending'),
    ]
    request = models.CharField(max_length=100, choices=REQUEST_CHOICES, default='pending')

    def __str__(self):
        return f"Delivery from {self.start} to {self.end} - {self.request}"