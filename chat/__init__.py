import azure.functions as func
from openai import OpenAI
import os
import json

OPENAI_API_KEY = os.environ.get("PROJ-OPENAI-API-KEY")
client = OpenAI(api_key=OPENAI_API_KEY)
model = "gpt-3.5-turbo"

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="chat", methods=[func.HttpMethod.POST])
def chat(req: func.HttpRequest) -> func.HttpResponse:
    stream = client.chat.completions.create(
        model=model,
        messages=req.get_json()['messages'],
    )
    return func.HttpResponse(stream.choices[0].message.content)