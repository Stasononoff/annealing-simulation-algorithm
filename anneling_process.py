import numpy as np

from functions import *


def SimulatedAnnealing( cities, initialTemperature, endTemperature):
    
    energy_history = []
    t_history = []
    
    
    n = cities.shape[1]
    
    state = np.random.permutation(n)
    currentEnergy = CalculateEnergy(state, cities)
    T = initialTemperature
    
    
    
    for i in range(100000):
        
        
        stateCandidate = GenerateStateCandidate(state)
        candidateEnergy = CalculateEnergy(stateCandidate, cities)
        
        if(candidateEnergy < currentEnergy): # если кандидат обладает меньшей энергией
            currentEnergy = candidateEnergy; # то оно становится текущим состоянием
            state = stateCandidate;
        else:
            p = GetTransitionProbability(candidateEnergy-currentEnergy, T)# иначе, считаем вероятность
            if (MakeTransit(p) == True): # и смотрим, осуществится ли переход
                currentEnergy = candidateEnergy
                state = stateCandidate

        
       
        t_history.append(T)
        energy_history.append(currentEnergy)
        
        T = DecreaseTemperature(initialTemperature, i) # уменьшаем температуру отжига
        
        if(T <= endTemperature): # условие выхода
            break
            

    
            
    return energy_history, t_history, state 
            
    