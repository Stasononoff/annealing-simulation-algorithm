import numpy as np

def DecreaseTemperature(init_t, i):
#     T = init_t  / (i+1)              # Быстрый отжиг Коши
    T = init_t *0.1/ (np.log(2 + i)) # Больцмановский отжиг
    return T

def GetTransitionProbability( dE, T):
    P = np.exp(-dE/T) # Расчитаем вероятность перехода из Больцмановского распределения 
    return P

def MakeTransit(probability):
    value = np.random.random(); 
    if(value <= probability): # Смоделируем вероятностный переход
        a = True;
    else:
        a = False; 
    return a
    

def GenerateStateCandidate(seq1):
    seq = seq1.copy()

    n = seq.shape[0]  # Количество городов
    i = np.random.randint(n) # Порядковые номера двух 
    j = np.random.randint(n) # городов для перестановки
    
    if(i > j):  # Меняем порядок прохождения городов между выбранной парой
        seq[j:i+1] = seq[j:i+1][::-1]
    else:
        seq[i:j+1] = seq[i:j+1][::-1]  
    return seq

def CalculateEnergy(state, cities): # В данной задаче в качестве функции потерь (энергии системы) принята дляна пути между городами в Евклидовом пространстве
    dist = 0
    for i in range(state.shape[0]-1):
        dist += np.sqrt((cities[0][state[i+1]] - cities[0][state[i]])**2 + 
                        (cities[1][state[i+1]] - cities[1][state[i]])**2)

    dist += np.sqrt((cities[0][state[0]] - cities[0][state[-1]])**2 + 
                        (cities[1][state[0]] - cities[1][state[-1]])**2) # Расстояние от последнего города до первого , тк задача замкнутая
    return dist
        
    
