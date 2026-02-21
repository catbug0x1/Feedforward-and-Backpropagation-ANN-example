# Artificial Neural Network

## Feedforward and Backpropagation Implementation

---

### Course

AI323 – Computational Neuroscience

### Submitted To

A. Prof. Noha El-Attar

---

## Objective

This project demonstrates the training process of a Multilayer Artificial Neural Network (ANN) using:

* Feedforward computation
* Backward propagation of errors
* Gradient descent optimization

The aim is to minimize the prediction error by iteratively adjusting network weights.

---

## Network Architecture

| Layer        | Neurons |
| ------------ | ------- |
| Input Layer  | 2       |
| Hidden Layer | 2       |
| Output Layer | 2       |

Activation Function: **Sigmoid**
Learning Rate: **0.5**

---

## Given Inputs

```
i1 = 0.05  
i2 = 0.10
```

## Target Outputs

```
t1 = 0.01  
t2 = 0.99
```

---

## Project Files

| File              | Description             |
| ----------------- | ----------------------- |
| report.md         | Mathematical derivation |
| implementation.py | Python implementation   |
| results.md        | Error reduction proof   |

---

## Result

Backpropagation successfully reduced the total network error after the second iteration, confirming proper gradient descent learning.
