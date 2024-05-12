import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://127.0.0.1:5500/E8_Scrapping_Web/source/index.html"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

skills_arr = []
exp_arr = []

skills = soup.select("div.main .div .name")
for skill in skills:
    skills_arr.append(skill.text)

exps = soup.select("div.main .div .exp")
for exp in exps:
    exp_arr.append(exp.text)

main_dict = {
    "Skills" : skills_arr,
    "Experience" : exp_arr,
}

df = pd.DataFrame(main_dict)
df.to_csv("output.csv", index=False)

print("CSV file created successfully!")
