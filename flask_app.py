from flask import Flask, request, jsonify
from database import *
import openai
app = Flask(__name__)

def isMathProblem(user_input_text):
    conversation = list()
    conversation.append('USER: %s' % user_input_text + " Is this a math problem? Answer with yes or no.")
    text_block = '\n'.join(conversation)
    prompt = prompt_chat_wordbased.replace('<<BLOCK>>', text_block)
    prompt = prompt + '\nCortana:'
    mathProblemTrue = gpt3_completion(prompt)
    conversation.append('Cortana: %s' % mathProblemTrue)

    return mathProblemTrue

@app.route('/get/', methods=['GET'])
def respond():
    # Retrieve the name from the url parameter /get/?text=
    user_input_text = request.args.get("text", None)

    resp = ""
    conversation = list()

    if user_input_text != "":

        #Checks if prompt is math problem
        checkProb = isMathProblem(user_input_text)

        if "yes" in checkProb.lower():
            conversation.append('USER: %s' % user_input_text)
            text_block = ''.join(conversation)
            prompt = prompt_chat_math.replace('<<BLOCK>>', text_block)
            prompt = prompt + 'CortaAI:'
            resp = gpt3_completion(prompt)
            conversation.append('CortaAI: %s' % resp)
        else:
            conversation.append('USER: %s' % user_input_text)
            text_block = ''.join(conversation)
            prompt = prompt_chat_wordbased.replace('<<BLOCK>>', text_block)
            prompt = prompt + 'CortaAI:'
            resp = gpt3_completion(prompt)
            conversation.append('CortaAI: %s' % resp)


    response = resp

    # Return the response in json format
    return jsonify(response)


@app.route('/post/', methods=['POST'])
def post_something():
    pass


@app.route('/')
def index():
    # A welcome message to test our server
    return "Welcome, to ---BRAIN---"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)