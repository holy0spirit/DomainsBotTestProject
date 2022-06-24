from tkinter.messagebox import RETRY
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def testAPI():


    return jsonify({"data" : "end-point successful", "status" : "200"})

