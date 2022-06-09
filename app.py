from flask import Flask, request, jsonify, render_template
import json
from db_helpers import run_query


app = Flask(__name__)

@app.route('/')
def new_animal():
    return render_template('index.html')


# @app.route('/')
# def new_animal_form():
#     text = request.form['text']
#     return text
# This request is a general approach and not only for json
# @app.route('/users')
# def users():
#     print(request)
#     login_dictionary = {"loginToken" : "abc123"}
#     user_list = [
#         {"id" : 1, "name" : "John"},
#         {"id" : 2, "name" : "Jill"}
#     ]
#     print(json.dumps(login_dictionary))
#     return Response(json.dumps(user_list, default=str), mimetype="application/json", status=200)

# These are api calls
# Just specify a call to an API endpoint in these functions
# @app.post('/users')
# def users_post():
#     login_dictionary = {"loginToken" : "abc123"}
#     return Response(json.dumps(login_dictionary, default=str), mimetype="application/json", status=200)

# @app.get('/users')
# def users_get():
#     user_list = [
#         {"id" : 1, "name" : "John"},
#         {"id" : 2, "name" : "Jill"}
#     ]
#     return Response(json.dumps(user_list, default=str), mimetype="application/json", status=200)


# Let's create a new request in just a json format which is easier, using jsonify
animals = ['cat', 'dog', 'bird', 'amphibian', 'fish']

@app.route('/api/animals')
def animals_get():
    query_result = run_query("SELECT animal_name FROM animals")
    animals_list = []
    for animal in query_result:
        animals_list.append(animal[0])
    resp = {"Animals" : animals_list}
    return jsonify(resp), 200


@app.post('/api/animals')
def new_animal_post(new_animal):
    animal_data = request.json
    run_query("INSERT INTO animals(animal_name) VALUES (?)", [new_animal])
    return "Successfully added"

# @app.update('/api/animals')
# def animal_update():
#     animals = run_query("SELECT animal_name FROM animals")
#     for animal in animals:
#         if new_animal == animal:
#             return jsonify("That animal already exists")
#         else:
#             run_query("INSERT INTO animals(animal_name) VALUES (?)", [new_animal])
#             return jsonify("{} was successfully added to the database".format[new_animal])
        
# @app.delete('/api/animals')
# def animal_delete():
#     animals = run_query("SELECT animal_name FROM animals")
#     for animal in animals:
#         if new_animal == animal:
#             return jsonify("That animal already exists")
#         else:
#             run_query("INSERT INTO animals(animal_name) VALUES (?)", [new_animal])
#             return jsonify("{} was successfully added to the database".format[new_animal])