# misc

## Experiments 

We execute a varying number of the same compute unit (CU) on a varying number of cores. The kernel of the CU is Gromacs, as executed by this [use case](https://docs.google.com/document/d/1a8i38Z_aROQgylRNtbsePGH6UovRJgg0WW4gbk5kW4A/edit#heading=h.8tk04bz0vj23). 

## Experiments MD workload

We execute a varying number of the same compute unit (CU) on a varying number of cores measuring strong and weak scalability as defined in [Ref](https://arxiv.org/pdf/1602.00678.pdf). We execute two experiments with:

1. 1024 tasks executed on between 16 and 1024 
2. betwen 16 and 1024 tasks executed, respectively, on between 16 and 1024 cores.

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
