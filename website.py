import streamlit as st
import requests
from streamlit_lottie import st_lottie

# ---Title---
st.set_page_config(page_title="Welcome", page_icon=":shark:", layout="wide")

with st.container():
    # ---Subheader---
    st.title("Hello! My name is Aakash Yadav :wave:")
    # ---About Me---
    st.write("I am a full stack AI/ML Developer with a passion for creating innovative solutions. Here are some of my key skills and tools:")

    def load_lottie(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    
    lottie_loading = 'https://lottie.host/09eb522e-7008-4473-86a9-da8b971ec44a/eAFtF1rUI7.json'
    my_skill = 'https://lottie.host/06e9371e-48df-4d6e-afaa-627e1beca159/XvCM62bMjN.json'
    project = 'https://lottie.host/a64c15a5-ff56-4a80-a1d7-dccc32bda88c/hMwrq3Nia4.json'

# Divider
st.write("---")

# ---Content Section---
left_column, right_column = st.columns(2)

with left_column:
    st.header("What I do")
    st.write("""
    - As a full stack AIML developer, you possess a diverse skill set that spans both the development of machine learning models and their deployment.
    - Creating machine learning models typically includes data preprocessing, feature engineering, model selection, training, and evaluation.
    - You likely use popular libraries such as TensorFlow, PyTorch, or scikit-learn for these tasks.
    - Once the models are trained and evaluated, the next step is deployment.
    - Deployment often involves setting up virtual machines (VMs) on cloud platforms like AWS, Azure, or Google Cloud.
    - You configure these VMs to host your models, ensuring they are scalable and can handle real-time predictions.
    - Tools like Docker and Kubernetes are commonly used to containerize and orchestrate these deployments, providing a robust and flexible environment for your applications.
    - Additionally, you create end-to-end pipelines for machine learning prediction models.
    - These pipelines automate the workflow from data ingestion to model training, evaluation, and deployment.
    - Tools like Apache Airflow, Kubeflow, and MLflow are instrumental in building these pipelines, allowing for continuous integration and continuous deployment (CI/CD) of machine learning models.
    - In summary, your expertise lies in not only developing sophisticated machine learning models but also in deploying them efficiently and creating automated pipelines that ensure seamless operation and scalability.
    - This combination of skills is crucial for delivering robust and reliable AI solutions in a production environment.
    """)

with right_column:
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st_lottie(load_lottie(lottie_loading), height=300, key="coding")


# --- Skills Section ---
left_column, right_column = st.columns(2)


with left_column:
    # Divider
    st.write("---")
    st.header("My Skills")
    st.write("""
    - Programming Languages: Python
    - Machine Learning Libraries: TensorFlow, PyTorch, scikit-learn, XGBoost, LightGBM
    - Data Processing Libraries: Pandas, NumPy, Dask, Vaex
    - Data Visualization Libraries: Matplotlib, Seaborn, Plotly
    - Deep Learning Frameworks: TensorFlow, PyTorch, Keras, Fastai, ONNX, OpenCV, Scikit-image, CNN, RNN, LSTM, GAN, Transformer
    - Cloud Platforms: AWS, Azure, Google Cloud
    - Containerization: Docker, Kubernetes, Prefect, DVC
    - Workflow Automation: Apache Airflow, Kubeflow, MLflow
    - Web Development: streamlit, Flask, Django
    - Databases: SQL, NoSQL
    - Version Control: Git, GitHub, GitLab, Bitbucket, Azure DevOps
    - Operating Systems: Linux, Windows
    - Soft Skills: Problem-Solving, Communication, Teamwork, Time Management, Adaptability, Creativity, Leadership, Critical Thinking, Decision Making
    """)
    with right_column:
        st.write('---')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st_lottie(load_lottie(my_skill), height=300, key="skills")


with left_column:
    # Divider
    st.write("---")
    st.header("Projects")
    st.write("""
    - Programming Languages: Python
    - Machine Learning Libraries: TensorFlow, PyTorch, scikit-learn, XGBoost, LightGBM
    - Data Processing Libraries: Pandas, NumPy, Dask, Vaex
    - Data Visualization Libraries: Matplotlib, Seaborn, Plotly
    - Deep Learning Frameworks: TensorFlow, PyTorch, Keras, Fastai, ONNX, OpenCV, Scikit-image, CNN, RNN, LSTM, GAN, Transformer
    - Cloud Platforms: AWS, Azure, Google Cloud
    - Containerization: Docker, Kubernetes, Prefect, DVC
    - Workflow Automation: Apache Airflow, Kubeflow, MLflow
    - Web Development: streamlit, Flask, Django
    - Databases: SQL, NoSQL
    - Version Control: Git, GitHub, GitLab, Bitbucket, Azure DevOps
    - Operating Systems: Linux, Windows
    - Soft Skills: Problem-Solving, Communication, Teamwork, Time Management, Adaptability, Creativity, Leadership, Critical Thinking, Decision Making
    """)
    with right_column:
        st.write('---')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st_lottie(load_lottie(my_skill), height=300, key="skills")