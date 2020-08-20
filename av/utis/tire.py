""" 
How to calculate the tire diameter?

  1. Measure the distance between herself and an object directly behind her.
  2. Turn her wheels exactly one full rotation.
  3. Make the same distance measurement again.
  4. Use the measurements from 1 and 3 to calculate the distance traveled. This is the current circumference of her tires.
  5. Perform the appropriate math to compute the current diameter of her tires.

"""
from math import pi

def get_tire_diameter(dist_before_turn, dist_after_turn):    
    circumference = dist_after_turn - dist_before_turn
    diameter = circumference / pi
    return diameter