import requests
import pandas as pd

url = "https://api.github.com/repos/pandas-dev/pandas/issues"

resp = requests.get(url)

# Check for HTTP errors
resp.raise_for_status()

data = resp.json()

# data is a python dictionary
print(data[0]["title"])

issues = pd.DataFrame(data, columns=["number", "title", "labels", "state"])
print(issues)