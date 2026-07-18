"""
One-time script to seed Qdrant from all existing notes in MongoDB.
Run from project root:
    python -m scripts.backfill_from_mongo
"""

import time

from app.ingestion.mongo_reader import iter_notes
from app.rag.splitter import split_text
from app.rag.vectorstore import get_vectorstore

PROJECT_ID = "exam_notes_generator" # Project_id
DELAY = 0.2  # small delay between notes to avoid overwhelming embedding model


def run():
    total_notes = 0
    total_chunks = 0
    skipped = 0

    print(f"Starting backfill for project: {PROJECT_ID}")
    print("-" * 50)

    for note in iter_notes(): # call iterate notes form mongoDB
        try:
            metadata = {
                "note_id": note["note_id"],
                "owner_id": note["owner_id"],
                "note_title": note["title"],
                **note["metadata"],  # class_level, exam_type, created_at
            }

            docs = split_text(note["text"], metadata)
            get_vectorstore(PROJECT_ID).add_documents(docs)

            total_notes += 1
            total_chunks += len(docs)
            print(f"✓ [{total_notes}] {note['title']} — {len(docs)} chunks")

            time.sleep(DELAY)

        except Exception as e:
            skipped += 1
            print(f"✗ Skipped note {note['note_id']}: {e}")
            continue

    print("-" * 50)
    print(f"Done. {total_notes} notes indexed, {total_chunks} total chunks, {skipped} skipped.")


if __name__ == "__main__":
    run()