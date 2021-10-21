from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)

# update_last_login
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class CustomAccountManager(BaseUserManager):
    def create_user(
        self,
        user_name,
        team_type,
        position,
        company_number,
        phone_number,
        email,
        notice_permission,
        password=None,
        **extra_fields
    ):
        if not user_name:
            raise ValueError("You must provide an user_name")
        elif not team_type:
            raise ValueError("You must provide an team_type")
        elif not position:
            raise ValueError("You must provide an position")
        # elif not company_number: # null 이 어도 되는건 제외시켜서 만들면 됨 python manage.py createsuperuser일 경우
        #     raise ValueError("You must provide an company_number")
        elif not phone_number:
            raise ValueError("You must provide an phone_number")
        elif not email:
            raise ValueError("You must provide an email")
        # elif not notice_permission:
        #     raise ValueError("You must provide an notice_permission") # False 입력할수도 있어서 우선 주석 처리
        email = self.normalize_email(email)
        user = self.model(
            user_name=user_name,
            team_type=team_type,
            position=position,
            company_number=company_number,
            phone_number=phone_number,
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
        self,
        user_name,
        team_type,
        position,
        company_number,
        phone_number,
        email,
        notice_permission,
        password,
    ):
        user = self.create_user(
            user_name,
            team_type,
            position,
            company_number,
            phone_number,
            email,
            notice_permission,
            password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    user_name = models.CharField(max_length=50, unique=True)  # 이름
    team_type = models.CharField(max_length=50)  # 팀
    position = models.CharField(max_length=50)  # 직급
    company_number = models.CharField(max_length=50, null=True, blank=True)  # 유선번호(선택)
    phone_number = PhoneNumberField(unique=True, null=True, blank=True)  # 휴대폰 번호
    email = models.EmailField(db_index=True, unique=True)  # 이메일
    notice_permission = models.BooleanField(default=False)  # 공지사항 작성권한여부
    is_staff = models.BooleanField(default=False)  # 로그인만 할수 있는 권한
    is_active = models.BooleanField(default=True)  # 활성화 여부

    objects = CustomAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "user_name",
        "phone_number",
        "team_type",
        "position",
        "company_number",
        "notice_permission",
    ]

    def __str__(self):
        return str(self.email)


class Phone(models.Model):
    number = PhoneNumberField(unique=True)
    key = models.CharField(max_length=100, unique=True, blank=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return str(self.number)
