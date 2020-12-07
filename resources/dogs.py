import models

from flask import Blueprint, jsonify, request

from playhouse.shortcuts import model_to_dict


# first argument is blueprints name
# second argument is it's import_name
dog = Blueprint('dogs', 'dog')
