## Rapid Reduction Loss Equation from Output Number:

$$
\text{loss}(ep, on) = e^{-\alpha \cdot (ep + b)} + c \quad \text{where} \quad ep \leq E
$$

where:
- $ep$ = epoch number
- $on$ = output number
- $\alpha = 0.0027 \cdot on + 0.1433$
- $b = 2.1546 \cdot e^{0.0391 \cdot on}$
- $E = 21.0875 \cdot e^{0.0059 \cdot on}$
- $\text{loss}(E, on) = 0.3454
- $c = \text{loss}(E, on) - e^{-\alpha \cdot (E + b)}$
