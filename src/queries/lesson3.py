from sqlalchemy import select, func, and_

from src.database import session_maker
from src.models import Customer, Product, Supplier, Category, Order, Employee, OrderDetail, Shipper


# Найти заказчиков и обслуживающих их заказы сотрудников таких, что и заказчики и сотрудники из города London,
# а доставка идёт компанией Speedy Express. Вывести компанию заказчика и ФИО сотрудника.
def l3_query1():
    query = select(
        Customer.company_name, func.concat(Employee.first_name, " ", Employee.last_name)
    ).select_from(Customer).join(Order, Order.customer_id == Customer.customer_id).join(
        Employee, Employee.employee_id == Order.employee_id).join(Shipper, Order.ship_via == Shipper.shipper_id).where(
        and_(Customer.city == 'London', Employee.city == 'London', Shipper.company_name == 'Speedy Express')
    )
    print(query)
    with session_maker() as session:
        res = session.execute(query)
        result = res.all()
    print(result)


# Найти активные (см. поле discontinued) продукты из категории Beverages и Seafood, которых в продаже менее 20 единиц.
# Вывести наименование продуктов, кол-во единиц в продаже, имя контакта поставщика и его телефонный номер.
def l3_query2():
    query = select(
        Product.product_name, Product.units_in_stock, Supplier.contact_name, Supplier.phone
    ).select_from(Product).join(Supplier, Product.supplier_id == Supplier.supplier_id).join(
        Category, Product.category_id == Category.category_id).where(
        and_(Category.category_name.in_(["Beverages", "Seafood"]), Product.units_in_stock < 20, Product.discontinued != 1)
    ).order_by(Product.units_in_stock)
    print(query)
    with session_maker() as session:
        res = session.execute(query)
        result = res.all()
    print(result)


# Найти заказчиков, не сделавших ни одного заказа. Вывести имя заказчика и order_id.
def l3_query3():
    query = select(
        Customer.contact_name, Order.order_id
    ).select_from(Customer).outerjoin(Order, Customer.customer_id == Order.customer_id).where(Order.order_id.is_(None))
    print(query)
    with session_maker() as session:
        res = session.execute(query)
        result = res.all()
    print(result)


def l3_part1():
    l3_query1()
    l3_query2()
    l3_query3()
