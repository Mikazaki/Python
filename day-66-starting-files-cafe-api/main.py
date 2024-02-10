from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random


app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)
    
    def to_dict(self):
        #Method 1. 
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            #Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary
        
        #Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}



with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route('/random')
def get_random_cafe():
     with app.app_context():
        result = db.session.execute(db.select(Cafe).order_by(Cafe.name)).scalars()
        all_cafes = result.all()
        random_cafe = random.choice(all_cafes)
        return jsonify(cafe=random_cafe.to_dict())
    

@app.route('/all')
def all_cafes():
    with app.app_context():
        result = db.session.execute(db.select(Cafe).order_by(Cafe.name)).scalars()
        all_cafes = result.all()
    
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])

@app.route('/search')
def search():
    loc = request.args.get('loc')

    with app.app_context():
        cafe = db.session.execute(db.select(Cafe).where(Cafe.location == loc)).scalar()
        
    if cafe:
        return jsonify(cafe=cafe.to_dict())
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})
    




# HTTP POST - Create Record
@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        # Default values for optional fields
        default_img_url = "default_image_url_here"  # Provide a default image URL
        default_location = "default_location_here"  # Provide a default location
        default_seats = "default_seats_info_here"   # Provide default seats information
        default_coffee_price = "default_price_here" # Provide a default coffee price

        new_cafe = Cafe(
            name=request.form.get('name'),
            map_url=request.form.get('map_url'),
            img_url=request.form.get('img_url', default_img_url),  # Corrected field name
            location=request.form.get('location', default_location),
            seats=request.form.get('seats', default_seats),
            has_toilet=int(request.form.get('has_toilet', 0)),
            has_wifi=int(request.form.get('has_wifi', 0)),
            has_sockets=int(request.form.get('has_sockets', 0)),
            can_take_calls=int(request.form.get('can_take_calls', 0)),
            coffee_price=request.form.get('coffee_price', default_coffee_price)
        )
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully added the new cafe."})
  
    
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def patch_new_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = Cafe.query.get(cafe_id)

    if cafe is None: 
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404

    cafe.coffee_price = new_price
    db.session.commit()
    return jsonify(response={"success": "Successfully updated the price."}), 200



@app.route('/report-closed/<int:cafe_id>', methods=['DELETE'])
def delete(cafe_id):
    api_key = "TopSecretAPIKey"
    key = request.args.get('api-key')

    if key != api_key:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403

    cafe = Cafe.query.get(cafe_id)
    if cafe:
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


    
    
    


# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
