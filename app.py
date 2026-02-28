from flask import Flask, render_template,url_for,request,jsonify
from text_sentiment_prediction import *

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict-emotion', methods=['POST'])
def predict_emootion():

    print("entro a predict-emotion")
    print("JSON recibido:", request.json)

    input_text = request.json.get("text")

    print("texto recibido:", input_text)

    if not input_text:
        response = {
            "status": "error",
            "message": "¡Por favor, ingresa algun texto para predecir la emocion"
        }
        return jsonify(response)
    else:
        predicted_emotion,predicted_emotion_img_url = predict(input_text)
        response = {
            "status": "success",
            "data": {
                "predicted_emotion": predicted_emotion,
                "predicted_emotion_img_url": predicted_emotion_img_url
            }
        }
        return jsonify(response)

app.run(debug=True)
