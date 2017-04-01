## Experiments MD workload


In these experiments, we vary the number of the executables (referred to as compute unit (CU)) on a varying number of cores of Titan. We meeasure strong and weak scalability as defined in [Ref](https://arxiv.org/pdf/1602.00678.pdf). Each executable is Gromacs, consistent with this use case.(https://docs.google.com/document/d/1a8i38Z_aROQgylRNtbsePGH6UovRJgg0WW4gbk5kW4A/edit#heading=h.8tk04bz0vj23) 

We execute two experiments with:

1. Strong Scaling: 512 tasks executed using between 128 and 512 cores
2. Weak Scaling: Betwen 128 and 512 tasks executed on between 16 and 1024 cores, so as to keep ratio of number of tasks to cores constant (=1).

In both experiments we record the time to completion (TTC) of the execution as a measure of strong and weak scalability.

### Experiment 1

[Weak Scalability](https://github.com/ATLAS-Titan/misc/blob/master/Meetings/meeting-2017-02-13/weak.gif)


### Experiment 2
[Strong Scalability](https://github.com/ATLAS-Titan/misc/blob/master/Meetings/meeting-2017-02-13/strong.gif)




# Experiments-ATLAS-paper
