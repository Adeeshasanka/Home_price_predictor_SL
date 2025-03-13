from flask import Flask, request, jsonify, render_template
import util

app = Flask(__name__, template_folder = r".\client")

@app.route('/')
def get_town_names():
    util.load_saved_artifacts()
    response = jsonify({
        'Towns': util.get_town_names(),
        'districts': util.get_district_names()
    })

    Towns = util.get_town_names()
    Districts = util.get_district_names()

    response.headers.add('Access-Control-Allow-Origin', "*")
    return render_template("index.html", towns = Towns, districts = Districts)

@app.route('/predict_house_price', methods=['POST', 'GET'])
def predict_house_price():

    util.load_saved_artifacts()
    Towns = util.get_town_names()
    Districts = util.get_district_names()

    sqft = float(request.form['sqftarea'])
    town = request.form['town']
    district = request.form['district']
    bed = request.form['bedroom']
    bath = request.form['bathroom']
    land = request.form['landarea'] 

    response = jsonify({
        'estimated_price': util.get_estimated_price(bed,bath,land,sqft,town,district)
    })

    estimated_price = util.get_estimated_price(bed,bath,land,sqft,town,district)

    response.headers.add('Access-Control-Allow-Origin', "*")
    return render_template("index.html", towns = Towns, districts = Districts, estimated_price = estimated_price)


if __name__=='__main__':
    print("Starting python flask app for Home price predictor...")
    app.run(debug=True)