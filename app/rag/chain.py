from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

from app.rag.llm import get_llm
from app.rag.vectorstore import get_vectorstore

def answer_question(project_id: str, question:str) -> dict:
    # Retriver
    retriever = get_vectorstore(project_id).as_retriever(
        search_type="similarity",
        search_kwargs={"k": 4},  # return top 4 most relevant chunks
    )

    docs = retriever.invoke(question) # Embedded int question and seraches in vectorstore

    context = "\n\n".join(doc.page_content for doc in docs)

    # Prompt
    prompt = PromptTemplate(
        template="""
            You are a helpful study assistant. Answer ONLY using the context below,
            which is made up of exam notes. If the context is insufficient, say you
            don't know — do not make anything up.

            Context:
            {context}

            Question: {question}
            """,
                    input_variables=["context", "question"],
                )
    # Run chain
    prompt_value = prompt.invoke({"context": context, "question": question})
    response = get_llm().invoke(prompt_value)
    answer = StrOutputParser().invoke(response)

    # collect source note titles for attribution
    sources = sorted({doc.metadata.get("note_title", "untitled") for doc in docs})

    return {"answer": answer, "sources": sources}

