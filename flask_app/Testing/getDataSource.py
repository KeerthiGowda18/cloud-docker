from app import app
from app.dataAccess.mongoData import mongoData
from tools import JSONEncoder

from flask import abort


@app.route('/dataSource/<string:id>')
def get_data_source(id):

    db = mongoData(app)
    source = db.get_one(id)
    return JSONEncoder.JSONEncoder().encode(source)