# 396 Final Project

#### Table of Contents
###### 1. The Body
###### 2. The Brain
###### 3. Evolution
###### 4. A/B Testing

## The Control & Experiment #2
My creature originates from a central link, with a fixed size, and has arms that grows out in at least 1 of the following directions: -x, +x, -y, and +y. As links are added, the z-coordinate is increased so links are connected at their edges, not faces. Each of the 4 arms contains a random number of links, constrained by [1,5], with the dimensions being constrained by [0,1]. The joint axis for each joint is randomly generated. 

## Experiment #1
The only difference between the control and the first experiment is that the number of links in each arm is constrained by [1,9] - the upper bound has been increased by 4. 

![alt text](https://github.com/juliagangi/mybots/blob/finalExperiment/bodyydiagram.png?raw=true)

## The Brain
#### Control & Experiment #1
Every link has a 3 in 5 chance of receiving a sensor neuron: if the integer randomly selected from [0,4] is greater than 1, a sensor neuron is placed in the given link. Every joint receives a motor neuron. To form the brain, every motor neuron is connected to the sensor neurons in adjoining links (if they exist). Each synapse is given a random weight, which is a floating point number constrained by [-1,1]. The total number of synapses is equal to twice the number of motor neurons (or joints).

![alt text](https://github.com/juliagangi/mybots/blob/finalExperiment/braindiagram.png?raw=true)

#### Experiment #2
The neural network of the creature I am testing is more complex than that of the control. The sensors and motors are placed in the same way, but a random number of hidden neurons, constrained by [2,4], are added to the robot. The synapses are completely different than in the control: one set is sent from each sensor neuron to each hidden neuron, and a second set is sent from each hidden neuron to each motor neuron. The total number of synapses is equal to numHiddenNeurons*numSensorNeurons + numHiddenNeurons*numMotorNeurons.

![alt text](https://github.com/juliagangi/mybots/blob/finalExperiment/neuralnetwork.png?raw=true)

## Evolution
The body shape influences the behavior of the robot. A robot with symmetrical arms is more likely to move in a constant direction, while a robot where the arms don't all have arms opposite themselves may be more likely to move in a curved trajectory. Furthermore, a robot with longer arms is more likely to topple over and move on its side, while a robot with shorter arms may remain upright while moving.

#### Mutations
There are 7 possible mutations, all with an equal chance of occurring. First, a sensor neuron can be added to a link that doesn't currently have one. Second, a sensor neuron can be removed from a link that currently has one. Third, a random dimension of a random link can be changed. Fourth, a link, with random dimensions, can be added to a random arm. Fifth, a random link can be removed from a random arm. Sixth, the weight of a random synapse can be changed. Seventh, a random joint axis can be changed. 

![alt text](https://github.com/juliagangi/mybots/blob/finalExperiment/mutations.png?raw=true)

#### Fitness 
The fitness function calculates the straight-line displacement of the robot's base from (0,0) on the xy plane. It takes the square root of the squared x- and y-components of its location. A robot with a higher displacement has a higher fitness and will be selected for.

#### Selection
![alt text](https://github.com/juliagangi/mybots/blob/finalExperiment/selection.png?raw=true)

## A/B Testing
#### My Hypotheses

I hypothesized that increasing the upper bound on the number of links in the arms by 4 (experiment #1) would result in improved locomotion when compared to the control robot. I also hypothesized that adding a hidden neural network with 2 hidden neurons (experiment #2) would result in locomotion that is even better than the control group and the group with longer arms, which both have neural networks that contain only sensor and motor neurons. 

###### Why?
In my control, there is an upper limit of 5 on the number of links in each arm. I have noticed that the most successful creature at the end of every run is very elongated, as robots with longer limbs were selected for. I was curious as to whether increasing the upper limit on the length of the arms would or making a fundamental change in the brain (adding a hidden neural network) would improve locomotion to a greater degree.

#### The Testing
I tested my hypothesis with 3 different runs. Each run involved testing one version of the robot. Each of these involved a loop that occurred 5 times, with the random seed incremented each time, and each loop simulated a population size of 10 over 500 generations. For example, for the first run, the control was simulated (pop. 25, gens. 200) with random seed 1, 2, 3, 4, and finally 5. Next, experiment #1 was simulated with the same parameters and the same random seeds (1-5) to ensure that the populations were identical except for the longer limbs. Lastly, experiment #2 was simulated with the same parameters and seeds.

#### The Results
The results of my experiment confirmed my hypothesis, with the maximum distance traveled from the origin being 38 (get decimal)for the control, 59.81 for experiment #1 and 75.7 for experiment #2. Each graph below shows the evolution that occurred during 1 run, over 500 generations. For each random seed, I plotted the highest fitness of the 10 parents at each generation. The mean curve is equal to the average of the 5 random seed curves, and it includes a 95% confidence interval for these 5 fitness values at each generation. It can be observed from the legend that for the control, the most successful creature for the mutated robot came from random seed 5, while for both experiments it came from random seed 1.

###### Control
![alt text](https://github.com/juliagangi/mybots/blob/finalExperiment/plot1.png?raw=true)

###### Experiment #1
![alt text](https://github.com/juliagangi/mybots/blob/finalExperiment/plot2.png?raw=true)

###### Experiment 2
![alt text](https://github.com/juliagangi/mybots/blob/finalExperiment/plot3.png?raw=true)

## Running It
First, follow these instructions to install pybullet for python3: <https://www.reddit.com/r/ludobots/wiki/installation/> 

Next, clone my repo to your computer.

To watch a random robot, run this command:

```bash
python3 run.py random
```

To watch a the best evolved control robot, run this command:

```bash
python3 run.py control optional:[1,5]*
```

To watch the best evolved robot from experiment #1, run this command:

```bash
python3 run.py exp1 optional:[1,5]*
```

To watch the best evolved robot from experiment #2, run this command:

```bash
python3 run.py exp2 optional:[1,5]*
```

*Add a 3rd argument, an integer [1,5], to see the best robot from that random seed.

## Videos

Click this link to watch a comparison between random and evolved creatures: <https://youtu.be/XodranJEfPs>

## Credit

Credit goes to r/ludobots (<https://www.reddit.com/r/ludobots/>), Pyrosim, and CS 396: Artificial Life

