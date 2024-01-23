# app.py
# app.py
# app.py
# app.py

from flask import Flask

from flask_migrate import Migrate

from flask import jsonify, request
from models import Pizza, Restaurant, RestaurantPizza

from models import db 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza.db'

migrate = Migrate(app, db)

db.init_app(app)

# ... (Ajoutez les modèles ci-dessus)

# Route pour obtenir tous les restaurants
@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([{"id": r.id, "name": r.name, "address": r.address} for r in restaurants])

# Route pour obtenir un restaurant par ID
@app.route('/restaurants/<int:restaurant_id>', methods=['GET'])
def get_restaurant(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)

    if restaurant:
        pizzas = [{"id": restaurant_pizza.pizza.id, "name": restaurant_pizza.pizza.name, "ingredients": restaurant_pizza.pizza.ingredients} for restaurant_pizza in restaurant.restaurant_pizzas]
        return jsonify({"id": restaurant.id, "name": restaurant.name, "address": restaurant.address, "pizzas": pizzas})
    else:
        return jsonify({"error": "Restaurant not found"}), 404

# Route pour supprimer un restaurant par ID
@app.route('/restaurants/<int:restaurant_id>', methods=['DELETE'])
def delete_restaurant(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)

    if restaurant:
        RestaurantPizza.query.filter_by(restaurant_id=restaurant.id).delete()
        db.session.delete(restaurant)
        db.session.commit()
        return jsonify({}), 204
    else:
        return jsonify({"error": "Restaurant not found"}), 404

# Route pour obtenir toutes les pizzas
@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([{"id": p.id, "name": p.name, "ingredients": p.ingredients} for p in pizzas])

# Route pour créer une nouvelle RestaurantPizza
@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()

    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    if not (1 <= price <= 30):
        return jsonify({"errors": ["Validation errors"]}), 400

    restaurant_pizza = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
    db.session.add(restaurant_pizza)
    db.session.commit()

    pizza = Pizza.query.get(pizza_id)
    return jsonify({"id": pizza.id, "name": pizza.name, "ingredients": pizza.ingredients}), 201



if __name__=='__main__':
    app.run(port=5555, debug=True)
    