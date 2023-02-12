# 396 Assignment 7

## The Code

My creature grows up along the z-axis, then out in the -x, +x, -y, and +y directions. It is spider-like, except that there are 4 legs instead of 8. Each of the 4 "legs" contains the same number of links, the dimensions of which are constrained by [0,2), and which are jointed at the base of each. The number of links in the arm is at least 2 greater than the number of links in the vertical portion, to ensure that the arms can reach the ground. A random integer selector decides whether or not to place a sensor neuron in the current link. 

## The Robot

![alt text](https://github.com/juliagangi/mybots/blob/3DCreature/above.png?raw=true)

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

credit goes to r/ludobots

