<br>

Variational

The project's prediction models are Bayesian Structural Time Series (STS) models.  A Bayesian Structural Time Series algorithm is a state space algorithm, in brief


$$y_{t} = \mathbf{x}^{T}_{t}\pmb{\beta}_{t} + \epsilon_{t}$$


\begin{equation}
\pmb{\beta}_{t} = \pmb{F}_{t}\pmb{\beta}_{t - 1} + \pmb{\varsigma}_{t}
\label{eq:0002}
\end{equation}

$$\epsilon_{t} \sim \mathcal{N}\bigl(0, \sigma^{2}_{t}  \bigr)$$

$$\mathbf{\varsigma}\_{t} \sim \mathcal{N}\bigl(\mathbf{0}, \mathbf{\mathcal{Z}}\_{t}\bigr)$$

whereby


<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
