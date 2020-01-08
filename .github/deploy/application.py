from flask import Flask, render_template, request, jsonify, flash, url_for, request, redirect
import numpy as np
import pickle as p
import json
# sample deplyment file

app = Flask(__name__)

modelfile = 'model.pickle'
model = p.load(open(modelfile, 'rb'))


@app.route("/predict/", methods=['post','get'])
def makecalc():
    message = 'hey'

    if request.method == 'POST':
        age = request.form.get('age')  # access the data inside
        message=age

        data = [[1, 1, int(age), 1, 1, 100.25]]
        prediction = np.array2string(model.predict(data))
        message=str(prediction)
        print(age)

    return render_template('predict.html', message=message)

@app.route('/api/', methods=['post'])
def makecalc2():
    #modelfile = '.artifacts/model.pickle'
    #model = p.load(open(modelfile, 'rb'))
    #data = [[1, 1, 2, 1, 1, 100.25]]
    data = request.get_json()
    prediction = np.array2string(model.predict(data))

    return jsonify(prediction)

if __name__ == '__main__':
    app.run()
