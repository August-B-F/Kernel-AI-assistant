from components.Constants import *

def send_text(OPENAI_API_KEY, text, engine, message_type):
    if AI_mode == "Free": 
        message_type = ""
        
    if engine == "gpt3":
        openai.api_key = OPENAI_API_KEY
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                    {"role": "system", "content": "Answer as short as possible. But still so that the user understands."},
                    {"role": "user", "content": f"{text}"},
                ],
            temperature=0.2,
            max_tokens=1000,
        )
    
    else: 
        openai.api_key = OPENAI_API_KEY
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                    {"role": "system", "content": ""},
                    {"role": "user", "content": f"{text}"},
                ],
            temperature=0.2,
            max_tokens=4000,
        )

    return response.choices[0].message.content

#https://toolbaz.com/writer/ai-text-generator
#https://www.copy.ai/tools
#https://www.phind.com/

def webscraping(text):
    pass