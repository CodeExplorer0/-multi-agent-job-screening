import ollama

def summarize_job_description(jd_text):
    prompt = f"Summarize the job description, extract skills, experience, and responsibilities:\n{jd_text}"
    response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"]

if __name__ == "__main__":
    with open("../data/job_description.csv", encoding="Windows-1252") as f:
        jd_text = f.read()

    summary = summarize_job_description(jd_text)
    print(summary)
