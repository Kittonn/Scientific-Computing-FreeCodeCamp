import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self,**kwargs):
    self.contents = []
    for (i,v) in kwargs.items():
      for j in range(v):
        self.contents.append(i)
  def draw(self,number_balls):
    if number_balls > len(self.contents):
      return self.contents
    else:
      return [self.contents.pop(random.randrange(len(self.contents))) for i in range(number_balls)]

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  M = 0
  for i in range(num_experiments):
    expected_balls_copy = copy.deepcopy(expected_balls)
    hat_copy = copy.deepcopy(hat)
    ball_draw = hat_copy.draw(num_balls_drawn)
    count = 0
    for color in ball_draw:
      if color in expected_balls_copy:
        expected_balls_copy[color] -= 1
    for color in expected_balls_copy:
      if expected_balls_copy[color] <= 0:
        count += 1
    if count == len(expected_balls_copy):
      M +=1 
  return int(M) / num_experiments
    
