Flask Streamlit DockerHub GCP GitHub Actions

MedIQ-ChatBot
Introduction
MedIQ ChatBot is a smart and intuitive platform designed to provide you with medical information and assistance in a convenient and personalized manner. MedIQ chatbot leverages advanced natural language processing and deep learning techniques to simulate a virtual doctor's appointment, addressing your medical queries and concerns.

Technologies used in this project

Flask
Streamlit
Docker
Google Cloud Platform
GitHub CI/CD pipline
Files
📦 MedIQ-ChatBot
├─ .github
│  └─ workflows
│     ├─ CD-pipeline.yml
│     └─ docker-image.yml
├─ .gitignore
├─ README.md
├─ docker-compose.yml
├─ flask
│  ├─ Dockerfile
│  ├─ chat_model
│  │  ├─ assets
│  │  │  └─ .placeholder
│  │  ├─ fingerprint.pb
│  │  ├─ keras_metadata.pb
│  │  ├─ saved_model.pb
│  │  └─ variables
│  │     ├─ variables.data-00000-of-00001
│  │     └─ variables.index
│  ├─ intents.json
│  ├─ label_encoder.pickle
│  ├─ main.py
│  ├─ requirements.txt
│  ├─ tokenizer.pickle
│  └─ train.py
└─ streamlit
   ├─ Dockerfile
   ├─ health_bg.jpg
   ├─ home.py
   ├─ pages
   │  └─ app.py
   └─ requirements.txt
Description of Dataset
For this task, I used the medical question answer dataset prepared by Lasse Regin Nelson. This dataset is uploaded in his GitHub https://github.com/LasseRegin/medical-question-answer-data. He has gathered such question answer pairs from prominent medical websites such as eHealth Forum, iCliniq, Question Doctors, WebMD where real doctors have provided public answers to the questions asked by patients. We are provided with about 25K question answer pairs. Along with the question answer pairs we are also given tags to efficiently categorize the questions into belonging to a particular disease, etc.

Implementation
Developed a healthcare chatbot leveraging natural language processing (NLP) techniques, enabling users to interactively seek medical advice and insights similar to a virtual doctor's appointment
Enhanced performance through lemmatization, tokenization and hyperparameter tuning, attaining 79% reduction in loss
Trained a deep learning LSTM RNN model on question-answer dataset for precise responses to queries/medical concerns, with 94% accuracy
Designed and implemented RESTful APIs using Flask, to expose backend functionalities of the application to end-users
Developed a Streamlit web application that allows users to interact with the trained model
Containerized both Streamlit and Flask microservices using 2 Docker containers, allowing for easier sharing and scalability. Published the Docker images on DockerHub, making it easily accessible to others over the internet (https://hub.docker.com/r/mittal15/flask_mediq/tags, https://hub.docker.com/r/mittal15/streamlit_mediq/tags)
Administered GitHub CI/CD pipeline to automatically build and deploy code, and streamline the development process
Deployed the application on a Google Cloud Platform (GCP) VM instance through a docker compose file, utilizing top-tier cloud computing infrastructure to provide fast and reliable hosting
Installation
To clone and replicate the project, please follow the steps below:

Open the command line interface (CLI) on your computer.
Navigate to the directory where you want to clone the repository.
Type git clone https://github.com/Hmittal15/MedIQ-ChatBot.git and press Enter. This will clone the repository to your local machine.
Navigate into the cloned repository using cd your-repo
Pull the docker images from DockerHub using commands- docker pull mittal15/flask_mediq:latest and docker pull mittal15/streamlit_mediq:latest
Fire up the dockers using command docker compose up from project root directory. Streamlit app should be running on port 8000 and Flask should be running on port 8090. Happy chatting!
Application demo:-
Demo GIF

Link to full explanatory video:-
https://youtu.be/hU_MGfL9Hqo

Application public link:
http://34.148.161.201:8000

GitHub CI/CD workflow:
CI Pipeline

You can find me on 
