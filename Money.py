import numpy as np
import matplotlib.pyplot as plt

дни = np.arange(1, 31)
доходы = [1000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
расходы = [200, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
прибыль = np.subtract(доходы, расходы)

#создание графика
fig, ax = plt.subplots()
ax.plot(дни, доходы, label = 'Доходы')
ax.plot(дни, расходы, label = 'Расходы')
ax.plot(дни, прибыль, label = 'Прибыль')

#Настройка внешнего вида
ax.set_xlabel('День месяца')
ax.set_ylabel('Деньги')
ax.set_title('График доходов расходов и прибыли по дням')
ax.legend()

plt.show()

'''
Этот код создаёт график с тремя линиями, показывающими доходы, расходы и прибыль
в течении 30 дней. Дни месяца на оси X и деньги на оси Y.
'''