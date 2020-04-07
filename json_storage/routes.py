import json
from flask import abort, request, url_for, current_app as app

from json_storage import db
from json_storage.models import Jsons


@app.route('/')
def index():
    return f'<p><a href="{url_for("get_all_json")}">Show all JSONs</a></p>'


@app.route('/api/json', methods=['GET'])
def get_all_json():
    result = '\n'.join((f'{x.id}: {x.data}' for x in Jsons.query.all()))
    return result


@app.route('/api/json/<id>', methods=['GET'])
def get_json(id):
    item = Jsons.query.get(id)
    if item is not None:
        return f'{item.data}'
    else:
        abort(404)


@app.route('/api/json', methods=['POST'])
def post_json():
    if request.is_json:
        new_jsons = Jsons(data=json.dumps(request.get_json()))
        db.session.add(new_jsons)
        db.session.commit()
        return f"{dict(id=new_jsons.id)}"
    else:
        abort(400)


@app.route('/api/json/<int:id>', methods=['DELETE'])
def del_json(id):
    item = Jsons.query.get(id)
    if item is not None:
        db.session.delete(item)
        db.session.commit()
        return 'ok'
    else:
        abort(404)
