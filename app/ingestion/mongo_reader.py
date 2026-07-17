from typing import Iterator # Iterator is a type hint — tells Python this function yields values one at a time rather than returning a list all at once.
import pymongo

from app.config import settings


def _flatten_content(content) -> str: # Takes the content dict (the Mixed field from MongoDB) and returns a single plain string we can chunk and embed.
    """
    Extracts and combines the most useful text from the mixed `content` field.
    Falls back gracefully if any subfield is missing.
    """
    parts = []

    # get main content
    notes_text = content.get("notes", "")
    if notes_text:
        parts.append(notes_text)

    # get revision points
    revision_points = content.get("revisionPoints", [])
    if revision_points:
        parts.append("Revision Points:\n" + "\n".join(f"- {p}" for p in revision_points))

    # get questions in notes (can be useful)
    questions = content.get("questions", {})
    short_qs = questions.get("short", [])
    long_qs = questions.get("long", [])
    all_questions = short_qs + long_qs
    if all_questions:
        parts.append("Practice Questions:\n" + "\n".join(f"- {q}" for q in all_questions))

    return "\n\n".join(parts) # Join all parts and return


def iter_notes() -> Iterator[dict]: # It is Iterator, so produces one notes at a time instead of entire db
    """
    Yields one dict per note with fields our ingestion pipeline expects:
    note_id, owner_id, title, text, and extra metadata.
    """
    client = pymongo.MongoClient(settings.mongo_uri) # Open connection
    db = client[settings.mongo_db_name] # select db
    collection = db[settings.mongo_notes_collection] # select collection

    for doc in collection.find({}):
        content = doc.get("content", {}) # get content

        # skip notes with no usable text
        if not content or not isinstance(content, dict):
            continue

        text = _flatten_content(content)
        if not text.strip():
            continue

        yield {
            "note_id": str(doc["_id"]),
            "owner_id": str(doc.get("user", "")),
            "title": doc.get("topic", "untitled"),
            "text": text,
            # extra metadata stored alongside each chunk in Qdrant
            "metadata": {
                "class_level": doc.get("classLevel", ""),
                "exam_type": doc.get("examType", ""),
                "created_at": str(doc.get("createdAt", "")),
            }
        }

    client.close() # close the connection