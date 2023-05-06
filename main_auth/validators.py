from rest_framework import serializers
from .models import CustomUser


def user_register(data):
    roles = ('builder', 'agency', 'bank')
    # print(data['role'] == 'manager', 'roless')
    errors = []
    if data['role'].name not in roles:
        errors.append({'role': 'Вы можете добавить только эти роли builder, agency, bank'})

    if data['password'] != data['password2']:
        errors.append({'password': 'Поля пароля не совпадают.'})

    if CustomUser.objects.filter(first_name__iexact=data['first_name'], last_name__iexact=data['last_name']).exists():
        errors.append({'user': f"{data['first_name']} {data['last_name']} уже в база существует"})

    return errors


def builder_staff_register(data):

    roles = ('manager', 'salemanager')
    print(data['role'], 'roleeee')
    errors = []

    if data['role'].name not in roles:
        errors.append({'role': 'Вы можете добавить только эти роли manager, sale manager'})

    if data['password'] != data['password2']:
        errors.append({'password': 'Поля пароля не совпадают.'})

    if CustomUser.objects.filter(first_name__iexact=data['first_name'], last_name__iexact=data['last_name']).exists():
        errors.append({'user': f"{data['first_name']} {data['last_name']} уже в база существует"})

    return errors
