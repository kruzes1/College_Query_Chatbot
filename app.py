from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('classes.pkl', 'rb'))


@app.route('/predict',methods=['GET'])
def predict():
	return render_template('chatgui.py')

if __name__ == "__main__":
    app.run(debug=True)