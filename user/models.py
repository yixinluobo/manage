from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    class Meta:
        db_table = 't_user'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
