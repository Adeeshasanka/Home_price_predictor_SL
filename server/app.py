from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_town_names')
def get_town_names():
    util.load_saved_artifacts()
    response = jsonify({
        'Towns': util.get_town_names(),
        'districts': util.get_district_names()
    })
    response.headers.add('Access-Control-Allow-Origin', "*")
    return response

@app.route('/predict_house_price', methods=['POST', 'GET'])
def predict_house_price():

    util.load_saved_artifacts()

    sqft = float(request.form['total_sqft'])
    town = request.form['town']
    district = request.form['district']
    bed = request.form['no_bedrooms']
    bath = request.form['no_bathrooms']
    land = request.form['land_perch'] 

    response = jsonify({
        'estimated_price': util.get_estimated_price(bed,bath,land,sqft,town,district)
    })

    response.headers.add('Access-Control-Allow-Origin', "*")
    return response


if __name__=='__main__':
    print("Starting python flask app for Home price predictor...")
    app.run(debug=True)