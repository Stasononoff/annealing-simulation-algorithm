import numpy as np
from matplotlib import pyplot as plt

def plot_graph(cities, state, Title = 'Путь коммивояжера до оптимизации'):  # Отрисуем путь коммивояжера между городами
    cities_np = np.array(cities)
    
    fig, ax = plt.subplots(figsize = (10,10))
    ax.set_title(label = Title)
    ax.set_xlabel(xlabel = 'X координата городов')
    ax.set_ylabel(ylabel = 'Y координата городов')
    ax.scatter(cities_np[0], cities_np[1])
    ax.plot(cities[0][state],cities[1][state])
    ax.plot(cities[0][[state[0],state[-1]]],cities[1][[state[0],state[-1]]], label = 'Дорога между последним и первым городом')
    ax.scatter(cities_np[0][state[0]], cities_np[1][state[0]], label = 'Первый город', color = 'r')
    ax.scatter(cities_np[0][state[-1]], cities_np[1][state[-1]], label = 'Последний город', color = 'g')
    plt.legend()
    plt.show()
    
def plot_hist(E_hist, T_hist): # Отрисуем изменение энергии и температуры в процессе оптимизации

    fig1, ax1 = plt.subplots()
    fig2, ax2 = plt.subplots()
    
    ax1.set_title(label = 'Зависимость функции потерь от иттерации')
    ax2.set_title(label = 'Зависимость температуры от иттерации')
    
    ax1.set_xlabel(xlabel = 'Иттерация алгоритма')
    ax1.set_ylabel(ylabel = 'Значение функции потерь')
    
    ax2.set_xlabel(xlabel = 'Иттерация алгоритма')
    ax2.set_ylabel(ylabel = 'Температура')
    
    ax1.plot(E_hist)
    ax2.plot(np.log(T_hist))
    
#     plt.legend()
    plt.show()
    
