## Rapid Reduction Loss Equation from Input Number:

$$
\text{loss}(ep, on) = e^{-\alpha \cdot (ep + b)} + c \quad \text{where} \quad ep \leq E
$$

where:
- $ep$ = epoch number
- $in$ = input number
- $\alpha = 0.0119 \cdot in + 0.0496$
- $b = 20.8522 \cdot e^{-0.1650 \cdot in}$
- $E = 78.2304 \cdot e^{-0.1189 \cdot in}$
- $\text{loss}(E, in) = 0.0056 \cdot in + 0.1080$
- $c = \text{loss}(E, in) - e^{-\alpha \cdot (E + b)}$
