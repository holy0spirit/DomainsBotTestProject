from tkinter.messagebox import RETRY
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def testAPI():
    if request.method == 'GET':
        try:
            return jsonify({"data" : "end-point successful", "status" : "200"})
        except:
            return jsonify({"status" : "503", "message" : "App Crash"})
    else:
        return jsonify({"status" : "405", "message" : "Method Not Allowed"})


@app.route('/palindrome', methods=['GET', 'POST'])
def mPalindrome():
    if request.method == 'POST':
        try:
            mString = request.json
            mOriginalText = mString["text"]
            mStringLen = len(mOriginalText)
            mTextArray = []
            for s in mOriginalText:
                mStringLen = mStringLen - 1
                mTextArray.append(mOriginalText[mStringLen])

            mSecondaryText = ''.join(mTextArray)

            if mOriginalText == mSecondaryText:
                # print("True, it is a Palindrome Text")
                return jsonify({"status" : "200", "message" : "True, it is a Palindrome Text", "original-text" : mOriginalText, "palindrome-text" : mSecondaryText})
            else:
                # print("False, it is not a Palindrome Text")
                return jsonify({"status" : "200", "message" : "False, it is not a Palindrome Text", "original-text" : mOriginalText, "palindrome-text" : mSecondaryText})   
        except:
            return jsonify({"status" : "503", "message" : "App Crash"})
    else:
        return jsonify({"status" : "405", "message" : "Method Not Allowed"})


@app.route('/lenghty', methods=['GET', 'POST'])
def mLenghty():
    if request.method == 'POST':
        try:
            mS = request.json
            mString = mS["text"]
            mSelected = []

            for s in mString:
                if s not in mSelected:
                    mSelected.append(s)
            
            mLenght = len(mSelected)

            return jsonify({"status" : "200", "lenght" : mLenght, "sub-string" : mString, "character" : ''.join(mSelected)})
        except:
            return jsonify({"status" : "503", "message" : "App Crash"})
    else:
        return jsonify({"status" : "405", "message" : "Method Not Allowed"})
