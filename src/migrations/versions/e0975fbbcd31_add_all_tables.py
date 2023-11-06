"""add all tables

Revision ID: e0975fbbcd31
Revises: 
Create Date: 2023-11-06 14:01:54.805905

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'e0975fbbcd31'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('category_name', sa.String(length=15), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('picture', sa.LargeBinary(), nullable=False),
    sa.PrimaryKeyConstraint('category_id')
    )
    op.create_table('customers',
    sa.Column('customer_id', sa.String(length=5), nullable=False),
    sa.Column('company_name', sa.String(length=40), nullable=False),
    sa.Column('contact_name', sa.String(length=30), nullable=False),
    sa.Column('contact_title', sa.String(length=30), nullable=False),
    sa.Column('address', sa.String(length=60), nullable=False),
    sa.Column('city', sa.String(length=15), nullable=False),
    sa.Column('region', sa.String(length=15), nullable=True),
    sa.Column('postal_code', sa.String(length=10), nullable=True),
    sa.Column('country', sa.String(length=15), nullable=False),
    sa.Column('phone', sa.String(length=24), nullable=True),
    sa.Column('fax', sa.String(length=24), nullable=True),
    sa.PrimaryKeyConstraint('customer_id')
    )
    op.create_table('employees',
    sa.Column('employee_id', sa.Integer(), nullable=False),
    sa.Column('last_name', sa.String(length=20), nullable=False),
    sa.Column('first_name', sa.String(length=10), nullable=False),
    sa.Column('title', sa.String(length=30), nullable=False),
    sa.Column('title_of_courtesy', sa.String(length=25), nullable=False),
    sa.Column('birth_date', sa.Date(), nullable=False),
    sa.Column('hire_date', sa.Date(), nullable=False),
    sa.Column('address', sa.String(length=60), nullable=False),
    sa.Column('city', sa.String(length=15), nullable=False),
    sa.Column('region', sa.String(length=15), nullable=True),
    sa.Column('postal_code', sa.String(length=10), nullable=False),
    sa.Column('country', sa.String(length=15), nullable=False),
    sa.Column('home_phone', sa.String(length=24), nullable=False),
    sa.Column('extension', sa.String(length=4), nullable=False),
    sa.Column('photo', sa.LargeBinary(), nullable=False),
    sa.Column('notes', sa.String(), nullable=False),
    sa.Column('reports_to', sa.Integer(), nullable=True),
    sa.Column('photo_path', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('employee_id')
    )
    op.create_table('shippers',
    sa.Column('shipper_id', sa.Integer(), nullable=False),
    sa.Column('company_name', sa.String(length=40), nullable=False),
    sa.Column('phone', sa.String(length=24), nullable=False),
    sa.PrimaryKeyConstraint('shipper_id')
    )
    op.create_table('suppliers',
    sa.Column('supplier_id', sa.Integer(), nullable=False),
    sa.Column('company_name', sa.String(length=40), nullable=False),
    sa.Column('contact_name', sa.String(length=30), nullable=False),
    sa.Column('contact_title', sa.String(length=30), nullable=False),
    sa.Column('address', sa.String(length=60), nullable=False),
    sa.Column('city', sa.String(length=15), nullable=False),
    sa.Column('region', sa.String(length=15), nullable=True),
    sa.Column('postal_code', sa.String(length=10), nullable=False),
    sa.Column('country', sa.String(length=15), nullable=False),
    sa.Column('phone', sa.String(length=24), nullable=False),
    sa.Column('fax', sa.String(length=24), nullable=True),
    sa.Column('homepage', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('supplier_id')
    )
    op.create_table('orders',
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.String(length=5), nullable=False),
    sa.Column('employee_id', sa.Integer(), nullable=False),
    sa.Column('order_date', sa.Date(), nullable=False),
    sa.Column('required_date', sa.Date(), nullable=False),
    sa.Column('shipped_date', sa.Date(), nullable=True),
    sa.Column('ship_via', sa.Integer(), nullable=False),
    sa.Column('freight', sa.Float(), nullable=False),
    sa.Column('ship_name', sa.String(length=40), nullable=False),
    sa.Column('ship_address', sa.String(length=60), nullable=False),
    sa.Column('ship_city', sa.String(length=15), nullable=False),
    sa.Column('ship_region', sa.String(length=15), nullable=True),
    sa.Column('ship_postal_code', sa.String(length=10), nullable=True),
    sa.Column('ship_country', sa.String(length=15), nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.customer_id'], ),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.employee_id'], ),
    sa.ForeignKeyConstraint(['ship_via'], ['shippers.shipper_id'], ),
    sa.PrimaryKeyConstraint('order_id')
    )
    op.create_table('products',
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('product_name', sa.String(length=40), nullable=False),
    sa.Column('supplier_id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('quantity_per_unit', sa.String(length=20), nullable=False),
    sa.Column('unit_price', sa.Float(), nullable=False),
    sa.Column('units_in_stock', sa.Integer(), nullable=False),
    sa.Column('units_on_order', sa.Integer(), nullable=False),
    sa.Column('reorder_level', sa.Integer(), nullable=False),
    sa.Column('discontinued', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['categories.category_id'], ),
    sa.ForeignKeyConstraint(['supplier_id'], ['suppliers.supplier_id'], ),
    sa.PrimaryKeyConstraint('product_id')
    )
    op.create_table('order_details',
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('unit_price', sa.Float(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('discount', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['order_id'], ['orders.order_id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.product_id'], ),
    sa.PrimaryKeyConstraint('order_id', 'product_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_details')
    op.drop_table('products')
    op.drop_table('orders')
    op.drop_table('suppliers')
    op.drop_table('shippers')
    op.drop_table('employees')
    op.drop_table('customers')
    op.drop_table('categories')
    # ### end Alembic commands ###
