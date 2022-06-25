import sqlalchemy
from .db_session import SqlAlchemyBase


class Product(SqlAlchemyBase):
    __tablename__ = 'products'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    number = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    cost_rub = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    cost_dol = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    delivery_period = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    def __repr__(self):
        return str(self.id)
