# RegretMatching

The paper for regret-matching and Counter Factual Regret Minimzation can be found <a href="http://modelai.gettysburg.edu/2013/cfr/cfr.pdf">here</a>.
<br>
Below are some foundations for Game Theory. Inspired by the course MATH3911 - Game Theory and Strategy

-----

**A Game $G$ in the strategic form consists of**
1. A set $N=\\{1, 2,\dots, n\\}$ players
2. For each player $i$, $S^i = \\{s^i_1, s^i_2, \dots, s^i_{m^i}\\}$ strategies of $i$
3. For each player, a payoff function $h^i: \prod_{i \in N} S^i \rightarrow \mathbb{R}$ is given by $h^i(j^1, \ldots, j^k, \ldots, j^n)$, where $j^k \in S^k$ is the pure strategy chosen by player $k$.
-----
**The <b>mixed extension</b> of G**
1. A set $N=\\{1,2,\dots,n\\}$ players
2. For each player $i$, a set $P^i$ of all mixed strategies of player $i$ is defined as: $$P^i = \\{ p^i = (p^i_1, p^i_2, \ldots, p^i_{m^i}) \in \mathbb{R}^{m^i} : p^i_j \geq 0 \text{ for all } j, \text{ and } \sum_{j=1}^{m^i} p^i_j = 1 \\}$$
3. For each player $i$, a payoff function $H^i: \prod_{i \in N} P^i \rightarrow \mathbb{R}$ is defined, where each $H^i$ is a linear combination of his payoffs with coefficients equal to the product of the corresponding probabilities, i.e. $$H^i(p^1, \ldots, p^k, \ldots, p^n) = \sum_{j^1=1}^{m^1} \sum_{j^2=1}^{m^2} \cdots \sum_{j^n=1}^{m^n} [p^1_{j^1} \cdots p^k_{j^k} \cdots p^n_{j^n} h^i(j^1, \ldots, j^k, \ldots, j^n)]$$
-----
**We formulate Rock, Paper, Scissors in the strategic form**
1. $N = \\{1, 2\\}$
2. $S^1 = \\{R, S, P\\}$, $S^2 = \\{R, S, P\\}$, and $h^i(s^1, s^2)$ be the payoff of player $i$ where $i = 1, 2$.
3.  Define $h^1(s^1, s^2) = 1$ if $(s^1, s^2)$ = (R, S), (S, P) or (P, R), $h_1(s_1, s_2) = 0$ if $(s^1, s^2)$ = (R, R), (S, S) or (P, P), and $h^1(s^1, s^2) = -1$ if $(s^1, s^2)$ = (S, R), (P, S) or (R, P).
4.  Given that this is a zero sum game, define $h^2(s^1,s^2) = -h^1(s^1, s^2)$.

**The Payoff matrix of this Game**
Payoff | R | P | S 
--- | --- | --- | --- 
R | (0, 0) | (-1, 1) | (1, -1)  
P | (1, -1) | (0, 0) | (-1, 1)  
S | (-1, 1) | (1, -1) | (0, 0) 
-----
**Fundamental Theorem of Mixed Strategy Nash Equilibrium**
<br>
$p$ is a mixed Nash equilibrium if and only if, for any player $i = 1, \ldots, n$ with the pure strategy set $S_i = \\{s^i_1, s^i_2, \ldots, s^i_{m^i}\\}$ of strategies of $i$,
1. If $s^i_k, s^i_l \in S^i$ occur with positive probability in $p^i$, then $H^i(p\mid e^i_k) = H^i(p\mid e^i_l)$;
2. if $s^i_k$ occurs with positive probability in $p^i$ and $s^i_l$ occurs with zero probability in $p^i$, then $H^i(p\mid e^i_l) \leq H^i(p\mid e^i_k)$

Note that $e^i_j = (\underset{j}{\underbrace{0, 0, \ldots, 0, 1}}, 0, \ldots, 0)$, $e^i_j$ is the $j^{th}$ unit vector in $\mathbb{R}^{m^i}$ and it is identified with the $j^{th}$ pure strategy $s^i_j$ of player $i$. 
$H^i(p\mid e^i_j)$ refers to the following.
$$H^i(p\mid e^i_j) = \sum_{j^1=1}^{m^1} \cdots \sum_{j^1=1}^{m^i} \cdots \sum_{j^n=1}^{m^n} [p^1_{j^1} \cdots e^i_{j} \cdots p^n_{j^n} h^i(j^1, \ldots, j^k, \ldots, j^n)]$$

We state this theorem without proof. (I don't really want to type it out in Readme)

-----
**Apply Fundamental Theorem of Mixed Strategy Nash Equilibrium to RPS**

To prove $p = ((1/3, 1/3, 1/3), (1/3, 1/3, 1/3))$ is a mixed Nash equilibrium, one can check that
$$H^1((1, 0, 0), (1/3, 1/3, 1/3)) = H^1((0, 1, 0), (1/3, 1/3, 1/3)) = H^1((0, 0, 1), (1/3, 1/3, 1/3)) = 0$$ 
and 
$$H^2((1/3, 1/3, 1/3), (1, 0, 0)) = H^2((1/3, 1/3, 1/3), (0, 1, 0)) = H^2((1/3, 1/3, 1/3), (0, 0, 1)) = 0$$ 

We have shown that $p = ((1/3, 1/3, 1/3), (1/3, 1/3, 1/3))$ is a mixed Nash equilibrium.

-----
**Key Questions**
1. What will be the best response of player 1 if player 2 deviates from the mixed Nash Equilibrium $(1/3, 1/3, 1/3)$?
2. If both players use the regret matching method, will the equilibrium converge to the mixed Nash Equilibrium?

Feel free to check out the code!

-----
