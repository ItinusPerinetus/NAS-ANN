## Rapid Reduction Loss Equation from Output Number:

$$
\text{loss}(ep, on) = e^{-\alpha \cdot (ep + b)} + c \quad \text{where} \quad ep \leq E
$$

where:
- $ep$ = epoch number
- $on$ = output number
- $\alpha = 0.0027 \cdot on + 0.1433$
- $b = 2.1546 \cdot e^{0.0391 \cdot on}$
- $E = -0.1807 \cdot on + 25.4614$
- $\text{loss}(E, on) = -0.0008 \cdot on + 0.1660$
- $c = \text{loss}(E, on) - e^{-\alpha \cdot (E + b)}$
