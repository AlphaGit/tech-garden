Method of calculation to account for external flows in a portfolio (deposits, withdrawals). It does so by considering internal timeframes and calculating the return in each timeframe, then compounding them together.

> Suppose that the portfolio is valued immediately after each external flow. The value of the portfolio at the end of each sub-period is adjusted for the external flow which takes place immediately before. External flows into the portfolio are considered positive, and flows out of the portfolio are negative.

$${1+R={\frac {M_{1}-C_{1}}{M_{0}}}\times {\frac {M_{2}-C_{2}}{M_{1}}}\times {\frac {M_{3}-C_{3}}{M_{2}}}\times \cdots \times {\frac {M_{n-1}-C_{n-1}}{M_{n-2}}}\times {\frac {M_{n}-C_{n}}{M_{n-1}}}}$$
where

$R$ is the _time-weighted return_ of the portfolio,

$M_{0}$ is the initial portfolio value,

$M_t$ is the portfolio value at the end of sub-period $t$, immediately after external flow $C_{t}$,

$M_{n}$ is the final portfolio value,

$C_{t}$ is the net external flow into the portfolio which occurs just before the end of sub-period $t$,

and

$n$ is the number of sub-periods.

Source: https://en.wikipedia.org/wiki/Time-weighted_return

#Finance #Metrics