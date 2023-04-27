from django.contrib import admin

# Register your models here.
from .models import User1,User2
# Register your models here.
@admin.register(User1)
class UserAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'phonenumber', 'gender','fee','condition')

@admin.register(User2)
class User2Admin(admin.ModelAdmin):
    list_display=("id","name","Phonenumber","email","subject","message")
    

