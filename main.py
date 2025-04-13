from src.jd_summarizer import summarize_job_description
from src.resume_extractor import extract_text_from_pdf
from src.candidate_matcher import calculate_match_score
from src.database import insert_candidate, shortlist_candidates
from src.interview_scheduler import send_interview_email

jd_text = open("data/job_description.csv").read()
jd_summary = summarize_job_description(jd_text)

resumes = ["data/resumes/sample_resume.pdf"]
for resume in resumes:
    text = extract_text_from_pdf(resume)
    score = calculate_match_score(jd_summary, text)
    if score >= 80:
        insert_candidate("C001", "John Doe", ["Python", "AI"], "2 years", score)

for candidate in shortlist_candidates():
    send_interview_email("candidate@example.com", candidate[1])