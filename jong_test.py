import matplotlib.pyplot as plt
import numpy as np
from keras.models import Sequential
from keras.layers import Dense

pp = ['KJPLTE089','KJPLTE029','NWY24LTE2','NWY24LTE1','NWY24LTE3','NBIGI0001','KDRTLTE70','KDRTLTE45', 'KDRTLTE90']

# train 데이터셋 구성
train_set = np.genfromtxt("jong_train", delimiter=",", dtype="str", replace_space="0", autostrip=True, encoding='UTF-8')
x_train = train_set[:, 1:]
y_train = train_set[:, :1]

## input factor를 float로 변경
x_train2 = []
for xt in x_train:
    temp_x = []
    for xtt in xt:
        temp_x.append(float(xtt))

    x_train2.append(temp_x)

## 요금제 명칭을 숫자로 변경
for ytr, trp in enumerate(y_train):
    y_train[ytr] = pp.index(trp)


# test 데이터셋 생성
test_set = np.genfromtxt("jong_test", delimiter=",", dtype="str", replace_space="0", autostrip=True, encoding='UTF-8')
x_test = test_set[:, 1:]
y_test = test_set[:, :1]

"""
## input factor를 float로 변경
x_test2 = []
for xtt in x_test:
    temp_x = []
    for xttt in xtt:
        temp_x.append(float(xttt))

    x_test2.append(temp_x)
"""

## 요금제 명칭을 숫자로 변경
for yts, tsp in enumerate(y_test):
    y_test[yts] = pp.index(tsp)

# 2. 모델 구성하기
model = Sequential()
model.add(Dense(64, input_dim=14, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(10, activation='softmax'))
#model.add(Dense(38, input_dim=14, activation='softmax'))

# 3. 모델 학습과정 설정하기
model.compile(optimizer='rmsprop', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# 4. 모델 학습시키기
hist = model.fit(x_train2, y_train, epochs=10, batch_size=64)

# 5. 학습과정 살펴보기
fig, loss_ax = plt.subplots()

acc_ax = loss_ax.twinx()

#loss_ax.set_ylim([0.0, 1.0])
#acc_ax.set_ylim([0.0, 1.0])

loss_ax.plot(hist.history['loss'], 'y', label='train loss')
acc_ax.plot(hist.history['acc'], 'b', label='train acc')

loss_ax.set_xlabel('epoch')
loss_ax.set_ylabel('loss')
acc_ax.set_ylabel('accuracy')

loss_ax.legend(loc='upper left')
acc_ax.legend(loc='lower left')

plt.show()

# 6. 모델 평가하기
loss_and_metrics = model.evaluate(x_test2, y_test, batch_size=10)
print('loss_and_metrics : ' + str(loss_and_metrics))
