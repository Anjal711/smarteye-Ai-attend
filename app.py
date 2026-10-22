
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# Public demo data only. No real student records.
DEMO_STUDENTS = 12

DEMO_RECORDS = [
    {
        "Student ID": "DEMO001",
        "Name": "Demo Student",
        "Date": datetime.now().strftime("%Y-%m-%d"),
        "Time": "09:15:00",
        "Status": "Present",
    },
    {
        "Student ID": "DEMO002",
        "Name": "Sample Student",
        "Date": datetime.now().strftime("%Y-%m-%d"),
        "Time": "09:22:00",
        "Status": "Present",
    },
]


@app.route("/")
def home():
    return render_template(
        "index.html",
        total_students=DEMO_STUDENTS,
        present_today=len(DEMO_RECORDS),
        records=DEMO_RECORDS,
    )


if __name__ == "__main__":
    app.run(debug=True)
