# GitSteward — Doc Suggestions Index

Auto-generated summary of every README section GitSteward has flagged.

## Ai Exam Notes Generator (#ai-exam-notes-generator)
Status: updated
Commit: 5b7f65d
Updated: 2026-08-06T20:31:40+00:00
Summary: gitsteward-docs/modified_gitsteward_readme.md: The section is specific to the AI Exam Notes Generator project, but the diff introduces the service as a reusable instance that can serve multiple projects.

## How It Works (#how-it-works)
Status: updated
Commit: e622abc
Updated: 2026-08-06T20:31:00+00:00
Summary: app/rag/embeddings.py: The embeddings step now uses Google Generative AI instead of HuggingFace

## Project Structure (#project-structure)
Status: updated
Commit: 5b7f65d
Updated: 2026-08-06T20:31:40+00:00
Summary: gitsteward-docs/README.md: The project structure has changed with the update from HuggingFace to Google Generative AI in embeddings.py / gitsteward-docs/stack.md: The embeddings.py file has changed to use Google Generative AI instead of HuggingFace

## Required Environment Variables (#required-environment-variables)
Status: updated
Commit: 5b7f65d
Updated: 2026-08-06T20:31:40+00:00
Summary: gitsteward-docs/README.md: The environment variable HF_TOKEN is no longer used and should be replaced with GOOGLE_API_TOKEN / gitsteward-docs/required-environment-variables.md: The section still references the deprecated `HF_TOKEN` environment variable. / gitsteward-docs/stack.md: The HuggingFace token is no longer used for embeddings, but still used for LLM

## Stack (#stack)
Status: updated
Commit: 5b7f65d
Updated: 2026-08-06T20:31:40+00:00
Summary: gitsteward-docs/README.md: The stack has changed with the update from HuggingFace to Google Generative AI in embeddings.py / gitsteward-docs/stack.md: The embeddings layer has changed from HuggingFace to Google Generative AI

