from flask import Flask, request
import requests
from transformers import AutoTokenizer
model_repo = "google/flan-t5-xxl"
tk = AutoTokenizer.from_pretrained(model_repo)
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-xxl"
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
    text = request.form.get('text')
    
    output = query({
    "inputs": text,"parameters":{"max_new_tokens":tk.model_max_length}
    })

    print(output[0]["generated_text"])
    return render_template('index.html', echo=output[0]["generated_text"])

if __name__ == '__main__':
    app.run(debug=True)