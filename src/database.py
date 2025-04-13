import sqlite3

conn = sqlite3.connect("recruitment.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS candidates (
    id TEXT, name TEXT, skills TEXT, experience TEXT, match_score REAL)''')

def insert_candidate(cid, name, skills, exp, score):
    cursor.execute("INSERT INTO candidates VALUES (?, ?, ?, ?, ?)",
                   (cid, name, str(skills), exp, score))
    conn.commit()

def shortlist_candidates():
    cursor.execute("SELECT * FROM candidates WHERE match_score >= 80")
    return cursor.fetchall()

if __name__ == "__main__":
    insert_candidate("C001", "John", ["Python"], "2 years", 85)
    print(shortlist_candidates())