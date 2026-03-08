from flask import Flask, request, render_template
import xgboost as xgb
import pandas as pd
app = Flask(__name__)

loaded_model = xgb.XGBClassifier()
loaded_model.load_model('model')

@app.route('/')
def index():
    # Renders the HTML file in the 'templates' folder
    return render_template('index.html')

# Route to handle the form submission
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        floats = ["oldpeak", "ca", "thal"]

        data = request.form
        data = data.to_dict(flat=False)

        feature_names = data.keys()
        feature_data = {}

        for key in feature_names:
            if key in floats:
                feature_data[key] = [float(data[key][0])]
            else:
                feature_data[key] = [int(data[key][0])]

        df = pd.DataFrame(feature_data)

        predicted = int(loaded_model.predict(df)[0])
        risk = round(float(loaded_model.predict_proba(df)[0][1]) * 100, 1)

        return render_template('index.html', answer=predicted, risk=risk)

if __name__ == "__main__":
    app.run(port=8080, debug=True)