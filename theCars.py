import numpy as np

class Cars:
    name = [0,1,2,3,4,5,6,8,9,10,11,12]
    brand = ["BMW","Volvo","VW","VW","Ford","VW","Tesla","BMW","Volvo","Ford","Toyota","VW","Toyota"]
    color = ["red","black","gray","white","white","white","red","black","gray","white","gray","white","blue"]
    age = [5,4,8,7,2,17,2,9,4,11,12,9,6]
    speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
    autoPass = [True,True,False,True,True,True,True,True,False,False,False,False,True]

    meanS = np.mean(speed)
    medianS = np.median(speed)
    stDevS = np.std(speed)

    meanA = np.mean(age)
    medianA = np.median(age)
    stDevA = np.std(age)

    def carList(self):
        for i in range(len(self.name)+1):
            if self.autoPass[i]:
                print(f"Car {i} is a {self.brand[i]} that is {self.age[i]} years old, has an average speed of {self.speed[i]}, and has an AutoPass.")
            if self.autoPass[i] == False:
                print(f"Car {i} is a {self.brand[i]} that is {self.age[i]} years old, has an average speed of {self.speed[i]}, and does not have an AutoPass.")
    
    def MMM(self):

        print(f"The mean of the speeds is {self.mean}, the median is {self.median}, and the standard deviation is {self.stDev}.")


cars = Cars()
