from flask import Flask, render_template, redirect, url_for, request, flash
from datetime import datetime
import uuid
from model import db, Product, Location, ProductMovement
from forms import ProductForm, LocationForm, MovementForm

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sweetney.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)

    with app.app_context():
        db.create_all()

    # -------- Helper Functions --------
    def get_location_choices():
        """Get location choices for forms"""
        locations = Location.query.order_by(Location.name).all()
        return [('', '-- None --')] + [(loc.name, loc.name) for loc in locations]

    def get_product_choices():
        """Get product choices for forms"""
        products = Product.query.order_by(Product.product_id).all()
        return [(p.product_id, f"{p.product_id} — {p.name}") for p in products]


    # -------- Routes --------
    @app.route('/')
    def index():
        return render_template('index.html')

    # -------- Products CRUD --------
    @app.route('/products')
    def products():
        products_list = Product.query.order_by(Product.product_id).all()
        return render_template('products.html', products=products_list)

    @app.route('/products/add', methods=['GET', 'POST'])
    def add_product():
        form = ProductForm()

        if form.validate_on_submit():
            try:
                product_id = int(form.product_id.data)
                name = form.name.data.strip()
                total_qty=0 
                # Check if product ID already exists
                existing_product = Product.query.get(product_id)
                if existing_product:
                    flash(f'Product ID {product_id} already exists', 'danger')
                    return render_template('product_form.html', form=form, action='Add')

                # Create new product (no quantity/location fields)
                product = Product(
                    product_id=product_id,
                    name=name,
                )
                db.session.add(product)
                db.session.commit()

                flash(f'Product "{name}" added successfully with ID {product_id}', 'success')
                return redirect(url_for('products'))

            except Exception as e:
                db.session.rollback()
                print(f"Error adding product: {str(e)}")
                flash(f'Error adding product: {str(e)}', 'danger')

        else:
            if form.errors:
                print(f"Form errors: {form.errors}")
                for field, errors in form.errors.items():
                    for error in errors:
                        flash(f'{getattr(form, field).label.text}: {error}', 'danger')

        return render_template('product_form.html', form=form, action='Add')

    @app.route('/products/edit/<int:product_id>', methods=['GET', 'POST'])
    def edit_product(product_id):
        product = Product.query.get_or_404(product_id)
        form = ProductForm(obj=product)
        
        if form.validate_on_submit():
            try:
                new_product_id = int(form.product_id.data)
                new_name = form.name.data.strip()
                
                # Check for duplicate product ID (excluding current)
                existing = Product.query.filter(
                    Product.product_id == new_product_id,
                    Product.product_id != product_id
                ).first()
                if existing:
                    flash('Product ID already exists', 'danger')
                    return render_template('product_form.html', form=form, action='Edit')

                product.product_id = new_product_id
                product.name = new_name
                
                db.session.commit()
                flash('Product updated successfully', 'success')
                return redirect(url_for('products'))

            except Exception as e:
                db.session.rollback()
                flash(f'Error updating product: {str(e)}', 'danger')

        return render_template('product_form.html', form=form, action='Edit')

    @app.route('/products/delete/<int:product_id>', methods=['POST'])
    def delete_product(product_id):
        try:
            product = Product.query.get_or_404(product_id)
            
            # Delete associated movements first
            ProductMovement.query.filter_by(product_id=product_id).delete()
            
            db.session.delete(product)
            db.session.commit()
            flash('Product deleted successfully', 'info')
        except Exception as e:
            db.session.rollback()
            flash(f'Error deleting product: {str(e)}', 'danger')
        
        return redirect(url_for('products'))

    # -------- Locations CRUD --------
    @app.route('/locations')
    def locations():
        locations_list = Location.query.order_by(Location.name).all()
        return render_template('locations.html', locations=locations_list)

    @app.route('/locations/add', methods=['GET', 'POST'])
    def add_location():
        form = LocationForm()
        
        if form.validate_on_submit():
            try:
                location_name = form.name.data.strip()
                
                if Location.query.get(location_name):
                    flash('Location already exists', 'danger')
                    return render_template('location_form.html', form=form, action='Add')

                location = Location(name=location_name)
                db.session.add(location)
                db.session.commit()
                
                flash('Location added successfully', 'success')
                return redirect(url_for('locations'))

            except Exception as e:
                db.session.rollback()
                flash(f'Error adding location: {str(e)}', 'danger')

        return render_template('location_form.html', form=form, action='Add')

    @app.route('/locations/edit/<string:location_name>', methods=['GET', 'POST'])
    def edit_location(location_name):
        location = Location.query.get_or_404(location_name)
        form = LocationForm(obj=location)
        
        if form.validate_on_submit():
            try:
                new_name = form.name.data.strip()
                
                existing = Location.query.filter(
                    Location.name == new_name, 
                    Location.name != location_name
                ).first()
                if existing:
                    flash('Location name already exists', 'danger')
                    return render_template('location_form.html', form=form, action='Edit')

                location.name = new_name
                db.session.commit()
                
                flash('Location updated successfully', 'success')
                return redirect(url_for('locations'))

            except Exception as e:
                db.session.rollback()
                flash(f'Error updating location: {str(e)}', 'danger')

        return render_template('location_form.html', form=form, action='Edit')

    @app.route('/locations/delete/<string:location_name>', methods=['POST'])
    def delete_location(location_name):
        try:
            location = Location.query.get_or_404(location_name)
            db.session.delete(location)
            db.session.commit()
            flash('Location deleted successfully', 'info')
        except Exception as e:
            db.session.rollback()
            flash(f'Error deleting location: {str(e)}', 'danger')
        
        return redirect(url_for('locations'))

    # -------- Product Movements --------
    @app.route('/movements')
    def movements():
        movements_list = ProductMovement.query.order_by(ProductMovement.timestamp.desc()).limit(200).all()
        return render_template('movements.html', movements=movements_list)

    @app.route('/movements/add', methods=['GET', 'POST'])
    def add_movement():
        form = MovementForm()
        form.product.choices = get_product_choices()
        form.from_location.choices = get_location_choices()
        form.to_location.choices = get_location_choices()

        if form.validate_on_submit():
            try:
                product_id = int(form.product.data)
                qty = form.qty.data
                from_location = form.from_location.data or None
                to_location = form.to_location.data or None

                if not from_location and not to_location:
                    flash("Error: Both 'From' and 'To' locations cannot be empty", "danger")
                    return render_template('movement_form.html', form=form, action='Add')

                if from_location == to_location:
                    flash("Error: 'From' and 'To' locations cannot be the same", "danger")
                    return render_template('movement_form.html', form=form, action='Add')

                movement = ProductMovement(
                    from_location=from_location,
                    to_location=to_location,
                    product_id=product_id,
                    qty=qty
                )
                db.session.add(movement)
                db.session.commit()

                flash('Movement recorded successfully', 'success')
                return redirect(url_for('movements'))

            except Exception as e:
                db.session.rollback()
                flash(f'Error recording movement: {str(e)}', 'danger')

        return render_template('movement_form.html', form=form, action='Add')

    @app.route('/movements/delete/<string:movement_id>', methods=['POST'])
    def delete_movement(movement_id):
        try:
            movement = ProductMovement.query.get_or_404(movement_id)
            db.session.delete(movement)
            db.session.commit()
            flash('Movement deleted successfully', 'info')
        except Exception as e:
            db.session.rollback()
            flash(f'Error deleting movement: {str(e)}', 'danger')
        
        return redirect(url_for('movements'))

    # -------- Report --------
    @app.route('/report')
    def report():
        movements_list = ProductMovement.query.order_by(ProductMovement.timestamp.desc()).all()

        report_data = []
        for movement in movements_list:
            if not movement.product:
                continue

            report_data.append({
                'movement_id': movement.movement_id,
                'timestamp': movement.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                'product_id': movement.product.product_id,
                'product_name': movement.product.name,
                'from_location': movement.from_location if movement.from_location else '—',
                'to_location': movement.to_location if movement.to_location else '—',
                'qty': movement.qty
            })

        return render_template('report.html', report_data=report_data)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
