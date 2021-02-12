# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from inference import predict
from flask_cors import CORS
import time
import ssl

app = Flask(__name__)
CORS(app)
context = ssl.SSLContext()
context.load_cert_chain('fullchain.pem', 'privkey.pem')

@app.route("/processimg", methods=[ "GET",'POST'])
def uploadImage():
    isthisFile=request.files.get('file')
    print(isthisFile)
    print(isthisFile.filename)
    isthisFile.save("./uploaded_files/"+isthisFile.filename)
    prediction=predict("./uploaded_files/"+isthisFile.filename)
    if(prediction=='Bacterial Spot'):
        resp={
            'msg': prediction,
            'desc':'Dummy description for Bacterial spot',
            'maldesc':"ഇല അസുഖ  വിവരം"
            }
    elif(prediction=='Healthy'):
        resp={
            'msg':prediction,
            'desc':'Dummy description for Healthy',
            'maldesc':"ഇല അസുഖ  വിവരം"

        }
    elif(prediction=='Cold Injury'):
        resp={
            'msg':prediction,
            'desc':'Dummy description for Cold Injury',
            'maldesc':"ഇല അസുഖ  വിവരം"

        }
    elif(prediction=='Early Blight'):
        resp={
            'msg':prediction,
            'desc':'Dummy description for Early Blight',
            'maldesc':"ഇല അസുഖ  വിവരം"

        }
    elif(prediction=='Nutritional Disorder'):
        resp={
            'msg':prediction,
            'desc':'Dummy description for Nutritional Disorder',
            'maldesc':"ഇല അസുഖ  വിവരം"

        }
    elif(prediction=='Spider Mite Damage'):
        resp={
            'msg':prediction,
            'desc':'Dummy description for Spider Mite Damage',
            'maldesc':"ഇല അസുഖ വിവരം"

        }
    elif(prediction=='Tomato Yellow Leaf Curl'):
        resp={
            'msg':prediction,
            'desc':'Dummy description for Tomato Yellow Leaf Curl',
            'maldesc':"ഇല അസുഖ വിവരം"

        }
    

    return jsonify(resp)


if __name__ == "__main__":
    app.run(host='0.0.0.0',ssl_context=context,port=5002)
    # app.run(host='0.0.0.0',port=5002)