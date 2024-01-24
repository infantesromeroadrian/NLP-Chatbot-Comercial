import streamlit as st
import os
from data_processing.DocumentEmbedder import DocumentEmbedder
from data_processing.PDFLoader import PDFLoader
from data_processing.DocumentSplitter import DocumentSplitter
from data_processing.PDFDownloader import PDFDownloader
from retrieval.QAChain import QAChain
from chatbot.ChatBot import Chatbot

def main():
    st.title("Chatbot de Adrián Infantes")

    # Intentar obtener la clave API de OpenAI desde una variable de entorno primero
    openai_api_key = os.getenv("OPENAI_API_KEY")

    # Si no está en las variables de entorno, intentar con st.secrets
    if not openai_api_key and "openai" in st.secrets:
        openai_api_key = st.secrets["openai"]["api_key"]

    # Si no se encuentra la clave API, mostrar un error y detener la ejecución
    if not openai_api_key:
        st.error("No se pudo encontrar la clave API de OpenAI.")
        st.stop()

    # URLs de documentos PDF
    urls = [
        'https://arxiv.org/pdf/2306.06031v1.pdf',
        'https://arxiv.org/pdf/2306.12156v1.pdf',
        # ... otras URLs de documentos PDF ...
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

    # Verificar que el retriever esté inicializado correctamente
    if retriever is None:
        st.error("El objeto retriever no se ha inicializado correctamente.")
        st.stop()

    # Inicializar la cadena de consultas y respuestas (QAChain)
    qa_chain = QAChain(retriever)

    # Inicializar el chatbot
    chatbot = Chatbot(qa_chain, openai_api_key)

    # Campo de entrada para la pregunta del usuario
    user_input = st.text_input("Haz una pregunta al chatbot:")

    # Botón para obtener respuesta
    if st.button("Obtener respuesta"):
        if user_input:
            # Obtener respuesta del chatbot
            respuesta = chatbot.obtener_respuesta(user_input)
            st.write(respuesta)
        else:
            st.write("Por favor, introduce una pregunta.")

if __name__ == "__main__":
    main()
