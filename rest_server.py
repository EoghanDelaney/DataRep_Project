from flask import Flask, url_for, request, redirect, abort, jsonify

from crime_DOA import crimeDOA
from twitter_scrape import twitter
from flask import render_template

app = Flask(__name__, static_url_path='', static_folder='staticpages')

@app.route('/')
def index():
    return "hello"



# curl http://127.0.0.1:5000/crimes
@app.route('/crimes')
def getAll():
    return jsonify(crimeDOA.getAll())



# find By id
# curl http://127.0.0.1:5000/crimes/1

@app.route('/crimes/<int:id>')
def findById(id):
    return jsonify(crimeDOA.findByID(id))


# create
# curl -X POST -d "{\"User\":\"Mary\", \"date\":\"06-11-20\", \"type\":\"Egging a policeman\", \"lng\":9.789, \"lat\":36.756}" -H Content-Type:application/json "http://127.0.0.1:5000/crimes

@app.route('/crimes', methods=['POST'])
def create():

    if not request.json:
        abort(400)

    crime = {
        "User": request.json["User"],
        "date": request.json["date"],
        "type": request.json["type"],
        "lng": request.json["lng"],
        "lat": request.json["lat"],
    }

    return jsonify(crimeDOA.create(crime))

 
# Update
# curl -X PUT -d "{\"User\":\"Mary\", \"date\":\"06-11-20\", \"type\":\"Egging a policeman\", \"lng\":9.789, \"lat\":36.756}" -H Content-Type:application/json "http://127.0.0.1:5000/crimes/1

@app.route('/crimes/<int:id>', methods=['PUT'])
def update(id):
    foundCrime=crimeDOA.findByID(id)

    if foundCrime == {}:
        return jsonify({}), 404
    
    currentCrime = foundCrime

    if 'User' in request.json:
        currentCrime["User"] = request.json['User']  
    if 'date' in request.json:
        currentCrime["date"] = request.json['date']
    if 'type' in request.json:
        currentCrime["type"] = request.json['type']
    if 'lng' in request.json:
        currentCrime["lng"] = request.json['lng']
    if 'lat' in request.json:
        currentCrime["lat"] = request.json['lat']
    
    crimeDOA.update(currentCrime)    
    return jsonify(currentCrime)

# Delete
# curl -X DELETE http://127.0.0.1:5000/crimes/4

@app.route('/crimes/<int:id>', methods=['DELETE'])
def delete(id):

    return jsonify(crimeDOA.delete(id))

# curl http://127.0.0.1:5000/twitter
@app.route('/twitter')
def twitter_call():
    return jsonify(twitter('crime ireland',15))





if __name__ == "__main__":
    app.run(debug=True)