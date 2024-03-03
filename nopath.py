import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

#from google.colab import userdata
GOOGLE_API_KEY="AIzaSyBqWKFRezEgNrOp6jKutaVmSbWZ9CP57-0"

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

print("\nTo help you formulate a practical personal finance plan, we need some preiminary information:\n");
income = float(input("Annual Income in USD: "))
col = float(input("How much does one average meal cost in USD: "))
var = income/col
if(income >= col*600):
    print("our suggested saving level for you is 30% =", income*0.30, "per month")
    response = chat.send_message("Formulate a monthly fianncial plan for this person looking to save 30%, starting by asking me about theirincome to cost of living ratio")
    to_markdown(response.text)
    response = chat.send_message(f"their income is{income}, and the cost of one meal in their region is{col}.")
    to_markdown(response.text)
    print(response.text)

elif(col*600 > income >= col*400):
    print("our suggested saving level for you is 20% =", income*0.20, "per month")
    response = chat.send_message("Formulate a monthly fianncial plan for this person looking to save 20%, starting by asking me about theirincome to cost of living ratio")
    to_markdown(response.text)
    response = chat.send_message(f"their income is{income}, and the cost of one meal in their region is{col}.")
    to_markdown(response.text)
    print(response.text)

elif(col*400 > income >= col*300):
    print("our suggested saving level for you is 15% =", income*0.15, "per month")
    response = chat.send_message("Formulate a monthly fianncial plan for this person looking to save 15%, starting by asking me about theirincome to cost of living ratio")
    to_markdown(response.text)
    response = chat.send_message(f"their income is{income}, and the cost of one meal in their region is{col}.")
    to_markdown(response.text)
    print(response.text)

elif(col*300 > income >= col*200):
    print("our suggested saving level for you is 10% =", income*0.10, "per month")
    response = chat.send_message("Formulate a monthly fianncial plan for this person looking to save 10%, starting by asking me about theirincome to cost of living ratio")
    to_markdown(response.text)
    response = chat.send_message(f"their income is{income}, and the cost of one meal in their region is{col}.")
    to_markdown(response.text)
    print(response.text)

elif(col*200 > income >= col*100):
    print("our suggested saving level for you is 5% =", income*0.05, "per month")
    response = chat.send_message("Formulate a monthly fianncial plan for this person looking to save 5%, starting by asking me about theirincome to cost of living ratio")
    to_markdown(response.text)
    response = chat.send_message(f"their income is{income}, and the cost of one meal in their region is{col}.")
    to_markdown(response.text)
    print(response.text)

else:
    print("our suggested saving level for you is 5% (this will require very stringent financial planning, we suggest finding additional income or moving to lower cost spots in the long term) =", income*0.05, "per month")
    response = chat.send_message("Formulate a monthly fianncial plan for this person looking to save 5%, starting by asking me about theirincome to cost of living ratio")
    to_markdown(response.text)
    response = chat.send_message(f"their income is{income}, and the cost of one meal in their region is{col}.")
    to_markdown(response.text)
    print(response.text)



