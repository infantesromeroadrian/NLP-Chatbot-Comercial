import os
from getpass import getpass
from data_processing.PDFDownloader import PDFDownloader
from data_processing.PDFLoader import PDFLoader
from data_processing.DocumentSplitter import DocumentSplitter
from data_processing.DocumentEmbedder import DocumentEmbedder
from retrieval.QAChain import QAChain
from chatbot.ChatBot import Chatbot

def main():
    # Configuración de la clave API de OpenAI
    OPENAI_API_KEY = getpass("Enter your OpenAI API key: ")
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

    # URLs de documentos PDF
    urls = [
        'https://arxiv.org/pdf/2306.06031v1.pdf',
        'https://arxiv.org/pdf/2306.12156v1.pdf',
        # ... otras URLs ...
    ]

    # Descargar documentos PDF
    downloader = PDFDownloader(urls)
    ml_papers = downloader.download()

    # Cargar y procesar documentos
    loader = PDFLoader(ml_papers)
    documents = loader.load()
    splitter = DocumentSplitter(documents)
    documents = splitter.split()
    embedder = DocumentEmbedder(documents)
    retriever = embedder.embed()

    # Inicializar la cadena de consultas y respuestas
    chain = QAChain(retriever)

    # Inicializar el chatbot (aquí se debe definir openai_chat_model adecuadamente)
    openai_chat_model = None  # Esto debe ser reemplazado por la instancia del modelo de chat
    bot = Chatbot(chain, openai_chat_model)

    # Ejemplo de uso del chatbot
    while True:
        pregunta_usuario = input("Usuario: ")
        if pregunta_usuario.lower() == "salir":
            break
        respuesta = bot.obtener_respuesta(pregunta_usuario)
        print("Chatbot:", respuesta)

if __name__ == "__main__":
    main()
