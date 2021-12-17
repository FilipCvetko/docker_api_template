# DOCKER TEMPLATE FOR APIs

## About
This repository is intended to be cloned whenever you need to set up an API inside of a docker container quickly. We are using FastAPI and uvicorn, all packaged within a docker container, intended to be intercompatible.

All routing is done within ``src/main.py`` file, which can import all the other files within the src folder and below.

## Usage
**Step 1**: Create a Docker image like this:  
``docker build -t <image_name> ``

**Step 2**: Run the Docker image by mapping to port **5000** within the docker container.   
``docker run -d -p 12000:5000 <image_name>``  
This way port 12000 in this case would be visible to the LAN network. Note that in order for the API to be accessible outside the local network, port mapping on your local router is required.

**Step 3**: Now we can experiment sending a cURL requests like this:  
`` curl -X POST -H "Content-Type: application/json" -d '{"query": "test"}' http://0.0.0.0:12000/classify ``

or like this:  
  
``curl -X GET http://0.0.0.0:12000``
