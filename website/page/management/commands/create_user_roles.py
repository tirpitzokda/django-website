from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from clients.models import Product

class Command(BaseCommand):
    help = 'Создание групп и разрешений'

    def handle(self, *args, **kwargs):
        # Создание групп
        director_group, created = Group.objects.get_or_create(name='Director')
        seller_group, created = Group.objects.get_or_create(name='Seller')
        hr_group, created = Group.objects.get_or_create(name='HR')

        # Получение разрешений для модели Product
        content_type = ContentType.objects.get_for_model(Product)
        content_type = ContentType.objects.get_for_model(User)

        permissions = {
            'add_product': 'Can add product',
            'change_product': 'Can change product',
            'delete_product': 'Can delete product',
            'view_product': 'Can view product',
            'add_user': 'Can add user',
            'change_user': 'Can change user',
            'delete_user': 'Can delete user',
            'view_user': 'Can view user',
        }

        for codename, name in permissions.items():
            permission, created = Permission.objects.get_or_create(
                codename=codename,
                name=name,
                content_type=content_type
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Создано разрешение: {name}'))

        # Назначение разрешений группам
        director_group.permissions.set(Permission.objects.filter(codename__in=permissions.keys()))
        seller_group.permissions.set(Permission.objects.filter(codename__in=['change_product']))
        hr_group.permissions.set(Permission.objects.filter(codename__in=[]))

        self.stdout.write(self.style.SUCCESS('Группы и разрешения созданы успешно'))