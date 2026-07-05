[![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![DockerHub](https://img.shields.io/badge/DockerHub-0db7ed?style=flat-square&logo=docker&logoColor=white)](https://hub.docker.com/)
[![GCP](https://img.shields.io/badge/GCP-4285F4?style=flat-square&logo=google-cloud&logoColor=white)](https://cloud.google.com/)
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=github-actions&logoColor=white)](https://github.com/features/actions)

# MediCare-ChatBot

## Introduction
MediCare ChatBot is a smart and intuitive platform designed to provide you with medical information and assistance in a convenient and personalized manner. MediCare chatbot leverages advanced natural language processing and deep learning techniques to simulate a virtual doctor's appointment, addressing your medical queries and concerns.

Technologies used in this project
* Flask
* Streamlit
* Docker
* Google Cloud Platform
* GitHub CI/CD pipline

## Files

```
📦 MediCare-ChatBot
├─ .github
│  └─ workflows
├─ .gitignore
├─ README.md
├─ flask
│  ├─ chat_model
│  │  ├─ assets
│  │  │  └─ .placeholder
│  │  ├─ fingerprint.pb
│  │  ├─ keras_metadata.pb
│  │  ├─ saved_model.pb
│  │  └─ variables
│  │     ├─ variables.data-00000-of-00001
│  │     └─ variables.index
│  ├─ intents.json
│  ├─ label_encoder.pickle
│  ├─ main.py
│  ├─ requirements.txt
│  ├─ tokenizer.pickle
│  └─ train.py
└─ streamlit
   ├─ health_bg.jpg
   ├─ home.py
   ├─ pages
   │  └─ app.py
   └─ requirements.txt
```

## Description of Dataset
For this task, I used the medical question answer dataset prepared by Lasse Regin Nelson. This dataset is uploaded in his GitHub https://github.com/LasseRegin/medical-question-answer-data. He has gathered such question answer pairs from prominent medical websites such as eHealth Forum, iCliniq, Question Doctors, WebMD where real doctors have provided public answers to the questions asked by patients. We are provided with about 25K question answer pairs. Along with the question answer pairs we are also given tags to efficiently categorize the questions into belonging to a particular disease, etc.

## Implementation
1. Developed a healthcare chatbot leveraging natural language processing (NLP) techniques, enabling users to interactively seek medical advice and insights similar to a virtual doctor's appointment
2. Enhanced performance through lemmatization, tokenization and hyperparameter tuning, attaining 79% reduction in loss
3. Trained a deep learning LSTM RNN model on question-answer dataset for precise responses to queries/medical concerns, with 94% accuracy
4. Designed and implemented RESTful APIs using Flask, to expose backend functionalities of the application to end-users
5. Developed a Streamlit web application that allows users to interact with the trained model
6. Containerized both Streamlit and Flask microservices using 2 Docker containers, allowing for easier sharing and scalability. Published the Docker images on DockerHub, making it easily accessible to others over the internet (https://hub.docker.com/r/mittal15/flask_mediq/tags, https://hub.docker.com/r/mittal15/streamlit_mediq/tags)
7. Administered GitHub CI/CD pipeline to automatically build and deploy code, and streamline the development process
9. Deployed the application on a Google Cloud Platform (GCP) VM instance through a docker compose file, utilizing top-tier cloud computing infrastructure to provide fast and reliable hosting


## Application demo:-
![Demo GIF](https://github.com/ibadlaskar/MediCare/blob/main/demo.gif?raw=true)


## You can find me on <a href="linkedin.com/in/ibad-laskar"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/768px-LinkedIn_logo_initials.png" width="17" height="17" /></a>
