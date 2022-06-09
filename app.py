from flask import Flask, request, jsonify, Response
import json
import db_helpers


app = Flask(__name__)

@app.route('/')
def homepage():
    print(request)
    return "Hello World people"



# Let's create a new request in just a json format which is easier, using jsonify

@app.get('/api/animals')
def animals_get():
    params = request.args
    print("Arguments for the GET"+ str(params))
    animal_id = params.get('id')
    print(animal_id)
    if animal_id:
        query_result = db_helpers.run_query("SELECT id, animal_name from animals WHERE id=?",[animal_id])
    else:
        query_result = db_helpers.run_query("SELECT id, animal_name from animals ORDER BY id ASC")
    animals_list = []
    for animal in query_result:
        animals_list.append(animal[1])
    resp = {"Animals" : animals_list}
    return jsonify(resp), 200


@app.post('/api/animals')
def animal_post():
    animal_data = request.json
    print(animal_data)
    if not animal_data.get('animal_name'):
        return jsonify("Missing required field: animal name"), 422
    for animal in animal_data:
        if animal_data.get('animal_name') == animal[0]:
            return jsonify("Animal already exists")
    db_helpers.run_query("INSERT INTO animals (animal_name) VALUES(?)", 
                        [animal_data.get('animal_name')])
    # Some database operations that create the user
    # More DB operations that generate a login token
    
    # return Response(json.dumps(login_dictionary, default=str), mimetype="application/json", status=201)
    # Above and below are equivalent
    return jsonify("Thanks, the animal was added to the database!")

@app.post('/api/animals')
def animal_patch():
    params = request.args
    print("Arguments for the GET"+ str(params))
    animal_id = params.get('id')
    animals_name = params.get('animal_name')
    print(animal_id)
    if animal_id:
        db_helpers.run_query("UPDATE animals SET animal_name WHERE animal_name=?",[animals_name])
        if not animals_name:
            return jsonify("Missing required field: animal name"), 422
        else:
            return jsonify("Animal has been updated")
    else:
        return jsonify("That animal doesn't exist.")
    
# @app.post('/api/animals')
# def animal_delete():
#     params = request.args
#     print("Arguments for the GET"+ str(params))
#     animal_id = params.get('id')
#     animals_name = params.get('animal_name')
#     print(animal_id)
#     if animal_id:
#         db_helpers.run_query("UPDATE animals SET animal_name WHERE ")
#         if not animals_name:
#             return jsonify("Missing required field: animal name"), 422
#         else:
#             return jsonify("Animal has been updated")
#     else:
#         return jsonify("That animal doesn't exist.")