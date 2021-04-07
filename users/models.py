from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name="Email do usuário",
        max_length=194,
        unique=True,
    )

    # *Necessary* attributes for django custom users
    is_active = models.BooleanField(
        verbose_name="Usuário está ativo",
        default=True,
    )

    is_staff = models.BooleanField(
        verbose_name="Usuário é da equipe de desenvolvimento",
        default=False,
    )

    is_superuser = models.BooleanField(
        verbose_name="Usuário é super-usuário",
        default=False,
    )

    USERNAME_FIELD = "email"

    # Metadata 
    class Meta:
        # Give the user model a name (useful in django admin)
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        db_table = "custom_user"

    def __str__(self):
        return self.email