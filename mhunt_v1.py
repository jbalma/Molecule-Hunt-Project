import requests, pandas as pd


url = "https://www.fpbase.org/api/proteins/basic/?format=json"
df = pd.DataFrame(requests.get(url, timeout=60).json())
df = df.dropna(subset=["qy", "ex_max", "em_max"])
df["shift_meV"] = 1000 * (1240 / df.ex_max - 1240 / df.em_max)

print(df.head())
print(df.info())

best = df[df.qy >= 0.9].sort_values("shift_meV")
print(len(df), "proteins with a quantum yield")
print(best[["name", "ex_max", "em_max", "qy", "shift_meV"]].head(10))

