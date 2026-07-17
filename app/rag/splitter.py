from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def split_text(text: str, metadata:dict)-> list[Document]:
    splitter = RecursiveCharacterTextSplitter( # Use revursive character text splitter
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks=splitter.split_text(text)
    return [Document(page_content=chunk, metadata=metadata) for chunk in chunks] # Return a document object