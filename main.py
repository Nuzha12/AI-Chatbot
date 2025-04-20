from openai import OpenAI
import os

#implemented an AI chatbot using openrouter
api_key = os.getenv("API_KEY")

if not api_key:
    raise ValueError ("Api Key not found")

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key= api_key
)

chat_history = []

personas = {
    "default": "You are a helpful AI assistant",
    "sarcastic": "You are a sarcastic AI who gives witty and mocking respones",
    "poet" : "You are a poetic AI that respondes in rhymes and verses"
}



print ("choose a persona : (default / sarcastic / poet)")

user_persona_input = input("Enter Persona :").strip().lower()


chat_history.append( {
        "role": "system",
        "content": personas[user_persona_input]
    })


while True:

    user_input = input("Enter your prompt: ")

    if user_input == 'clear':
        chat_history = []
        chat_history.append ({"role": "system","content": personas[user_persona_input] })

        print("Chat history cleared ")
        continue

    chat_history.append(
        
        {
        "role": "user",
        "content": user_input
    }
    )

    

   
          
    if user_input == "exit":
        break
    
    completion = client.chat.completions.create(
    
    model="deepseek/deepseek-r1-zero:free",
    messages=chat_history
  
    )    
    response = completion.choices[0].message.content 
    print(response)

    chat_history.append(
        
        {
            "role": "user",
        "content": response
        }      
    )
