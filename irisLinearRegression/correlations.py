# Laura Nichols
# 9 December 2017

import pandas
import seaborn
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, ShuffleSplit, cross_val_score, KFold,learning_curve
import numpy
import lcplot

def myPredict(x,model):
	return x*model.coef_ + model.intercept_


# Data path
dataPath = r"C:/Users/LJUDY/Desktop/MyStuff/Classes/Fall 2017/PythonWorkshop/data/"

# File name
fileName = "iris.csv"

# Read csv file using built in pandas function
# Data is imported as a data frame
data = pandas.read_csv(dataPath + fileName)


# Want to predict petal width using petal length
seaborn.lmplot(x='PetalWidth',y='PetalLength',data=data)

x = data[['PetalLength']]
y = data['PetalWidth']

# Make model
model = LinearRegression()
model.fit(x,y)

# Get coefficients
model.coef_
model.intercept_

# Use your model to predict
model.predict([[1.5], [1.3], [2.0]])

# Evaluate model

xTrain, xTest, yTrain, yTest = train_test_split(x,y,train_size=0.9)

model.fit(xTrain,yTrain)
print('Score: ', model.score(xTest,yTest))

# Only doing one split can be biased. Need to cross validate by
# taking the average of multiple splits

cv = ShuffleSplit(n_splits=100,train_size=0.9)
scores = cross_val_score(model,x,y,cv=cv)
scores
scores.mean()


# Could have left out certain data points which could make your 
# model worse
# Can use k fold cross validations

score = cross_val_score(model,x,y,cv=KFold(n_splits=10,shuffle=True))
score.mean()

# Look at how much model improves based on experience
train_sizes, train_scores, valid_scores = learning_curve(model,x,y,train_sizes=numpy.linspace(0.1,1,10), cv=KFold(n_splits=10,shuffle=True))

# Training score and testing score are scoring based on training and testing 
# score. If there is a big difference, we need to learn more. If not, our
# model is good.

lcplot.plot(model,x,y,cv=KFold(n_splits=10,shuffle=True))




