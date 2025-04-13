import ollama
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def get_embedding(text):
    response = ollama.embeddings(model='nomic-embed-text', prompt=text)
    return response['embedding']

def calculate_match_score(jd_summary, resume_text):
    jd_vec = np.array(get_embedding(jd_summary)).reshape(1, -1)
    resume_vec = np.array(get_embedding(resume_text)).reshape(1, -1)
    score = cosine_similarity(jd_vec, resume_vec)[0][0] * 100
    return round(score, 2)

if __name__ == "__main__":
    score = calculate_match_score("Python, ML", "Python, TensorFlow")
    print(f"Score: {score}%")
