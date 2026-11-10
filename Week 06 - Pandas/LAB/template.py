
"""
RECORD CHECK  -  completed pandas version
===========================

Name  : Mathieu Foissang
Lane  : AI / Data Science
Date  : 06/11/2026


"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("records_sample.csv")


df["percent"] = (df["value"] / df["limit"]) * 100
df["status"] = df["percent"].apply(
    lambda percent: "OVER LIMIT" if percent >= 100 else "WARNING" if percent >= 90 else "OK"
)

print(df)
print("\nRecords that need attention:")
print(df[df["status"] != "OK"])

print("\nRecord count by status:")
status_counts = df["status"].value_counts()
print(status_counts)

df.to_csv("records_report.csv", index=False)

status_counts.plot(kind="bar", title="Records by Status")
plt.xlabel("Status")
plt.ylabel("Number of records")
plt.tight_layout()
plt.savefig("status_counts.png")
plt.show()
