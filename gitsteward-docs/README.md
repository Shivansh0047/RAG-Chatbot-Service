# GitSteward — Doc Suggestions Index

Auto-generated summary of every README section GitSteward has flagged.

## How It Works (#how-it-works)
Status: updated
Commit: db57fb3
Updated: 2026-08-16T20:01:48+00:00
Summary: app/rag/llm.py: the workflow still says the context is sent to Google Generative AI, which is no longer true

## Project Structure (#project-structure)
Status: updated
Commit: db57fb3
Updated: 2026-08-16T20:01:48+00:00
Summary: app/rag/llm.py: llm.py now uses HuggingFace Llama instead of Gemini, so the file description is outdated

## Required Environment Variables (#required-environment-variables)
Status: updated
Commit: db57fb3
Updated: 2026-08-16T20:01:48+00:00
Summary: app/rag/llm.py: `GOOGLE_API_TOKEN` is no longer required for LLM calls after switching to HuggingFace

## Stack (#stack)
Status: updated
Commit: db57fb3
Updated: 2026-08-16T20:01:48+00:00
Summary: app/rag/llm.py: LLM entry still lists `gemini-2.5-flash` via Google Generative AI despite the code now using HuggingFace

