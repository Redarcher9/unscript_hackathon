from flask import Flask, flash, request, redirect, url_for,send_from_directory,render_template
from flask_restplus import fields, Api, Resource
from flask_restplus import reqparse
from chatbot import userinput
import json
app = Flask(__name__)
api = Api(app)
raw_text = api.model('Rawtext', {'Input1' : fields.String('Your Input.') })

@api.route('/Chatbot')
class Preprocessor(Resource):
    @api.expect(raw_text)
    def post(self):
        #data received from post request
        input_text = api.payload
        #dumps the json object into an element
        json_str = json.dumps(input_text)
        #load the json to a string
        resp = json.loads(json_str)
        #Stopwords elimination begins here
        doc11=userinput(resp['Input1'].lower())
        return {'reply' : doc11}



if __name__ == "__main__":
    app.run(port=4555,debug=True)
