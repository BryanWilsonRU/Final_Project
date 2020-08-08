from flask import Flask, request, render_template
# create instance of Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/predict',methods=['POST'])
# def predict():



if __name__ == '__main__':
    app.run(debug=True)	