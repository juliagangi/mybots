# 396 Assignment 8

## The Code

#### The body
My creature originates from a central link and grow out in the -x, +x, -y, and +y directions, and finally down in the -z direction. It is spider-like, except that there are 4 legs instead of 8. Each of the 4 "legs" contains the same number of links, the dimensions of which are constrained by [.5,1.5], and which are jointed at the vertical center of each. The vertical portions of the legs are jointed in the horizontal center. The joint axis for each joint is randomly generated. The number of links in the upper legs is constrained by [1,5] while the number of links in the lower legs is constrained by [1,3]. 

#### The brain
Every link has a 3 in 5 chance of receiving a sensor neuron: if the integer randomly selected from [0,4] is greater than 1, a sensor neuron is placed in the given link. Every joint receives a motor neuron. To form the brain, every motor neuron is connected to a randomly selected sensor neuron. Each synapse is given a random weight, which is a floating point number constrained by [-1,1]. A synapse could create a connection between a link and a joint that are separated by many links and joints -- there is no restriction, besides numerical bounds, on how links can influence joints.

## Possible Creatures

The body shape influences the behavior of the robot. For example, if the robot is tall but has few links in the upper legs, it will be unstable and may fall over. Alternately, if the robot has many links in the upper legs, it will be more stable, with smaller and more precise movements, but the central link may sink towards the ground, causing friction and impeding movement. Consequently, the behavior of the robot depends on the ratio of height to leg length: for optimal motion, the spider should be slightly shorter than its length. Regardless, the width must be able to support movement of the legs to prevent toppling. There is a tradeoff between size of movements and precision/success of movements.

## The Robot
![alt text](https://github.com/juliagangi/mybots/blob/3DEvolved/robotcycle.png?raw=true)

![alt text](https://github.com/juliagangi/mybots/blob/3DEvolved/aboveview.png?raw=true)

![alt text](https://github.com/juliagangi/mybots/blob/3DEvolved/sideview.png?raw=true)

## Running It

First, clone my repo to your computer.

To watch a random spider, run this command:

```bash
python3 run.py random
```

To watch a final evolved spider, run this command:

```bash
python3 run.py evolved
```

## Videos

Click this link to watch a comparison between a random and evolved creature.

## Credit

Credit goes to r/ludobots <https://www.reddit.com/r/ludobots/> and pyrosim

