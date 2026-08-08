---
source_anchor: "README.md#ai-exam-notes-generator"
source_commit: "4282fd4b246413c8ead576e1b52a44f68eefdf45"
status: "updated"
---

**Why flagged:** gitsteward-docs/modified_gitsteward_readme.md: The number of currently indexed notes and chunks may have changed.

The primary integration. The knowledge base (`exam_notes_generator` collection in Qdrant) is seeded from all notes stored in the project's MongoDB database via a one-time backfill script (`scripts/backfill_from_mongo.py`). Going forward, new notes are auto-ingested by the Express backend calling `POST /ingest/note` after each generation.  
**Currently indexed:** 75 notes, 432 chunks  
---
