🌟 README for Chatbot Project with Streamlit and LangChain 🌟
📖 Project Description
This project implements an interactive chatbot using Streamlit for the user interface and LangChain for document processing and response generation. The chatbot is designed to respond to queries using information extracted from PDF documents and OpenAI's chat model.

🏗️ Project Structure
The project is organized as follows:

app.py: Main script for the Streamlit user interface.
data_processing/: Scripts for downloading, loading, and processing PDF documents.
retrieval/: Implementation for information retrieval and the query-response chain.
chatbot/: Implementation of the chatbot.
diagram/: Script to generate a flowchart diagram of the project.
utils/: Optional directory for additional and utility scripts.
📋 Requirements
Python 3.7 or higher.
Poetry for dependency management.
Streamlit.
NLTK (Natural Language Toolkit).
Graphviz (for project diagram).
LangChain and its dependencies.
⚙️ Installation
Clone the repository:

bash
Copy code
git clone <https://github.com/infantesromeroadrian/NLPChatbotComercial.git>
Navigate to the project directory:

bash
Copy code
cd <ChatBotComercial>
Install dependencies using Poetry:

bash
Copy code
poetry install
🔧 Configuration
Set your OpenAI API key in the environment:

bash
Copy code
export OPENAI_API_KEY='your_api_key'
Replace your_api_key with your actual OpenAI API key.

🚀 Running the Application
Start the Streamlit application with:

bash
Copy code
streamlit run app.py
The application will open in your default browser.

💬 Using the Chatbot
Interact with the chatbot by entering questions in the text field. It will respond based on information from the documents and the OpenAI chat model.

📊 Generating the Project Diagram
To generate a diagram:

Navigate to diagram/.
Run the diagram.py script:
bash
Copy code
python diagram.py
This will create a visual diagram in the current directory.

📝 Additional Notes
This README provides a basic guide to get started with the chatbot. Be sure to customize it to reflect any specific features or additional steps necessary for your project.


