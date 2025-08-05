from fastapi import FastAPI, HTTPException,status
from typing import Optional,List
from pydantic import BaseModel,Field
from datetime import datetime



#initialize the fastapi
app=FastAPI()

class note(BaseModel):
    ID: Optional[int] = 1
    title: str
    Content: str
    Created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = None
    Tags: Optional[List[str]] = None
    Status: bool = Field(default="False")

"""
ID (unique identifier)

Title

Content

Created_at timestamp

Updated_at timestamp

Tags (optional)

User ID (if multi-user)

Status (optional, e.g., archived)

Priority (optional)
"""

# The raw data 
notes_data=[{"ID":1,"title":"Idea burst","Content":"Breathe, focus, move.","Created_at":"2025-08-04T01:09:00Z","updated_at":"2025-08-04T02:23:00Z","Tags":"focus","Status":"unpin"},{"ID":2,"title":"Mindful moment","Content":"Doing less, but better.","Created_at":"2025-08-05T21:58:00Z","updated_at":"2025-08-05T23:48:00Z","Tags":"growth","Status":"unpin"},{"ID":3,"title":"Idea burst","Content":"Creativity often hides in silence.","Created_at":"2025-08-02T16:24:00Z","updated_at":"2025-08-02T17:34:00Z","Tags":"reflection","Status":"pin"},{"ID":4,"title":"Focus journal","Content":"Not all those who wander are lost.","Created_at":"2025-08-04T16:55:00Z","updated_at":"2025-08-04T18:05:00Z","Tags":"journal","Status":"pin"},{"ID":5,"title":"Mindful moment","Content":"Breathe, focus, move.","Created_at":"2025-08-03T10:47:00Z","updated_at":"2025-08-03T11:57:00Z","Tags":"clarity","Status":"pin"},{"ID":6,"title":"Note on clarity","Content":"Doing less, but better.","Created_at":"2025-08-06T08:27:00Z","updated_at":"2025-08-06T09:57:00Z","Tags":"reflection","Status":"pin"},{"ID":7,"title":"Deep thoughts","Content":"Every step forward counts.","Created_at":"2025-08-06T00:40:00Z","updated_at":"2025-08-06T01:53:00Z","Tags":"clarity","Status":"pin"},{"ID":8,"title":"Quick reminder","Content":"The mind recharges in silence.","Created_at":"2025-08-05T11:40:00Z","updated_at":"2025-08-05T12:10:00Z","Tags":"mindset","Status":"unpin"},{"ID":9,"title":"Mindful moment","Content":"Time spent in reflection is never wasted.","Created_at":"2025-08-01T18:45:00Z","updated_at":"2025-08-01T20:38:00Z","Tags":"thoughts","Status":"pin"},{"ID":10,"title":"Evening insight","Content":"Creativity often hides in silence.","Created_at":"2025-08-03T21:06:00Z","updated_at":"2025-08-03T22:06:00Z","Tags":"focus","Status":"unpin"},{"ID":11,"title":"Note on clarity","Content":"Doing less, but better.","Created_at":"2025-08-04T12:50:00Z","updated_at":"2025-08-04T14:00:00Z","Tags":"clarity","Status":"pin"},{"ID":12,"title":"Deep thoughts","Content":"The mind recharges in silence.","Created_at":"2025-08-04T17:42:00Z","updated_at":"2025-08-04T19:02:00Z","Tags":"thoughts","Status":"pin"},{"ID":13,"title":"Evening insight","Content":"Every step forward counts.","Created_at":"2025-08-02T15:20:00Z","updated_at":"2025-08-02T15:59:00Z","Tags":"reflection","Status":"unpin"},{"ID":14,"title":"Late-night thoughts","Content":"Breathe, focus, move.","Created_at":"2025-08-05T19:16:00Z","updated_at":"2025-08-05T20:40:00Z","Tags":"motivation","Status":"unpin"},{"ID":15,"title":"Focus journal","Content":"Doing less, but better.","Created_at":"2025-08-06T02:14:00Z","updated_at":"2025-08-06T03:26:00Z","Tags":"journal","Status":"pin"},{"ID":16,"title":"Note on clarity","Content":"Growth isn't always visible, but it's happening.","Created_at":"2025-08-02T19:13:00Z","updated_at":"2025-08-02T20:33:00Z","Tags":"growth","Status":"unpin"},{"ID":17,"title":"Morning motivation","Content":"Focus on the essential and let go of the rest.","Created_at":"2025-08-03T07:09:00Z","updated_at":"2025-08-03T07:29:00Z","Tags":"motivation","Status":"unpin"},{"ID":18,"title":"Late-night thoughts","Content":"Time spent in reflection is never wasted.","Created_at":"2025-08-04T05:25:00Z","updated_at":"2025-08-04T06:14:00Z","Tags":"thoughts","Status":"pin"},{"ID":19,"title":"Morning motivation","Content":"Focus on the essential and let go of the rest.","Created_at":"2025-08-06T06:41:00Z","updated_at":"2025-08-06T07:12:00Z","Tags":"focus","Status":"unpin"},{"ID":20,"title":"Evening insight","Content":"The mind recharges in silence.","Created_at":"2025-08-02T13:19:00Z","updated_at":"2025-08-02T14:13:00Z","Tags":"mindset","Status":"pin"}]





@app.get("/")
def root():
    return "Hello world"


@app.get("/notes-list")
async def notes_list():
    data=[
    {
        "ID": note["ID"],
        "title": note["title"],
        "Content": note["Content"],
        "updated_at": note["updated_at"],
        "Status": note["Status"]
    }
    for note in notes_data
]
    return {"data": data}



@app.get("/notes-list/{id}")
async def Singlenote(id: int):
    data=[{"id":note["ID"],"title":note["title"],"Content":note["Content"], "tag": note["Tags"] ,"created_at": note["Created_at"]} for note in notes_data if note["ID"]==id]
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"There is no data with ID: {id}")
    return {"data": data}



@app.post("/notes")
async def create_note(notedata:note):
    notedata.ID+=len(notes_data)
    notes_data.append(notedata.dict())
    return {"data": "Note created successfully"}