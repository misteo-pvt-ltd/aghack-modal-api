from flask import Flask, request, jsonify
from inference import predict
import time
import ssl

app = Flask(__name__)
context = ssl.SSLContext()
context.load_cert_chain('/etc/letsencrypt/live/dev.misteo.co/fullchain.pem', '/etc/letsencrypt/live/dev.misteo.co/privkey.pem')

@app.route("/processimg", methods=[ "GET",'POST'])
def uploadImage():
    isthisFile=request.files.get('file')
    print(isthisFile)
    print(isthisFile.filename)
    isthisFile.save("./uploaded_files/"+isthisFile.filename)
    prediction=predict("./uploaded_files/"+isthisFile.filename)
    return jsonify({'msg': prediction})


if __name__ == "__main__":
    app.run(host='0.0.0.0',ssl_context=context,port=5002)