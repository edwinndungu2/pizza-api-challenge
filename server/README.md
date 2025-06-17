# 🍕 Pizza API Challenge

A simple RESTful API for managing restaurants and pizzas, built with Flask, SQLAlchemy, and Flask-Migrate.

## 🚀 Features

- List all restaurants
- Get details (and pizzas) for a single restaurant
- Delete a restaurant (with cascading deletes)
- List all pizzas
- Add a pizza to a restaurant (with price validation)

## 🏗️ Project Structure

```
server/
├── __init__.py
├── app.py
├── config.py
├── models/
│   ├── __init__.py
│   ├── restaurant.py
│   ├── pizza.py
│   └── restaurant_pizza.py
├── controllers/
│   ├── __init__.py
│   ├── restaurant_controller.py
│   ├── pizza_controller.py
│   └── restaurant_pizza_controller.py
├── seed.py
migrations/
challenge-1-pizzas.postman_collection.json
README.md
```

## 🧰 Setup Instructions

1. **Clone the repo:**
   ```bash
   git clone https://github.com/edwinndungu2/pizza-api-challenge.git
   cd pizza-api-challenge
   ```

2. **Install dependencies:**
   ```bash
   pipenv install
   pipenv shell
   ```

3. **Set up the database:**
   ```bash
   export FLASK_APP=server/app.py
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

4. **Seed the database:**
   ```bash
   python server/seed.py
   ```

5. **Run the server:**
   ```bash
   flask run
   ```
   The API will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000).

## 🛣️ API Endpoints

### Restaurants

- `GET /restaurants`  
  List all restaurants.

- `GET /restaurants/<id>`  
  Get a single restaurant and its pizzas.

- `DELETE /restaurants/<id>`  
  Delete a restaurant and its related restaurant-pizzas.

### Pizzas

- `GET /pizzas`  
  List all pizzas.

### Restaurant Pizzas

- `POST /restaurant_pizzas`  
  Add a pizza to a restaurant.  
  **Body:**  
  ```json
  {
    "price": 5,
    "pizza_id": 1,
    "restaurant_id": 3
  }
  ```

## 🧪 Testing

- Use [Postman](https://www.postman.com/downloads/) and import `challenge-1-pizzas.postman_collection.json` to test endpoints.
- Or use `curl`:
  ```bash
  curl http://127.0.0.1:5000/restaurants
  ```

