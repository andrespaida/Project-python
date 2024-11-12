from flask import Flask, render_template

# Create the Flask application instance
app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)