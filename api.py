from flask import Flask, request, jsonify, render_template
app = Flask(__name__)


@app.route('/')
def index():
    # Renders the HTML file in the 'templates' folder
    return render_template('index.html')

# Route to handle the form submission
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':

        print(request)
        # Get the data from the form using the 'name' attribute from the HTML input field
        user_input_data = "HElLop"
        
        # You can now use 'user_input_data' in your Python code (e.g., print it, save to a database, etc.)
        print("Data received from form:", user_input_data)
        
        # Return a confirmation message or another template
        return render_template('index.html', answer=user_input_data)
    

if __name__ == "__main__":
    app.run(debug=True)