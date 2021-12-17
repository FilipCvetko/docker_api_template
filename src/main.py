# DO NOT DELETE THIS FILE!

# This is the master file which will be called by uvicorn manager.
# It has the topmost directory structure, so it can call all lower subdirectory scripts and functions

from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/help")
def get_help():
    return "Help on the way! Nothing written so far though. :("


# Below is a sample endpoint for classification
# Note: There can be any number of endpoints available, with any HTTP request type (GET, POST, PUT, DELETE)

# Let's suppose we are creating a text classification model, with string as input and list of strings as output
# It is wise to create request and response models in advance.
# typing library helps with creating typing hints with NO code functionality alterations
class Request(BaseModel):
    query: str
class Response(BaseModel):
    labels: List[str] # Is this okay?

@app.post("/classify", response_model=Response)
def classify(request: Request):
    query = request.query

    # Perform logic on the string within the function.
    labels = [query] * 5 # Spam output for example

    # Output the response as specified in the response model
    return Response(labels=labels)
