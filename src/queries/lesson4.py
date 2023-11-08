import datetime

from sqlalchemy import select, func, and_, any_, all_
from sqlalchemy.orm import aliased

from src.database import session_maker
from src.models import Supplier, Customer, Category, Product, Order, OrderDetail


# Вывести продукты количество которых в продаже меньше самого малого среднего количества продуктов в деталях заказов
# (группировка по product_id). Результирующая таблица должна иметь колонки product_name и units_in_stock.
def l4_query1():
    d = aliased(OrderDetail)
    p = aliased(Product)
    subquery = select(func.avg(d.quantity).label("avg_quantity")).select_from(p).join(
        d, p.product_id == d.product_id).group_by(p.product_id)
    query = select(p.product_name, p.units_in_stock).where(
        p.units_in_stock < all_(subquery.scalar_subquery())
    ).order_by(p.units_in_stock.desc())
    print(query)
    with session_maker() as session:
        res = session.execute(query)
        result = res.all()
    print(result)


# Напишите запрос, который выводит общую сумму фрахтов заказов для компаний-заказчиков для заказов,
# стоимость фрахта которых больше или равна средней величине стоимости фрахта всех заказов,
# а также дата отгрузки заказа должна находится во второй половине июля 1996 года.
# Результирующая таблица должна иметь колонки customer_id и freight_sum,
# строки которой должны быть отсортированы по сумме фрахтов заказов.
def l4_query2():
    o = aliased(Order)
    subquery = select(o.customer_id, func.avg(o.freight).label('freight_avg')).group_by(o.customer_id).alias("oa")
    query = select(o.customer_id, func.sum(o.freight).label("freight_sum")).select_from(o).join(
        subquery, subquery.c.customer_id == o.customer_id
    ).where(and_(o.freight > subquery.c.freight_avg, o.shipped_date.between(
        datetime.date(1996, 7, 16), datetime.date(1996, 7, 31)
    ))).group_by(o.customer_id)
    print(query)
    with session_maker() as session:
        res = session.execute(query)
        result = res.all()
    print(result)


def l4():
    l4_query1()
    l4_query2()