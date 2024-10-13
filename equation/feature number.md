## Rapid Reduction Loss Equation from Feature Number:

$$
\text{loss}(ep, fn) = e^{-\alpha \cdot (ep + b)} + c ; \text{ where } ep \leq E
$$

where:
- $ep$ = epoch number
- $fn$ = feature number

- $a = 0.0167 \cdot fn + 0.0098$
- $b = 34.3415 \cdot e^{-0.3066 \cdot fn}$
- $E = 111.2616 \cdot e^{-0.1605 \cdot fn}$
$$
\text{loss}(E, fn) = 0.1968
$$
$$
c = \text{loss}(E, fn) - e^{-\alpha \cdot (E + b)}
$$
