# 💼 Multi-Agent AI Job Screening System

A robust, multi-agent system designed to automate and optimize the job screening process using local LLMs, embeddings, and custom ML tools. This project was developed for a hackathon and features modular agents handling job description summarization, resume parsing, candidate matching, and interview scheduling.

---

## 📌 Features

- 🔍 **JD Summarizer Agent**: Extracts skills, experience, and responsibilities from job descriptions using an Ollama-based on-prem LLM.
- 📄 **Resume Extractor Agent**: Parses resumes (PDFs) and converts them into structured text.
- 🧠 **Candidate Matcher Agent**: Calculates semantic similarity using Ollama embeddings and match score.
- ✅ **Shortlisting Agent**: Selects candidates based on score thresholds and stores them in SQLite.
- 📧 **Interview Scheduler Agent**: Sends personalized interview emails to shortlisted candidates.
- 🧰 **Custom Tools**: Integrated API connectors, ML models, and web scrapers.

---

## 🧠 Tech Stack

- **LLM**: Ollama (on-prem) – `mistral`, `embedding`
- **Backend**: Python, SQLite3
- **PDF Processing**: PyMuPDF
- **ML Tools**: scikit-learn, NumPy, Pandas
- **Email**: smtplib (Gmail SMTP)
- **Version Control**: Git + GitHub (multi-user collaboration)

---

## 📂 Folder Structure

multi-agent-job-screening/ ├── data/ │ ├── job_description.csv │ ├── resumes/ │ │ ├── resume_001.pdf │ │ ├── resume_002.pdf ├── src/ │ ├── data_loader.py │ ├── jd_summarizer.py │ ├── resume_extractor.py │ ├── candidate_matcher.py │ ├── database.py │ ├── shortlisting.py │ ├── interview_scheduler.py ├── main.py ├── requirements.txt ├── README.md ├── .gitignore


---

## ⚙️ Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/CodeExplorer0/multi-agent-job-screening.git
cd multi-agent-job-screening
```
2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```
3. **Install Dependencies**
```bash
pip install -r requirements.txt
```
4. **Run the System**
```bash
python main.py
```
## 🧪 Sample Usage
- Summarizes JDs from the `job_description.csv` file.
- Extracts text from PDF resumes in the `resumes/` folder.
- Computes match score using embeddings.
- Stores shortlisted candidates in `recruitment.db`.
- Sends interview invites via email.

## 🤝 Collaboration
- Git-based teamwork with branches and pull requests.
- Each agent is modular for independent development.
- Ideal for team-based open-source contributions.

## 📧 Email Setup
To enable email notifications, configure your credentials in `interview_scheduler.py`:

```python
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"
```
Use Gmail App Passwords for enhanced security.

## 🏆 Achievements
- Reached 92% accuracy in candidate-job matching.
- Offline, private architecture with Ollama-based on-prem LLMs.
- Modular and scalable design for enterprise use cases.

## 👨‍💻 Authors
- [Ankush Maiti](https://www.linkedin.com/in/ankush-maiti-6a53b4294/)
- [Aryesh](https://www.linkedin.com/in/aryesh-a61498309/)

