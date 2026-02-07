---
paper_id: "simulation-of-arbitrage-free-implied-volatility-surfaces"
source_file: "Simulation of Arbitrage-Free Implied Volatility Surfaces.pdf"
title: "Simulation of Arbitrage-Free Implied Volatility Surfaces"
authors: []
year: 2023
doi: "10.1080/1350486X.2023.2277960"
page_count: 29
extracted_at: "2026-02-07T06:35:37.022776+00:00"
status: "success"
---

# Simulation of Arbitrage-Free Implied Volatility Surfaces

## Metadata

- **Source File:** `Simulation of Arbitrage-Free Implied Volatility Surfaces.pdf`
- **Authors:** Unknown
- **Year:** 2023
- **DOI:** 10.1080/1350486X.2023.2277960

## Abstract

ARTICLE HISTORY Received 26 June 2023 We present a computationally tractable method for simulating Accepted 25 October 2023 arbitrage-free implied volatility surfaces. We illustrate how our method may be combined with a data-driven model based on hisKEYWORDS torical SPX implied volatility data to generate dynamic scenarios for Implied volatility; options arbitrage-free implied volatility surfaces. Our approach conciliates markets; volatility index; staticarbitrageconstraintswitharealisticrepresentationofstatistical simulation; arbitrage properties of implied volatility co-movements.

## Main Text

### Applied Mathematical Finance
ISSN: 1350-486X (Print) 1466-4313 (Online) Journal homepage: www.tandfonline.com/journals/ramf20
## Simulation of Arbitrage-Free Implied Volatility
## Surfaces
Rama Cont & Milena Vuletić
To cite this article: Rama Cont & Milena Vuletić (2023) Simulation of ArbitrageFree Implied Volatility Surfaces, Applied Mathematical Finance, 30:2, 94-121, DOI:
10.1080/1350486X.2023.2277960
To link to this article: https://doi.org/10.1080/1350486X.2023.2277960
© 2023 The Author(s). Published by Informa
UK Limited, trading as Taylor & Francis
Group.
Published online: 19 Nov 2023.
Submit your article to this journal
Article views: 6283
View related articles
View Crossmark data
Citing articles: 6 View citing articles
Full Terms & Conditions of access and use can be found at
https://www.tandfonline.com/action/journalInformation?journalCode=ramf20

2023, VOL. 30, NO. 2, 94–121
https://doi.org/10.1080/1350486X.2023.2277960
Simulation of Arbitrage-Free Implied Volatility Surfaces
Rama Cont and Milena Vuletić
Mathematical Institute, University of Oxford, Oxford, England
ABSTRACT
ARTICLE HISTORY
Received 26 June 2023
We present a computationally tractable method for simulating
Accepted 25 October 2023
arbitrage-free implied volatility surfaces. We illustrate how our
method may be combined with a data-driven model based on hisKEYWORDS
torical SPX implied volatility data to generate dynamic scenarios for
Implied volatility; options
arbitrage-free implied volatility surfaces. Our approach conciliates
markets; volatility index;
staticarbitrageconstraintswitharealisticrepresentationofstatistical
simulation; arbitrage
properties of implied volatility co-movements.
1. Introduction
Market prices of options are quoted in terms of their Black-Scholes implied volatilities,
obtained by inverting the Black Scholes formula given the market price of the option. It
has been empirically documented across many options markets that the implied volatility
t(K, T) associated with a call option with exercise price K and maturity date T actually depends on (K, T) (Cont and da Fonseca 2002; Dumas, Fleming, and Whaley 1998;
Dupire 1994; Gatheral 2011; Heynen 1994). The function t : (K, T) →t(K, T) which
represents this dependence, called the implied volatility surface at date t, provides a snapshot of prices in the options market (Kamal and Gatheral 2010). An example is given in
Figure 1 for SPX index options.
Two features of this surface have captured the attention of researchers in financial modeling. First, the non-flat instantaneous profile of the surface, whether it be a ‘smile’, ‘skew’ or
the existence of a term structure, point out to the insufficiency of the Black Scholes model
for matching a set of option prices at a given time instant and have led to various generalizations of the Black-Scholes model which aim at reproducing realistic instantaneous
profiles for the surface t(K, T). Second, the fact that the surface itself changes randomly
with time as a result of supply and demand in the options market means that a good risk
management model must not only fit the shape of the surface at a given date but also give
realistic dynamics for co-movements of implied volatilities across strikes and maturities.
Market models of implied volatility (Babbar 2001; Carmona, Ma, and Nadtochiy 2017;
Cohen, Reisinger, and Wang 2023; Cont and da Fonseca 2002; Cont, Fonseca, and Durrleman 2002; Gatheral and Jacquier 2014; Martini and Mingone 2022; Schönbucher 1999;
Schweizer and Wissel 2008) attempt to directly model the cross-section and dynamics
of implied volatilities. One of the challenges in modeling implied volatility surfaces is to
CONTACT Milena Vuletić
milena.vuletic@maths.ox.ac.uk
© 2023 The Author(s). Published by Informa UK Limited, trading as Taylor & Francis Group.
This is an Open Access article distributed under the terms of the Creative Commons Attribution License (http://creativecommons.org/
licenses/by/4.0/), which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.
The terms on which this article has been published allow the posting of the Accepted Manuscript in a repository by the author(s) or with their
consent.

95
Figure 1. SPX implied volatility surface on 01/11/2021.
ensure that the absence of static arbitrage is satisfied. Indeed, the profile of the implied
volatility surface cannot be arbitrary: static arbitrage constraints on the values of call
and put options (Davis and Hobson 2007) put restrictions on the possible shape of the
implied volatility surface. Analytical modeling has focused on obtaining parameterisations
of implied volatility surfaces which guarantee that such arbitrage constraints are satisfied
(Carmona, Ma, and Nadtochiy 2017; Cohen, Reisinger, and Wang 2023; Schweizer and
Wissel 2008). Such models, however, are computationally challenging to implement, and
even more challenging to calibrate to obtain realistic surface dynamics.
We present a computationally tractable method for simulating arbitrage-free implied
volatility surfaces, which correctly captures the co-movements of implied volatility across
a range of strikes and maturities. We first perform data analysis on the SPX implied volatility surface, and we then illustrate how our method may be combined with a factor model
for the implied volatility surface to generate dynamic scenarios for arbitrage-free implied
volatility surfaces. We give two examples: a stylized model using basis functions representing level, skew and curvature, and a data-driven example based on principal component
analysis of daily changes in the logarithm of the SPX implied volatility surfaces. Our
approach conciliates static arbitrage constraints with a realistic representation of statistical
properties of implied volatility co-movements.
Outline Section 2 defines some notation for implied volatility surfaces and recalls some
desired properties that market models of implied volatility have attempted to capture. In
this section, we also perform data analysis of the SPX implied volatility and show that
the co-movements can be captured by a small number of principal components. Section 3
recalls static arbitrage constraints on the implied volatility surface and introduces a penalty
function for quantifying static arbitrage violations. We propose a Weighted Monte Carlo
approach (Avellaneda et al. 2001) in Section 4 which prunes scenarios generated from a

96
base model using this penalty function. We illustrate in Section 5 how this approach may
be applied to a factor model for the implied volatility surface (Cont and da Fonseca 2002).
2. Implied Volatility Surfaces
2.1. Properties of Implied Volatility Surfaces
Consider a market where (European) call and put options are traded on an underlying asset
whose price we shall denote by St, across a range of strikes K and maturity dates T. The
Black Scholes formula for the value of a call option with time to maturity τ = T −t and
moneyness m = K/St is:
CBS(St, K, τ, σ) = StN(d1) −Ke−rτN(d2)
(1)
d1 = −ln m + τ(r + σ 2
d2 = −ln m + τ(r −σ 2
2 )
2 )
σ√τ
σ√τ
(2)
where N(u) = (2π)−1/2  u
−∞exp(−z2
2 )dz.
Conversely, given the (observed) market price C∗
t (K, T) of such a call option, the BlackScholes implied volatility t(K, T) is defined as the value of the volatility parameter which
equates the market price with the Black-Scholes value:
CBS(S, K, T −t, t(K, T)) = C∗
∃!
t(K, T) > 0,
t (K, T)
(3)
From the implicit function theorem, one expects that in general  will depend on t, S, T, K
(and of course on the randomness ω!). For fixed (K, T), t(K, T) is in general a stochastic
process and, for fixed t, its value depends on the characteristics of the option: the maturity T
and the strike level K. The function t : (K, T) →t(K, T) is called the implied volatility
surface at date t. Using the moneyness m = K/St of the option, one can also represent the
implied volatility surface as a function of moneyness and maturity:
σt(m, τ) = t(mSt, t + τ)
(4)
This representation is convenient since there is usually a range of moneyness around m = 1
for which the options are most liquid and therefore the empirical data is most readily available. The implied volatility surface today gives a snapshot of today’s market prices of vanilla
options: given the current term structure of interest rates and dividends, specifying the
implied volatility surface is equivalent to specifying prices of all vanilla options quoted on
the market.
A plethora of models have been proposed to model the instantaneous profile in (m, τ) of
the implied volatility surface: local volatility models, jump-diffusion models and stochastic
volatility models with or without jumps (Gatheral 2011). These ‘smile’ models are defined
in terms of stochastic differential equations whose parameters describe the infinitesimal
evolution of the asset price: since this evolution is not directly observed, calibration of
model parameters to market prices of options turns out to be a non-trivial problem. However, even in cases where perfect calibration to today’s option prices is achievable by a
non-parametric model (for example, a local volatility model), getting a perfect fit of the
implied volatility surfaces does not mean the model will generate realistic future scenarios.

97
This problem can be seen in the shape of the future smile (that is, the smile for forward-start
options) generated by the model: many of these models, while giving good fits to today’s
implied volatility/ call prices generate unrealistic forms for future smiles, thus leading to a
bias in prices of forward options.
Empirical studies of the behaviour of implied volatilities of exchange-traded options on
various market indices (SP500, FTSE, DAX and others) point to many common statistical properties across markets (Avellaneda et al. 2020; Cont and da Fonseca 2002), which
we summarize here and demonstrate on SPX data from 2000 to 2021 in the following
subsection:
(1) The implied volatility surface has a non-flat profile and exhibits both strike and term
structure.
(2) The shape of the implied volatility surface undergoes deformation in time.
(3) Implied volatilities display high (positive) autocorrelation and mean-reverting
behaviour.
(4) The variance of the daily log-variations in implied volatility can be satisfactorily
explained in terms of a small number of principal components.
(5) The first principal component reflects an overall shift in the level of all implied
volatilities.
(6) The second principal component reflects opposite movements in (out of the money)
call and put implied volatility.
(7) The third and fourth principal components reflect the term structure and the changes
in convexity of the implied volatility surface.
(8) Global level shifts in implied volatility are negatively correlated with the returns of the
underlying asset.
(9) The projections of the surface on its principal components (‘principal component
processes’) exhibit high (positive) autocorrelation and mean reversion. This autocorrelation structure is well represented by an AR(1)/ Ornstein Uhlenbeck process (Cont
and da Fonseca 2002).
These dynamical properties of co-movements of implied volatilities and the underlying
have important implications for hedging and should be reflected in any model used for
risk management.
The possible shapes of implied volatility surfaces are limited by the arbitrage constraints
on option prices. Call prices should be:
• increasing in time to maturity: ∂τCBS(St, K, τ, σt(m, τ)) ≥0,
• decreasing in moneyness: ∂mCBS(St, K, τ, σt(m, τ)) ≤0,
• convex in moneyness: ∂2
mCBS(St, K, τ, σt(m, τ)) ≥0.
These constraints translate to nonlinear inequalities involving σt, ∂mσt, ∂2
mσt, ∂τσt (Cont,
Fonseca, and Durrleman 2002). The resulting constraints on σt and the appropriate
derivatives impose restrictions on the possible shapes.
Any option pricing model implies a dynamic model for the implied volatility surface.
However, the corresponding shapes and dynamics are often intractable. ‘Market models’
of implied volatility aim to model implied volatility directly. The goal of such models has

98
been to correctly capture the co-movements of implied volatilities of options across different strikes and maturities while satisfying the no-arbitrage conditions, a challenging
task, which has been capturing the attention of researchers for over 20 years. Statistical
models of implied volatility dynamics (Avellaneda et al. 2020; Cont and da Fonseca 2002)
have focused on correctly capturing the statistical properties of the market data and the
co-movements across different strikes and maturities. These models are tractable and have
been adopted for risk management applications, such as margin computations, but may
lead to scenarios which are not compatible with arbitrage constraints. In parallel, analytical
models have been developed with the goal of satisfying static (Gatheral and Jacquier 2014;
Martini and Mingone 2022; Zhang, Li, and Zhang 2023), and dynamic arbitrage constraints
(Carmona, Ma, and Nadtochiy 2017; Cohen, Reisinger, and Wang 2023; Schweizer and
Wissel 2008; Wissel 2008). These models are computationally challenging to implement,
simulate or estimate.
In the remainder of the paper, we describe an approach which aims to conciliate computational tractability, arbitrage constraints and realistic dynamics for the surface, and
demonstrate its performance in two examples.
2.2. Case Study: Dynamics of the SPX Implied Volatility Surface
We consider a grid (m, τ) with 10 equispaced moneyness values between 0.6 and 1.4, and
8 time-to-maturity values of 30, 60, 91, 122, 152, 182, 273, 365 calendar days. We use
daily time series of implied volatility for SPX options from the OptionMetrics SPX Implied
Volatility Surface File for the period 2000-2021. Surfaces are interpolated linearly first in
moneyness, and then in time to maturity to yield values on the grid (m, τ). The average
SPX implied volatility profile σ shown in Figure 2.
We note that the Implied Volatility Surface File is based on a previous interpolation of listed option prices so may not necessarily be arbitrage-free, as already noted in
Cohen, Reisinger, and Wang (2023). We perform principal component analysis on the daily
changes in the logarithm of the implied volatility surface
Yt(m, τ) = log σt(m, τ)
(5)
using a Karhunen-Loève decomposition (Cont and da Fonseca 2002). We denote by fi the
eigenvectors of the covariance operator of Yt = Yt+t −Yt ordered by decreasing eigenvalue. Each eigenvector may be represented as a function (m, τ) →fi(m, τ) of moneyness
and time to maturity. We project Yt −˜Y, where ˜Y = log σ(m, τ), onto the eigenbasis:
k

Yt(m, τ) = ˜Y(m, τ) +
Xi
tfi(m, τ) + ϵt(m, τ),
(6)
i=1
where



t = ⟨Yt −˜Y, fi⟩=
Yt(m, τ) −˜Y(m, τ)
Xi
fi(m, τ)
(7)
(m,τ)∈(m,τ)

99
Figure 2. Average SPX implied volatility surface (2000–2021).
and ϵt(m, τ) is the projection error. The rank-k approximation of implied volatility
dynamics is given by
 k


Xi
σt(m, τ) ≈σ(m, τ) exp
tfi(m, τ)
.
(8)
i=1
2.2.1. Principal Component Analysis
To determine the number k of significant factors we consider the eigenvalues of the
correlation matrix of the daily log-variations in the SPX implied volatility surface Yt
and compare them with the corresponding Marčenko-Pastur threshold λ+ (Avellaneda
et al. 2020; Dobi 2014):
2

N
λ+ =
1 +
M
where N is the number of points on the grid (N = NmNτ), and M is the number of
observations. We treat the eigenvalues below λ+ as statistically insignificant.
As shown in Figure 3, there are k = 4 eigenvalues clearly above the Marčenko-Pastur
threshold. The first four principal components of the daily changes in the log SPX implied
volatility surface explain over 90% of the variance in the corresponding data (Table 1 ).
The first four eigenfunctions are shown in Figure 4. All four significant principal
components f1, f2, f3, f4 (Equation (8)) have natural interpretations:

100
Figure 3. Eigenvalues of the correlation matrix of the daily changes in the log SPX implied volatility
surface and the Marčenko-Pastur threshold λ+ (in red).
Table 1. Variance explained by the ﬁrst ﬁve eigenvectors of the covariance and the correlation operator
of the daily log returns of SPX implied volatilities.
PC1
PC2
PC3
PC4
PC5
Variance explained
68.88%
12.17%
5.67%
2.86%
1.41%
(covariance)
Cumulative variance explained
68.88%
82.05%
87.72%
90.59%
92.00%
(covariance)
Cumulative variance explained
61.39%
76.67%
81.88%
85.18%
86.96%
(correlation)
• The first principal component can be interpreted as the average level of implied volatilities. A positive shock along this mode would result in a global shift in implied
volatility.
• The second principal component corresponds to the skew. Shocks along this direction
result in opposite movements in out-of-the-money call and put implied volatilities.
• The third principal component reflects the term structure of implied volatilities.
• The fourth principal component can be interpreted as curvature. A positive shock along
this mode would have an opposite effect on the implied volatilities close to the money
and on the far out-of-the-money and in-the-money implied vols.
Projections of Yt(m, τ) −˜Yt(m, τ) onto the first four principal components Xi
t, (i =
1, . . . , 4) (defined by Equation (7) ) are shown in Figure 5. All processes exhibit high positive autocorrelation and mean-reverting behaviour with a period of mean reversion of
several months. The ACF and PACF of X1
t are shown in Figure 6. As shown in Figure 6,
the autocorrelation functions decay exponentially, suggesting that they can be modeled as
Ornstein-Uhlenbeck/AR(1) processes, as already observed by Cont and da Fonseca (2002).

101
Figure 4. The ﬁrst four principal components of the daily changes in log SPX implied volatility surface.
(a) Level (b) Skew (c) Term structure (d) Curvature.
Correlations of daily increments Xi
t = Xi
t+t −Xi
t (i = 1, . . . 4) and the log-returns
of the underlying Rt = log St+t −log St over a two-year rolling window are shown in
Table 2. We note that the log-returns Rt are negatively correlated with X1
t , X2
t , X4
t ,
while there is a positive correlation between the log-returns and the increments of the termstructure process X3.
2.2.2. Relationship with the VIX
The CBOE Volatility Index (VIX) is constructed as a linear combination of out-of-themoney tradable calls and puts with one month to expiry (CBOE 2022). We investigate the

102
t , X3
Figure 5. Principal component processes X1
t , X2
t , X4
t .
Table 2. Long-term and 2-year rolling daily correlation between the log-increments of SPX and the
t , X3
increments of X1
t , X2
t , X4
t (Equation (7)).
X3
X1
X2
X4
Correlation between Rt and
t
t
t
t
−38.21%
−25.64%
−26.39%
Long-term
26.42%
−48.83%
−37.75%
−32.63%
Rolling: mean
31.60%
relationship between the VIX and different variables of interest by considering the historical closing VIX prices available on the CBOE website. Figure 7 displays the correlations
between the log returns of VIX, one-month at-the-money SPX implied volatility, SPX and
the increments of the level process X1
t over a rolling 2-year window. We note a high positive correlation between the level movements and the log-returns of VIX and ATM vol.
Similarly, the returns of the underlying are negatively correlated with the increments of
the level process (Table 2), log-returns of VIX and with the log-returns of the ATM vol.
Correlations increasing in magnitude from 2006 onwards.
The one-month realized volatility ˆσt is estimated as
20

21
R2
ˆσt =
t−it.
(9)
252
i=0
Figure 8 shows that the realized volatility is usually below the implied volatility. The average ratio of realized volatility to ATM volatility is 0.59, with a standard deviation of 0.209
(Figure 8).
3. Static Arbitrage Constraints
We now consider shape constraints on the implied volatility surfaces arising from static
arbitrage inequalities (Davis and Hobson 2007). We are interested in a realistic setting

103
Figure 6. Autocorrelation and partial autocorrelation of the log implied volatility projection on the ﬁrst
principal component. The autocorrelation function (above) in logarithmic scale shows an exponential
decay characteristic of OU processes.
where only a finite number of options are available. We fix a grid in moneyness and time to
maturity (m, τ) = (mi, τj)i=1,...,Nm;j=1,...Nτ , with mi < mi+1 and τj < τj+1 for all i, j. Using
the notation introduced in Section 2, denote by
c(m, τ) := 1
SCBS(S, K, τ, σ) = N(d1) −me−rτN(d2)
the relative call price, which is a dimensionless quantity with 0 ≤c(m, τ) ≤1.
3.1. Arbitrage Constraints and Arbitrage Penalty
As shown by Davis and Hobson (Corollaries 4.2 and 4.3 in Davis and Hobson 2007),
absence of static arbitrage among options with strikes and maturities defined by (m, τ)
is equivalent to the following three conditions:

104
Figure 7. Correlation over a 2-year window between daily changes in the level process X1
t and daily
log-returns of one-month ATM vol, VIX, and SPX.
(1) Absence of calendar spread arbitrage:
c(mi, τj) −c(mi, τj+1)
≤0,
τj
(10)
τj+1 −τj
for j = 1, . . . , Nτ −1 and i = 1, . . . , Nm.
(2) Absence of call spread arbitrage:
c(mi+1, τj) −c(mi, τj)
≤0
(11)
mi+1 −mi
for i = 1, . . . , Nm −1 and j = 1, . . . , Nτ.
(3) Absence of butterfly spread arbitrage:
c(mi, τj) −c(mi−1, τj)
−c(mi+1, τj) −c(mi, τj)
≤0
(12)
mi −mi−1
mi+1 −mi
for i = 2, . . . , Nm −1 and j = 1, . . . , Nτ.
Conversely, a non-zero positive part of the left-hand side of these inequalities indicates the
presence of static arbitrage. We investigate whether an implied volatility surface σ(m, τ) is
arbitrage-free by considering the inequalities (10), (11) and (12).
Hence, for an implied volatility surface σ(m, τ), we define the arbitrage penalty
(σ(m, τ)) as
(σ(m, τ)) = p1(σ(m, τ)) + p2(σ(m, τ)) + p3(σ(m, τ)),
(13)

105
Figure 8. Above: SPX realized volatility (blue), one-month ATM volatility (orange) and VIX (green).
Below: ratio of VIX to one-month ATM volatility (blue) and ratios of 21-day realized volatility to onemonth ATM volatility, VIX to ATM volatility, and VIX to realized volatility.
where

+
Nm
Nτ


c(mi, τj) −c(mi, τj+1)
p1(σ(m, τ)) =
τj
,
(14)
τj+1 −τj
i=1
j=1
c(mi+1, τj) −c(mi, τj)
+
Nm
Nτ


p2(σ(m, τ) =
,
(15)
mi+1 −mi
i=1
j=1
c(mi, τj) −c(mi−1, τj)
+
Nm
Nτ


−c(mi+1, τj) −c(mi, τj)
p3(σ(m, τ)) =
.
(16)
mi −mi−1
mi+1 −mi
i=1
j=1

106
The quantities p1, p2, p3 correspond to deviations from the calendar, call, and butterfly
spread arbitrage constraints, respectively. They are the positive parts of the left-hand sides
of the inequalities (10), (11), and (12). If p1, p2, p3 are all equal to zero, there is no arbitrage. Conversely, if any of p1, p2, p3 are non-zero, then there is arbitrage present in σ(m, τ).
Therefore,
(σ(m, τ)) = 0 ⇐⇒σ(m, τ) is arbitrage-free.
We introduce the Nm · Nτ penalty matrices P1, P2, P3 defined as

+
c(mi+1, τj) −c(mi, τj)
+
c(mi, τj) −c(mi, τj+1)
(P1)i,j =
τj
(P2)i,j =
,
τj+1 −τj
mi+1 −mi
+
c(mi, τj) −c(mi−1, τj)
−c(mi+1, τj) −c(mi, τj)
(P3)i,j =
,
mi −mi−1
mi+1 −mi
with the appropriate endpoints being set to zero: (P1)i,Nτ = 0 for i = 1, . . . Nm, (P2)Nm,j =
0, (P3)Nm,j = (P3)0,j = 0 for j = 1, . . . , Nτ. The arbitrage penalty may then be expressed as
the 1-norm of the matrix P1 + P2 + P3:
Nm
Nτ


(σ(m, τ)) =
(P1 + P2 + P3)i,j = ∥P1 + P2 + P3∥1.
i=1
j=1
Remark 3.1 (Extension to swaption implied volatility cube): When working with swaptions, for every tenor Ta there is an implied volatility surface σ a(m, τ). Hence, one could
calculate the arbitrage penalty for each possible surface (across all of the available tenors)
in order to reach an aggregated penalty for the swaption implied volatility cube. That is,
suppose that we have available tenors T1, . . . , TA. Then we may define the arbitrage penalty
for the swaption implied volatility cube {σ a
t (m, τ)}a=1...A by
A

1({σ a
(σ a
t (m, τ)}a=1...A) =
t (m, τ)),
(17)
a=1
or by
∞({σ a
a=1,...,A (σ a
t (m, τ)}a=1...A) =
t (m, τ)).
max
(18)
3.2. Behaviour of Arbitrage Penalty Under Perturbations
To gain intuition about the properties of arbitrage penalty (13) we investigate its behaviour
under perturbations of an arbitrage-free implied volatility surface by IID noise and parallel
shifts. In the numerical results below, the initial implied volatility surface is taken to be the
SPX implied volatility surface on 31/12/2021.
Addition of IID noise We sample 10,000 implied volatility surfaces by adding IID noise
(i.e. ,independent across strike and maturity) with a standard deviation of ϵ = 0.001 to
the initial arbitrage-free SPX implied volatility surface. We observe that 23% of generated
surfaces exhibit butterfly spread arbitrage. The mean butterfly arbitrage penalty matrix P3 is

107
Figure 9. Butterﬂy penalty matrices (P3) arising from noise and parallel shifts. (a) Mean eﬀect of adding
noise (b) Sample parallel shift eﬀect.
displayed in Figure 9. We note that violations occur only for far from the money, long-dated
options.
Parallel shifts Rogers and Tehranchi (2010) showed that moving implied volatility surfaces by parallel shifts will eventually result in configurations with static arbitrage. We
explore this phenomenon quantitatively by adding a parallel shift to an initial arbitragefree implied volatility surface (SPX implied volatility surface on 31/12/2021) and testing
for static arbitrage. The absolute value of the largest negative shift is taken to be smaller
than the smallest implied volatility value, guaranteeing non-negativity. The effect of parallel shifts on the arbitrage penalty are displayed in Figure 10: arbitrage constraints are
violated for large enough positive shifts, and the arbitrage penalty grows linearly thereafter. For such large shifts, the constraint which is violated is convexity. A sample butterfly
arbitrage penalty matrix P3 is displayed in Figure 9(b). These results give a quantitative
perspective on the results of Rogers and Tehranchi (2010).
3.3. Arbitrage Penalty in SPX Implied Volatility Data
Data sources on implied volatility, such as OptionMetrics, are often interpolated from
actual market quotes, a procedure which may itself introduce static arbitrage. This has
been previously noted by several studies, see e.g. Cohen, Reisinger, and Wang (2023). We
study this phenomenon using daily SPX implied volatility surfaces from 2000 to end 2021.
We observe non-zero arbitrage penalties, with a decomposition displayed in Figure 11 and
Table 3. 90.5% of dates display no calendar arbitrage, 97.3% display no call spread arbitrage and 84.9% no butterfly arbitrage. Overall 80.2% of the observations correspond to
abitrage-free surfaces.
We observe a number of spikes in arbitrage penalties. The two largest spikes happen on
29/09/2008 (during the 2008 financial crisis) and on 13/03/2020 (the start of the Covid-19
pandemic). Figure 11 shows that the majority of arbitrage violations happen during the
2008 financial crisis and during the start of the Covid-19 pandemic. For comparisons, the

108
Figure 10. Arbitrage violations induced by parallel shifts on SPX implied volatility surface (31/12/2021).
Figure 11. Arbitrage penalty decomposition for SPX options.
calendar, call, and butterfly arbitrage penalty matrices P1, P2, P3 on dates 29/09/2008 and
13/03/2020 are displayed in Figures 12–14, respectively.

109
Table 3. Quantiles of arbitrage penalties for SPX options.
Penalty
Median
90th quantile
95th quantile
99th quantile
Total
0
0.075
0.13
0.5
Calendar spread p1
0
0
0.002
0.038
Call spread p2
0
0
0
0.009
Butterﬂy spread p3
0
0.01
0.06
0.458
Figure 12. Calendar spread arbitrage (P1) for SPX options. (a) 29.09.2008 (b) 13.03.2020.
Figure 13. Call spread arbitrage (P2) for SPX options. (a) 29.09.2008 (b) 13.03.2020.

110
Figure 14. Butterﬂy spread arbitrage (P3) for SPX options. (a) 29.09.2008 (b) 13.03.2020.
4. Penalizing Static Arbitrage
4.1. Penalization Via Scenario Reweighting
Our starting point is a baseline model P0 for implied volatility surface dynamics, which
correctly captures the co-movements and statistical properties of implied volatilities and
the underlying asset, but may not necessarily be arbitrage-free. For example, this may
be a factor model based on PCA, such as Avellaneda et al. (2020) and Cont and da
Fonseca (2002).
We are interested in generating market scenarios over a time grid T = {0, . . . , tmax}. P0
may be a discrete-time or continuous-time model. For ease of notation, we will continue
to denote by P0 the joint law of the variables (St, σt(m, τ), t ∈T) under P0.
Our idea is to penalize arbitrage along the paths generated by P0 by ‘tilting’ the probabilities associated with such paths. We choose β > 0 and define a new probability Pβ on
the space of market scenarios by


−β 
t∈T (σt(m, τ; ω))
dPβ
(ω) = exp
(19)
dP0
Z(β)
where Z(β) is a normalization factor:




Z(β) = EP0
−β
(σt(m, τ))
exp
.
(20)
t∈T
If the baseline modelP0 is arbitrage-free then (σt(m, τ)) = 0P0-almost surely so Z(β) =
1 and Pβ = P0. If, however, P0 generates surfaces which violate static arbitrage constraints,
then the change of measure (19) penalizes such scenarios, and may be thought of as an
importance sampling method which penalizes static arbitrage violations. This penalization
increases if we take large β and as β →∞we reject all scenarios violating static arbitrage
constraints. Thus one may think of 1/β as a ‘tolerance’ for static arbitrage.

111
Note that Pβ is absolutely continuous with respect to P0 so we are keeping the same
paths but re-weighting them. In the case where the dynamics of variables are given by
stochastic differential equations driven by Brownian motion, Girsanov’s theorem implies
that the re-weighting will impact the drift, but not the quadratic covariation of the variables.
However, our approach does not assume that variables are driven by Brownian motion
factors, and may be applied in a more general setting. Indeed, the whole procedure also
makes sense for a discrete-time time series model.
4.2. A ‘Weighted Monte Carlo’ Approach
We now propose a method for sampling from Pβ, using a Weighted Monte Carlo approach
(Avellaneda et al. 2001). We proceed as follows:
• Simulate N independent paths (ωi, i = 1, . . . , N) from P0. Each path corresponds to the
joint evolution of the underlying asset and the implied volatility surface:
ωi = (St(ωi), σ t(m, τ; ωi); t ∈{0, . . . , tmax})
• Compute the arbitrage penalty ϕ(ωi) along each path:

ϕ(ωi) =
(σ t(m, τ; ωi)).
(21)
t∈{0,...,tmax}
• Associate a weight wi(β) with each path:
exp (−βϕ(ωi))
wi(β) =

.
(22)
N
−βϕ(ωj)
j=1 exp
• Sample from the weighted model PN
β defined as
PN
β (ωi) = wi(β)
i = 1, . . . , N.
(23)
That is, instead of sampling each simulated path ωi with probability 1
N , sample it with
probability wi(β).
This step-by-step procedure is summarized in Table 4.
Note that we keep the same paths but modify their weight. Thus, all quantities computed
along the path, such as realized volatility and realized covariances will remain the same.
As β →∞, wi(β) →0 as soon as ϕ(ωi) > 0 so only paths with arbitrage-free implied
volatility surfaces survive for large β. Hence, 1
β can be viewed as an arbitrage tolerance
parameter.
If the model P0 is arbitrage-free, then the re-weighting will have no influence as for
every β > 0 we will have wi(β) = 1
N , implying that PN
β is simply the empirical distribution
associated with the N simulated paths. In the general case, the relative entropy of PN
β with
respect to this empirical distirbution (i.e. ,the uniform distirbution on {ωi, i = 1, . . . , N} is

112
Table 4. Weighted Monte Carlo for implied volatility scenarios.
Ingredients
• ‘Baseline model’ P0 for implied volatility surface dynamics.
• Time grid T = {0 = t0 < t1 < · · · < tmax}.
• Moneyness and time to maturity grid (m, τ) = (mi, τj)i=1,...,Nm;j=1,...Nτ .
• Number of paths N.
• Arbitrage penalty parameter β > 0.
Step 1: Simulate N independent scenarios ωi, i = 1, . . . , N from the
baseline model P0. Each scenario ωi represents a joint evolution of the
underlying asset St and the implied volatility surface σ t(m, τ) for t ∈{0, . . . , tmax}:
ωi = (St(ωi), σ t(m, τ; ωi); t ∈{t0, . . . , tmax}) .
Step 2: For each simulated path σ(m, τ)i, compute the arbitrage penalty

ϕ(ωi) =
(σt(m, τ; ωi) ).
t∈T
Step 3: If ϕ(ωi) = 0 for all i = 1 . . . N →STOP, else.
Step 4: Compute the weights
exp(−βϕ(ωi))
wi(β) =
.
N
j=1 exp(−βϕ(ωj))
Step 5: Compute the relative entropy EN(β) = H(PN
β|PN
0 ).
Step 6: Sample the scenarios ωi, i = 1, . . . , N with probability wi(β):
PN
β(ωi) = wi(β).
an indicator of the ‘distance to no-abitrage’:
N

EN(β) = H(PN
β |PN
0 ) = −N ln N −N
wi(β) ln wi(β).
(24)
i=1
When there is no static arbitrage in the scenarios ωi generated by P0, then relative entropy
is zero: EN(β) = 0. On the other hand, the model P0 is far from being arbitrage-free, the
arbitrage penalties ϕ(ωi) are large and the relative entropy EN(β) will be large.
Our approach is more efficient than rejection sampling, as we sample a fixed number of
paths, regardless of the initial model P0, so the complexity is of order O(N). If the scenarios
generated by P0 are likely to admit static arbitrage, even if the penalty is small and arises
from interpolation, rejection sampling may result in an infinite loop.
The following result, which we state for completeness, clarifies the relation between the
various probability measures involved. We use the notation of Section 4.1.
Proposition 4.1: (i) PN
β weakly converges to Pβ as the number of scenarios N →∞.
(ii) Let U = {ω ∈, ϕ(ω) = 0} be the set of scenarios free of static arbitrage. If P0(U) > 0
then, as β →∞, the support of Pβ concentrates on U:
β→∞
Pβ ({ϕ > ε})
∀ε > 0,
→0.
(25)
Proof: (i) is a consequence of the weak law of large numbers. To show (ii), first note that
if P0 is supported on arbitrage-free scenarios, then so is Pβ. Hence, suppose that P0 is not
supported on the (closed) set U = {ω ∈, ϕ(ω) = 0}. The arbitrage penalty

ϕ : ω ∈ →
(σt; ω)
t∈T

113
defines a random variable on scenario space and U = {ϕ = 0} ∈Ftmax. Note that since
defined by (13) is bounded, so is ϕ. Define
An = {ω ∈, ϕ(ω) > 1/n} ∈Ftmax.
Then A = Uc = {ϕ > 0} = ∩n≥1An. If P0 is not supported on U, there exists n ≥1 such
that P0(An) > 0.

An exp (−βϕ(ω)) dP0(ω)
Pβ(An) =
.
Z(β)
Since ϕ = 0 on U ⊂Ac
n, we have


Uc exp (−βϕ(ω)) dP0(ω) +
dP0(ω) ≥P0(U)
Z(β) =
U
Also, since ϕ > 1/n on An, we have

exp (−βϕ(ω)) dP0(ω) ≤P0(An) exp(−β/n) →0
as β →∞.
An
Hence,
Pβ(An) ≤P0(An) exp(−β/n)
→0
as β →∞.
P0(U)
■
Taking n > 1/ε yields the result.
5. Factor Models for Implied Volatility Dynamics
In order to illustrate our approach, we consider factor models for implied volatility dynamics as the baseline model P0. We first simulate scenarios from the three-factor model
introduced in Cont and da Fonseca (2002), and then from a four-factor model for the SPX
implied volatility surface based on our previous analysis in Section 2.
5.1. Example: A Stylized Factor Model for Implied Volatility
We first consider a three-factor for implied volatility dynamics introduced in Cont and da
Fonseca (2002), based on a Karhunen-Loeve decomposition of co-movements in implied
volatilities. The evolution of implied volatility surface paths in this model is given by


x1
t f1(m, τ) + x2
t f2(m, τ) + x3
σt(m, τ) = σ0(m, τ) exp
t f3(m, τ)
(26)
t , x3
where the factors x1
t , x2
t correspond to level, skew and curvature, as projections on principal components with the analogous representations (Cont and da Fonseca 2002). Their
dynamics are modeled as independent Ornstein-Uhlenbeck processes:


dxi
αi −xi
dt + γi dWi
t = λi
t,
(27)
t
where Wi
t are independent Brownian motions. The basis functions f1, f2, f3 are the first
three principal components of the log-implied volatility surface. The price of the underlying asset S is modeled as a diffusion with stochastic volatility σt(1, 0), which corresponds

114
Figure 15. Basis functions f1, f2, f3 corresponding to level, skew and curvature used to simulate scenarios from the factor model (26)–(27). (a) f1(m, τ) (b) f2(m, τ) (c) f3(m, τ).
to the short-term at-the-money implied volatility:

1 −ρ2 Bt,
dSt = σt(1, 0)St dW0
W0
t = ρW1
t +
t ,
(28)
where ρ < 0 and B is a Brownian motion independent from Wi, i = 1, 2, 3. The increments of the first factor x1
t are negatively correlated with the returns of the underlying
asset: cov(W0
t , W1
t ) = ρt < 0. We use ρ = −0.5 and r = 0 as an example.
Given that this model is based on a principal component analysis of market data,
the simulated paths correctly capture the covariance structure of implied volatility comovements. Furthermore, the functional form (26) of the implied volatility surface
guarantees smoothness of the surface and continuity of simulated paths.
In the first example, we suppose αi = 0, γi = 1 and use the coefficients λi given in Cont
and da Fonseca (2002) for the SPX implied volatilities to drive the level, skew and curvature
t , x3
processes x1
t , x2
t . The basis functions are based on the first three principal components
of the market data and displayed in Figure 15. The initial surface σ0 was taken to be the
arbitrage-free SPX implied volatility surface on 31/12/2021.
As shown by Rogers and Tehranchi (2010), an affine factor model such as (26)–(27)
may violate static arbitrage constraints, so we apply the re-weighting procedure described
in Table 4. We simulate N = 100,000 3-month scenarios from the factor model (26)–(27).
Among these scenarios, 64.8% were arbitrage-free. However, even when the arbitrage
penalty of a simulated path was non-zero, it was much lower than that of SPX implied vol
data. Quantiles of arbitrage penalties across different Pβ are displayed in Table 5. When
comparing the arbitrage penalty quantiles to those of SPX implied volatility displayed in
Table 3, it is important to note that the factor model arbitrage penalties are calculated for
paths, whereas the SPX market data arbitrage penalties are for individual surfaces only.
In the scenarios generated by the factor model (26)–(27), only butterfly arbitrage was
observed. All simulated implied volatility surfaces satisfied the absence of calendar and
call spreads. The pattern of violations in the butterfly constraint resemble the violations
induced by the addition of IID noise perturbations in Section 3.
Table 5 displays quantiles of the arbitrage penalty ϕ defined by (21) under PN
β . To compute the qth quantile of the arbitrage penalty under PN
β , we sort the scenarios in increasing
order of arbitrage penalties ϕ(ω(1)) ≤ϕ(ω(2)) ≤· · · ≤ϕ(ω(N)). The qth quantile is then

115
Table 5. QuantilesofarbitragepenaltyunderPN
β inscenariossimulatedfromthefactormodel(26)–(27).
102
103
104
105
β
0
90th quantile
0.044
0.001
0
0
0
95th quantile
0.09
0.004
0.0001
0
0
99th quantile
0.206
0.014
0.001
0.0004
0
Figure 16. Relative entropy H(PN
β|PN
0) in (26)–(27) as a function of β.
estimated as:
j

F−1
ϕ (q) = ϕ(ω(k)),
k = min{j ∈{1, . . . , N} :
w(ω(i)) ≥q}.
(29)
i=1
As we increase β, we are less and less likely to sample a path with non-zero arbitrage penalty.
Table 5 shows that with β = 105, 99% of scenarios are arbitrage-free. In this example, for
β = 1010, we are left with arbitrage-free paths only.
Figure 16 shows the relative entropy E(β) = H(PN
β |PN
0 ) as a function of β. We observe a
sharp transition around β = 100, suggesting that for β ≫102 the penalization eliminates
scenarios with arbitrage.
The histogram of weights wi(102) (Figure 17) illustrates the clustering of weights into
two groups: those corresponding to arbitrage-free scenarios, which are equally weighted,
and those corresponding to scenarios with arbitrage penalty ϕ(ωi) > 0 whose weights are
driven very close to zero. We note that even with β = 102, some of the weights are already
very close to zero.
We conclude that for the factor model (26)–(27) the impact of the penalty step is small
in terms of entropy distance.

116
Figure 17. Histogram of Nw(β) with β = 102 in (26)–(27).
5.2. Example: Factor Model for the SPX Implied Volatility Surface
We now give an example of a factor model for the SPX implied volatility surface based on
the findings from Section 2. As in the factor model (26)–(27), we consider the following
dynamics:
 4

xi
σt(m, τ) = σ(m, τ) exp
tfi(m, τ)
,
(30)
i=1
t , x3
where the factors x1
t , x2
t , x4
t in this case correspond to level, skew, term structure and curvature, as projections on principal components with the analogous representations. Their
dynamics are once again modeled as independent Ornstein-Uhlenbeck processes:


dxi
αi −xi
dt + γi dWi
t = λi
i = 1, . . . , 4.
t,
(31)
t
The underlying asset S is modeled as a process with stochastic volatility proportional to the
one-month ATM volatility σt(1, 1
12), as discussed in Section 2:


1, 1
St dW0
dSt = ν σt
t ,
(32)
12



W0
t = ρ1W1
t + ρ2W2
t + ρ3W3
t + ρ4W4
ρ2
1 + ρ2
2 + ρ2
3 + ρ2
t +
1 −
Bt,
(33)
4
where ν > 0, ρ1, ρ2, ρ4 < 0, ρ3 > 0 and B, Wi, i = 1, . . . , 4 are independent Brownian
motions.
The factor model (30)–(31) may be adapted to any underlying asset. We demonstrate the
approach for SPX options, by using as factors the first four principal components displayed

117
Table 6. Estimated OU parameters for SPX implied volatility factors.
λ
α
γ
X1
2.018
–0.422
4.414
t
X2
0.986
–0.312
1.993
t
X3
1.258
0.097
1.295
t
X4
1.497
–0.021
0.824
t
Figure 18. Relative entropy H(PN
β|PN
0) as a function of β: SPX factor model (30)–(31).
in Figure 4 for f1, f2, f3, f4. We estimate αi, λi, γi, i = 1, . . . , 4 via a Generalized Method of
Moments (GMM), using the first two moments and the autocorrelation function at various lags as moment conditions. Estimates are shown in Table 6. We set ν = 1
2 and the
correlations ρi, i = 1, . . . , 4 to be the historical correlations from Table 2.
As in the previous example, we simulate 100,000 3-month paths from the model
(30)–(31), using the above hyperparameters. The initial surface is the average SPX implied
volatility σ (Figure 2), and the starting values for the level, skew, term structure and curvature processes are those observed on 31/12/2021. The percentage of paths and surfaces
admitting a non-zero arbitrage penalty is shown in Table 7.
The relative entropy, shown in Figure 18, exhibits a sharp transition around β = 10
indicating that the penalization efficiently eliminates scenarios with arbitrage. The effect
of β on arbitrage penalty is shown in Table 8. The arbitrage penalty in simulated scenarios is much lower than the historically observed penalties in the SPX implied volatilities
(Table 3), considering that the penalties in Table 8 correspond to 3-month paths. It becomes
negligible with β = 102, and arbitrage is effectively removed for β > 104 in this example.
Furthermore, we note that the quantiles of the arbitrage penalty in the SPX model (30)–(31)
(Table 8) decay faster with β compared to the corresponding quantiles in the factor
model (26)–(27) (Table 5).

118
Table 7. Arbitrage presence in scenarios from the SPX factor model (30)–(31).
Total
Calendar
Call
Butterfuly
Paths
62.761%
21.245%
36.548%
36.548%
Surfaces
16.055%
4.004%
9.117%
7.073%
Table 8. Quantiles of arbitrage penalty under PN
β for SPX factor model (30)–(31).
102
104
106
1010
1015
β
0
5 · 10−5
5 · 10−10
2 · 10−13
90th quantile
0.20
0
0
2 · 10−7
3 · 10−9
4 · 10−15
0
95th quantile
0.77
0.002
3 · 10−7
2 · 10−9
1 · 10−11
4 · 10−16
99th quantile
4.49
0.01
Figure 19. Simulation of a 10-year scenario for VIX (red) and SPX (blue) using the SPX factor
model (31)–(33).
Simulating the volatility index We simulate the VIX dynamics associated with the SPX
four-factor model (30)–(33) using the methodology from CBOE (2022). We fix the moneyness grid by taking 100 equispaced values between 0.5 and 1.5. We simulate 10-year VIX
1
and SPX paths using a frequency of one day t =
252 with the average SPX implied volatility surface, and the SPX price on the 31st Dec 2021 as the starting point. The remaining
hyperparameters are as in the previous simulations. Figure 19 displays simulated sample
paths for the underlying and VIX. We note that the model (30)–(33) is able to produce high
VIX values as historically observed during the 2008 financial crisis and during the Covid19 pandemic. Figure 20 displayes simulated paths for one-month realized vol, one-month
ATM vol and VIX. We note that the VIX and the ATM vol are higher than the one-month
forward realized vol. The ATM vol is usually below the VIX in the simulations, which is
consistent with the post-pandemic dynamics (Figure 8).
We further investigate the relationship between the simulated values of VIX, ATM vol,
SPX, and the level process. Pearson correlation between the simulated log-increments of
SPX, ATM vol, VIX, and the increments of the level process is shown in Table 9. We note
that the log-returns of the underlying are negatively correlated with the increments of the

119
Figure 20. Simulation of VIX (red), ATM volatility (green), and the 30-day realized volatility (purple)
using the SPX factor model (31)–(33).
Figure 21. Joint distribution of log-returns of VIX and the log-returns of SPX in simulations via the SPX
factor model (31)–(33) and in the historically observed data (2012–2021).

120
Table 9. Pearsoncorrelationbetweensimulatedvaluesoflog-returnsofSPX,returnsofthelevelprocess,
log-returns of the ATM vol, log-returns of VIX using the SPX factor model (31)–(33).
 log σ ATM
 log σ VIX
X1
 log St
t
t
t
 log St
1.00
–0.45
–0.31
–0.30
X1
–0.45
1.00
0.96
0.94
t
 log σ ATM
–0.31
0.96
1.00
0.99
t
 log σ VIX
–0.30
0.94
0.99
1.00
t
level process, the log-returns of ATM vol, and the log-returns of VIX. There is a high positive correlation between the log increments of the ATM vol, VIX, and the increments of
the level process. This is consistent with the historical correlations displayed in Figure 7.
In Figure 21 we compare the historical (2012–2021) and the simulated joint distribution
of the log-returns of SPX and of VIX. The means of the two distributions align, and the
corresponding marginal distributions of the simulated and historical values are close to
each other. However, we note that as the historical correlation between the log-returns of
SPX and of VIX is non-constant (Figure 7), the joint distribution changes through time as
well. The correlation between the log-returns SPX and VIX being lower in the simulations
than in the 2012–2021 historical data (Figure 21) can be contributed to the correlation
ρ1 used in simulations being lower than the average historical daily correlation of Rt and
X1
t for the time period 2012–2021 (Figure 7). Overall, we conclude that the four-factor
model (31)–(33) is able to generate realistic scenarios for VIX, consistent with the historical
observations.
6. Conclusion
We introduced a simple and computationally tractable method for simulating arbitragefree implied volatility surfaces. Our approach offers flexibility with respect to the underlying model for implied volatility dynamics, whilst preserving the co-movements across
strikes and maturities.
Our approach enables to combine a data-driven multifactor model with a Weighted
Monte Carlo method in order to conciliate static arbitrage constraints with a statistically
realistic representation of co-movements of implied volatilities.
Acknowledgments
We thank Katia Babbar, Andrey Chirikhin, Samuel N. Cohen, Bruno Dupire, Blanka Horvath,
Terry Lyons, Fabio Mercurio, Christoph Reisinger, Justin Sirignano and seminar participants at
QuantMinds 2022 for helpful comments and remarks.
Disclosure statement
No potential conflict of interest was reported by the author(s).
Funding
Milena Vuletić’s research is supported by BNP Paribas through the EPSRC Centre for Doctoral
Training in Mathematics of Random Systems: Analysis, Modelling and Simulation (ESPRC Grant
EP/S023925/1).

121
References
Avellaneda M., Buff R., Friedman C., Grandchamp N., Kruk L., and Newman J. 2001. “Weighted
Monte Carlo: A New Technique for Calibrating Asset-Pricing Models.” International Journal of
Theoretical and Applied Finance 04 (01): 91–119. https://doi.org/10.1142/S0219024901000882.
Avellaneda M., Healy B., Papanicolaou A., and Papanicolaou G. 2020. “PCA for Implied Volatility
Surfaces.” The Journal of Financial Data Science 2 (2): 85–109. https://doi.org/10.3905/jfds.2020.
1.032.
Babbar K. A. 2001. “Aspects of Stochastic Implied Volatility in Financial Markets.” PhD diss.,
Imperial College London.
Carmona R., Ma Y., and Nadtochiy S. 2017. “Simulation of Implied Volatility Surfaces
Via Tangent Lévy Models.” SIAM Journal on Financial Mathematics 8 (1): 171–213.
https://doi.org/10.1137/15M1015510.
CBOE. 2022. “Volatility Index Methodology: CBOE Volatility Index.” Accessed May 08, 2023.
https://cdn.cboe.com/api/global/us_indices/governance/VIX_Methodology.pdf.
Cohen S. N., Reisinger C., and Wang S. 2020. “Detecting and Repairing Arbitrage in Traded Option
Prices.” Applied Mathematical Finance 27 (5): 345–373. https://doi.org/10.1080/1350486X.2020.
1846573.
Cohen S. N., Reisinger C., and Wang S. 2023. “Arbitrage-free Neural-SDE Market Models.” Applied
Mathematical Finance 30 (1): 1–46. https://doi.org/10.1080/1350486X.2023.2257217.
Cont R., and da Fonseca J. 2002. “Dynamics of Implied Volatility Surfaces.” Quantitative Finance 2
(1): 45–60. https://doi.org/10.1088/1469-7688/2/1/304.
Cont R., Fonseca J. D., and Durrleman V. 2002. “Stochastic Models of Implied Volatility Surfaces.”
Economic Notes 31 (2): 361–377. https://doi.org/10.1111/ecno.2002.31.issue-2.
Davis M. H., and Hobson D. G. 2007. “The Range of Traded Option Prices.” Mathematical Finance
17 (1): 1–14. https://doi.org/10.1111/mafi.2007.17.issue-1.
Dobi D. 2014. “Modeling Systemic Risk in the Options Market.” PhD diss., Department of Mathematics, New York University.
Dumas B., Fleming J., and Whaley R. E. 1998. “Implied Volatility Functions: Empirical Tests.” The
Journal of Finance 53 (6): 2059–2106. https://doi.org/10.1111/jofi.1998.53.issue-6.
Dupire B. 1994. “Pricing with a Smile.” Risk 7 (1): 18–20.
Gatheral J. 2011. The Volatility Surface: A Practitioner’s Guide. Chichester: John Wiley & Sons.
Gatheral J., and Jacquier A. 2014. “Arbitrage-Free SVI Volatility Surfaces.” Quantitative Finance 14
(1): 59–71. https://doi.org/10.1080/14697688.2013.819986.
Heynen R. 1994. “An Empirical Investigation of Observed Smile Patterns.” Review of Futures
Markets13:317–317.
Kamal M., and Gatheral J. 2010. “Implied Volatility Surface.” In Encyclopedia of Quantitative Finance,
edited by R. Cont, Chichester: John Wiley & Sons, Ltd.
Martini C., and Mingone A. 2022. “No Arbitrage SVI.” SIAM Journal on Financial Mathematics 13
(1): 227–261. https://doi.org/10.1137/20M1351060.
Rogers L. C. G., and Tehranchi M. R. 2010. “Can the Implied Volatility Surface Move by Parallel
Shifts?.” Finance and Stochastics 14 (2): 235–248. https://doi.org/10.1007/s00780-008-0081-9.
Schönbucher P. J. 1999. “A Market Model for Stochastic Implied Volatility.” Philosophical Transactions of the Royal Society of London. Series A: Mathematical, Physical and Engineering
Sciences357 (1758): 2071–2092. https://doi.org/10.1098/rsta.1999.0418.
Schweizer M., and Wissel J. 2008. “Arbitrage-Free Market Models for Option Prices: The MultiStrike Case.” Finance and Stochastics 12 (4): 469–505. https://doi.org/10.1007/s00780-0080068-6.
Wissel J. S. 2008. “Arbitrage-Free Market Models for Liquid Options.” PhD diss., ETH Zurich.
Zhang W, Li L., and Zhang G. 2023. “A Two-Step Framework for Arbitrage-Free Prediction of the
Implied Volatility Surface.” Quantitative Finance 23 (1): 21–34. https://doi.org/10.1080/14697688.
2022.2135454.

## Tables

### Table 1

*Caption:* Table 1. Variance explained by the ﬁrst ﬁve eigenvectors of the covariance and the correlation operator

|  | PC1 |  | PC2 | PC3 | PC4 | PC5 |
| --- | --- | --- | --- | --- | --- | --- |
| Variance explained | 68.88% |  | 12.17% | 5.67% | 2.86% | 1.41% |
| (covariance) |  |  |  |  |  |  |
| Cumulative variance explained | 68.88% |  | 82.05% | 87.72% | 90.59% | 92.00% |
| (covariance) |  |  |  |  |  |  |
| Cumulative variance explained | 61.39% |  | 76.67% | 81.88% | 85.18% | 86.96% |
| (correlation) |  |  |  |  |  |  |
| • |  |  |  |  |  |  |
|  | The first principal component can be interpreted as the average level of implied volatil- |  |  |  |  |  |
| ities. A positive | shock along this mode would result |  |  | in a global | shift | in implied |
| volatility. |  |  |  |  |  |  |
| • |  |  |  |  |  |  |
|  | The second principal component corresponds to the skew. Shocks along this direction |  |  |  |  |  |
|  | result in opposite movements in out-of-the-money call and put implied volatilities. |  |  |  |  |  |
| • |  |  |  |  |  |  |
|  | The third principal component reflects the term structure of implied volatilities. |  |  |  |  |  |
| • |  |  |  |  |  |  |
|  | The fourth principal component can be interpreted as curvature. A positive shock along |  |  |  |  |  |
|  | this mode would have an opposite effect on the implied volatilities close to the money |  |  |  |  |  |
|  | and on the far out-of-the-money and in-the-money implied vols. |  |  |  |  |  |
|  | Projections of Yt(m, τ ) − ˜Yt(m, τ ) onto the first |  |  | four principal | components Xi | (i = |
|  |  |  |  |  |  | t, |
|  | 1, . . . , 4) (defined by Equation (7) ) are shown in Figure 5. All processes exhibit high pos- |  |  |  |  |  |
|  | itive autocorrelation and mean-reverting behaviour with a period of mean reversion of |  |  |  |  |  |
|  | several months. The ACF and PACF of X1 |  |  | are shown in Figure 6. As shown in Figure 6, |  |  |
|  |  | t |  |  |  |  |
|  | the autocorrelation functions decay exponentially, suggesting that they can be modeled as |  |  |  |  |  |
|  | Ornstein-Uhlenbeck/AR(1) processes, as already observed by Cont and da Fonseca (2002). |  |  |  |  |  |

Raw CSV: `assets/table_001.csv`

### Table 2

*Caption:* Table 1. Variance explained by the ﬁrst ﬁve eigenvectors of the covariance and the correlation operator

| 100 | R. CONT AND M. VULETIĆ |
| --- | --- |
| Figure 3. Eigenvalues of the correlation matrix of the daily changes in the log SPX implied volatility |  |
| surface and the Marčenko-Pastur threshold λ+ (in red). |  |

Raw CSV: `assets/table_002.csv`

### Table 3

*Caption:* Table 2. Long-term and 2-year rolling daily correlation between the log-increments of SPX and the

| Correlation between Rt and | (cid:8)X1 |  |  | (cid:8)X2 | (cid:8)X3 | (cid:8)X4 |
| --- | --- | --- | --- | --- | --- | --- |
|  | t |  |  | t | t | t |
| Long-term | −38.21% |  |  | −25.64% | 26.42% | −26.39% |
| Rolling: mean | −48.83% |  |  | −37.75% | 31.60% | −32.63% |
| relationship between the VIX and different variables of interest by considering the histor- |  |  |  |  |  |  |
| ical closing VIX prices available on the CBOE website. Figure 7 displays the correlations |  |  |  |  |  |  |
| between the log returns of VIX, one-month at-the-money SPX implied volatility, SPX and |  |  |  |  |  |  |
| the increments of the level process X1 |  |  |  |  |  |  |
|  |  | t over a rolling 2-year window. We note a high pos- |  |  |  |  |
|  | itive correlation between the level movements and the log-returns of VIX and ATM vol. |  |  |  |  |  |
| Similarly, the returns of | the underlying are negatively correlated with the increments of |  |  |  |  |  |
| the level process (Table 2), |  | log-returns of VIX and with the log-returns of the ATM vol. |  |  |  |  |
|  | Correlations increasing in magnitude from 2006 onwards. |  |  |  |  |  |
|  | The one-month realized volatility ˆσt |  | is estimated as |  |  |  |
|  |  | (cid:11)(cid:12)(cid:12)(cid:13) |  | 20(cid:3) |  |  |
|  |  |  | 21 |  |  |  |
|  | σt = |  |  | R2 |  | (9) |
|  |  |  |  | t−i(cid:8)t. |  |  |
|  |  |  | 252 |  |  |  |
|  |  |  |  | i=0 |  |  |
|  | Figure 8 shows that the realized volatility is usually below the implied volatility. The aver- |  |  |  |  |  |
|  | age ratio of realized volatility to ATM volatility is 0.59, with a standard deviation of 0.209 |  |  |  |  |  |
| (Figure 8). |  |  |  |  |  |  |
| 3. Static Arbitrage Constraints |  |  |  |  |  |  |
| We now consider shape constraints on the implied volatility surfaces arising from static |  |  |  |  |  |  |
| arbitrage inequalities (Davis and Hobson 2007). We are interested in a realistic setting |  |  |  |  |  |  |

Raw CSV: `assets/table_003.csv`

### Table 4

*Caption:* Table 2. Long-term and 2-year rolling daily correlation between the log-increments of SPX and the

| 102 | R. CONT AND M. VULETIĆ |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Figure 5. Principal component processes X1 |  | , X2 | , X3 | , X4 | . |

Raw CSV: `assets/table_004.csv`

### Table 5

*Caption:* Table 3. 90.5% of dates display no calendar arbitrage, 97.3% display no call spread arbitrage and 84.9% no butterfly arbitrage. Overall 80.2% of the observations correspond to

<table>
  <tr>
    <th>Figure 9. Butterﬂy penalty matrices (P3) arising from noise and parallel shifts. (a) Mean eﬀect of adding</th>
  </tr>
  <tr>
    <td>noise (b) Sample parallel shift eﬀect.</td>
  </tr>
  <tr>
    <td>displayed in Figure 9. We note that violations occur only for far from the money, long-dated</td>
  </tr>
  <tr>
    <td>options.</td>
  </tr>
  <tr>
    <td>Parallel shifts Rogers and Tehranchi (2010) showed that moving implied volatility sur-</td>
  </tr>
  <tr>
    <td>faces by parallel shifts will eventually result in configurations with static arbitrage. We</td>
  </tr>
  <tr>
    <td>explore this phenomenon quantitatively by adding a parallel shift to an initial arbitrage-</td>
  </tr>
  <tr>
    <td>free implied volatility surface (SPX implied volatility surface on 31/12/2021) and testing</td>
  </tr>
  <tr>
    <td>for static arbitrage. The absolute value of the largest negative shift is taken to be smaller</td>
  </tr>
  <tr>
    <td>than the smallest implied volatility value, guaranteeing non-negativity. The effect of par-</td>
  </tr>
  <tr>
    <td>allel shifts on the arbitrage penalty are displayed in Figure 10: arbitrage constraints are</td>
  </tr>
  <tr>
    <td>violated for large enough positive shifts, and the arbitrage penalty grows linearly there-</td>
  </tr>
  <tr>
    <td>after. For such large shifts, the constraint which is violated is convexity. A sample butterfly</td>
  </tr>
  <tr>
    <td>arbitrage penalty matrix P3 is displayed in Figure 9(b). These results give a quantitative</td>
  </tr>
  <tr>
    <td>perspective on the results of Rogers and Tehranchi (2010).</td>
  </tr>
  <tr>
    <td>3.3. Arbitrage Penalty in SPX Implied Volatility Data</td>
  </tr>
  <tr>
    <td>Data sources on implied volatility, such as OptionMetrics, are often interpolated from</td>
  </tr>
  <tr>
    <td>actual market quotes, a procedure which may itself introduce static arbitrage. This has</td>
  </tr>
  <tr>
    <td>been previously noted by several studies, see e.g. Cohen, Reisinger, and Wang (2023). We</td>
  </tr>
  <tr>
    <td>study this phenomenon using daily SPX implied volatility surfaces from 2000 to end 2021.</td>
  </tr>
  <tr>
    <td>We observe non-zero arbitrage penalties, with a decomposition displayed in Figure 11 and</td>
  </tr>
  <tr>
    <td>Table 3. 90.5% of dates display no calendar arbitrage, 97.3% display no call spread arbi-</td>
  </tr>
  <tr>
    <td>trage and 84.9% no butterfly arbitrage. Overall 80.2% of the observations correspond to</td>
  </tr>
  <tr>
    <td>abitrage-free surfaces.</td>
  </tr>
  <tr>
    <td>We observe a number of spikes in arbitrage penalties. The two largest spikes happen on</td>
  </tr>
  <tr>
    <td>29/09/2008 (during the 2008 financial crisis) and on 13/03/2020 (the start of the Covid-19</td>
  </tr>
  <tr>
    <td>pandemic). Figure 11 shows that the majority of arbitrage violations happen during the</td>
  </tr>
  <tr>
    <td>2008 financial crisis and during the start of the Covid-19 pandemic. For comparisons, the</td>
  </tr>
</table>

Raw CSV: `assets/table_005.csv`

### Table 6

*Caption:* Table 3. Quantiles of arbitrage penalties for SPX options.

| Penalty | Median | 90th quantile | 95th quantile | 99th quantile |
| --- | --- | --- | --- | --- |
| Total (cid:11) | 0 | 0.075 | 0.13 | 0.5 |
| Calendar spread p1 | 0 | 0 | 0.002 | 0.038 |
| Call spread p2 | 0 | 0 | 0 | 0.009 |
| Butterﬂy spread p3 | 0 | 0.01 | 0.06 | 0.458 |
| Figure 12. Calendar spread arbitrage (P1) for SPX options. (a) 29.09.2008 (b) 13.03.2020. |  |  |  |  |

Raw CSV: `assets/table_006.csv`

### Table 7

*Caption:* Table 5. QuantilesofarbitragepenaltyunderPN

| β |  |  | 0 |  | 102 103 |  | 104 | 105 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 90th quantile |  |  | 0.044 |  | 0.001 0 |  | 0 | 0 |
| 95th quantile |  |  | 0.09 |  | 0.004 0.0001 |  | 0 | 0 |
| 99th quantile |  |  | 0.206 |  | 0.014 0.001 |  | 0.0004 | 0 |
| Figure 16. Relative entropy H(PN |  |  |  | β \|PN | ) in (26)–(27) as a function of β. |  |  |  |
|  |  |  |  | 0 |  |  |  |  |
| estimated as: |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  | (cid:3) |  |  |
|  |  | −1 |  |  |  |  |  |  |
|  | F | ϕ | (q) = ϕ(ω(k)), |  | k = min{j ∈ {1, . . . , N} : |  | w(ω(i)) ≥ q}. | (29) |

Raw CSV: `assets/table_007.csv`

### Table 8

*Caption:* Table 6. Estimated OU parameters for SPX implied volatility factors.

|  | λ |  | α | γ |
| --- | --- | --- | --- | --- |
| X1 | 2.018 |  | –0.422 | 4.414 |
| t |  |  |  |  |
| X2 | 0.986 |  | –0.312 | 1.993 |
| t |  |  |  |  |
| X3 | 1.258 |  | 0.097 | 1.295 |
| t |  |  |  |  |
| X4 | 1.497 |  | –0.021 | 0.824 |
| t |  |  |  |  |
| Figure 18. Relative entropy H(PN | β \|PN |  | ) as a function of β: SPX factor model (30)–(31). |  |
|  |  | 0 |  |  |
| in Figure 4 for f1, f2, f3, f4. We estimateα i, λi, γi, i = 1, . . . , 4 via a Generalized Method of |  |  |  |  |
|  | Moments (GMM), using the first two moments and the autocorrelation function at var- |  |  |  |
|  | ious lags as moment conditions. Estimates are shown in Table 6. We setν = 1 |  |  | and the |

Raw CSV: `assets/table_008.csv`

### Table 9

*Caption:* Table 7. Arbitrage presence in scenarios from the SPX factor model (30)–(31).

|  |  | Total |  | Calendar |  | Call |  | Butterfuly |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Paths |  | 62.761% |  | 21.245% |  | 36.548% |  | 36.548% |
| Surfaces |  | 16.055% |  | 4.004% |  | 9.117% |  | 7.073% |
|  | Table 8. Quantiles of arbitrage penalty under PN |  |  |  | β for SPX factor model (30)–(31). |  |  |  |
| β | 0 |  | 102 | 104 | 106 |  | 1010 | 1015 |
| 90th quantile | 0.20 |  | 5 · 10−5 | 5 · 10−10 | 2 · 10−13 |  | 0 | 0 |
| 95th quantile | 0.77 |  | 0.002 | 2 · 10−7 | 3 · 10−9 |  | 4 · 10−15 | 0 |
| 99th quantile | 4.49 |  | 0.01 | 3 · 10−7 | 2 · 10−9 |  | 1 · 10−11 | 4 · 10−16 |
|  | Figure 19. Simulation of | a | 10-year | scenario for VIX (red) |  | and SPX (blue) using the |  | SPX factor |
| model (31)–(33). |  |  |  |  |  |  |  |  |
|  | Simulating the volatility index We simulate the VIX dynamics associated with the SPX |  |  |  |  |  |  |  |

Raw CSV: `assets/table_009.csv`

### Table 10

*Caption:* Table 8. Quantiles of arbitrage penalty under PN

| β | 0 |  | 102 | 104 | 106 | 1010 | 1015 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 90th quantile | 0.20 |  | 5 · 10−5 | 5 · 10−10 | 2 · 10−13 | 0 | 0 |
| 95th quantile | 0.77 |  | 0.002 | 2 · 10−7 | 3 · 10−9 | 4 · 10−15 | 0 |
| 99th quantile | 4.49 |  | 0.01 | 3 · 10−7 | 2 · 10−9 | 1 · 10−11 | 4 · 10−16 |
|  | Figure 19. Simulation of | a | 10-year | scenario for VIX (red) |  | and SPX (blue) using the | SPX factor |
| model (31)–(33). |  |  |  |  |  |  |  |
|  | Simulating the volatility index We simulate the VIX dynamics associated with the SPX |  |  |  |  |  |  |
|  | four-factor model (30)–(33) using the methodology from CBOE (2022). We fix the mon- |  |  |  |  |  |  |
|  | eyness grid by taking 100 equispaced values between 0.5 and 1.5. We simulate 10-year VIX |  |  |  |  |  |  |
|  | and SPX paths using a frequency of one day(cid:8)t = 1 |  |  |  |  |  |  |
|  |  |  |  |  | 252 with the average SPX implied volatil- |  |  |
|  | ity surface, and the SPX price on the 31st Dec 2021 as the starting point. The remaining |  |  |  |  |  |  |
|  | hyperparameters are as in the previous simulations. Figure 19 displays simulated sample |  |  |  |  |  |  |

Raw CSV: `assets/table_010.csv`

### Table 11

*Caption:* Table 8. Quantiles of arbitrage penalty under PN

| 118 | R. CONT AND M. VULETIĆ |  |  |  |
| --- | --- | --- | --- | --- |
| Table 7. Arbitrage presence in scenarios from the SPX factor model (30)–(31). |  |  |  |  |
|  | Total | Calendar | Call | Butterfuly |
| Paths | 62.761% | 21.245% | 36.548% | 36.548% |
| Surfaces | 16.055% | 4.004% | 9.117% | 7.073% |

Raw CSV: `assets/table_011.csv`

### Table 12

*Caption:* Table 9. Pearsoncorrelationbetweensimulatedvaluesoflog-returnsofSPX,returnsofthelevelprocess,

|  | (cid:8) log St | (cid:8)X1 | (cid:8) log σ ATM | (cid:8) log σ VIX |
| --- | --- | --- | --- | --- |
|  |  | t |  |  |
| (cid:8) log St | 1.00 | –0.45 | –0.31 | –0.30 |
| (cid:8)X1 | –0.45 | 1.00 | 0.96 | 0.94 |
| t |  |  |  |  |
| (cid:8) log σ ATM | –0.31 | 0.96 | 1.00 | 0.99 |
| (cid:8) log σ VIX | –0.30 | 0.94 | 0.99 | 1.00 |
|  | level process, the log-returns of ATM vol, and the log-returns of VIX. There is a high pos- |  |  |  |
|  | itive correlation between the log increments of the ATM vol, VIX, and the increments of |  |  |  |
|  | the level process. This is consistent with the historical correlations displayed in Figure 7. |  |  |  |
|  | In Figure 21 we compare the historical (2012–2021) and the simulated joint distribution |  |  |  |
|  | of the log-returns of SPX and of VIX. The means of the two distributions align, and the |  |  |  |
|  | corresponding marginal distributions of |  | the simulated and historical values are close to |  |
|  | each other. However, we note that as the historical correlation between the log-returns of |  |  |  |
|  | SPX and of VIX is non-constant (Figure 7), the joint distribution changes through time as |  |  |  |
|  | well. The correlation between the log-returns SPX and VIX being lower in the simulations |  |  |  |
|  | than in the 2012–2021 historical data (Figure 21) can be contributed to the correlation |  |  |  |
|  | ρ1 used in simulations being lower than the average historical daily correlation of Rt and |  |  |  |
| (cid:8)X1 | for the time period 2012–2021 (Figure 7). Overall, we conclude that the four-factor |  |  |  |
| t |  |  |  |  |
|  | model (31)–(33) is able to generate realistic scenarios for VIX, consistent with the historical |  |  |  |
| observations. |  |  |  |  |
| 6. Conclusion |  |  |  |  |
|  | We introduced a simple and computationally tractable method for simulating arbitrage- |  |  |  |
|  | free implied volatility surfaces. Our approach offers flexibility with respect to the under- |  |  |  |
| lying model | for implied volatility dynamics, whilst preserving the co-movements across |  |  |  |
| strikes and maturities. |  |  |  |  |
|  | Our approach enables to combine a data-driven multifactor model with a Weighted |  |  |  |
|  | Monte Carlo method in order to conciliate static arbitrage constraints with a statistically |  |  |  |
|  | realistic representation of co-movements of implied volatilities. |  |  |  |

Raw CSV: `assets/table_012.csv`

## Figures

![Figure 1: Figure 1. SPX implied volatility surface on 01/11/2021.](assets/fig_001.jpeg)

![Figure 2: Figure 2. Average SPX implied volatility surface (2000–2021).](assets/fig_002.jpeg)

![Figure 3: Figure 3. Eigenvalues of the correlation matrix of the daily changes in the log SPX implied volatility](assets/fig_003.png)

![Figure 4: Figure 4. The ﬁrst four principal components of the daily changes in log SPX implied volatility surface.](assets/fig_004.png)

![Figure 5: Figure 5. Principal component processes X1](assets/fig_005.png)

![Figure 6: Figure 6. Autocorrelation and partial autocorrelation of the log implied volatility projection on the ﬁrst](assets/fig_006.png)

![Figure 7: Figure 7. Correlation over a 2-year window between daily changes in the level process X1](assets/fig_007.jpeg)

![Figure 8: Figure 8. Above: SPX realized volatility (blue), one-month ATM volatility (orange) and VIX (green).](assets/fig_008.png)

![Figure 9: Figure 9. Butterﬂy penalty matrices (P3) arising from noise and parallel shifts. (a) Mean eﬀect of adding](assets/fig_009.jpeg)

![Figure 10: Figure 10. Arbitrage violations induced by parallel shifts on SPX implied volatility surface (31/12/2021).](assets/fig_010.png)

![Figure 11: Figure 10. Arbitrage violations induced by parallel shifts on SPX implied volatility surface (31/12/2021).](assets/fig_011.png)

![Figure 12: Figure 12. Calendar spread arbitrage (P1) for SPX options. (a) 29.09.2008 (b) 13.03.2020.](assets/fig_012.jpeg)

![Figure 13: Figure 12. Calendar spread arbitrage (P1) for SPX options. (a) 29.09.2008 (b) 13.03.2020.](assets/fig_013.jpeg)

![Figure 14: Figure 14. Butterﬂy spread arbitrage (P3) for SPX options. (a) 29.09.2008 (b) 13.03.2020.](assets/fig_014.jpeg)

![Figure 15: Figure 15. Basis functions f1, f2, f3 corresponding to level, skew and curvature used to simulate scenarios from the factor model (26)–(27). (a) f1(m, τ) (b) f2(m, τ) (c) f3(m, τ).](assets/fig_015.jpeg)

![Figure 16: Figure 16. Relative entropy H(PN](assets/fig_016.jpeg)

![Figure 17: Figure 17. Histogram of Nw(β) with β = 102 in (26)–(27).](assets/fig_017.jpeg)

![Figure 18: Figure 18. Relative entropy H(PN](assets/fig_018.png)

![Figure 19: Figure 19. Simulation of a 10-year scenario for VIX (red) and SPX (blue) using the SPX factor](assets/fig_019.png)

![Figure 20: Figure 20. Simulation of VIX (red), ATM volatility (green), and the 30-day realized volatility (purple)](assets/fig_020.jpeg)

![Figure 21: Figure 20. Simulation of VIX (red), ATM volatility (green), and the 30-day realized volatility (purple)](assets/fig_021.jpeg)

## Extraction Notes

- discarded 17 tiny-placement embedded figure(s)
- discarded 1 dense-page embedded figure candidate(s)
- camelot lattice produced no usable tables; using stream output
- camelot:stream table quality filter dropped 4 low-quality table(s)
