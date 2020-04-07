import json
from flask import abort, request, url_for, current_app as app

from json_storage import db
from json_storage.models import Jsons


@app.route('/')
def index():
    return f'''<p><a href="{url_for("get_all_json")}">Show all JSONs</a></p>
            <p><a href="{url_for("stat")}">Show stats</a></p>
            '''


@app.route('/api/stat')
def stat():
    sql_request = """SELECT n_live_tup,
                        seq_scan + idx_tup_fetch as reading, 
                        n_tup_ins, 
                        n_tup_del 
                    FROM pg_stat_user_tables WHERE relname='jsons'"""

    row = db.engine.execute(sql_request).first()
    result = {'rows':row[0], 'reads':row[1], 'writes':row[2], 'deletes':row[3]}
    print(result)
    return json.dumps(result, indent=4)


@app.route('/api/json', methods=['GET'])
def get_all_json():
    result = {k:json.loads(v.data) for k, v in enumerate(Jsons.query.all())}
    return json.dumps(result, indent=4)


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
