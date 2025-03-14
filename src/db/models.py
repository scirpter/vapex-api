from tortoise import fields
from tortoise.models import Model


class Account(Model):
    uuid = fields.UUIDField(pk=True)
    full_name = fields.TextField()
    username = fields.TextField()
    password_hash = fields.TextField()


class Product(Model):
    uuid = fields.UUIDField(pk=True)
    name = fields.TextField()
    flavor = fields.TextField()
    stock = fields.IntField()
