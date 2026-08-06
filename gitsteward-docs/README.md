# GitSteward — Doc Suggestions Index

Auto-generated summary of every README section GitSteward has flagged.

## Ai Exam Notes Generator (#ai-exam-notes-generator)
Status: updated
Commit: 7b3d1f2
Updated: 2026-08-06T20:33:14+00:00
Summary: gitsteward-docs/ai-exam-notes-generator.md: The section is now outdated as the AI Exam Notes Generator is introduced as a reusable instance that can serve multiple projects. / gitsteward-docs/modified_gitsteward_readme.md: The section still refers to the AI Exam Notes Generator as the primary integration, but the code diff indicates it is now one of many possible projects.

## How It Works (#how-it-works)
Status: updated
Commit: 7b3d1f2
Updated: 2026-08-06T20:33:14+00:00
Summary: gitsteward-docs/README.md: The embeddings step now uses Google Generative AI instead of HuggingFace / gitsteward-docs/project-structure.md: The description of how the service works may no longer be accurate due to the change from HuggingFace to Google Generative AI in embeddings.py / gitsteward-docs/stack.md: The change in embeddings layer may affect the embedding and retrieval process

## Project Structure (#project-structure)
Status: updated
Commit: 7b3d1f2
Updated: 2026-08-06T20:33:14+00:00
Summary: gitsteward-docs/README.md: The project structure has changed with the update from HuggingFace to Google Generative AI in embeddings.py / gitsteward-docs/project-structure.md: The project structure description in the README no longer matches the updated structure in the code, specifically the change from HuggingFace to Google Generative AI in embeddings.py / gitsteward-docs/stack.md: The embeddings.py file has changed to use Google Generative AI instead of HuggingFace

## Required Environment Variables (#required-environment-variables)
Status: updated
Commit: 7b3d1f2
Updated: 2026-08-06T20:33:14+00:00
Summary: gitsteward-docs/README.md: The environment variable HF_TOKEN is no longer used and should be replaced with GOOGLE_API_TOKEN / gitsteward-docs/modified_gitsteward_readme.md: The section lists HF_TOKEN as being used for both embeddings and LLM, but the code diff indicates that GOOGLE_API_TOKEN is used for embeddings and HF_TOKEN is used for LLM. / gitsteward-docs/project-structure.md: The required environment variables may have changed due to the update from HuggingFace to Google Generative AI, potentially requiring a new token or API key / gitsteward-docs/required-environment-variables.md: The section still references the deprecated `HF_TOKEN` environment variable and its usage is outdated. / gitsteward-docs/stack.md: The HuggingFace token environment variable may no longer be needed or may need to be replaced with a Google Generative AI token

## Stack (#stack)
Status: updated
Commit: 7b3d1f2
Updated: 2026-08-06T20:33:14+00:00
Summary: gitsteward-docs/project-structure.md: The stack description in the README no longer matches the updated technology stack, specifically the change from HuggingFace to Google Generative AI in embeddings.py / gitsteward-docs/stack.md: The embeddings layer has changed from HuggingFace to Google Generative AI

