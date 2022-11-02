import pandas as pd

newFile = open("fertility_and_child_mortality.csv","w+")

fert = pd.read_csv("bgd_fertility.csv")
cm = pd.read_csv("bgd_child_mortality.csv")
newTable = pd.read_csv("fertility_and_child_mortality.csv")

years = fert['Years']
fr = fert['Fertility Rate']
cmr = cm['Child Mortality Rate']

newTable['Years'] = years
newTable['Fertility Rate'] = fr
newTable['Child Mortality Rate'] = cmr
