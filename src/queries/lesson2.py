from sqlalchemy import select
from sqlalchemy.sql.functions import count, func

from src.database import session_maker
from src.models import Customer, Order, Product, Employee, Supplier


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


# Выбрать все заказы из стран France, Austria, Spain
def l2_query8():
    query = select(Order).where(Order.ship_country.in_(['France', 'Austria', 'Spain']))
    print(query)
    with session_maker() as session:
        res = session.execute(query)
        result = res.all()
    print(result)


# Выбрать все заказы, отсортировать по required_date (по убыванию) и отсортировать по дате отгрузке (по возрастанию)
def l2_query9():
    query = select(Order).order_by(Order.required_date.desc(), Order.shipped_date.asc())
    print(query)
    with session_maker() as session:
        res = session.execute(query)
        result = res.all()
    print(result)


# Выбрать минимальное кол-во единиц товара среди тех продуктов, которых в продаже более 30 единиц.
def l2_query10():
    query = select(func.min(Product.units_in_stock)).where(Product.units_in_stock > 30)
    print(query)
    with session_maker() as session:
        res = session.execute(query)
        result = res.all()
    print(result)


# Выбрать максимальное кол-во единиц товара среди тех продуктов, которых в продаже более 30 единиц.
def l2_query11():
    query = select(func.max(Product.units_in_stock)).where(Product.units_in_stock > 30)
    print(query)
    with session_maker() as session:
        res = session.execute(query)
        result = res.all()
    print(result)


# Найти среднее значение дней уходящих на доставку с даты формирования заказа в USA
def l2_query12():
    query = select(func.avg(Order.shipped_date - Order.order_date)).where(Order.ship_country == 'USA')
    print(query)
    with session_maker() as session:
        res = session.execute(query)
        result = res.all()
    print(result)


# Найти сумму, на которую имеется товаров (кол-во * цену) причём таких, которые планируется продавать и в будущем (см. на поле discontinued)
def l2_query13():
    query = select(func.sum(Product.units_in_stock * Product.unit_price)).where(Product.discontinued != 1)
    print(query)
    with session_maker() as session:
        res = session.execute(query)
        result = res.all()
    print(result)


def l2_part2():
    l2_query8()
    l2_query9()
    l2_query10()
    l2_query11()
    l2_query12()
    l2_query13()


# Выбрать все записи заказов в которых наименование страны отгрузки начинается с 'U'
def l2_query14():
    query = select(Order).where(Order.ship_country.like('U%'))
    print(query)
    with session_maker() as session:
        res = session.execute(query)
        result = res.all()
    print(result)


# Выбрать записи заказов (включить колонки идентификатора заказа, идентификатора заказчика, веса и страны отгузки),
# которые должны быть отгружены в страны имя которых начинается с 'N',
# отсортировать по весу (по убыванию) и вывести только первые 10 записей.
def l2_query15():
    query = select(Order.order_id, Order.customer_id, Order.freight, Order.ship_country).where(
        Order.ship_country.like('N%')
    ).order_by(Order.freight.desc()).limit(10)
    print(query)
    with session_maker() as session:
        res = session.execute(query)
        result = res.all()
    print(result)


# Выбрать записи работников (включить колонки имени, фамилии, телефона, региона) в которых регион неизвестен
def l2_query16():
    query = select(
        Employee.first_name, Employee.last_name, Employee.home_phone, Employee.region
    ).where(Employee.region.is_(None))
    print(query)
    with session_maker() as session:
        res = session.execute(query)
        result = res.all()
    print(result)


# Подсчитать кол-во заказчиков регион которых известен
def l2_query17():
    query = select(func.count()).select_from(Customer).where(Customer.region.is_(None))
    print(query)
    with session_maker() as session:
        res = session.execute(query)
        result = res.all()
    print(result)


# Подсчитать кол-во поставщиков в каждой из стран и отсортировать результаты группировки по убыванию кол-ва
def l2_query18():
    query = select(Supplier.country, func.count()).group_by(Supplier.country).order_by(func.count().desc())
    print(query)
    with session_maker() as session:
        res = session.execute(query)
        result = res.all()
    print(result)


# Подсчитать суммарный вес заказов (в которых известен регион) по странам,
# затем отфильтровать по суммарному весу (вывести только те записи где суммарный вес больше 2750)
# и отсортировать по убыванию суммарного веса.
def l2_query19():
    query = select(Order.ship_country, func.sum(Order.freight)).group_by(Order.ship_country).having(
        func.sum(Order.freight) > 2750
    ).order_by(func.sum(Order.freight).desc())
    print(query)
    with session_maker() as session:
        res = session.execute(query)
        result = res.all()
    print(result)


# Выбрать все уникальные страны заказчиков и поставщиков и отсортировать страны по возрастанию
def l2_query20():
    query = select(Supplier.country).union(select(Customer.country))
    print(query)
    with session_maker() as session:
        res = session.execute(query)
        result = res.all()
    print(result)


# Выбрать такие страны в которых "зарегистированы" одновременно и заказчики и поставщики и работники.
def l2_query21():
    query = select(Supplier.country).intersect(select(Customer.country), select(Employee.country))
    print(query)
    with session_maker() as session:
        res = session.execute(query)
        result = res.all()
    print(result)


def l2_part3():
    l2_query14()
    l2_query15()
    l2_query16()
    l2_query17()
    l2_query18()
    l2_query19()
    l2_query20()
    l2_query21()
