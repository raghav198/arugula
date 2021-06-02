from . import db

class Recipe(db.Model):
    __tablename__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    cuisine = db.Column(db.String(32))
    servings = db.Column(db.Integer)
    prep_time = db.Column(db.Integer)
    cook_time = db.Column(db.Integer)
    instructions = db.Column(db.Text)
    description = db.Column(db.Text)
    dietary_tags = db.Column(db.String(32))
    ingredients = db.relationship('RecipeIngredientAssoc', back_populates='ingredients')

class Ingredient(db.Model):
    __tablename__ = 'ingredients'
    name = db.Column(db.String(64), primary_key=True)
    measurement_type = db.Column(db.String(16))
    recipes = db.relationship('RecipeIngredientAssoc', back_populates='recipes')

class RecipeIngredientAssoc(db.Model):
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredients.name'), primary_key=True)
    quantity = db.Column(db.Float)
    recipe = db.relationship('Recipe', back_populates='recipes')
    ingredient = db.relationship('Ingredient', back_populates='ingredients')