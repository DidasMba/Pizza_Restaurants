from app import app
import random
from models import db, Pizza, Restaurant, RestaurantPizza
from faker import Faker


with app.app_context():

    db.drop_all()
    db.create_all()

    fake = Faker()


    print("🦸‍♀️ Seeding pizzas...")
    pizzas = [
        
        {"name": "Cheese", "ingredients": "Dough, Tomato Sauce, Cheese"},
        {"name": "Pepperoni", "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"},
        {"name": "Margherita", "ingredients": " Pizza dough, tomato sauce, fresh mozzarella cheese, fresh basil, olive oil"},
        {"name": "Pepperoni and Mushroom", "ingredients": "Pizza dough, tomato sauce, pepperoni slices, sliced mushrooms, shredded mozzarella cheese"},
        {"name": "BBQ Chicken", "ingredients": " Pizza dough, BBQ sauce, cooked and shredded chicken, red onion slices, cilantro, shredded mozzarella cheese"},
        {"name": "Vegetarian Mediterranean", "ingredients": "Pizza dough, hummus, cherry tomatoes, black olives, red onion, feta cheese, spinach leaves"},
        {"name": "Pesto and Sun-Dried Tomato", "ingredients": "Pizza dough, pesto sauce, sun-dried tomatoes, pine nuts, goat cheese"},
        {"name": "Hawaiian", "ingredients": "Pizza dough, tomato sauce, ham slices, pineapple chunks, shredded mozzarella cheese"},
        {"name": "Caprese", "ingredients": " Pizza dough, fresh tomatoes, fresh mozzarella slices, balsamic glaze, fresh basil"},
        {"name": "White Pizza", "ingredients": "Pizza dough, ricotta cheese, garlic, sautéed spinach, artichoke hearts, shredded mozzarella cheese"},
        {"name": "Buffalo Chicken", "ingredients": "Pizza dough, buffalo sauce, cooked and shredded chicken, blue cheese crumbles, celery slices"},
        {"name": "Meat Lovers'", "ingredients": "Pizza dough, tomato sauce, pepperoni, Italian sausage, bacon, ground beef, shredded mozzarella cheese"}
    ]
    for pizza_data in pizzas:
        pizza = Pizza(**pizza_data)
        db.session.add(pizza)

        
    print("🦸‍♀️ Seeding restaurants...")

    restaurants = []

    for i in range(20):
        restaurant = Restaurant(
            name=fake.company(),
            address=fake.address(),
        )
        restaurants.append(restaurant)

    db.session.add_all(restaurants)
    db.session.commit() 

    print("🦸‍♀️ Adding pizzas to restaurants...")
    
    for pizza in Pizza.query.all():
        for _ in range(random.randint(1, 3)):
            price = random.randint(1, 30)
            restaurant = Restaurant.query.order_by(db.func.random()).first()
            restaurant_pizzas = RestaurantPizza(pizza_id=pizza.id, restaurant_id=restaurant.id, price=price)
            db.session.add(restaurant_pizzas)

    db.session.commit()
    print("🦸‍♀️ Done seeding!")