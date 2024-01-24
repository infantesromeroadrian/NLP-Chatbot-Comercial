from graphviz import Digraph

dot = Digraph(comment='Chatbot Application')

# Definir los nodos
dot.node('A', 'app.py (Streamlit UI)')
dot.node('B', 'data_processing')
dot.node('C', 'retrieval')
dot.node('D', 'chatbot')

# Subcomponentes de data_processing
dot.node('B1', 'PDFDownloader.py')
dot.node('B2', 'PDFLoader.py')
dot.node('B3', 'DocumentSplitter.py')
dot.node('B4', 'DocumentEmbedder.py')

# Subcomponente de retrieval
dot.node('C1', 'QAChain.py')

# Subcomponente de chatbot
dot.node('D1', 'ChatBot.py')

# Definir las conexiones
dot.edges(['AB', 'AC', 'AD'])
dot.edge('B', 'B1')
dot.edge('B', 'B2')
dot.edge('B', 'B3')
dot.edge('B', 'B4')
dot.edge('C', 'C1')
dot.edge('D', 'D1')

# Conexiones de flujo de trabajo específicas
dot.edge('B4', 'C1', label='retriever')
dot.edge('C1', 'D1', label='QAChain')

# Renderizar y guardar el diagrama
dot.render('chatbot_application_diagram', view=True)