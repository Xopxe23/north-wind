import datetime

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class Category(Base):
    __tablename__ = 'categories'

    category_id: Mapped[int] = mapped_column(primary_key=True)
    category_name: Mapped[str] = mapped_column(String(15))
    description: Mapped[str]
    picture: Mapped[bytes]


class Customer(Base):
    __tablename__ = 'customers'

    customer_id: Mapped[str] = mapped_column(String(5), primary_key=True)
    company_name: Mapped[str] = mapped_column(String(40))
    contact_name: Mapped[str] = mapped_column(String(30))
    contact_title: Mapped[str] = mapped_column(String(30))
    address: Mapped[str] = mapped_column(String(60))
    city: Mapped[str] = mapped_column(String(15))
    region: Mapped[str] = mapped_column(String(15), nullable=True)
    postal_code: Mapped[str] = mapped_column(String(10), nullable=True)
    country: Mapped[str] = mapped_column(String(15))
    phone: Mapped[str] = mapped_column(String(24), nullable=True)
    fax: Mapped[str] = mapped_column(String(24), nullable=True)


class Employee(Base):
    __tablename__ = 'employees'

    employee_id: Mapped[int] = mapped_column(primary_key=True)
    last_name: Mapped[str] = mapped_column(String(20))
    first_name: Mapped[str] = mapped_column(String(10))
    title: Mapped[str] = mapped_column(String(30))
    title_of_courtesy: Mapped[str] = mapped_column(String(25))
    birth_date: Mapped[datetime.date]
    hire_date: Mapped[datetime.date]
    address: Mapped[str] = mapped_column(String(60))
    city: Mapped[str] = mapped_column(String(15))
    region: Mapped[str] = mapped_column(String(15), nullable=True)
    postal_code: Mapped[str] = mapped_column(String(10))
    country: Mapped[str] = mapped_column(String(15))
    home_phone: Mapped[str] = mapped_column(String(24))
    extension: Mapped[str] = mapped_column(String(4))
    photo: Mapped[bytes]
    notes: Mapped[str]
    reports_to: Mapped[int] = mapped_column(Integer(), nullable=True)
    photo_path: Mapped[str] = mapped_column(String(255))


class Supplier(Base):
    __tablename__ = 'suppliers'

    supplier_id: Mapped[int] = mapped_column(primary_key=True)
    company_name: Mapped[str] = mapped_column(String(40))
    contact_name: Mapped[str] = mapped_column(String(30))
    contact_title: Mapped[str] = mapped_column(String(30))
    address: Mapped[str] = mapped_column(String(60))
    city: Mapped[str] = mapped_column(String(15))
    region: Mapped[str] = mapped_column(String(15), nullable=True)
    postal_code: Mapped[str] = mapped_column(String(10))
    country: Mapped[str] = mapped_column(String(15))
    phone: Mapped[str] = mapped_column(String(24))
    fax: Mapped[str] = mapped_column(String(24), nullable=True)
    homepage: Mapped[str] = mapped_column(nullable=True)


class Shipper(Base):
    __tablename__ = 'shippers'

    shipper_id: Mapped[int] = mapped_column(primary_key=True)
    company_name: Mapped[str] = mapped_column(String(40))
    phone: Mapped[str] = mapped_column(String(24))


class Product(Base):
    __tablename__ = 'products'

    product_id: Mapped[int] = mapped_column(primary_key=True)
    product_name: Mapped[str] = mapped_column(String(40))
    supplier_id: Mapped[int] = mapped_column(ForeignKey('suppliers.supplier_id'))
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.category_id'))
    quantity_per_unit: Mapped[str] = mapped_column(String(20))
    unit_price: Mapped[float]
    units_in_stock: Mapped[int]
    units_on_order: Mapped[int]
    reorder_level: Mapped[int]
    discontinued: Mapped[int]


class Order(Base):
    __tablename__ = 'orders'

    order_id: Mapped[int] = mapped_column(primary_key=True)
    customer_id: Mapped[str] = mapped_column(ForeignKey('customers.customer_id'))
    employee_id: Mapped[int] = mapped_column(ForeignKey('employees.employee_id'))
    order_date: Mapped[datetime.date]
    required_date: Mapped[datetime.date]
    shipped_date: Mapped[datetime.date] = mapped_column(nullable=True)
    ship_via: Mapped[int] = mapped_column(ForeignKey('shippers.shipper_id'))
    freight: Mapped[float]
    ship_name: Mapped[str] = mapped_column(String(40))
    ship_address: Mapped[str] = mapped_column(String(60))
    ship_city: Mapped[str] = mapped_column(String(15))
    ship_region: Mapped[str] = mapped_column(String(15), nullable=True)
    ship_postal_code: Mapped[str] = mapped_column(String(10), nullable=True)
    ship_country: Mapped[str] = mapped_column(String(15))


class OrderDetail(Base):
    __tablename__ = 'order_details'

    order_id: Mapped[str] = mapped_column(ForeignKey('orders.order_id'), primary_key=True)
    product_id: Mapped[str] = mapped_column(ForeignKey('products.product_id'), primary_key=True)
    unit_price: Mapped[float]
    quantity: Mapped[int]
    discount: Mapped[float]
