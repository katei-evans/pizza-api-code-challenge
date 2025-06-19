from flask import Blueprint, jsonify
from server.models import Pizza

pizza_bp = Blueprint('pizzas', __name__, url_prefix='/pizzas')

@pizza_bp.route('', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    result = []
    for p in pizzas:
        result.append({
            "id": p.id,
            "name": p.name,
            "ingredients": p.ingredients
        })
    return jsonify(result), 200