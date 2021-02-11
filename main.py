from flask import Flask, request, jsonify
from inference import predict
import time

app = Flask(__name__)

@app.route("/im_size", methods=[ "GET",'POST'])
def uploadImage():
    isthisFile=request.files.get('file')
    print(isthisFile)
    print(isthisFile.filename)
    isthisFile.save("./uploaded_files/"+isthisFile.filename)
    prediction=predict("./uploaded_files/"+isthisFile.filename)
    return jsonify({'msg': prediction})


if __name__ == "__main__":
    app.run(debug=True)