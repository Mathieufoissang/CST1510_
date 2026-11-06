# Warm-up 3: convert numbers stored as text before doing arithmetic.

import pandas as pd

df = pd.DataFrame({"value": ["87", "120", "45"], "limit": [100, 100, 100]})

df["value"] = pd.to_numeric(df["value"])
df["percent"] = (df["value"] / df["limit"]) * 100
print(df)
