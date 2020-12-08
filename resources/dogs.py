import models
#https://git.generalassemb.ly/prudential-0921/flask-intro-get-post#setting-up-our-controller-aka-a-resource
#https://git.generalassemb.ly/prudential-0921/flask-edit-delete-put-dogs-app
#Blueprint module: setup Routes(Express)
from flask import Blueprint, jsonify, request
#peewee,http://docs.peewee-orm.com/en/latest/peewee/playhouse.html
from playhouse.shortcuts import model_to_dict


# first argument is blueprints name
# second argument is it's import_name
dog = Blueprint('dogs', 'dog')
#set up the GET and POST route
@dog.route('/', methods=["GET"])
def get_all_dogs():
    ## find the dogs and change each one to a dictionary into a new array
    try:
        #list comprehension python[]
        dogs = [model_to_dict(dog) for dog in models.Dog.select()]
        print(dogs)#like console.log
        return jsonify(data=dogs, status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "Error getting the resources"})

#POST ROUTE
@dog.route('/', methods=["POST"])
def create_dogs():
    ## see request payload anagolous to req.body in express
    payload = request.get_json()
    print(type(payload), 'payload')
    dog = models.Dog.create(**payload)
    ## see the object
    print(dog.__dict__)
    ## Look at all the methods
    print(dir(dog))
    # Change the model to a dict
    print(model_to_dict(dog), 'model to dict')
    dog_dict = model_to_dict(dog)
    return jsonify(data=dog_dict, status={"code": 201, "message": "Success"})

#SHOW ROUTE
@dog.route('/<id>', methods=["GET"])
def get_one_dog(id):
    print(id, 'reserved word?')
    dog = models.Dog.get_by_id(id)
    print(dog.__dict__)
    return jsonify(data=model_to_dict(dog), status={"code": 200, "message": "Success"})

#UPDATE ROUTE
@dog.route('/<id>', methods=["PUT"])
def update_dog(id):
    payload = request.get_json()
    #** is like ... spreadoperation
    #dog = models.Dog.update(name=payload['owner'], owner=payload["owner"], breed=payload["breed"]).where(models.Dog.id==id)
    #where method from peewee very SQL like
    query = models.Dog.update(**payload).where(models.Dog.id==id)
    #call it to excute
    query.execute()
    return jsonify(data=model_to_dict(models.Dog.get_by_id(id)), status={"code": 200, "message": "resource updated successfully"})

#DELETE ROUTE
@dog.route('/<id>', methods=["Delete"])
def delete_dog(id):
    query = models.Dog.delete().where(models.Dog.id==id)
    query.execute()
    return jsonify(data='resource successfully deleted', status={"code": 200, "message": "resource deleted successfully"})