from flask import Flask, render_template, request, jsonify
import requests
import json
import os
from chat import get_response

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def air_quality():
    air_quality_data = []
    error_message = None

    if request.method == 'POST': 
        city = request.form.get('station').replace(' ', '-') 
        api_key = 'a5b2dedd1fc471b8e8e59ba73350ee50eeea6a6e'  
        api_url = f"https://api.waqi.info/feed/{city}/?token={api_key}"  
        try:
            response = requests.get(api_url) 
            response.raise_for_status()
            data = response.json()  

            if data.get('status') == 'ok' and data['data']:
                aqi_str = data['data'].get('aqi', 'N/A')
                try:
                    aqi = int(aqi_str)
                except ValueError:
                    aqi = 'N/A'
                
                color_class = 'black' if aqi == 'N/A' else (
                    'green' if 0 <= aqi <= 50 else (
                    'yellow' if 51 <= aqi <= 100 else (
                    'orange' if 101 <= aqi <= 150 else (
                    'red' if 151 <= aqi <= 200 else (
                    'purple' if 201 <= 300 else 'maroon')))))
                
                updated_at = data['data'].get('time', {}).get('iso', 'N/A') 
                station_name = data['data'].get('city', {}).get('name', 'Unknown') 
               
                air_quality_data = [{
                    'air_quality': aqi_str,
                    'color_class': color_class,
                    'station_name': station_name,
                    'updated_at': updated_at
                }]

            else:
                error_message = "Não foi possível obter os dados de qualidade do ar para a localização especificada."

        except requests.RequestException as e:
            error_message = f"Não foi possível se conectar à API de qualidade do ar. Erro: {e}"

    return render_template('index.html', air_quality_data=air_quality_data, error_message=error_message)

@app.route("/chat", methods=["GET", "POST"])
def chat():
    response = None
    if request.method == "POST":
        user_input = request.form.get("user_input") 
        response = get_response(user_input)  
    return render_template("index.html", response=response)

@app.route("/predict", methods=["POST"])
def predict():
    text = request.get_json().get("message") 
    response = get_response(text) 
    message = {"answer": response}
    return jsonify(message) 

if __name__ == "__main__":
    app.run(debug=True, port=5000) 