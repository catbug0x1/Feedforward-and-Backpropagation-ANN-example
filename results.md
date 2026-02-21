# Iteration-2 Error Reduction Proof

---

## Initial Error (Iteration 1)

```
E_total(1) = 0.298371109
```

---

## After Weight Update (Iteration 2)

New Outputs:

```
o1 = 0.742088112
o2 = 0.775284968
```

New Error:

```
E_total(2) = 0.291027924
```

---

## Error Reduction

```
ΔE = E_total(1) - E_total(2)
ΔE = 0.007343185
```

---

## Conclusion

Since the total error after iteration 2 is less than iteration 1:

```
E_total(2) < E_total(1)
```

This confirms that the backpropagation algorithm successfully minimized the network loss using gradient descent.
