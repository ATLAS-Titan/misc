# misc

## Document how to use RP on Titan 

We document how to execute a varying number of the same compute unit (CU) on a varying number of cores of Titan. The kernel of the CU might be Gromacs, as executed by this [use case](https://docs.google.com/document/d/1a8i38Z_aROQgylRNtbsePGH6UovRJgg0WW4gbk5kW4A/edit#heading=h.8tk04bz0vj23). `/bin/date` will be used if difficulties emerge with Gromacs.

The documentation will use examplanotory runs consistent with the following parameters:

1. 128 CU - 64 cores;

2. 128 CU - 128 cores;

3. 256 CU - 64 cores;

4. 256 CU - 128 Cores;

No diagrams will be produced.

## Experiments MD workload

We execute a varying number of the same compute unit (CU) on a varying number of cores measuring strong and weak scalability as defined in [Ref](https://arxiv.org/pdf/1602.00678.pdf). We execute two experiments with:

1. Strong Scaling: 1024 tasks executed using between 16 and 1024 cores
2. Weak Scaling: Betwen 16 and 1024 tasks executed on between 16 and 1024 cores, so as to keep ratio of number of tasks to cores constant (=1).

In both experiments we record the time to completion (TTC) of the execution as a measure of strong and weak scalability.

[Weak Scalability](https://github.com/ATLAS-Titan/misc/blob/master/Meetings/meeting-2017-02-13/weak.gif)




### Experiment 2
[Strong Scalability](https://github.com/ATLAS-Titan/misc/blob/master/Meetings/meeting-2017-02-13/strong.gif)


