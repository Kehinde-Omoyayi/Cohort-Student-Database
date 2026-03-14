from django.db import models

#required to customise base user
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

#creating the student account
from django.conf import settings
from django.utils import timezone

#customisin the required object manager
class custom_user_manager(BaseUserManager):
    def create_user (self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save(using = self.db)
        return user

    def create_superuser(self, email, first_name, last_name, password):
        user = self.create_user(email, first_name, last_name, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user

#customised based user
class custom_user(AbstractBaseUser,PermissionsMixin):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = custom_user_manager()

    def __str__(self):
        return f'{self.email}'
    
class Department(models.Model):
    name = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

#customising the student account
class Student(models.Model):
    class graduation(models.TextChoices):
        YEAR_1 = '1 Year'
        YEAR_2 = '2 Years'
        YEAR_3 = '3 Years'
        YEAR_4 = '4 Years'
        YEAR_5 = '5 Years'
        YEAR_6 = '6 Years'
        
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='03_xboxseriesx_tech_chassis_mkt_wbrand_16x9_rgb_resized.jpg', upload_to = 'student_pics')
    matric_num = models.CharField(max_length=8,blank=True,unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    current_level = models.CharField(max_length=20, blank=True)
    level_duration = models.CharField(max_length=9, choices=graduation.choices, default=graduation.YEAR_1)
    admission_year = models.CharField(max_length=4, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    #to customise the matric number making it automated by years
    def save (self, *args, **kwargs):
        if not self.matric_num:
            year = timezone.now().year
            year_count = Student.objects.filter(created_at__year=year).count() + 1 # to count current year and add 1 
            result = str(year_count).zfill(4) #to extra 3 zeros to the count number
            self.matric_num = f'{year}{result}'
            
    #to customise the admission making it automated by years
        if not self.admission_year:
            year = timezone.now().year
            self.admission_year = f'{year}'

    #to customise the level making it automated by years
        if not self.current_level:
            test = (((year - int(self.admission_year))*100)+100)
            max_level = int(self.level_duration.split(' ')[0])
            if test > max_level:
                self.current_level = 'Graduate'
            self.current_level = f'{test} Level'
    
    #to make all capitalised
        for field in self._meta.fields:
            if isinstance(field,models.CharField):
                value = getattr(self,field.name)
                if value:
                    setattr(self, field.name, value.upper())
        super().save(*args,**kwargs)
    def __str__(self):
        return f'{self.user.first_name} of Matric No: {self.matric_num}' 
