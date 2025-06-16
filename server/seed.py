from server.app import create_app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    # Create Restaurants
    r1 = Restaurant(name="Mario's Pizza", address="123 Main St")
    r2 = Restaurant(name="Kiki's Pizza", address="456 Side Ave")
    db.session.add_all([r1, r2])

    # Create Pizzas
    p1 = Pizza(name="Emma", ingredients="Dough, Tomato Sauce, Cheese")
    p2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
    db.session.add_all([p1, p2])

    db.session.commit()

    # Create RestaurantPizzas
    rp1 = RestaurantPizza(price=10, restaurant_id=r1.id, pizza_id=p1.id)
    rp2 = RestaurantPizza(price=12, restaurant_id=r1.id, pizza_id=p2.id)
    rp3 = RestaurantPizza(price=8, restaurant_id=r2.id, pizza_id=p1.id)
    db.session.add_all([rp1, rp2, rp3])

    db.session.commit()

    print("Database seeded!")