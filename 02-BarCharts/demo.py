from matplotlib import pyplot as plt
from collections import Counter
import pandas as pd

plt.style.use("fivethirtyeight")

data = pd.read_csv('data.csv')
responder_ids = data['Responder_id']
languages_worked_with = data['LanguagesWorkedWith']

# print(type(languages_worked_with))
language_counter = Counter()
for response in languages_worked_with:
    language_counter.update(response.split(';'))

languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)

plt.title("Most Popular Languages")
plt.xlabel("Number of People Who Use")

plt.tight_layout()
plt.savefig('plot.png')
plt.show()
