# from django.db import models
# from django.contrib.auth.models import PermissionsMixin, BaseUserManager, AbstractBaseUser
# from django.utils import timezone




# class UserManager(BaseUserManager):
#     #--- initial create function
#     def _create_user(self, email, password, is_staff, is_superuser, **kwargs):
#         if not email:
#             raise ValueError('email account is needed')
        
#         email = self.normalize_email(email)
#         now = timezone.now()
#         user = self.model(
#             email=email,
#             is_staff=is_staff,
#             is_superuser=is_superuser,
#             last_login = now,
#             date_joined=now,
#             **kwargs
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
    
#     # --- basic user create function
#     def create_user(self, email=None, password=None, **kwargs):
#         return self._create_user(email, password, False, False, **kwargs)
    
#     # -- admin user main create function
#     def create_superuser(self, email=None, password=None, **kwargs):
#         user = self._create_user(email, password, True, True, **kwargs)
#         user.save(using=self._db)
#         return user
    


# # --  custom user model(with email only)    
# class User(PermissionsMixin, AbstractBaseUser):
#     fullname = models.CharField(blank=True, null=True, max_length=255)
#     email = models.EmailField(unique=True)
#     is_active = models.BooleanField(default=True)
#     is_superuser = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     last_login = models.DateTimeField(null=True, blank=True)
#     date_joined = models.DateTimeField(auto_now_add=True)
#     objects = UserManager()
#     USERNAME_FIELD = 'email'
#     EMAIL_FIELD = 'email'
#     REQUIRED_FIELDS = []
    
#     def get_absolute_url(self):
#         return "/users/%i/" % (self.pk)
    
#     def get_email(self):
#         if not self.fullname:
#             return self.email
#         else:
#             return self.fullname