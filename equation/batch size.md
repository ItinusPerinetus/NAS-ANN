## Rapid Reduction Loss Equation from Batch Size:

$$
\text{loss}(ep, bs) = e^{-\alpha \cdot (ep + b)} + c \quad \text{where} \quad ep \leq E
$$

where:
- $ep$ = epoch number
- $bs$ = batch size
- $\alpha = 1.8029 \cdot e^{-0.4728 \cdot bs} + 0.1343$
- $b = 0.2693 \cdot bs + 0.8414$
- $E = 1.6947 \cdot bs + 1.9053$
- $\text{loss}(E, bs) = 0.0004 \cdot bs + 0.1916$
- $c = \text{loss}(E, bs) - e^{-\alpha \cdot (E + b)}$
