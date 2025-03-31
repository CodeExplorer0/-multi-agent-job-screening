import pandas as pd

def load_job_descriptions(csv_path):
    df = pd.read_csv(csv_path, encoding="Windows-1252")
    df = df[['Job Title', 'Job Description']].dropna()  # Drop empty rows
    df['Job Description'] = df['Job Description'].str.replace('\n', ' ')  # Remove newline chars
    return df

if __name__ == "__main__":
    jobs = load_job_descriptions("../data/job_description.csv")
    print(jobs.head())