# misc

## Document how to use RP on Titan 

We document how to execute a varying number of the same compute unit (CU) on a varying number of cores of Titan. The kernel of the CU might be Gromacs, as executed by this [use case](https://docs.google.com/document/d/1a8i38Z_aROQgylRNtbsePGH6UovRJgg0WW4gbk5kW4A/edit#heading=h.8tk04bz0vj23). `/bin/date` will be used if difficulties emerge with Gromacs.

The documentation will use examplanotory runs consistent with the following parameters:

No diagrams will be produced.

## Experiments MD workload

We execute a varying number of the same compute unit (CU) on a varying number of cores measuring strong and weak scalability as defined in [Ref](https://arxiv.org/pdf/1602.00678.pdf). We execute two experiments with:

1. Strong Scaling: 1024 tasks executed using between 16 and 1024 cores
2. Weak Scaling: Betwen 16 and 1024 tasks executed on between 16 and 1024 cores, so as to keep ratio of number of tasks to cores constant (=1).

In both experiments we record the time to completion (TTC) of the execution as a measure of strong and weak scalability.

### Experiment 1
```
TTC |                         Strong scaling test for RP on Titan
    |               BoT of 1024 tasks executed on btween 16 and 1024 cores
    |
    |
    |
    |
----|----------------------------------------------------------------------------
    |  1024/16   1024/32   1024/64   1024/128   1024/256   1024/512   1024/1024
                                           CU/cores
```

### Experiment 2
```
TTC |                Weak scalabiling test for RP on Titan
    |             BoT of between 16 and 1024 tasks executed on
    |                       btween 16 and 1024 cores
    |
    |
    |
----|-------------------------------------------------------------------
    |  16/16   32/32   64/64   128/128   256/256   512/512   1024/1024
                                    CU/cores

```
