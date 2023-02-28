# 396 Assignment 8

## The Code

#### The body
My creature originates from a central link, with a fixed size, and has arms that grows out in at least 1 of the following directions: -x, +x, -y, and +y. As links are added, the z-coordinate is increased so links are connected at their edges, not faces. Each of the 4 arms contains a random number of links, constrained by [1,5], with the dimensions being constrained by [0,1]. The joint axis for each joint is randomly generated. 

#### The brain
Every link has a 3 in 5 chance of receiving a sensor neuron: if the integer randomly selected from [0,4] is greater than 1, a sensor neuron is placed in the given link. Every joint receives a motor neuron. To form the brain, every motor neuron is connected to the sensor neurons in adjoining links (if they exist). Each synapse is given a random weight, which is a floating point number constrained by [-1,1].

## Possible Creatures

The body shape influences the behavior of the robot. A robot with symmetrical arms is more likely to move in a constant direction, while a robot where the arms don't all have arms opposite themselves may be more likely to move in a curved trajectory. Furthermore, a robot with longer arms is more likely to topple over and move on its side, while a robot with shorter arms may remain upright while moving.

#### Possible Mutations
There are 7 possible mutations, all with an equal chance of occurring. First, a sensor neuron can be added to a link that doesn't currently have one. Second, a sensor neuron can be removed from a link that currently has one. Third, a random dimension of a random link can be changed. Fourth, a link, with random dimensions, can be added to a random arm. Fifth, a random link can be removed from a random arm. Sixth, the weight of a random synapse can be changed. Seventh, a random joint axis can be changed. 

#### Fitness 
The fitness function calculates the straight-line displacement of the robot's base from (0,0) on the xy plane. It takes the square root of the squared x- and y-components of its location. A robot with a higher displacement has a higher fitness and will be selected for.

## The Robot
![alt text](https://github.com/juliagangi/mybots/blob/3DEvolved/botdiagram.png?raw=true)

![alt text](https://github.com/juliagangi/mybots/blob/3DEvolved/botabove.png?raw=true)

![alt text](https://github.com/juliagangi/mybots/blob/3DEvolved/botside.png?raw=true)

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

Click this link to watch a comparison between random and evolved creatures: <https://youtu.be/XodranJEfPs>

## Credit

Credit goes to r/ludobots <https://www.reddit.com/r/ludobots/> and pyrosim

