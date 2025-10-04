from app import create_app
from model import db, Product, Location, ProductMovement
from datetime import datetime, timedelta
import uuid
import random

app = create_app()

with app.app_context():
    # wipe existing data
    db.drop_all()
    db.create_all()

    # --- create 3 sample products ---
    products = [
        Product(product_id='1', name='Gummy Bears'),
        Product(product_id='2', name='Lollipop'),
        Product(product_id='3', name='Alomond Dips'),
    ]
    db.session.add_all(products)

    # --- create 4 sample locations ---
    locations = [
        Location(name='Salem'),
        Location(name='Chennai'),
        Location(name='Palakkad'),
        Location(name='Bangalore'),
    ]
    db.session.add_all(locations)
    db.session.commit()

    # --- create 20 random movements ---
    movements = []
    now = datetime.utcnow()
    for i in range(20):
        prod = random.choice(products).product_id
       
        qty = random.randint(1, 20)
        timestamp = now - timedelta(days=random.randint(0, 10), hours=random.randint(0, 23))
        
       
        a, b = random.sample(locations, 2)
        mv = ProductMovement(
            
            timestamp=timestamp,
            from_location=a.name,
            to_location=b.name,
            product_id=prod,
            qty=qty
            )
        movements.append(mv)

    db.session.add_all(movements)
    db.session.commit()
    print("Seeded DB with 3 products, 4 locations, and 20 movements.")
