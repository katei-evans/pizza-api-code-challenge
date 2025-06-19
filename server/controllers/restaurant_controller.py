from flask import Blueprint, jsonify, request
from server.models import Restaurant, RestaurantPizza, Pizza
from server.app import db

restaurant_bp = Blueprint('restaurants', __name__, url_prefix='/restaurants')

@restaurant_bp.route('', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    result = []
    for r in restaurants:
        result.append({
            "id": r.id,
            "name": r.name,
            "address": r.address
        })
    return jsonify(result), 200

@restaurant_bp.route('/<int:id>', methods=['GET'])
def get_restaurant_by_id(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    pizzas = [
        {
            "id": rp.pizza.id,
            "name": rp.pizza.name,
            "ingredients": rp.pizza.ingredients
        }
        for rp in restaurant.restaurant_pizzas
    ]

    data = {
        "id": restaurant.id,
        "name": restaurant.name,
        "address": restaurant.address,
        "pizzas": pizzas
    }

    return jsonify(data), 200

@restaurant_bp.route('/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    db.session.delete(restaurant)
    db.session.commit()
    return '', 204