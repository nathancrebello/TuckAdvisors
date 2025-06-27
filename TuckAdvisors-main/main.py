## Nathan Rebello

from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends
from sqlalchemy.exc import NoResultFound
import db, models
import json

# tables in models
models.Base.metadata.create_all(bind = db.engine)

# init app
app = FastAPI()

# model for post requests
class UpdateRequest(BaseModel):
    text: str

# grabs gptOutout key from JSON
def parse_gpt_output(data: dict) -> str:

    if "gptOutput" not in data:
        raise ValueError("Missing 'gptOutput' key!")
    return data["gptOutput"]

# dependecny to get DB session for each request
def get_db():
    database = db.LocalSession()
    try:
        yield database
    finally:
        database.close()

# load init MD from input.jslon
with open("input.json") as input:
    json_data = json.load(input)
    init_MD = parse_gpt_output(json_data)

# make sure init records exist in DB
def init_records():
    database: Session = db.LocalSession()
    try:
        record = database.query(models.gptOutput).one()
    except NoResultFound:
        record = models.gptOutput(id = 1, content = init_MD)
        database.add(record)
        database.commit()
    finally:
        database.close()
# run record init
init_records()

# GET endpoing which returns current MD string (gptOutptu)
@app.get("/", response_model=str)
def get_gptOutput(database: Session = Depends(get_db)):
    record = database.query(models.gptOutput).first()
    if not record:
        raise HTTPException(status_code=404, detail = "No MD found")
    return record.content

# POST endpoint which appends new text to MD
@app.post("/", response_model=str)
def update_gptOutput(update: UpdateRequest, database: Session = Depends(get_db)):

    record = database.query(models.gptOutput).first()
    if not record:
        raise HTTPException(status_code=404, detail = "No MD found")
    record.content = record.content.rstrip()+" "+update.text.strip()
    database.add(record)
    database.commit()
    return record.content 
