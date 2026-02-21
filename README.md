# Feedforward and Backpropagation Example (ANN 2-2-2)

## Network Architecture

* Input Layer: 2 neurons
* Hidden Layer: 2 neurons
* Output Layer: 2 neurons
* Activation Function: Sigmoid
* Learning Rate: 0.5

---

## Given Data

### Inputs

```
i1 = 0.05
i2 = 0.10
```

### Targets

```
t1 = 0.01
t2 = 0.99
```

### Initial Weights

```
w1=0.15  w2=0.20
w3=0.25  w4=0.30
w5=0.40  w6=0.45
w7=0.50  w8=0.55
```

### Biases

```
b1 = 0.35
b2 = 0.60
```

---

## Feedforward

### Hidden Layer

```
h1 = 0.593269992
h2 = 0.596884378
```

### Output Layer

```
o1 = 0.75136507
o2 = 0.772928465
```

---

## Total Error

```
E_total = 0.298371109
```

---

## Backpropagation

### Updated Output Weights

```
w5' = 0.35891648
w6' = 0.408666186
w7' = 0.51130127
w8' = 0.561370121
```

### Updated Hidden Weights

```
w1' = 0.149780675
w2' = 0.199561351
w3' = 0.2497515
w4' = 0.299503
```

---

## Conclusion

Weights were successfully updated using gradient descent to minimize total error.
