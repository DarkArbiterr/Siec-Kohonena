import numpy as np

class Kohonen(object):
    def __init__(self, height, width, dimension, alpha, sigma):
        self.shape = (height,width,dimension)
        self.som = np.array([[(j/height, i/width) for i in range(width)] for j in range(height)])
        self.lamb = 300
        self.sigma = sigma
        self.alpha = alpha
        self.data = []
        self.step = 0

    def BestNeuron(self, start):
        listOfNeurons = []
        
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                self.som[i,j]
                distance = np.linalg.norm(start - self.som[i,j])
                listOfNeurons.append(((i,j),distance))
        listOfNeurons.sort(key=lambda x:x[1])
        return listOfNeurons[0][0]

    def G(self, distance):
        return np.exp(-distance**2/(2*self.sigma**2))

    def Alpha(self, t):
        return self.alpha * np.exp(-t/self.lamb)

    def RecordUpdate(self, record, dataPoint, st, distance):
        self.som[record] += self.Alpha(st) * self.G(distance) * (dataPoint - self.som[record])

    def SomUpdate(self, bestNeuron, dataPoint, step):
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                distanceToBestNeuron = np.linalg.norm(np.array(bestNeuron) - np.array([i,j]))
                self.RecordUpdate((i,j), dataPoint, step, distanceToBestNeuron)

    def Training(self, data):
        self.data = data
        i = np.random.choice(range(len(self.data)))
        bestNeuron = self.BestNeuron(self.data[i])
        self.SomUpdate(bestNeuron, self.data[i], self.step)
        self.step += 1
        

    
