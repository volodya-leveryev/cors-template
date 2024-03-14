import json

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api/persons/')
def persons():
    with open('persons.json', encoding='utf-8') as f:
        persons = json.load(f)
    # TODO: добавить разбивку по страницам
    res = jsonify({
        'data': persons,
    })
    # TODO: добавить заголовок для CORS
    return res


app.run()