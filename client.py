from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)