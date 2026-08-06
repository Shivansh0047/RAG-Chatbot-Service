---
source_anchor: "README.md#ai-exam-notes-generator"
source_commit: "5b7f65d10ac4ea1c3c10df6b41a83618f4f95c06"
status: "updated"
---

**Why flagged:** gitsteward-docs/modified_gitsteward_readme.md: The section is specific to the AI Exam Notes Generator project, but the diff introduces the service as a reusable instance that can serve multiple projects.

The primary integration and one of many possible projects. The knowledge base is seeded from all notes stored in the project's MongoDB database via a one-time backfill script (`scripts/backfill_from_mongo.py`). Going forward, new notes are auto-ingested by the Express backend calling `POST /ingest/note` after each generation. This project's data lives in the `exam_notes_generator` collection in Qdrant, isolated from other projects' data. **Currently indexed:** 30 notes, 168 chunks
