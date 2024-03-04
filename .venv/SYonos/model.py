import pandas as pd
import numpy as np
import os
from sys import platform
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split


if platform == "darwin":
    os.chdir('/Users/dhyanadesai/Downloads')
else:
    os.chdir('C:\\Users\\anany\\Downloads')


file = 'DataProcessed.csv'

df = pd.read_csv(file)

# print(f'OP <-> LIFESPAN:  {df["OP"].corr(df["LIFESPAN"])}')
# print(f'SO <-> LIFESPAN:  {df["SO"].corr(df["LIFESPAN"])}')


model = Sequential()
model.add(Dense(32, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1))

model.compile(loss='mse', optimizer='adam', metrics=['mse'])

x = (df[['OP', 'SO']].to_numpy()-1)/4

# print(x)

# x = df['OP'].to_numpy()

# x  = np.array(range(100))

y = (df['LIFESPAN'].to_numpy()-82)/46

# y = (np.array(range(100)) + 10)

# print(x)
# print(y)

# print(x)
# print(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model.fit(x_train, y_train, epochs=100, batch_size=7000)

# model.fit(x, y, epochs=100, batch_size=40)

model.save('ModelLongevity.keras')

# y_pred = model.predict(x_test)
#
# error = y_test-y_pred
#
# count = np.count_nonzero(abs(error) < 1.5)
#
# print(f'Accuracy: {count/len(error)}')
#
#
# loss, accuracy = model.evaluate(x_test, y_test)
#
# print(f'Loss: {loss}')
# print(f'Mean Average Percentage Error: {accuracy}')


# print(f'OP <-> SO:  {df["OP"].corr(df["SO"])}')







# df1.to_csv('DataModel.csv')