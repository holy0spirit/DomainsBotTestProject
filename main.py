from tkinter.messagebox import RETRY
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def testAPI():


    return jsonify({"data" : "end-point successful", "status" : "200"})

@app.route('/palindrome', methods=['POST'])
def mPalindrome():
    mString = request.json
    mOriginalText = mString["original-text"]
    mStringLen = len(mOriginalText)
    mTextArray = []
    for s in mOriginalText:
        mStringLen = mStringLen - 1
        mTextArray.append(mOriginalText[mStringLen])

    mSecondaryText = ''.join(mTextArray)

    if mOriginalText == mSecondaryText:
        # print("True, it is a Palindrome Text")
        return jsonify({"message" : "True, it is a Palindrome Text", "original-text" : mOriginalText, "palindrome-text" : mSecondaryText})
    else:
        # print("False, it is not a Palindrome Text")
        return jsonify({"message" : "False, it is not a Palindrome Text", "original-text" : mOriginalText, "palindrome-text" : mSecondaryText})
    
    return '200'



