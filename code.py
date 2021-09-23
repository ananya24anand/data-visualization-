import pandas as pd
from matplotlib import pyplot as py
df = pd.read_csv("Latest Covid-19 India Status.csv")

#Maharashtra has the highest number of cases
states = []
for i in df["State/UTs"]:
    states.append(i)
"""py.scatter(states, df["Total Cases"])
py.xticks(rotation=90)
py.xlabel("States")
py.ylabel("Cases")
py.title("STATE WISE CASES")
py.show()

#Total and discharged
py.bar(states, df["Total Cases"], label = "Overall Cases", color = "mediumorchid", width = 0.8)
py.bar(states, df["Discharged"], label = "Discharged", color = "mediumspringgreen", width = 0.4)
py.xticks(rotation = 90)
py.xlabel("States")
py.ylabel("Cases")
py.title("DISCHARGED CASES OUT OF THE TOTAL CASES")
py.legend()
py.show()"""

#Active, discharge and death ratio
active = df["Active Ratio (%)"].mean()
cure = df["Discharge Ratio (%)"].mean()
death = df["Death Ratio (%)"].mean()
case = [active,cure,death]
label = ["Active Cases", "Discharged Cases", "Deaths"]
color = ["cyan", "springgreen", "plum"]
py.pie(case, colors = color, shadow = True, explode = (0.1,0.3,0.1))
py.legend(labels =[f'{l}, {s:0.1f}%' for l, s in zip(label, case)], loc = "upper right")
py.title("ACTIVE, DISCHARGED AND DEATH RATES")
py.show()






