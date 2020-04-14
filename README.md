# epidemic-propagation-model
A epidemic propagation model on real sociopatterns data
## Model description
Assume that the lifetime of virus or disease is much shorter than the lifetime of nodes in the population. At the same time, assume the connection between nodes is identical when the time change; therefore, every iteration the same network is used. 
In a typical epidemic propagation model, the states of all individuals in a population are classified into 3 kind: 
* S(Susceptible) – healthy state (can be infected by others)
* I(Infected) – infected state (can infect others)
* R(Recovered)-recovered state (cannot be infected by others again)
In this project, the recover state is not taken into consideration and a new state is added：
* C(Carried) – Incubation period state (can infect others with lower probabilities)
For the network model, every nodes i represent a real people with two labels (state Si and incubation time Ti). State label Si=0 means node i is in S(Susceptible) state, Si=1 means node i is in C(Carried) state and Si=2 means node i is in I(Infected) state. Time label Ti is days of node’s state label Si=1, which means days of individuals in an Incubation period. 

If two nodes have face two face connection then there is an edge between them with an edge label weight wij, which associated with the total time of face-to-face connection.
Simulation Steps.

First set all nodes’ S=0, T=0. Then a node is randomly selected in the network to make state label S=1 and T=1, which is the only source of infection in the entire network. 
In first iteration, all nodes in the space are scanned without repeat at each iteration, and accordingly to the following rules performing status updated.

1. For every pairs of nodes, if their state Si and Sj and edge weight wij can find a corresponding probability P in table, then nodes with state S=0 will become infected and status S=1, otherwise pass this pair of nodes and turn to next pair.

state|wij <=3|3< wij <=10|10< wij
:-:|:-:|:-:|:-:
Si=1, Sj=0|p1|p2|p3|
Si=2, Sj=0|p4|p5|p6|
2. After all pairs have been scanned, find all nodes with status S=1, then update their time label T=T+1.
3. If T>=maximum incubation period, node may become infected state (S=2) with probability P5.
4. Turn to next iteration. 
