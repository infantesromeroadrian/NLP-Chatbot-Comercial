from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

class DocumentEmbedder:
    def __init__(self, documents):
        self.documents = documents
        self.model = "text-embedding-ada-002"
        self.embeddings = OpenAIEmbeddings(model=self.model)

    def embed(self):
        vectorstore = Chroma.from_documents(
            documents=self.documents, embedding=self.embeddings)
        return vectorstore.as_retriever(search_kwargs={"k": 3})

