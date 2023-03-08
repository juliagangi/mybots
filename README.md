# 396 Final Project

#### Table of Contents
###### 1. The Body
###### 2. The Brain
###### 3. Evolution
###### 4. A/B Testing

## The Control & Experimental Robot #2
My creature originates from a central link, with a fixed size, and has arms that grows out in at least 1 of the following directions: -x, +x, -y, and +y. As links are added, the z-coordinate is increased so links are connected at their edges, not faces. Each of the 4 arms contains a random number of links, constrained by [1,5], with the dimensions being constrained by [0,1]. The joint axis for each joint is randomly generated. 

## Experimental Robot #1
The only difference between the control and the first experimental robot is that the number of links in each arm is constrained by [1,9] - the upper bound has been increased by 4. 

![alt text](https://github.com/juliagangi/mybots/blob/finalExperiment/thebody.png?raw=true)

## The Brain
#### Control & Experimental Robot #1
Every link has a 3 in 5 chance of receiving a sensor neuron: if the integer randomly selected from [0,4] is greater than 1, a sensor neuron is placed in the given link. Every joint receives a motor neuron. To form the brain, every motor neuron is connected to the sensor neurons in adjoining links (if they exist). Each synapse is given a random weight, which is a floating point number constrained by [-1,1]. The total number of synapses is equal to twice the number of motor neurons (or joints).

#### Experimental Robot #2
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

I hypothesized that increasing the upper bound on the number of links in the arms by 4 (experimental robot #1) would result in improved locomotion when compared to the control robot. I also hypothesized that adding a hidden neural network with 2 hidden neurons (experimental robot #2) would result in locomotion that is even better than the control group and the group with longer arms, which both have neural networks that contain only sensor and motor neurons. 

###### Why?
In my code, there is an upper limit of 5 on the number of links in each arm. I have noticed that the most successful creature at the end of every run is very elongated, as robots with longer limbs were selected for. I was curious as to whether increasing the upper limit on the length of the arms would or making a fundamental change in the brain (adding a hidden neural network) would improve locomotion to a greater degree.

#### The Testing
I tested my hypothesis with 3 different runs. Each run involved testing one version of the robot. Each of these involved a loop that occurred 5 times, with the random seed incremented each time, and each loop simulated a population size of 10 over 500 generations. For example, for the first run, the control was simulated (pop. 25, gens. 200) with random seed 1, 2, 3, 4, and finally 5. Next, experimental creature #1 was simulated with the same parameters and the same random seeds (1-5) to ensure that the populations were identical except for the longer limbs. Lastly, experimental creature #2 was simulated with the same parameters and seeds.

#### The Result
My experiment found great results, with the distance traveled from the origin doubling for some runs. The graphs below compare the control and mutated creature for each run. It can be observed from the legend that for each runs, the most successful creature for the mutated robot came from a different random seed than the control robot did.  

###### The Graphs


## Running It
First, clone my repo to your computer.

To watch a random robot, run this command:

```bash
python3 run.py random
```

To watch a final evolved robot, run this command:

```bash
python3 run.py evolved
```

## Videos

Click this link to watch a comparison between random and evolved creatures: <https://youtu.be/XodranJEfPs>

## Credit

Credit goes to r/ludobots <https://www.reddit.com/r/ludobots/> and pyrosim

