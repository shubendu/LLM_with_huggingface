from flask import Flask, request
import requests
from flask import jsonify

from transformers import AutoTokenizer
# model_repo = "google/flan-t5-xxl"
model_repo = "timdettmers/guanaco-33b-merged"
# tk = AutoTokenizer.from_pretrained(model_repo)
API_URL = f"https://api-inference.huggingface.co/models/{model_repo}"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
    
# print(f"Maximum token limit of {model_repo} is {tk.model_max_length}")

# app = Flask(__name__)

# @app.route('/api/response', methods=['POST'])
# def echo():
#     text = request.json.get('text')
#     output = query({
#     "inputs": text,"parameters":{"max_new_tokens":tk.model_max_length}
#     })
    
#     return {'response': output[0]["generated_text"]}

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/res', methods=['POST'])
def echo():
    text = request.json.get('text')
    print("++++++++++++++++++++++++++++++++++")
    print(type(text))
    print(text)
    
    output = query({
    "inputs": text,"parameters":{"max_new_tokens":250, "return_full_text": False}
    })

    print("++++++++++++++++++++++++++++++++++")
    print(output[0]["generated_text"])
    return render_template('index.html', echo=output[0]["generated_text"])

@app.route('/api/postman', methods=['POST'])
def echo_postman():
    text = request.json.get('text')
    print(text)
    output = query({
    "inputs": text,"parameters":{"max_new_tokens":250,"return_full_text": False}
    })
    #return {'res':text}
    return {'response': output[0]["generated_text"]}

if __name__ == '__main__':
    app.run(debug=True)