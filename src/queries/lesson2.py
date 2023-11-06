from sqlalchemy import select
from sqlalchemy.sql.functions import count, func

from src.database import session_maker
from src.models import Customer, Order


# Выбрать все данные из таблицы customers
def l2_query1():
    query = select(Customer)
    print(query)
    with session_maker() as session:
        res = session.execute(query)
        result = res.all()
    print(result)


# Выбрать все записи из таблицы customers, но только колонки "имя контакта" и "город"
def l2_query2():
    query = select(Customer.contact_name, Customer.city)
    print(query)
    with session_maker() as session:
        res = session.execute(query)
        result = res.all()
    print(result)


# Выбрать все записи из таблицы orders, но взять две колонки: идентификатор заказа и колонку, значение в которой
# мы рассчитываем как разницу между датой отгрузки и датой формирования заказа.
def l2_query3():
    query = select(Order.order_id, Order.shipped_date - Order.order_date)
    print(query)
    with session_maker() as session:
        res = session.execute(query)
        result = res.all()
    print(result)


# Выбрать все уникальные города в которых "зарегестрированы" заказчики
def l2_query4():
    query = select(Customer.city).distinct()
    print(query)
    with session_maker() as session:
        res = session.execute(query)
        result = res.all()
    print(result)


# Выбрать все уникальные сочетания городов и стран в которых "зарегестрированы" заказчики
def l2_query5():
    query = select(Customer.city, Customer.country).distinct()
    print(query)
    with session_maker() as session:
        res = session.execute(query)
        result = res.all()
    print(result)


# Посчитать кол-во заказчиков
def l2_query6():
    query = select(func.count()).select_from(Customer)
    print(query)
    with session_maker() as session:
        res = session.execute(query)
        result = res.all()
    print(result)


# Посчитать кол-во уникальных стран в которых "зарегестрированы" заказчики
def l2_query7():
    query = select(count(Customer.country.distinct()))
    print(query)
    with session_maker() as session:
        res = session.execute(query)
        result = res.all()
    print(result)


# Выполнить первую часть
def l2_part1():
    l2_query1()
    l2_query2()
    l2_query3()
    l2_query4()
    l2_query5()
    l2_query6()
    l2_query7()
