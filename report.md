# Mathematical Solution of Feedforward and Backpropagation

---

## Step 1: Initial Parameters

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

## Step 2: Feedforward

Hidden Layer:

```
net_h1 = 0.3775
net_h2 = 0.3925
```

Sigmoid Activation:

```
h1 = 0.593269992
h2 = 0.596884378
```

Output Layer:

```
net_o1 = 1.105905967
net_o2 = 1.224921404
```

```
o1 = 0.75136507
o2 = 0.772928465
```

---

## Step 3: Error Calculation

```
E1 = 0.274811083
E2 = 0.023560026
Total Error = 0.298371109
```

---

## Step 4: Backpropagation

Output Layer Gradients:

```
δo1 = 0.138498561
δo2 = -0.038098236
```

Updated Output Weights:

```
w5' = 0.35891648
w6' = 0.408666186
w7' = 0.51130127
w8' = 0.561370121
```

Hidden Layer Gradients:

```
δh1 = 0.00877299
δh2 = 0.00994
```

Updated Hidden Weights:

```
w1' = 0.149780675
w2' = 0.199561351
w3' = 0.2497515
w4' = 0.299503
```
