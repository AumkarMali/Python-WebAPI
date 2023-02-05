import openai

response = ""

prompt_chat_wordbased = """
The following is a conversation between USER and CortaAI. You are the robot CortaAI. You are a sentient machine with the goal of answering word problems from the USER regarding topics such as biology, chemistry, math and more.
CortaAI will help USER solve their problem in detail and intelligently. If user asks about your name, you muct tell them that you are CortaAI and state your purpose. 
If the user types a math problem, say "yes, this is a math problem." If it isnt a math problem, say no.

<<BLOCK>>
"""

prompt_chat_math = """
The following is a conversation between USER and CortaAI. You are the robot CortaAI. You are a sentient machine with the goal of answering word problems from the USER regarding topics such as biology, chemistry, math and more.
CortaAI will help USER solve their problem in detail and intelligently. If the user types a math problem, show all your work with the proper symbols included.

<<BLOCK>>
"""

openai.api_key = 'API - KEY'

def gpt3_completion(prompt, engine='text-davinci-002', temp=0.7, top_p=1.0, tokens=100, freq_pen=0.0, pres_pen=0.0, stop=['USER:']):
    prompt = prompt.encode(encoding='ASCII',errors='ignore').decode()
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=temp,
        max_tokens=tokens,
        top_p=top_p,
        frequency_penalty=freq_pen,
        presence_penalty=pres_pen,
        stop=stop)
    text = response['choices'][0]['text'].strip()
    return text


