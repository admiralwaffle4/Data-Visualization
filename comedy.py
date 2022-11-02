import pandas as pd
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

df = pd.read_csv("shows.csv")

countryToNumber = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(countryToNumber)
goneToNumber = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(goneToNumber)

print(df)

features = ['Age', 'Experience', 'Rank', 'Nationality']

X = df[features]
y = df['Go']

print(X)
print(y)

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('mydecisiontree.png')

img=pltimg.imread('mydecisiontree.png')
imgplot = plt.imshow(img)
plt.show()


def predict(age,experience,rank,nationality):
    if nationality.lower() == "usa":
        nationalityInt=1
    elif nationality.lower() == "uk":
        nationalityInt=0
    else :
        nationalityInt=2
    dtree.predict([[age,experience,rank,nationalityInt]])

print(predict(45,12,7,"UK"))