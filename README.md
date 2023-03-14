# 396 Final Project

#### Table of Contents
###### 1. The Robot
###### 2. The Hypotheses
###### 3. The Results
###### 4. Discussion
###### 5. Watch the robots!

## The Robot
#### Group A (Control)
###### The Body
My creature originates from a central link, with a fixed size, and has arms that grows out in at least 1 of the following directions: -x, +x, -y, and +y. As links are added, the z-coordinate is increased so links are connected at their edges, not faces. Each of the 4 arms contains a random number of links, constrained by [1,5], with the dimensions being constrained by [0,1]. The joint axis for each joint is randomly generated. 

![alt text](https://github.com/juliagangi/mybots/blob/finalExperiment/bodyandcycle.png?raw=true)

###### The Brain
Every link has a 3 in 5 chance of receiving a sensor neuron: if the integer randomly selected from [0,4] is greater than 1, a sensor neuron is placed in the given link. Every joint receives a motor neuron. To form the brain, every motor neuron is connected to the sensor neurons in adjoining links (if they exist). An array is generated that assigns a random weight (a floating point number constrained by [-1,1]) to each synapse. The total number of synapses is equal to twice the number of motor neurons (or joints). 

![alt text](https://github.com/juliagangi/mybots/blob/finalExperiment/braindiagram.png?raw=true)

## Group B
###### The Body
The only difference between the robots in the control and in Group B is that the number of links in each arm is constrained by [1,9] - the upper bound has been increased by 4. 

![alt text](https://github.com/juliagangi/mybots/blob/finalExperiment/bodydiff.png?raw=true)

###### The Brain
The robot in Group B has the same brain as the control robot.

## Group C
###### The Body
The robot in Group C has the same body as the control robot.

###### The Brain
The neural network of the creature in Group C is more complex than that of the control. The sensors and motors are placed in the same way, but a random number of hidden neurons, constrained by [2,4], are added to the robot. The synapses are completely different than in the control: one set is sent from each sensor neuron to each hidden neuron, and a second set is sent from each hidden neuron to each motor neuron. One array is generated for each of the 2 sets of synapses, and it holds random floating point numbers constrained by [-1,1]. The total number of synapses is equal to numHiddenNeurons*numSensorNeurons + numHiddenNeurons*numMotorNeurons.

![alt text](https://github.com/juliagangi/mybots/blob/finalExperiment/neuraldiff.png?raw=true)

## Evolution
The body shape influences the behavior of the robot. A robot with symmetrical arms is more likely to move in a constant direction, while a robot where the arms don't all have arms opposite themselves may be more likely to move in a curved trajectory. Furthermore, a robot with longer arms is more likely to topple over and move on its side, while a robot with shorter arms may remain upright while moving.

#### Mutations
There are 7 possible mutations, all with an equal chance of occurring. First, a sensor neuron can be added to a link that doesn't currently have one. Second, a sensor neuron can be removed from a link that currently has one. Third, a random dimension of a random link can be changed. Fourth, a link, with random dimensions, can be added to a random arm. Fifth, a random link can be removed from a random arm. Sixth, the weight of a random synapse can be changed. Seventh, a random joint axis can be changed. 

![alt text](https://github.com/juliagangi/mybots/blob/finalExperiment/mutations.png?raw=true)

#### Fitness 
The fitness function calculates the straight-line displacement of the robot's base from (0,0) on the xy plane. It takes the square root of the squared x- and y-components of its location. A robot with a higher displacement has a higher fitness and will be selected for.

```math
fitness = \sqrt{x^2+y^2}
```

#### Selection
![alt text](https://github.com/juliagangi/mybots/blob/finalExperiment/selection.png?raw=true)

## The Hypotheses
I hypothesized that increasing the upper bound on the number of links in the arms by 4 (Group B) would result in improved locomotion when compared to the control robot (Group A). I also hypothesized that adding a hidden neural network with 2 hidden neurons (Group C) would result in locomotion that is even better than the control group (Group A) and the group with longer arms (Group B). 

#### Why?
In my control, there is an upper limit of 5 on the number of links in each arm. I have noticed that the most successful creature at the end of every run is very elongated, as robots with longer limbs were selected for. I was curious as to whether increasing the upper limit on the length of the arms to 9 would or making a fundamental change in the brain (adding a hidden neural network), as the body was already fairly successful would improve locomotion to a greater degree. In other words, past a certain length of arms, does the fitness continue to improve, or does it flatten out as if approaching an asymptote? 

#### The Testing
I tested my hypothesis with 3 different runs. Each run involved testing one version of the robot. Each of these involved a loop that occurred 5 times, with the random seed incremented each time, and each loop simulated a population size of 10 over 500 generations. For the first run, the control was simulated (pop. 10, gens. 500) with random seed 1, 2, 3, 4, and finally 5. Next, Group B was simulated with the same parameters and the same random seeds (1-5) to ensure that the populations were identical except for the longer limbs. Lastly, Group C was simulated with the same parameters and seeds.

## The Results
The results of my experiment supported my hypotheses, with the maximum distance traveled from the origin being 38.19 for Group A, 59.81 for Group B and 75.7 for Group C - increasing with each group, as I predicted. Group B was 56.6% fitter than the control, while Group C was 26.6% fitter than Group B and 98.2% fitter than the control. Each graph below shows the evolution that occurred during 1 run, over 500 generations. For each random seed, I plotted the highest fitness of the 10 parents at each generation. The mean curve is equal to the average of the 5 random seed curves, and it includes a 95% confidence interval for these 5 fitness values at each generation. It can be observed from the legend that for the control, the most successful creature for the mutated robot came from random seed 5, while for groups B and C it came from random seed 1.

#### Group A
![alt text](https://github.com/juliagangi/mybots/blob/finalExperiment/plot1.png?raw=true)

###### A few mutations caused seed 5 maximum fitness to increase from about 3 to about 30 in the first 20 generations, so seed 5 was the fittest for the majority of the experiment. However, seeds 1-4 still saw improvement over the first 100 generations, and a flattening of curves after that.

#### Group B
![alt text](https://github.com/juliagangi/mybots/blob/finalExperiment/plot2.png?raw=true)

###### In the first 100 generations, evolution improved at a fairly high rate, with seed 4 being the fittest, but around generation 130 a single mutation occurred that caused seed 1's maximum displacement to increase from about 12 to about 35, while the rest of the seeds' curves remained fairly flat. 

#### Group C
![alt text](https://github.com/juliagangi/mybots/blob/finalExperiment/plot3.png?raw=true)

You can observe that the most successful creature alternated between seeds 1 and 3 until after the 200th generation, when it remained as seed 1. Most of the seeds still saw continuous growth throughout all 500 generations.

## Discussion
#### Additional Analysis
The main question I had throughout this experiment was why adding a hidden neural network affected such a drastic change in fitness. Hidden neural networks work by indirectly connecting sensor neurons to motor neurons (as contrasted with direct, single-synapse connections). They don't have a location, and apply complex non-linear activation functions to the data. Hidden neurons are useful for training robots to accomplish complicated tasks, so it makes sense that they would be so successful with a relatively uncomplicated task: locomotion.

#### Discussion of Results
It makes sense that group B was more successful than group A because of the implications of having longer limbs. Robots with multiple shorter arms (such as group A, seed 1-4) are able to remain upright and tend to move by vibrating, which is still effective for locomotion but requires many small movements. Meanwhile robots with a main long arm (such as group B, seed 1) tend to topple over and make leaping strides, and locomotion consists of fewer, more impactful movements. The longer the arm is, the more they bend, so the result is longer strides. Additionally, I expected that using a hidden neural network in Group C would result in it being more successful than groups A and B, as I explain in the previous section (Additional Analysis).

#### Conclusion
In conclusion, both of my hypotheses were supported. My first hypothesis, that robots with longer limbs would travel farther than robots with shorter limbs, was correct as a result of the differing body proportions that resulted from the bounds on the body parts. My second hypothesis, that robots with a hidden neural network would travel farther than robots with only sensor and motor neurons, was correct. This outcome requires more analysis, since hidden neural networks are still largely misunderstood. 

###### Further Research
Further research could include seeing how the number of hidden neurons affects the success of the robot, and if there are diminishing returns as hidden neurons are added. A separate experiment could test whether there diminishing returns from the upper limit on the number of links in each arm.

## Watch the robots!
#### Running it
First, follow these instructions to install pybullet for python3: <https://www.reddit.com/r/ludobots/wiki/installation/> 

Next, clone my repo to your computer.

To watch a random robot, run this command:

```bash
python3 run.py random
```

To watch a the best evolved control (Group A) robot, run this command:

```bash
python3 run.py A optional:[1,5]*
```

To watch the best evolved robot from Group B, run this command:

```bash
python3 run.py B optional:[1,5]*
```

To watch the best evolved robot from Group C, run this command:

```bash
python3 run.py C optional:[1,5]*
```

*Add a 3rd argument, an integer [1,5], to see the best robot from that random seed.

#### Videos

Click this link to watch a 10-second comparison between random and evolved creatures: <https://youtu.be/PnveOMKyw64>

Watch a 2-minute video on my project: <>

#### Credit

Credit goes to r/ludobots (<https://www.reddit.com/r/ludobots/>), Pyrosim, and CS 396: Artificial Life

