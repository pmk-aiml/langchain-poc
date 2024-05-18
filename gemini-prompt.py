import google.generativeai as genai

#Read the api key from Config file
with open('config.txt', 'r') as file:
    config = {}
    for line in file:
        key, value = line.strip().split('=')
        config[key] = value

#Access the values
api_key = config['GEMINI_API_KEY']

if api_key is not None:
  print(f"API Key found. Configuring the Key ")
  genai.configure(api_key=api_key)
  model = genai.GenerativeModel('gemini-pro')
  response = model.generate_content("Write two line story about elon musk")
  print(response.text)
else:
  print("API Key not found in environment variables")
