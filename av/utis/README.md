# Util functions for self-driving cars

### Tire diameter

  1. Measure the distance between herself and an object directly behind her.
  2. Turn her wheels exactly one full rotation.
  3. Make the same distance measurement again.
  4. Use the measurements from 1 and 3 to calculate the distance traveled. This is the current circumference of her tires.
  5. Perform the appropriate math to compute the current diameter of her tires.
  > See more in [tire.py](tire.py)

### Latitudinal Acceleration
How to not slide off the track?

The equation for lateral acceleration (side to side acceleration) is:

 <img src="https://render.githubusercontent.com/render/math?math=a_{\text{lat}} = \frac{v^2}{R}">

Where **_v_** is velocity and **_R_** is the turning radius.


