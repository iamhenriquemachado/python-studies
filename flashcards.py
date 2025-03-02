from fastapi import FastAPI
from pydantic import BaseModel, Field
import itertools
from typing import ClassVar
import sqlite3
import json

app = FastAPI()


class FlashCardCreate(BaseModel):
    flashcard_id: int = Field(None, description="ID of the flashcard, auto-generated")
    question: str
    answer: str
    category: int

    _id_counter: ClassVar[itertools.count] = itertools.count(
        1
    )  # Class variable with auto-incrementing counter

    @classmethod
    def generate_id(cls) -> int:
        """Retrieves the next ID from the counter."""
        return next(cls._id_counter)

# Create a new flashcard
@app.post("/flashcards/create/")
async def create_flashcard(flashcard_data: FlashCardCreate):
    flashcard_data.flashcard_id = FlashCardCreate.generate_id()

    with sqlite3.connect("YOURDATABASE.bd") as db:
        db_cursor = db.cursor()
        db_cursor.execute(
            """INSERT INTO flashcards(question, answer, category) VALUES (?, ?, ?) """,
            (flashcard_data.question, flashcard_data.answer, flashcard_data.category),
        )
        db.commit()

    return {
        "msg": "Flashcard created successfully",
        "flashcard_id": flashcard_data.flashcard_id,
        "question": flashcard_data.question,
        "answer": flashcard_data.answer,
        "category": flashcard_data.category,
    }

# Get all flashcards 
@app.get("/flashcards/")
async def get_flashcards():
    with sqlite3.connect("YOURDATABASE.db") as database:
        cursor = database.cursor()

        statement = "SELECT * FROM flashcards"
        cursor.execute(statement)
        output = cursor.fetchall()

        return json.dumps(output)

# Get flashcards by id 
@app.get("/flashcards/{flashcard_id}")
async def get_flashcard_by_id(flashcard_id: int):
    with sqlite3.connect("YOURDATABASE.db") as database:
        cursor = database.cursor()

        print(f"Fetching flashcard with ID: {flashcard_id}")

        cursor.execute("""SELECT * FROM flashcards WHERE flashcard_id = (?)""", (
            flashcard_id,
        ))
        flashcard = cursor.fetchone()

        print(f"Fetched flashcard: {flashcard}")

        if not flashcard:
            return {"error": "Flashcard not found"}

        if len(flashcard) < 4:
            return {"error": "Database schema mismatch. Expected at least 4 columns."}


        return {"flashcard_id": flashcard[0], "question": flashcard[1], "answer": flashcard[2], "hint": flashcard[3]}

# Delete flashcard by id    
@app.delete("/flashcards/delete/{flashcard_id}")
async def delete_flashcard_by_id(flashcard_id: int):
    try:
        with sqlite3.connect("YOURDATABASE.bd") as database:
            cursor = database.cursor()

            print(f"Fetching flashcard with ID: {flashcard_id}")

            cursor.execute("""DELETE FROM flashcards WHERE flashcard_id = (?)""", (
                flashcard_id,
            ))
            flashcard = cursor.fetchone()
            return {"message": "Flashcard deleted"}
            
        if not flashcard:
            return {"error": "Flashcard not found"}
        

    except sqlite3.Error as error:
        print("Failed to delete record from sqlite table", error)



if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
