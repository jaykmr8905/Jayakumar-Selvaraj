 
##from google import genai
##
##robo = genai.Client(api_key="AQ.Ab8RN6Kgb151bGb2TZNL60262ALtZ2wDtHjy4w7Y8SvgYkJb7Q")
##
##response= robo.models.generate_content(
##    model = "gemini-2.5-flash",
##    contents = "what is Ai give me the 10 of words."
##        )
##print(response.text)





##from google import genai
##
### Create client
##robo = genai.Client(api_key="AQ.Ab8RN6Kgb151bGb2TZNL60262ALtZ2wDtHjy4w7Y8SvgYkJb7Q")
##
### 👇 Take input from user
##user_prompt = input("Enter your question: ")
##
### Generate response using user input
##response = robo.models.generate_content(
##    model="gemini-2.5-flash",
##    contents=user_prompt
##)
##
### Print result
##print("\nResponse:")
##print(response.text)




 
##from google import genai
##
##robo = genai.Client(api_key="AQ.Ab8RN6Kgb151bGb2TZNL60262ALtZ2wDtHjy4w7Y8SvgYkJb7Q")
##
##mychat = robo.chats.create(model="gemini-flash-lite-latest")
##
##coms= ".you are an expert python developer.\
##Answer only questions related to python programming.\
##For any non-python question. reply exactly:\
##Please ask a Python-related question.\
##Do not answer questions outside the python domain."
##
##while True:
##    question = input ("How can i help you:")
##    question = question + coms
##    response = mychat.send_message(question)
##    print(response.text)




##from google import genai
##from google.genai import types
##robo = genai.Client(api_key="AQ.Ab8RN6Kgb151bGb2TZNL60262ALtZ2wDtHjy4w7Y8SvgYkJb7Q")
##
##mychat = robo.chats.create(model="gemini-flash-lite-latest")
##
##config = types.Generatecontenetconfig(
##    System_instruction = ".You are an expert python developer.\
##Answer only questions related to python programming.\
##For any non-python question. reply exactly:\
##Please ask a Python-related question.\
##Do not answer questions outside the python domain."
##    )
##
##
##while True:
##    question = input ("Ask any: ")
##    response = mychat.send_message(question)
##    print(response.text)


##from google import genai
## 
##robo = genai.Client(api_key="AQ.Ab8RN6Kgb151bGb2TZNL60262ALtZ2wDtHjy4w7Y8SvgYkJb7Q")
## 
##mychat = robo.chats.create(model="gemini-flash-lite-latest")
## 
##coms = "You are an expert of Python developer.\for any non-python question. reply exactly:\
##Please ask a Python-related question.\
##Do not answer questions outside the python domin."
## 
## 
##while True:
##        question = input ("How can i help you: ")
##        question = question + coms
##        response = mychat.send_message(question)
##        print(response.text)


from google import genai
 
robo = genai.Client(api_key="AQ.Ab8RN6Kgb151bGb2TZNL60262ALtZ2wDtHjy4w7Y8SvgYkJb7Q")
 
mychat = robo.chats.create(model="gemini-flash-lite-latest")
 
coms = "You are an expert of Internet information."
 
 
while True:
        question = input ("How can i help you: ")
        question = question + coms
        response = mychat.send_message(question)
        print(response.text)

























 
 

