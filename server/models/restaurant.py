from server import db

restaurant_pizza = db.Table(
    'restaurant_pizza',
    db.Column('restaurant_id', db.Integer, db.ForeignKey('restaurants.id'), primary_key=True),
    db.Column('pizza_id', db.Integer, db.ForeignKey('pizzas.id'), primary_key=True),
    db.Column('price', db.Integer, nullable=False)
)

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String, nullable=False)

    pizzas = db.relationship(
        'Pizza',
        secondary=restaurant_pizza,
        back_populates='restaurants',
        cascade='all, delete'
    )

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'pizzas': [pizza.to_dict() for pizza in self.pizzas]
        }