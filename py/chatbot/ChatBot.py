import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from py.retrieval.QAChain import QAChain
from langchain.chat_models import ChatOpenAI
import os

# Descargar recursos de NLTK
nltk.download('punkt')
nltk.download('stopwords')


class Chatbot:
    def __init__(self, qa_chain, openai_chat_model):
        self.qa_chain = qa_chain
        self.openai_chat_model = openai_chat_model
        self.respuestas_predefinidas = {
            "inicio_conversacion": "Hola, estás escribiendo a la DG Flota - Partner de Yango Perú. ¿Cómo podemos ayudarte?",
            "como_usar_yango": "Descubre cómo usar la app YANGO con nuestro video tutorial. Disponible en Lima, Arequipa y Trujillo, y próximamente en más ciudades. Guía para Lima: https://youtu.be/P1c7s2l14_s, y para otras provincias: aquí https://youtu.be/lxAH7UCJ_6g",
            "proceso_afiliacion": "Para afiliarse y comenzar a usar Yango, complete los siguientes formularios: Afiliación a DG FLOTA: https://forms.gle/43sM6PaZttYX5hom8 Registro de Cuenta para Pagos: https://forms.gle/sQVmDxDe9Gq3Gsku6 Una vez completados, envíenos capturas de pantalla de ambos para confirmar su afiliación.",
            "registrar_informacion_bancaria": "Para habilitar los depósitos de tu saldo en Yango, por favor, completa este formulario: https://forms.gle/sQVmDxDe9Gq3Gsku6.",
            "bono": "Para obtener bonos con Yango, ten en cuenta lo siguiente: En el aplicativo, consulta el sistema de bonificación que ofrece recompensas por alcanzar un número específico de viajes. Mantén un puntaje de Actividad de 40 o más para calificar para el bono. Los bonos se añadirán a tu saldo al día siguiente de haber completado los viajes requeridos. Cuantos más viajes completes, mayores serán los beneficios que recibirás.",
            "referir_conductor": "Para referir conductores a Yango, sigue estos pasos según cada situación: Referir a un Nuevo Conductor: Ve a tu perfil y selecciona 'Invitar a un amigo'. Copia y comparte tu código con el nuevo conductor. El referido debe descargar la app Yango y usar tu código al registrarse. Si no encuentra DG Flota como opción de partner, puede contactarnos a través de este enlace: https://wa.me/51991672576 Conductor en Otra Flota: Para conductores que deseen cambiar a nuestra flota, comparte este enlace: https://wa.me/51991672576",
            "cambiar_partner": "Para cambiarte a la DG Flota, sigue estos pasos: Completa el formulario de Afiliación de DG FLOTA en: https://forms.gle/43sM6PaZttYX5hom8 Llena el formulario para tu Cuenta de Pagos en: https://forms.gle/sQVmDxDe9Gq3Gsku6 Envíanos capturas de pantalla de ambos formularios una vez que estén completados.",
            "cambio_vehiculo": "Para cambiar tu vehículo en la aplicación, envíanos los siguientes detalles: Marca del vehículo, Modelo, Color, Año, Placa del vehículo, Número de licencia en la aplicación Yango. Tras enviar esta información, espera nuestra confirmación para reiniciar la app y visualizar los cambios.",
            "condiciones_pago": "Frecuencia: Diaria (lunes a viernes) o Semanal (Pago los Martes). El horario regular de pago de saldos es de 6pm a 8pm. Horarios de Corte: 3pm-6pm; pago al día siguiente. Mínimo para Pago: Saldo de 20 soles al corte. No Pagos: Fines de semana y feriados. Comunicación: Contacto inicial por WhatsApp, esperar confirmación para cambios en app.",
            "comisiones": "La comisión total por viaje para conductores afiliados a DG Flota es del 15%, incluyendo la comisión de Yango del 12% y una comisión adicional de 3%.",
            "preguntas_sin_informacion": "En este momento te derivamos con un operador para que atienda tu duda."
        }

    def identificar_palabras_clave(self, texto):
        palabras = word_tokenize(texto)
        palabras_filtradas = [palabra for palabra in palabras if palabra not in stopwords.words('spanish')]
        return palabras_filtradas

    def obtener_respuesta(self, clave_pregunta):
        clave_pregunta = clave_pregunta.lower()
        respuesta = self.respuestas_predefinidas.get(clave_pregunta)

        if respuesta:
            return respuesta
        else:
            # Primero intentar con QAChain
            respuesta_qa_chain = self.qa_chain.query(clave_pregunta)
            if respuesta_qa_chain:
                return respuesta_qa_chain
            else:
                # Si QAChain no encuentra respuesta, usar OpenAI Chat Model
                return self.openai_chat_model.query(clave_pregunta)


# Ejemplo de inicialización y uso
if __name__ == "__main__":
    # Asumiendo que 'retriever' está definido y configurado
    from py.data_processing.DocumentEmbedder import DocumentEmbedder
    from py.data_processing.PDFLoader import PDFLoader
    from py.data_processing.DocumentSplitter import DocumentSplitter
    from py.data_processing.PDFDownloader import PDFDownloader

    # Ejemplo de URLs de documentos PDF
    urls = ["https://arxiv.org/pdf/2306.06031v1.pdf", "https://arxiv.org/pdf/2306.12156v1.pdf"]

    # Proceso de descarga y procesamiento de documentos
    downloader = PDFDownloader(urls)
    filenames = downloader.download()
    loader = PDFLoader(filenames)
    documents = loader.load()
    splitter = DocumentSplitter(documents)
    split_documents = splitter.split()
    embedder = DocumentEmbedder(split_documents)
    retriever = embedder.embed()

    # Inicialización de QAChain y ChatOpenAI
    qa_chain = QAChain(retriever)
    chat_openai = ChatOpenAI(api_key=os.environ["OPENAI_API_KEY"], model="gpt-3.5-turbo")

    # Inicialización del chatbot
    chatbot = Chatbot(qa_chain, chat_openai)

    # Bucle de chat interactivo
    while True:
        pregunta_usuario = input("Usuario: ")
        if pregunta_usuario.lower() == "salir":
            break
        respuesta = chatbot.obtener_respuesta(pregunta_usuario)
        print("Chatbot:", respuesta)