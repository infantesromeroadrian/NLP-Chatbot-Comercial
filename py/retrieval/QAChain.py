import os
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

class QAChain:
    def __init__(self, retriever):
        self.retriever = retriever
        self.openai_api_key = os.environ["OPENAI_API_KEY"]
        self.model_name = "gpt-3.5-turbo"
        self.temperature = 0.0
        self.chat = ChatOpenAI(
            openai_api_key=self.openai_api_key,
            model_name=self.model_name,
            temperature=self.temperature)
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.chat, chain_type="stuff", retriever=self.retriever)

    def query(self, question):
        return self.qa_chain.run(question)
