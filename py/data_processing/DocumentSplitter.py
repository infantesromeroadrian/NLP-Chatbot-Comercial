from langchain.text_splitter import RecursiveCharacterTextSplitter

class DocumentSplitter:
    def __init__(self, documents):
        self.documents = documents

    def split(self):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1500, chunk_overlap=200, length_function=len)
        return text_splitter.split_documents(self.documents)