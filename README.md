# 396 Assignment 7

## The Code

My creature grows up along the z-axis, then out in the -x, +x, -y, and +y directions. It is spider-like, except that there are 4 legs instead of 8. Each of the 4 "legs" contains the same number of links, the dimensions of which are constrained by [0,1], and which are jointed at the base of each. The body, or the vertical portion, always contains 2 links, while the number of links in the leg is constrained by [4,8), to ensure that the legs can reach the ground. A random integer selector decides whether or not to place a sensor neuron in the current link, while every joint receives a motor neuron. To form the brain, every motor neuron is connected to a randomly selected sensor neuron. Each synapse is given a random weight, which is a floating point number contrainted by [-1,1].

## Possible Creatures

The body shape influences the behavior of the robot. For example, if the lower link in the body has a small x or y dimension and a larger z dimension, it will be unstable and likely fall to the side. However, if the lower link in the body has a larger base, or is more cube-like, it will promote more stability in motion. Furthermore, if there are many (7 or 8) links in the legs, that means there are more joints, and the legs will be able to cause larger but less precise movements. Meanwhile, if the number of links in the legs is closer to the lower bound (4), they will only be able to cause slight, although more precise, movement. There is a tradeoff between size of movements and precision of movements.

## The Robot

![alt text](https://github.com/juliagangi/mybots/blob/3DCreature/fromabove.png?raw=true)

![alt text](https://github.com/juliagangi/mybots/blob/3DCreature/below.png?raw=true)

## Running It

First, clone my repo to your computer.

To watch a series of random spiders being generated, run spiders.py or run this command:

```bash
python3 spiders.py
```

## Videos

Click this link to watch snakes generate: <https://youtu.be/kq59Hvzztgg>

## Credit

credit goes to r/ludobots <https://www.reddit.com/r/ludobots/> and pyrosim

