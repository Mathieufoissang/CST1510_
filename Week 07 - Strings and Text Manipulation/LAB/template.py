"""Record Check - AI / Data Science worked example.

Name: Mathieu Foissang
Lane: AI / Data Science
Run: python template.py

"""

def parse_line(raw_line):

    parts = raw_line.strip().split(",")

    survey_name = parts[0].strip().upper()

    data = {}

    for part in parts[1:]:
        key, value = part.split("=")

        key = key.strip().lower()
        value = value.strip()

        data[key] = value

    return {
        "survey": survey_name,
        "rating": int(data["rating"]),
        "age": int(data["age"])
    }
def status_of(record):

    if record["rating"] < 3:
        return "FLAGGED"
    else:
        return "OK"

sample_records = [
    "  Survey_2026 , rating=4 , age=23  ",
    "SURVEY_2026,RATING=2,AGE=19",
    " survey_2026 , Rating = 5 , Age = 30 ",
    "Survey_2026,rating=1,age=21",
    "  SURVEY_2026 , RATING = 3 , AGE=25 ",
    "Survey_2026, rating=abc, age=22"
]

with open("survey_records.txt", "w") as file:
    for record in sample_records:
        file.write(record + "\n")

raw_records = []

with open("survey_records.txt", "r") as file:
    for line in file:
        raw_records.append(line.strip())

total_records = 0
flagged_records = 0
error_records = 0

for raw_record in raw_records:

    total_records += 1
    try:
        cleaned_record = parse_line(raw_record)

        status = status_of(cleaned_record)

        print(cleaned_record, "Status:", status)

        if status == "FLAGGED":
            flagged_records += 1

    except (ValueError, KeyError) as error:
        error_records += 1
        print("ERROR:", error)

print("\n--- FINAL SUMMARY ---")

print(
    f"Total records: {total_records}, "
    f"Flagged: {flagged_records}, "
    f"Errors: {error_records}"
)
