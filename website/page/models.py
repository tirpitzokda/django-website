from django.db import models
from django.contrib.auth.models import User, Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType



@receiver(post_migrate)
def create_user_roles(sender, **kwargs):
    # Создаем группы, если они не существуют
    for role in ['Director', 'Seller', 'HR']:
        group, created = Group.objects.get_or_create(name=role)

    # Добавляем разрешения в зависимости от роли
    director_permissions = ['add_product', 'change_product', 'delete_product', 'add_user', 'change_user', 'delete_user']
    seller_permissions = ['change_product']
    hr_permissions = ['add_user', 'change_user', 'delete_user']

    director_group = Group.objects.get(name='Director')
    seller_group = Group.objects.get(name='Seller')
    hr_group = Group.objects.get(name='HR')

    for perm in director_permissions:
        permission = Permission.objects.get(codename=perm)
        director_group.permissions.add(permission)

    for perm in seller_permissions:
        permission = Permission.objects.get(codename=perm)
        seller_group.permissions.add(permission)

    for perm in hr_permissions:
        permission = Permission.objects.get(codename=perm)
        hr_group.permissions.add(permission)