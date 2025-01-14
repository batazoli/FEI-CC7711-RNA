#Giovana Ellero Vieira (RA: 22.220.003-2)
#Vagner Batazoli Pereira Filho (RA: 22.217.022-7)

import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor

print('Carregando Arquivo de teste')
arquivo = np.load('teste1.npy')
x = arquivo[0]
y = np.ravel(arquivo[1])

regr = MLPRegressor(hidden_layer_sizes=(2),
                    max_iter=100000,
                    activation='relu', #{'identity', 'logistic', 'tanh', 'relu'},
                    solver='adam',
                    learning_rate = 'adaptive',
                    n_iter_no_change=50)
print('Treinando RNA')
regr = regr.fit(x,y)

print('Preditor')
y_est = regr.predict(x)

print("Média: %.2f"%np.mean(y_est))
print("Desvio Padrão: %.2f"%np.std(y_est))

plt.figure(figsize=[14,7])

#plot curso original
plt.subplot(1,3,1)
plt.plot(x,y)

#plot aprendizagem
plt.subplot(1,3,2)
plt.plot(regr.loss_curve_)

#plot regressor
plt.subplot(1,3,3)
plt.plot(x,y,linewidth=1,color='yellow')
plt.plot(x,y_est,linewidth=2)

plt.show()
