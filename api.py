from flask import Flask, request, jsonify, render_template
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

        print(request)
        floats = ["oldpeak", "ca", "thal"]

        
        # Get the data from the form using the 'name' attribute from the HTML input field
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
        
        # You can now use 'user_input_data' in your Python code (e.g., print it, save to a database, etc.)
        predicted = loaded_model.predict(df)
        
        # Return a confirmation message or another template
        return render_template('index.html', answer=predicted[0])
    

if __name__ == "__main__":
    app.run(port=8080, debug=True)