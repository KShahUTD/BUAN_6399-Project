# FliptRx Configuration Lead AI Mentor


FliptRx Configuration Lead AI Mentor is an AI Agent built as a chatbox to help PBM admins with pharmacy claims analysis. It integrates with Google Vertex AI for NLP-based content generation and uses SentenceTransformer to handle complex queries efficiently. The chatbox allows users to inquire about the status and details of claims, rejected claims, paid claims, or duplicate claims based on the pharmacy claims data provided. It also provides rejection reason and resolution steps on how to resolve the claim

# Features

•	**Claim Status Inquiry**: Get real-time information about pharmacy claims (Paid, Rejected, or Duplicate).
•	**Natural Language Understanding**: Uses semantic embeddings to analyze user input and match relevant claims data.
•	**Interactive Chat Interface**: Built with ipywidgets to allow seamless user interaction

# Project Structure


<img width="763" height="137" alt="image" src="https://github.com/user-attachments/assets/353d72b2-2bd3-479c-a851-1c2e66ec6ca0" />

# File Descriptions

•	backend.py: Contains the logic for loading pharmacy claims data, generating embeddings using SentenceTransformer, and analyzing user input. It interacts with Google Vertex AI for content generation based on the provided claims data.

•	frontend.py: Defines the user interface using ipywidgets for user interaction. The frontend includes the chat interface where users can input their queries, click the ask button to submit, and view responses.

•	claims.json: JSON file containing pharmacy claims data, such as claim ID, drug name, pharmacy name, paid amount, date of service, and claim status. Here's an updated version of your README.md, which removes the requirements.txt and instead includes the pip install details directly. It also provides installation commands for all necessary dependencies.

# Installation
To run the FliptRx AI Claims Assistant locally, follow these steps:

1. Clone the Repository
git clone <repository-url>
cd FliptRx

2. Set Up a Virtual Environment
If you're using a virtual environment, you can set it up like this:
python3 -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate  # For Windows

3. Install Dependencies
Install the necessary Python libraries using pip:
pip install google-cloud-genai
pip install sentence-transformers
pip install ipywidgets
pip install numpy
These dependencies are required to run the backend (which uses the Google Cloud API and generates sentence embeddings), as well as the frontend (which provides an interactive UI).

4. Set Up Google Cloud Credentials
   
Ensure you have a Google Cloud account and set up a Service Account. Then, set up your credentials by downloading the JSON file for the service account and defining the path in your environment variable.

Example:

export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your-service-account-file.json"

This allows the backend to authenticate with Google Cloud services.

5. Mount Google Drive

In Google Colab, you will need to mount your Google Drive to access the claims.json file.

from google.colab import drive

drive.mount('/content/drive')

6. Run the Code

6.1. Backend Processing (backend.py)

•	The backend loads the pharmacy claims data, processes it, and uses embeddings to analyze user input. You can run this directly or interact with it through the frontend.

6.2. Frontend Interface (frontend.py)

After setting up the backend, you can use the following code to launch the interactive frontend UI in a Jupyter notebook or Google Colab:

from frontend import FliptRxFrontend

from backend import FliptRxBackend

# Initialize the backend with claims data and Google Cloud client

backend = FliptRxBackend("/content/drive/My Drive/FliptRx/claims.json", client)

# Initialize frontend

frontend = FliptRxFrontend(backend)

# Display the UI

frontend.display()

This will launch the chat interface where you can interact with the AI claims assistant.

# Usage 

•	After setting up the environment and starting the backend and frontend as mentioned above, you can use the following steps to interact with the system:

•	Ask Questions: Type your claim-related queries into the input box.

•	Submit the Query: Click the "Ask" button to submit the query.

•	View the Response: The AI-powered assistant will provide information about the claim based on the available data, such as payment details, rejection reasons, or duplicate claims and steps to resolve claim if claim was denied. 



