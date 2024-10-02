from django import forms
from .models import Appointment, Supplier, UserProfile, Product, Cart  # Ensure Product is imported correctly

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'quantity', 'reorderlevel']

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'confirm_password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Password and confirm password do not match."
            )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'age', 'profile_picture', 'groups', 'user_permissions']  # Include 'ema

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'price', 'image', 'quantity', 'reorderlevel']

   
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['user', 'product', 'quantity']

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['company_name', 'username', 'password', 'email', 'address']


class CustomLoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)




from django import forms
from .models import Supplier

class OrderForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)
    supplier = forms.ModelChoiceField(queryset=Supplier.objects.all(), required=True)



class EditProductForm(forms.Form):
    
    quantity = forms.IntegerField(label='Quantity')


from django import forms
from .models import Supplier

class SupplierFormedit(forms.ModelForm):
    class Meta:
        model = Supplier
        exclude = ['username', 'password']


##
from django import forms


class PetDataForm(forms.Form):
    # Define your form fields here
    pet_name = forms.CharField(max_length=100)
    breed = forms.CharField(max_length=100)
    age = forms.IntegerField()
    weight = forms.DecimalField(max_digits=5, decimal_places=2)
    symptoms = forms.CharField(widget=forms.Textarea)
    # Add more fields as necessary


#visualization
from django import forms
from .models import DiseaseRecord

class DiseaseRecordForm(forms.ModelForm):
    class Meta:
        model = DiseaseRecord
        fields = ['pet_name', 'disease_name', 'date_affected', 'days_to_cure']
        widgets = {
            'date_affected': forms.DateInput(attrs={'type': 'date'}),
        }

#consultation

# # forms.py
# from django import forms
# from .models import Consultation

# class ConsultationRequestForm(forms.ModelForm):
#     class Meta:
#         model = Consultation
#         fields = ['symptoms']

# class ConsultationUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Consultation
#         fields = ['diagnosis', 'prescription']


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'name', 'email', 'phone', 'date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'text', 'class': 'datepicker'}),
            'time': forms.TimeInput(attrs={'type': 'text', 'class': 'timepicker'}),
        }