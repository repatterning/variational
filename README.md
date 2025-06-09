<br>

Variational

The project's prediction models are Bayesian Structural Time Series (STS) models.  A Bayesian Structural Time Series algorithm is a state space algorithm, in brief


$$y_{t} = \mathbf{x}^{T}\_{t}\pmb{\beta}\_{t} + \epsilon_{t}$$

$$\pmb{\beta}\_{t} = \mathbf{F}\_{t}\pmb{\beta}\_{t - 1} + \pmb{\varsigma}_{t}$$

$$\epsilon_{t} \sim \mathcal{N}\bigl(0, \: \sigma^{2}_{t}  \bigr)$$

$$\pmb{\varsigma}\_{t} \sim \mathcal{N}\bigl(\mathbf{0}, \: \pmb{\mathcal{Z}}\_{t}\bigr)$$

whereby

&nbsp; | &nbsp;
:--- | :---
$y_{t}$ | $1 \times 1$ scalar.  Herein, it is a gauge's river level measure at time point $t$.
$\mathbf{x}_{t}$ | $p \times 1$.  A design vector.
$\pmb{\beta}_{t}$ | $p \times 1$.  A state vector.
$\epsilon_{t}$ | $1 \times 1$ scalar.  An observation error, observation innovation.
$\mathbf{F}_{t}$ | $p \times p$.  A transition matrix.
$\pmb{\varsigma}_{t}$ | $q \times 1$. A system error, or state innovation.[^1]


<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>

[^1]: For more about the structure options of $\pmb{\varsigma}_{t}$, i.e., system errors, study <a href="https://projecteuclid.org/journals/annals-of-applied-statistics/volume-9/issue-1/Inferring-causal-impact-using-Bayesian-structural-time-series-models/10.1214/14-AOAS788.full" target="_blank">Inferring causal impact using Bayesian structural time-series models</a>, and <a href="https://link.springer.com/book/10.1007/978-3-030-76124-0" target="_blank">Bayesian Inference of State Space Models</a>