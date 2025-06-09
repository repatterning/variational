<br>

Variational

The project's prediction models are Bayesian Structural Time Series (STS) models.  A Bayesian Structural Time Series algorithm is a state space algorithm, in brief


$$y_{t} = \pmb{x}^{T}\_{t}\pmb{\beta}\_{t} + \epsilon_{t} \qquad \qquad \qquad 1$$

$$\pmb{\beta}\_{t} = \mathbf{F}\_{t}\pmb{\beta}\_{t - 1} + \pmb{\varsigma}_{t} \qquad \qquad 2$$

$$\epsilon_{t} \sim \mathcal{N}\bigl(0, \: \sigma^{2}_{t}  \bigr) \qquad \qquad \qquad$$

$$\pmb{\varsigma}\_{t} \sim \mathcal{N}\bigl(\mathbf{0}, \: \pmb{\mathcal{Z}}\_{t}\bigr) \qquad \qquad \qquad$$

whereby

&nbsp; | &nbsp;
:--- | :---
$y_{t}$ | $1 \times 1$ scalar.  Herein, it is a gauge's river level measure at time point $t$.
$\pmb{x}_{t}$ | $p \times 1$.  A design vector.
$\pmb{\beta}_{t}$ | $p \times 1$.  A state vector.
$\epsilon_{t}$ | $1 \times 1$ scalar.  An observation error, observation innovation.
$\mathbf{F}_{t}$ | $p \times p$.  A transition matrix.
$\pmb{\varsigma}_{t}$ | $q \times 1$. A system error, or state innovation.[^1]


<br>

Formally, <b>Eq. 1</b>  is the <i>observation model</i>, whilst <b>Eq. 2</b> is the <i>transition or state model</i>.  The latter models the transition of a state from $t - 1$ to $t$.<br><br>

A key advantage of state space modelling is $\rightarrow$ modelling via the superimposition of behaviours.  In the case of river levels, we superimpose seasonality and autoregression.  The superimposition, encoding, of behaviours occurs via the components $\pmb{x}\_{t}$ & $\mathbf{F}\_{t}$.  For an in-depth outline, study <a href="https://link.springer.com/book/10.1007/978-3-030-76124-0" target="_blank">Bayesian Inference of State Space Models</a> by K. Triantafyllopoulos.<br><br>

In practice, model development is via <a href="https://www.tensorflow.org/probability" target="_blank">TensorFlow Probability</a> libraries.  Visit the project's river level modelling [GitHub] <a href="https://github.com/repatterning/variational/tree/master" target="_blank">repository</a>; <a href="https://github.com/repatterning/variational/blob/master/src/modelling/architecture.py" target="_blank">modelling class</a>; the modelling arguments are readable <a href="https://github.com/repatterning/configurations/blob/master/src/artefacts/architecture/variational/arguments.yaml" target="_blank">with</a> or <a href="https://github.com/repatterning/configurations/blob/master/src/artefacts/architecture/variational/arguments.json" target="_blank">without</a> comments/definitions.
              


<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>

[^1]: For more about the structure options of $\pmb{\varsigma}\_{t}$, i.e., system errors, study <a href="https://projecteuclid.org/journals/annals-of-applied-statistics/volume-9/issue-1/Inferring-causal-impact-using-Bayesian-structural-time-series-models/10.1214/14-AOAS788.full" target="_blank">Inferring causal impact using Bayesian structural time-series models</a>, and <a href="https://link.springer.com/book/10.1007/978-3-030-76124-0" target="_blank">Bayesian Inference of State Space Models</a>