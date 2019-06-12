import matplotlib.pyplot as plt
import numpy as np
from keras.models import Sequential
from keras.layers import Dense


# train 데이터셋 구성
train_set = np.genfromtxt("training_set_call.csv", delimiter=",", dtype="str", replace_space="0", autostrip=True)
x_train = train_set[:39606, 2:]
y_train = train_set[:39606, :1]
for i, x in enumerate(x_train):
        x_train[i] = [float(xx) for xx in x]

for j, y in enumerate(y_train):
    if y == 'y':
        y_train[j] = 1
    else:
        y_train[j] = 0


# train 데이터셋 생성
test_set = np.genfromtxt("test_set_call.csv", delimiter=",", dtype="str", replace_space="0", autostrip=True)
x_test = test_set[:9999, 2:]
y_test = test_set[:9999, :1]

for k, z in enumerate(x_test):
    x_test[k] = [float(yy) for yy in z]

for l, q in enumerate(y_test):
    if q == 'y':
        y_test[l] = 1
    else:
        y_test[l] = 0


# 2. 모델 구성하기
model = Sequential()
model.add(Dense(64, input_dim=116, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# 3. 모델 학습과정 설정하기
model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])

# 4. 모델 학습시키기
hist = model.fit(x_train, y_train, epochs=100, batch_size=64)

# 5. 학습과정 살펴보기
fig, loss_ax = plt.subplots()

acc_ax = loss_ax.twinx()

#loss_ax.set_ylim([0.0, 1.0])
#acc_ax.set_ylim([0.0, 1.0])

loss_ax.plot(hist.history['loss'], 'y', label='train loss')
acc_ax.plot(hist.history['acc'], 'b', label='train acc')

loss_ax.set_xlabel('epoch')
loss_ax.set_ylabel('loss')
acc_ax.set_ylabel('accuray')

loss_ax.legend(loc='upper left')
acc_ax.legend(loc='lower left')

plt.show()

# 6. 모델 평가하기
loss_and_metrics = model.evaluate(x_test, y_test, batch_size=64)
print('loss_and_metrics : ' + str(loss_and_metrics))
