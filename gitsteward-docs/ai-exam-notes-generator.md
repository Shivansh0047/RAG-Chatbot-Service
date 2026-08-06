---
source_anchor: "README.md#ai-exam-notes-generator"
source_commit: "7b3d1f2688fc0c849da3d444467ee40ddd1b5f7b"
status: "updated"
---

**Why flagged:** gitsteward-docs/ai-exam-notes-generator.md: The section is now outdated as the AI Exam Notes Generator is introduced as a reusable instance that can serve multiple projects. / gitsteward-docs/modified_gitsteward_readme.md: The section still refers to the AI Exam Notes Generator as the primary integration, but the code diff indicates it is now one of many possible projects.

The primary integration and one of many possible projects. The knowledge base is seeded from all notes stored in the project's MongoDB database via a one-time backfill script (`scripts/backfill_from_mongo.py`). Going forward, new notes are auto-ingested by the Express backend calling `POST /ingest/note` after each generation. This project's data lives in the `exam_notes_generator` collection in Qdrant, isolated from other projects' data. **Currently indexed:** 30 notes, 168 chunks
