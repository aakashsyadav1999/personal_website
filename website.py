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
    
    #Display Profile Image
    #st.image(r"D:\vscode\personal_website\Image.jpg", caption="Aakash Yadav", width=150)

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
    - **Machine Learning & AI Expertise**: Skilled in designing, training, and deploying machine learning algorithms and models using Python, TensorFlow, and PyTorch, as well as leveraging ChatGPT API and Google Gemini Vision Pro for advanced AI applications.
    - **Data Preparation & Processing**: Experienced in collecting, cleaning, and preprocessing large datasets, enabling high-quality analysis and training for accurate model outcomes.
    - **End-to-End Model Deployment**: Proficient in deploying machine learning models in production, ensuring performance optimization and scalability for real-world applications.
    - **Collaborative Problem-Solving**: Work effectively with cross-functional teams to understand and meet project requirements, delivering solutions tailored to specific industry needs.
    - **Continuous Learning**: Actively stay updated with the latest advancements in AI and ML to ensure projects benefit from cutting-edge technologies and methodologies.
    - **Adaptable Across Industries**: Successfully applied AI/ML solutions across sectors, tackling challenges from predictive analytics to natural language processing and beyond.
    - **Hands-On Approach**: Known for a practical, hands-on approach, delivering results-oriented solutions that meet both technical and business objectives.
    - **Tech-Savvy with Practical Insights**: Utilize technical knowledge to streamline workflows and enhance the AI/ML pipeline, improving model accuracy and operational efficiency.
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
    st.header("My Skills")
    st.write("""
    - **Programming Languages**: Python
    - **Machine Learning Libraries**: TensorFlow, PyTorch, scikit-learn, XGBoost, LightGBM
    - **Data Processing Libraries**: Pandas, NumPy, Dask, Vaex
    - **Data Visualization Libraries**: Matplotlib, Seaborn, Plotly
    - **Deep Learning Frameworks**: TensorFlow, PyTorch, Keras, Fastai, ONNX, OpenCV, Scikit-image, CNN, RNN, LSTM, GAN, Transformer
    - **Cloud Platforms**: AWS, Azure, Google Cloud
    - **Containerization**: Docker, Kubernetes, Prefect, DVC
    - **Workflow Automation**: Apache Airflow, Kubeflow, MLflow
    - **Web Development**: streamlit, Flask, Django
    - **Databases**: SQL, NoSQL
    - **Version Control**: Git, GitHub, GitLab, Bitbucket, Azure DevOps
    - **Operating Systems**: Linux, Windows
    - **Soft Skills**: Problem-Solving, Communication, Teamwork, Time Management, Adaptability, Creativity, Leadership, Critical Thinking, Decision Making
    """)
    with right_column:

        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st_lottie(load_lottie(my_skill), height=300, key="my_sskills")


with left_column:
    # Divider
    st.header("Projects")
    st.write("""
    - **[Dog-Breed-Classifier](https://github.com/aakashsyadav1999/Dog-Breed-Classifier.git):** A deep learning CNN model to predict dog breeds from images.
    
    - **[Store-Item-Demand-Forecasting-Challenge](https://github.com/aakashsyadav1999/Store-Item-Demand-Forecasting-Challenge):** Tracks the sales of store and items to forecast future sales.
    
    - **[Healthcare Summarizer](https://github.com/aakashsyadav1999/Healthcare.git):** Predicts the length of stay of a patient in a hospital. 
    
    - **[Hotel-Reservations](https://github.com/aakashsyadav1999/Hotel-Reservations-Dataset-mlflow.git):** Predicts which type of customer will cancel their hotel reservation.
    
    - **[Text Classification END-TO-END](https://github.com/aakashsyadav1999/Text_Classification-END-END.git):** An NLP project for end-to-end text classification and categorization.
    """)
    with right_column:
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st_lottie(load_lottie(project), height=300, key="projects")