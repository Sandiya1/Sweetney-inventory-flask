from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid

db = SQLAlchemy()

def generate_uuid():
    return str(uuid.uuid4())

class Product(db.Model):
    __tablename__ = "product"
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    total_qty = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return f'<Product {self.product_id} ({self.total_qty})>'

class Location(db.Model):
    __tablename__ = "location"
    name = db.Column(db.String(200), primary_key=True)

    def __repr__(self):
        return f'<Location {self.name}>'

class ProductMovement(db.Model):
    __tablename__ = "product_movement"
    movement_id = db.Column(db.String(64), primary_key=True, default=generate_uuid)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    from_location = db.Column(db.String(200), db.ForeignKey('location.name'), nullable=True)
    to_location = db.Column(db.String(200), db.ForeignKey('location.name'), nullable=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'), nullable=False)
    qty = db.Column(db.Integer, nullable=False)

    product = db.relationship("Product", backref="movements")
    from_loc = db.relationship("Location", foreign_keys=[from_location], lazy="joined")
    to_loc = db.relationship("Location", foreign_keys=[to_location], lazy="joined")

    def __repr__(self):
        return f'<Movement {self.movement_id} {self.product_id} {self.qty}>'