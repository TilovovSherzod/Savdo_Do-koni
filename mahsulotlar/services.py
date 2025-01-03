from django.db import connection
from contextlib import closing

from .models import ElektronXizmat

def barcha_xizmatlar_ol():
    """Barcha xizmatlarni olish."""
    return ElektronXizmat.objects.all()

def xizmat_qidir(nom):
    """Xizmatni nomi bo'yicha qidirish."""
    return ElektronXizmat.objects.filter(nom__icontains=nom)


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]

def dictfetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))

def get_product_by_id(product_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * from mahsulotlar_product where id=%s""", [product_id])
        product = dictfetchone(cursor)
        return product

def get_orderproduct_by_id(product_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * from mahsulotlar_orderproduct where id=%s""", [product_id])
        product = dictfetchone(cursor)
        return product

def get_user_by_phone(phone_number):
    with closing(connection.cursor()) as cursor:
        cursor.execute(""" SELECT * from mahsulotlar_customer where phone_number =%s""", [phone_number])
        user = dictfetchone(cursor)
        return user
