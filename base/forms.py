from django.forms import ModelForm
from .models import Room
from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm
class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['host','name','description','topic',]
        exclude = ['host','participants']

""" class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']
 """
class uSerForm(ModelForm):
    class Meta: 
      model = User
      fields = ['username', 'email']
    
       