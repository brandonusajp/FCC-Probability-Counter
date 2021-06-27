import random
import copy

class Hat:

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.contents = list()
        for k,v in kwargs.items():
            for i in range(v):
                self.contents.append(k)

    def draw(self,num_balls):
        self.pulled = list()
        if len(self.contents) < num_balls:
            num_balls = len(self.contents)
        
        for i in range(num_balls):
            self.pulled.append(self.contents.pop(random.randrange(len(self.contents))))
        return self.pulled

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0
    for i in range(num_experiments):
        pull_dict = {}
        found = True
        hat_copy = copy.deepcopy(hat)
        hat_copy.draw(num_balls_drawn)
        #print(hat_copy.pulled)
        for i in hat_copy.pulled:
            pull_dict[i] = hat_copy.pulled.count(i)
        for k,v in expected_balls.items():
            if k not in pull_dict:
                found = False
            elif expected_balls[k] > pull_dict[k]:
                found = False
        if found == True:
            success += 1

    probability = success / num_experiments
    print("probability:", probability)
    return probability

#test
why = Hat(yellow=5, red=1, green=3, blue=9, test=1)
print(why.contents)
experiment(why, {"yellow":2, "blue":3, "test": 1}, 22, 10)