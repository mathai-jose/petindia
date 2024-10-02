from datetime import timedelta
from django.db import models
from django.contrib.auth.models import AbstractUser, User

class UserProfile(AbstractUser):
    age = models.PositiveIntegerField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)  # Nullable email field
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Nullable phone number field
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_profiles',  # Custom related name to avoid clashes
        related_query_name='user_profile',
        blank=True,
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_profiles',  # Custom related name to avoid clashes
        related_query_name='user_profile',
        blank=True,
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='productimages/')
    is_active = models.BooleanField(default=True)
    quantity = models.IntegerField(default=0)
    reorderlevel = models.IntegerField(default=0)
    category = models.CharField(max_length=100, default='Uncategorized')
    is_ordered = models.BooleanField(default=False)  # New field to indicate if the product has been ordered
    
    def is_at_reorder_level(self):
        return self.quantity == self.reorderlevel

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Cart for {self.user.username}: {self.product.name}"
    
class Order(models.Model):
    STATUS_CHOICES = [
        ('processing', 'Processing'),
        ('out_for_delivery', 'Out for Delivery'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=False)
    fullname = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='processing')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order for {self.fullname} placed on {self.created_at}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in order {self.order.id}"

class Supplier(models.Model):
    company_name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    address = models.TextField()

    def __str__(self):
        return self.company_name

class PurchaseOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who placed the order
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.name} - Quantity: {self.quantity} - Date: {self.order_date}"

class RestockedProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    restocked_at = models.DateTimeField(auto_now_add=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.product} - Quantity: {self.quantity} - Restocked At: {self.restocked_at}"

from django.db import models

class PetData(models.Model):
    # Define your fields here
    pet_name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    weight = models.FloatField()
    # Add more fields as necessary

    def __str__(self):
        return self.pet_name


#visualization on disease
from django.db import models

class DiseaseRecord(models.Model):
    pet_name = models.CharField(max_length=100)
    disease_name = models.CharField(max_length=100)
    date_affected = models.DateField()
    days_to_cure = models.IntegerField()

    def __str__(self):
        return f"{self.pet_name} - {self.disease_name}"

    @property
    def cure_date(self):
        return self.date_affected + timedelta(days=self.days_to_cure)

#chatbot

from django.db import models
from django.contrib.auth.models import User

class ChatHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message_input = models.TextField()
    bot_response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"

#consultation

# # models.py
# from django.db import models
# from django.contrib.auth.models import User

# class Doctor(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     specialization = models.CharField(max_length=100)
#     available = models.BooleanField(default=True)

#     def __str__(self):
#         return self.user.username

# class Consultation(models.Model):
#     STATUS_CHOICES = [
#         ('pending', 'Pending'),
#         ('in_progress', 'In Progress'),
#         ('completed', 'Completed'),
#     ]

#     pet_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='consultations')
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
#     symptoms = models.TextField()
#     diagnosis = models.TextField(blank=True, null=True)
#     prescription = models.TextField(blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f'Consultation {self.id} - {self.status}'


class Doctor(models.Model):
    name = models.CharField(max_length=100,default='')
    specialization = models.CharField(max_length=100)
    location = models.CharField(max_length=100,default='')

    def __str__(self):
        return self.name

class Availability(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='availabilities')
    day_of_week = models.CharField(max_length=9, choices=[
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ])
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.doctor.name} - {self.day_of_week} ({self.start_time} - {self.end_time})"
    
class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"Appointment with Dr. {self.doctor.name} for {self.name} on {self.date} at {self.time}"