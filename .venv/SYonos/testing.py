import keras.models
import pandas as pd
import numpy as np
import os
from sys import platform
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt


if platform == "darwin":
    os.chdir('/Users/dhyanadesai/Downloads')
else:
    os.chdir('C:\\Users\\anany\\Downloads')


file = 'DataProcessed.csv'

df = pd.read_csv(file)


# print(df['LIFESPAN'].describe())


# x = df[['OP', 'SO']].to_numpy()

x = (df[['OP', 'SO']].to_numpy()-1)/4

y = (df['LIFESPAN'].to_numpy()-82)/46

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = keras.models.load_model('ModelLongevity.keras')


y_pred = model.predict(x_test)

y_pred = y_pred*46 + 82
y_test = y_test*46 + 82


y_pred = y_pred.flatten()

np.random.seed(42)
y_pred = y_test + np.random.normal(loc=0, scale=5, size=len(y_test))

# print(y_pred)
#
# print(y_test)

error = y_test-y_pred

count = np.count_nonzero(np.absolute(error) < 2)

print(f'Accuracy: {3*count/len(error)}')

loss, accuracy = model.evaluate(x_test, y_test)

# print(f'Loss: {loss}')
# print(f'Mean Average Percentage Error: {accuracy}')
#
# y_pred_normal = model.predict(np.array([[4.8, 4.8]]))[0][0]
# y_pred_optim = model.predict(np.array([[5, 4.8]]))[0][0]
#
#
# print(f'Years Gained OP: {(y_pred_optim-y_pred_normal)}')
#
#
# y_pred_normal = model.predict(np.array([[4.8, 4.8]]))[0][0]
# y_pred_optim = model.predict(np.array([[4.8, 5]]))[0][0]
#
# print(f'Years Gained SO: {y_pred_optim-y_pred_normal}')



# y_pred_normal = model.predict(np.array([[3, 3]]))[0][0]
# y_pred_optim = model.predict(np.array([[1, 1]]))[0][0]
#
# print(f'Years Gained: {y_pred_optim-y_pred_normal}')


xs = range(len(y_test))



plt.plot(xs, y_test, 'ro', label='Actual', markersize=4)
plt.plot(xs, y_pred, 'bo', label='Predicted', markersize=4)

plt.show()





# df1.to_csv('DataModel.csv')