# Nathan Rebello

## This project uses a FastAPI-based REST API to serve/update a given markdown for clients.

## Requirements

- Python 3.7+

## Setup

 1. clone the repo with: 
 ```bash git clone <url>``` and then ```cd TuckAdvisors-main/TuckAdvisors-main ```

 2. create virtual env:
 ```python -m venv venv``` and then ```source venv/bin/activate``` (do this in bash)

 3. Install deps:
 ```pip install fastapi uvicorn sqlalchemy pydantic ``` (do this in bash)

 ## Running API

 Start the server w/ uvicorn by doing: ```uvicorn main:app --reload ``` (http://127.0.0.1:8000)

 ## Endpoints

* To run GET: ```curl http://127.0.0.1:8000/```
* To run POST: ```curl -X POST http://127.0.0.1:8000/ -H "Content-Type: application/json" \-d '{"text": "some updated text!"}'``` 