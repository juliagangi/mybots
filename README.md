# 396 Assignment 7

## The Code

#### The body
My creature grows up along the z-axis, then out in the -x, +x, -y, and +y directions. It is spider-like, except that there are 4 legs instead of 8. Each of the 4 "legs" contains the same number of links, the dimensions of which are constrained by [.5,1.5], and which are jointed at the base of each. The joint axis for each joint is randomly generated. The body, or the vertical portion, always contains 2 links, while the number of links in the leg is constrained by [4,7], to ensure that the legs can reach the ground. 

#### The brain
Every link has a 3 in 5 chance of receiving a sensor neuron: if the integer randomly selected from [0,4] is greater than 1, a sensor neuron is placed in the given link. Every joint receives a motor neuron. To form the brain, every motor neuron is connected to a randomly selected sensor neuron. Each synapse is given a random weight, which is a floating point number constrained by [-1,1]. 

## Possible Creatures

The body shape influences the behavior of the robot. For example, if the lower link in the body has a small x or y dimension and a larger z dimension, it will be unstable and likely fall to the side. However, if the lower link in the body has a larger base, or is more cube-like, it will promote more stability in motion, although if it has dimensions that are too close to the upper bound (1), it will be harder for the legs to drag. Furthermore, if there are many (7 or 8) links in the legs, that means there are more joints, and the legs will be able to cause larger but less precise movements. Meanwhile, if the number of links in the legs is closer to the lower bound (4), they will only be able to cause slight, although more precise, movement. There is a tradeoff between size of movements and precision of movements.

## The Robot
![alt text](https://github.com/juliagangi/mybots/blob/3DCreature/cycles.png?raw=true)

![alt text](https://github.com/juliagangi/mybots/blob/3DCreature/fromabove.png?raw=true)

![alt text](https://github.com/juliagangi/mybots/blob/3DCreature/fromside.png?raw=true)

## Running It

First, clone my repo to your computer.

To watch a series of random spiders being generated, run spider.py or run this command:

```bash
python3 spider.py
```

## Videos

Click this link to watch snakes generate: <https://youtu.be/l9f6s1ssYkY>

## Credit

Credit goes to r/ludobots <https://www.reddit.com/r/ludobots/> and pyrosim

