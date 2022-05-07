from distutils.log import debug
import json
from flask import Flask, request, jsonify
import time
import chatbot

app = Flask(__name__)

@app.route('/bot', methods = ['POST'])


def index():
    #fetching the global response variable to manipulate inside the function
    global response
    #checking the request type we get from the app
    if(request.method == 'POST'):
        request_data = request.data #getting the response data
        request_data = json.loads(request_data.decode('utf-8')) #converting it from json to key value pair
        symptom = request_data['query'] #assigning it to name
        # print(symptom);
        if(request_data['recommendation'] == True):
            recommendation = chatbot.symptomRecommendation(symptom)
            return jsonify({'recommended' : recommendation})
        else:
            res = chatbot.diseaseDetection(symptom)
            disease = res[0]
            remedy = res[1]
            return jsonify({'disease' : disease, 'remedy' : remedy})        
    else:
        return None;

if __name__ =="__main__":
    app.run(debug = True)