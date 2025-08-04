from fastapi import FastAPI

app=FastAPI()

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
notes_data=[{"ID":1,"title":"First note", "Content":"The content of the first note is like this showing.","Created_at": "timestamp","updated_at": "timestamp", "Tags":"first","Status":"unpin"
},{"ID":1,"title":"Second note", "Content":"Wandering on this path without goal.","Created_at": "timestamp","updated_at": "timestamp", "Tags":"first","Status":"unpin"}]




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
