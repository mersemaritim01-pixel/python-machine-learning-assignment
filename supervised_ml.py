from sklearn.linear_model import LinearRegression
import numpy as np
X=np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
Y=np.array([30,40,45,55,65,70,80,85,90,95])
#preopare training data
#feature (houes studied)
X=[[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
#labels
Y=[30,40,45,55,65,70,80,85,90,95]
#create the Linear Regression model
model=LinearRegression()
#train yhe model
model.fit(X,Y)
#ask the user to enter hours studied
hours=float(input("Enter hours studied:"))
#make predictions
prediction=model.predict([[hours]])
print(round(prediction[0],2))

#visualize the data
import matplotlib.pyplot as plt
plt.scatter(X,Y,label="Actual score")
plt.plot(X,model.predict(X), label="regression line")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.title("Hours Studied VS Exam Scores")
plt.legend()
plt.grid(True)
plt.show()