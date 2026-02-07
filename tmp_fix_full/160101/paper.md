---
paper_id: "160101"
source_file: "160101.pdf"
title: "C:TRYRFS4326.DVI"
authors: ["Dr. Mirko Janc (Tech Typeset) 427 1999 Feb 15 15:33:29"]
year: 1973
doi: null
page_count: 43
extracted_at: "2026-02-07T06:10:45.401110+00:00"
status: "success"
---

# C:TRYRFS4326.DVI

## Metadata

- **Source File:** `160101.pdf`
- **Authors:** Dr. Mirko Janc (Tech Typeset) 427 1999 Feb 15 15:33:29
- **Year:** 1973
- **DOI:** Unknown

## Abstract

Not found.

## Main Text

### Stock Return Characteristics, Skew Laws,
### and the Differential Pricing of Individual
### Equity Options
Gurdip Bakshi
University of Maryland
Nikunj Kapadia
University of Massachusetts-Amherst
Dilip Madan
University of Maryland
This article provides several new insights into the economic sources of skewness. First,
we document the differential pricing of individual equity options versus the market index
and relate it to variations in return skewness. Second, we show how risk aversion introduces skewness in the risk-neutral density. Third, we derive laws that decompose individual return skewness into a systematic component and an idiosyncratic component.
Empirical analysis of OEX options and 30 stocks demonstrates that individual riskneutral distributions differ from that of the market index by being far less negatively
skewed. This article explains the presence and evolution of risk-neutral skewness over
time and in the cross section of individual stocks.
Skewness continues to occupy a prominent role in equity markets. In the
traditional asset pricing literature, stocks with negative coskewness command a higher equilibrium risk compensation [see Rubinstein (1973), and
the empirical applications in Kraus and Litzenberger (1976) and Harvey and
Siddique (2000)]. Realizing the inherent importance of skewness, Merton
(1976), Rubinstein (1994), Bakshi, Cao, and Chen (1997), Ait-Sahalia and
Lo (1998), Madan, Carr, and Chang (1998), Pan (1999), Bates (2000), and
We acknowledge discussions on this topic with Yacine Ait-Sahalia, Torben Anderson, Meghana Ayyagari,
Warren Bailey, Ravi Bansal, David Bates, Nick Bollen, Peter Carr, Charles Cao, Henry Cao, Zhiwu Chen,
George Chacko, Amy Chan, Dave Chapman, Alex David, Darrell Dufﬁe, Rob Engle, Rene Garcia, Eric
Ghysels, John Guo, Levent Guntay, Hua He, Mike Hemler, Harrison Hong, Ming Huang, Jon Ingersoll, Bob
Jarrow, Nengjiu Ju, Hossein Kazemi, Inanc Kirgiz, Haitao Li, Nour Meddahi, Maureen O’Hara, Jun Pan,
Gurupdesh Pande, Nagpurnanand Prabhala, Chandrasekhar Reddy Gokhul, Eric Renault, Lemma Senbet, Paul
Schultz, Ken Singleton, Tie Su, Michael Stutzer, Bhaskar Swaminathan, George Tauchen, Alex Triantis, Haluk
Unal, Bob Whaley, and Frank Zhang. We also thank workshop participants at CIRANO, Cornell, Maryland,
Massachusetts-Amherst, Notre Dame, Stanford, and Yale. Participants at EFA (London), WFA 2000 (Sun
Valley), and the Duke conference on risk-neutral and objective probability measures provided many useful
suggestions. A special thanks goes to Cam Harvey (the editor) and an anonymous referee, whose suggestions
have helped us improve this article substantially. Kristaps Licis provided expert research assistance. Any errors
are our own. An earlier version of this paper was circulated under the title “Why are Implied Volatility Curves
Embedded in Individual Equity Options So Flat?” Address correspondence to Gurdip Bakshi, Department of
Finance, Robert H. Smith School of Business, University of Maryland, College Park, MD 20742, or e-mail:
gbakshi@rhsmith.umd.edu.
The Review of Financial Studies Spring 2003 Vol. 16, No. 1, pp. 101–143
© 2003 The Society for Financial Studies

Dufﬁe, Pan, and Singleton (2000) have devised option models to characterize asymmetries in the underlying risk-neutral pricing distributions. Despite
these advances in empirical and theoretical modeling of skewness, extant
work has not yet formalized restrictions on the physical return density and
the pricing kernel process that could shift the risk-neutral distributions to the
left. What are the sources of risk-neutral skewness? What are its implications
for individual equity options? Our present goal is to ﬁll speciﬁc gaps from
theoretical and empirical standpoints. First, our innovations provide a theoretical characterization that links risk-neutral skews to risk aversion, and to
the higher-order moments of the physical distribution. Second, we develop a
relationship between individual skews, market index skews, and idiosyncratic
skews, which we call the skew laws. Third, we establish the differential pricing of individual equity options versus the market index. Critical to this thrust
is the link, to ﬁrst order, between skew laws and the differential pricing of
individual equity options that makes our empirical study tractable.
To make it easy to draw comparisons across option strikes and in the cross
section of equity options, the structure of option prices—how option prices
differ across strikes—is often represented through the slope of the implied
volatility curve [Rubinstein (1985, 1994)]. Given their equivalence, we will
use the slope of the implied volatility curve (or, the smile) and the structure of
option prices to exemplify the same primitive object throughout. Granted, a
one-to-one correspondence also exists between the smile and the risk-neutral
density, modeling the smile as a stochastic process is now a central feature
of some option models. While it is widely acknowledged that the smile is
somehow due to the existence of negatively skewed and heavy-tailed riskneutral return distributions, a formal test of this simple idea has proven hard
to implement. For example, is it skewness or kurtosis that is of ﬁrst-order
importance in explaining the observed variation in the structure of option
prices? When the return distribution is skewed to the left, will a higher level
of kurtosis induce a ﬂatter smile?
The hurdles in quantifying the basic link across a wide spectrum of options
stem from three sources. First, to infer the smile from the initial higher
moments requires the identiﬁcation of the underlying risk-neutral return density, and there is no natural way to reconstruct the density from just its higher
moments. Second, even when option models are well-enough speciﬁed across
the strike price range, it is not clear that any derived relation between option
prices and risk-neutral moments is a generic property, as opposed to being a
reﬂection of the particular modeling choice (i.e., parameterization can force
an artiﬁcial interdependence between skewness and kurtosis). Thus it appears
important that skews be recovered in a model-free fashion. Third, most stock
options are American and therefore their risk-neutral densities cannot be so
easily characterized using existing methods. Consequently much research in
the estimation of risk-neutral distributions, and its moments, has concentrated
102

on index, as opposed to individual equity, options. From a general asset pricing perspective, it is unsettling that we do not yet understand the properties
of individual equity risk-neutral return distributions or the structure of their
option prices.
Our study makes several theoretical contributions. One, we build the connection, in a model-free manner, between the differential pricing of individual stock options and the moments of the risk-neutral distribution. Here
we rely on the basic result from Bakshi and Madan (2000): any payoff can
be spanned and priced using an explicit positioning across option strikes.
Speciﬁcally we show that the cubic contract can quantify return asymmetry
by a speciﬁc position that simultaneously involves a long position in out of
the money calls and a short position in out of the money puts. When the
risk-neutral distribution is left-skewed, the combined cost of the positioning
in puts is larger than that of the combined positioning in calls. We refer to
the cost of reproducing the risk-neutral skewness and kurtosis as the price of
skewness and kurtosis even though the respective payoffs are not actually discounted.1 The contingent claims theory that we use here is applicable to both
European and American options, and the derived measures of tail asymmetry
and tail size are readily comparable across equities and over time.
Next, we develop the relation between the individual and index risk-neutral
return distributions, and analyze what may cause a wedge between the skewness of these distributions. We posit a market model in which individual
stock return can be decomposed into a systematic component and an idiosyncratic component, and derive the relation between the individual, index and
idiosyncratic skews. Provided the idiosyncratic risk component is symmetric
(or positively skewed) and the index distribution is negatively skewed, we can
restrict the risk-neutral individual skew to be less negative than the market.
In one particular example we show that the leverage argument for skews has
the implication that some individual equity returns are risk-neutrally more
left-skewed than the index, which is inconsistent with the data.
Our characterizations impart the crucial insight that negatively skewed
risk-neutral index distributions are possible even when the physical return
distribution is symmetric. Curiously this outcome is achieved when the return
process is in the family of fat-tailed physical distributions and the representative agent is risk averse. This result holds for a wide class of utility functions
and thereby provides the foundation for negative risk-neutral skewness.
We use our skewness paradigms to test the following hypotheses: (1) Index
volatility smiles are more negatively sloped than individual smiles. (2) In the
1 According to standard economic theory, the physical return density assesses the likelihood of different return
outcomes, while the corresponding risk-neutral density is concerned with the market price of contracts paying
a dollar contingent on various return outcomes. It is generally recognized that the physical and the risk-neutral
densities can be substantially different: large movements commanding a higher price and a lower probability,
while the reverse is true for smaller moves. Due to risk aversion, we typically observe higher prices for
downward market movements versus comparable upward movements.
103

stock cross section, or in the time series, the more negatively skewed the riskneutral return distribution, the steeper the volatility smiles. (3) Individual riskneutral distributions are less skewed to the left than the index distributions.
Our empirical study is based on nearly 350,000 option quotes written on
the S&P 100 index (hereafter OEX) and its 30 largest individual equity components over the period January 1991 through December 1995. Our principal
conclusions are as follows. First, the slopes of the individual equity smiles
are persistently negative, but are much less negative than the index. The documented differences in the slope of index and individual smiles produces a
substantial difference in the relative price of options: for the OEX (a representative stock), the implied volatility of a deep out of the money (hereafter
OTM) put is about 22% (29%), as compared to at the money (hereafter ATM)
implied of 14% (26%). Therefore we make the important observation that the
pricing structure of individual equity options is ﬂatter compared with that of
the market index. Our primary explanation for this phenomenon is based on
risk aversion.
Second, we conclude that variations in the risk-neutral skew are instrumental in explaining the differential pricing of individual equity options. We
ﬁnd that the more negatively skewed the return distribution, the steeper is
its volatility smile. Yet when risk-neutral distributions evolve to be more
fat-tailed, the smile gets less downward sloping. Speciﬁcally, a higher riskneutral kurtosis ﬂattens the smile in the presence of left-tails. The crosssectional regressions conﬁrm that, on average, less negatively skewed stocks
have ﬂatter smiles.
Third, our inquiry consolidates a number of core properties mirrored by
all individual risk-neutral (pricing) distributions:
• Individual stocks are mildly left-skewed (or even positively skewed),
while index return distributions are heavily left-skewed. By way of contrast, there is no consistent pattern for the price of the fourth moment
in the cross section.
• Although individual skews are negative much of the time, their magnitudes are seldom more negative relative to the index. Our sample
suggests that the index skews are never positive, even periodically.
Finally, we empirically relate the risk-neutral index skews to the higher
moments of the physical distribution. Our results indicate that the substantial
differences in the magnitudes of risk-neutral and physical skews are primarily a consequence of risk aversion and long-tailed physical distributions. A
variety of extended diagnostics support our main empirical ﬁndings.
This article is divided into several parts. Section 1 is devoted to formulating the key elements of the problem. In Section 2, we relate the structure of
option prices to higher-order risk-neutral return moments. Section 3 reviews
the equity options data. The differential pricing of individual equity options
104

versus the market index is demonstrated in Section 4. We empirically examine the role of skews. Conclusions are offered in Section 5. All proofs are
collected in the appendix.
1. Understanding and Recovering Risk-Neutral Skews
This section accomplishes three tasks. At the outset, we propose a methodology to span and price skewness and kurtosis. This step is rendered feasible
using only OTM calls and puts and without imposing any structure on the
underlying forcing process. Next, we establish when risk aversion causes the
aggregate index to have negative skews under the risk-neutral measure. We
then decompose the price of individual return skewness into market-induced
skewness and idiosyncratic skewness. Each conceptualization is critical for
the later empirical exercises.
1.1 Generic spanning and pricing characterizations
in Bakshi and Madan (2000)
Since our intent is to frugally represent the risk-neutral distribution (or some
feature thereof) in terms of traded option prices, it is only convenient to adopt
the setting outlined in Bakshi and Madan (2000). That is, to ﬁx notation,
denote the time t price of the stock n by Snt (for n = 1   N) and the
market index by Smt. Without any loss of generality, let the interest rate
be a constant r, and St > 0 with probability 1 for all t (suppressing the
subscript n).
To ease equation presentation, write the t +  period price of the stock,
St+, as S. Let the risk-neutral (pricing) density qtS, or simply qS,
embody all remaining uncertainty about S. The physical density, pS, and
the associated Radon–Nikodym derivative that delivers qS, for a given pricing kernel, will be formalized in Section 1.3. For any claim payoff HS that
 
0  HS  qSdS <
is integrable with respect to risk-neutral density (i.e.,
), the symbol ∗
t will represent the expectation operator under riskneutral density. That is, in what follows,
 
∗
t HS =
0 HSqSdS
(1)
With this understanding we can express the price of the European call and put
written on the stock with strike price K and expiring in  periods from time
 
 
0 e−rS −K+qSdS, and PtK =
0 e−rK −
t as CtK =
S+qSdS, where S −K+ ≡max0S −K.
As articulated in Bakshi and Madan (2000), any payoff function with
bounded expectation can be spanned by a continuum of OTM European calls
and puts. In particular, a special case of their Theorem 1 is that the entire
105

collection of twice-continuously differentiable payoff functions, HS ∈2,
can be spanned algebraically [see also Carr and Madan (2001)], as in
 
HS = HS+S −SHSS+
S HSSKS −K+dK
 S
0 HSSKK −S+dK
+
(2)
where HSS (HSSK) represents the ﬁrst-order (second-order) derivative of
the payoff with respect to S evaluated at some S (the strike price). Intuitively the position in options enables one to buy the curvature of the payoff
function.
Applying risk-neutral valuation to both sides of Equation (2), we have the
arbitrage-free price of the hypothetical claim as
t e−rHS = HS−S HSSe−r +HSSSt
∗
 
+
S HSSKCtKdK
 S
+
0 HSSKPtKdK
(3)
which merely formalizes how HS can be synthesized from (i) a zerocoupon bond with positioning: HS −S HSS, (ii) the stock with positioning: HSS, and (iii) a linear combination of calls and puts (indexed by
K) with positioning: HSSK. By observing the relevant market prices and
appealing to Equation (3), we can statically construct the intrinsic values of
most contingent claims.
1.2 Mimicking risk-neutral skewness and kurtosis
To streamline the discussion of stock return characteristics and the structure
of option prices, let the -period return be given by the log price relative:
Rt ≡lnSt+−lnSt. Deﬁne the volatility contract, the cubic contract, and the quartic contracts to have the payoffs

Rt2
volatility contract

Rt3
HS =
cubic contract
(4)

Rt4
quartic contract.

e−r Rt2

e−r Rt3
Let V t ≡∗
, Wt ≡∗
, and Xt ≡

e−r Rt4
t
t
∗
represent the fair value of the respective payoff. The folt
lowing theorem is a consequence of Equations (2) and (3).
106

Theorem 1.
Under all martingale pricing measures, the following contract
prices can be recovered from the market prices of OTM European calls and
puts:
1. The -period risk-neutral return skewness, SKEWt, is given by
t Rt3
∗
t Rt−∗
SKEWt ≡
t Rt2 3/2
∗
t Rt−∗
= erWt−3 terV t+2 t3
(5)
erV t− t23/2
2. The risk-neutral kurtosis, denoted KURTt, is

t Rt4
KURTt ≡∗
Rt−∗
t

t Rt22
∗
t Rt−∗
= erXt−4 terWt+6er t2 V t−3 t4
(6)

erV t− t22
with t displayed in Equation (39) of the appendix. The price of the
volatility contract,

K
 
1−ln
2
St
V t =
CtKdK
K2
St

St
 St
1+ln
2
K
+
PtKdK
(7)
K2
0
and the price of the cubic and the quartic contracts,
K

K
2
 
−3
6 ln
ln
St
St
Wt =
CtKdK
K2
St

St
2
St
 St
+3
ln
6 ln
K
K
−
PtKdK
(8)
K2
0
2 −4
3

K

K
 
12
ln
ln
St
St
Xt =
CtKdK
K2
St

St

St
2 +4
3
 St
12
ln
ln
K
K
+
PtKdK
(9)
K2
0
can each be formulated through a portfolio of options indexed by their
strikes.
The theorem formalizes a mechanism to extract the volatility, the skewness,
and the kurtosis of the risk-neutral return density from a collection of OTM
calls and puts. Notably one must always pay to go long the volatility and the
107

quartic/kurtosis contracts. Speciﬁcally, to unwind the price of volatility, all
OTM calls and puts are to be weighted by the strike price-dependent amount:
2−2lnK/St
. In the quartic contract, the positioning is cubic in moneyness,
K2
however. Heuristically, a more pronounced fourth moment can only give rise
to heavy-tailed distributions, a feature that will bid up the prices of both deep
OTM and in the money (hereafter ITM) calls and puts. When ﬁtting implied
volatility curves, this effect sometimes surfaces as a parabola in the space of
moneyness and implied volatility. Therefore the weighting structure assigning
far higher weight to OTM [versus near the money (hereafter NTM)] options
does have intuitive justiﬁcation.
The cubic contract displayed in Equation (8) permits a play on the skew.
With return distributions that are left-shifted, all OTM put options will be
priced at a premium relative to OTM calls. In this environment, the cost of the
short position in the linear combination of OTM puts will generally exceed
the call option counterpart. Equation (5) thus blends qualitative as well as
quantitative dimensions of asymmetry. More exactly, when the cubic contract
is normalized by V t, it quantiﬁes asymmetry both across time and in the
stock cross section. As we shall see, the option portfolio [Equation (5)] is
instrumental in quantifying ﬂuctuations in the smile and in reconciling the
relative structure of individual option prices.
Although it is possible to parameterize skews via a speciﬁc jump model,
for reasons already discussed, the model-free determination of skews is desirable on theoretical and empirical grounds. In our context, moment discovery
can be contemplated as summing a coarsely available grid of OTM calls
and puts; it also generalizes to American options. The latter assertion can
be supported in two ways. First, OTM options have negligible early exercise premiums. Second, even when early exercise premiums are not modest
[i.e., OTM options in the neighborhood of at the money (hereafter ATM)],
the portfolio weighting in these options is small by construction. In the converse, larger weighting applies to deep OTM options but their market prices
are declining rapidly with strikes. In reality, a ﬁnite positioning in options
should effectively span the payoffs of interest. We address issues of accuracy
in our implementations.
Equation (5) may be useful to researchers interested in measuring risk
compensation for individual/index skews [see Harvey and Siddique (2000)].
Rnt− n3
Suppose an individual holds the claim
3/2 , with no idiosyn-
erVnt− nt2
cratic exposure. The market price of this exposure is precisely given by
Equation (5). For any admissible stochastic discount factor, , and covariance operator, covt  , the reward for bearing skewness risk, S, is then
t +t
 SKEWt +t
S −r = −covt

(10)
t
SKEWt
which is, in principle, computable once the stochastic discount factor has
been identiﬁed. The identiﬁcation of can be rather involved and requires the
108

joint estimation and formulation of the physical and risk-neutral processes.
For details on this procedure we refer the reader to Pan (1999), Chernov and
Ghysels (2000), and Harvey and Siddique (2000).
1.3 Sources of risk-neutral index skews
For our synthesis involving the relationship between risk-neutral and physical
densities, let pRm denote the physical density of the -period index return,
Rm. Similarly denote the joint physical density of the stock collection by
pR1   RNRm. Under certain conditions, we must have, by the Radon–
Nikodym theorem, the identities (see the appendix)
e− Rm ×pRm

qRm =

and
(11)
e− Rm ×pRmdRm
e− Rm ×pR1   RNRm

qR1   RNRm =

(12)
e− Rm ×pR1   RNRmdR1 ···dRN dRm
where e− Rm is the pricing kernel in power utility economies, with coefﬁcient
of relative risk aversion . Here the risk-neutral index density is obtained by
exponentially tilting the physical density. Note that the normalization factor in
the denominator of Equation (11) ensures qRm is a proper density function
that integrates to unity. We now prove the main result of this subsection.
Theorem 2.
Up to a ﬁrst-order of , the risk-neutral skewness of index
returns is analytically attached to its physical counterparts via

SKEWmt ≈SKEWmt−
KURTmt−3
STDmt
(13)
where STDt, SKEWt, and KURTt represent return standard
deviation, skewness, and kurtosis, under the physical probability measure,
respectively. Thus exponential tilting of the physical density will produce
negative skew in the risk-neutral index distribution, provided the physical
distribution is fat-tailed (with nonzero ).
Because our characterization of individual equity skews hinge on negative
skewness in the risk-neutral index distribution, the result [Equation (13)] is
of special relevance. At a theoretical level, Theorem 2 provides sound economic reasons for the presence of risk-neutral skews, even when the physical
process is symmetric. Essentially it states that there are three sources of negative skew in the risk-neutral index distribution. First, a negative skew in
the physical distribution causes the risk-neutral index distribution to be leftskewed, even under  = 0 restriction. Second, risk-neutral index skews and
the kurtosis of the physical measure appear to be inversely related: for a
given volatility level and risk aversion, raising the level of kurtosis beyond
3 generates a more pronounced left tail. In a likewise manner, higher stock
109

market volatility will not guarantee left skew unless the parent distribution is
fat-tailed.
At the least, these features match the observations in Bates (1991) and
Rubinstein (1994) that the index distributions have become (risk-neutrally)
more negatively skewed after the crash of 1987. Finally, risk aversion makes
the risk-neutral density inherit negative skew, provided the kurtosis of the
physical distribution is in excess of 3. Since physical distributions estimated in practice are often symmetric [Jackwerth (2000)], according to Equation (13), heavy-tailed index distributions and risk aversion are the most
likely root of the risk-neutral index skew.
To see the working behind this counterintuitive ﬁnding that exponential
tilting of the physical index distribution produces no skew when kurtosis is
equal to 3, let us take a parametric example in which index returns are distributed normal with mean m and variance 2
m. With the aid of Equation (11)
and Gaussian pRm, we have (for some constants A0 > 0 and A1 > 0)
−Rm −¯ m2
qRm = A0 exp−Rm×exp
2 ¯2
m
−Rm − ¯ m − ¯2
m2
= A1 exp
(14)
2 ¯2
m
which is again a mean-shifted Gaussian variate with zero skewness. This
is consistent with our ﬁrst-order analysis that indicates a need for excess
kurtosis to generate a change in skew. The excess kurtosis is well-known to
be prevalent statistically in index returns. So long as the physical distribution
is fat-tailed, the end-result is similar in stochastic volatility and pure-jump
models as well. In Equations (49)–(51) of the appendix, it is explicitly shown
how exponential tilting of the physical density alters the (ﬁrst) three moments
of the risk-neutral distribution (whether the physical density is generated via
a partial equilibrium or a general equilibrium Lucas economy).
Can Theorem 2 be generalized to a broader family of utility functions? Is
the power utility assumption crucial for generating the negative skew phenomena? To resolve this issue, consider the wider class of marginal utility
functions, U ′Rm, given by
 
0 e−zRm dz
U ′Rm =
(15)
for a measure  on ℜ+. This includes as candidates for marginal utility, all
bounded Borel functions vanishing at inﬁnity [Revuz and Yor (1991)]. For
example, the choice of the gamma density for the measure   results in
HARA marginal utility. In particular, we can also accommodate, as a special
case, the bounded versions of the loss aversion utility functions considered by
Kahneman and Tversky (1979). With positive  , all completely monotone
utility functions (i.e., U ′Rm > 0, U ′′Rm < 0, U ′′′Rm > 0, and so on)
110

are also nested within Equation (15). Clearly the coefﬁcient of relative risk
aversion, Rm ≡−Rm U ′′Rm
U ′Rm , can vary stochastically with Rm.
For all such stochastic discount factors, deﬁne a  approximation by
 
0 e−zRm dz, which is just a functional arc approximation
U ′Rm =
in the space of marginal utilities. Hence
 
0 e−zRm dz
pRm×
 
qRm =
(16)
0 e−zRm dzpRmdRm
 
It then follows that SKEWm ≈SKEWm − 
0 zdz  KURTm −3STDm
(see the appendix for intermediate steps). Even though risk aversion may no
longer be time invariant, the skew dynamics are still being determined by
higher-order moments of the physical distribution. In particular, as we have
shown, the even moments are being weighted by a constant proportional to
risk aversion. This is the outcome, as the risk aversion dependence on the
market is getting integrated out. In the more general case of state-dependent
preferences, the skew dynamics can depend on conditional moves in risk
aversion.
Depending on the nature of return autocorrelation, the risk-neutral skews
may not aggregate linearly across the time spectrum. To develop this argument in some detail, suppose the one-period (say, weekly) rate of return follows an AR-1 process under the physical measure Rmt = Rmt−1+ut.
As usual, let the white noise, ut, have zero mean with  < 1. Keep the
higher moments STDut, SKEWut, and KURTut, unspeciﬁed for now.
Deﬁne the term structure of risk-neutral skews, SKEWmt, as a function
of . Using a standard logic,

 −La
STDmt = STDut×

(17)
1−22
 −Lb
SKEWmt = SKEWut×
 −La3/2 
and
(18)
 −Lc
KURTmt−3 =  KURTut−3×
 −La2 
(19)
where La ≡21−
−21−2
, Lb ≡31−
−321−2
+ 31−3
,
1−2
1−2
1−3
1−
1−
and Lc ≡41−
−621−2
+ 431−3
−41−4
. By combining Equa1−2
1−3
1−4
1−
tions (17)–(19) with Theorem 2, several observations are apparent:
1
• When =0, La =Lb =Lc =0. Therefore SKEWmt=
√ SKEWut−

√  KURTut −3STDut. As a result, absolute skews are declining
in the square root of maturity.
• With moderate levels of positive autocorrelation, the skew term structures display a U-shaped tendency: getting more negative with  initially
111

and then gradually shrinking to zero with large . With  < 0, the term
structure of skews bears the trait that short skews are always more negative than long skews. In either case, the presence of autocorrelation
slows down the rate at which the central limit theorem holds.
• If u is symmetric with kurtosis 3, the term structure of risk-neutral
index skews is ﬂat regardless of the nature of return dependency and
risk-taking behavior.
In summary, the preceding analysis integrates two insights about the term
structure of skews. First, the part of skew that relies on risk aversion and fattailed distribution is more consistent with the daily/weekly frequency. Second, as the observation frequency is altered from weekly to monthly, the term
structure of absolute skews can get upward-sloping even when KURTmt
approaches 3. Although not pursued here, higher-order autoregressive processes would lead to more ﬂexible forms for absolute skew term structures.
One can take advantage of Equation (13) to reverse engineer an estimate
of the presumed constant risk aversion coefﬁcient, and it requires only simple
inputs. To make the point precise, the risk-neutral index skew is recoverable
from option positioning Equation (5), and higher moments of the physical
distribution can be computed, with some sacriﬁce of quality, from the time
series of index returns. Informal as it may be, the reasonableness of the
estimates can serve as an additional metric to assess conformance with theory.
One such estimation strategy is discussed in the empirical section.
1.4 Skew laws for individual stocks
To formalize the next aspect of the problem, assume that the individual stock
return, Rnt, conforms with a generating process of the single-index type
Rnt = ant+bntRmt+nt
n = 1   N
(20)
where ant and bnt are scalers. Provided drift-induced restrictions
are placed on the parameters ant and bnt, the return process [Equation (20)] is also well-deﬁned under the risk-neutral measure. Presume that
the unsystematic risk component nt has zero mean (whether risk neutral
or physical) and is independent of Rmt for all t. Due to this property,
the coskews, E ntRmt − mt2 and E 2
ntRmt −
mt , are zero. We can now state:
Theorem 3.
If stock returns follow the one-factor linear model displayed
in Equation (20), then
(a)
The price of the skewness contract deﬁned in Equation (5), denoted
SKEWnt, is linked to the price of market skewness, SKEWmt,
as stated below ( for n = 1   N):
SKEWnt=ntSKEWmt+ntSKEWt (21)
112

where SKEWt represents the skewness of ; and
−3/2
Vt
nt ≡
1+
(22)
ntVmt−e−r 2
b2
mt
−3/2
ntVmt−e−r 2
1+ b2
mt
nt ≡
(23)
Vt
with 0 ≤nt ≤1 and 0 ≤nt ≤1.
(b)
The individual skew will be less negative than the skew of the market
n = 1   N
SKEWnt > SKEWmt
(24)
under the following conditions: (i) nt belongs to a member of
distributions that are symmetric around zero (i.e., ∗
t 3
nt = 0).
In this case, the variation in the price of individual skewness can
be bounded to be no more than that of the stock market index: 0 ≤
SKEWnt
SKEWmt ≤1; or, (ii) the distribution of nt is positively skewed.
In Equation (24), the risk-neutral index distribution is regarded as being
left skewed. The risk-neutral individual and index skews can be recovered
from the option tracking portfolio [Equation (5)].
Since the idiosyncratic return component requires no measure-change conversions, the skewness laws postulated in Equation (21) will be obeyed under
both the physical and risk-neutral measures (with appropriate adjustments to
t and t). Either way, this statement of the theorem should not
be interpreted to mean that individual return skewness will move in lockstep
with market skewness. From Equation (12), one can understand why total
volatility matters for pricing derivatives even though the stochastic discount
factor only prices systematic risk. This feature is reﬂected in the price of
skewness, as the latter is merely a portfolio of options.
Two polar cases can shed light on the precise role of idiosyncratic skewness. Case A: Rnt = ant+bntRmt, accommodates a generating structure in which individual return is perfectly correlated with the stock
market. When this is so, the risk-neutral skewness of the individual stock
coincides with that of the market. Case B: Rnt = ant + nt.
In this setting, the sole source of individual skewness is the idiosyncratic
skewness. In reality, the individual skewness will be partly inﬂuenced by
market skewness and partly by idiosyncratic skewness. In a later empirical
exercise, we study the skew law implication that 0 ≤nt ≤1. We can
also note that if Equations (21)–(24) hold simultaneously and the market is
heavily skewed to the left, then the idiosyncratic skews are bounded below
and cannot be highly negative.
Even though not stressed in the theorem, more can be said about the
character of individual risk-neutral distributions. Relying on the properties of
113

variance operators and Equation (20), ﬁrst observe that Vnt = b2
nt
Vmt + Vt. Thus, provided the variance of the unsystematic factor
is sufﬁciently well behaved, the individual risk-neutral distributions will be
inherently more volatile than the index. Next, as even moments are correlated
in general, we may expect individual stocks to display more leptokurtosis
than the market.
Due to the aforementioned, the differential pricing of index and individual
equity options is likely. First, as expected, the less negative individual equity
skew tempers the way all individual OTM puts are priced vis-à-vis all OTM
calls. In particular, the skewness premium should get alleviated for individual
stock options. Second, as individual stocks are more inclined to extreme
moves than the market, the valuation of deep OTM calls/puts versus NTM
calls/puts can be expected to diverge as well. These departures between the
index and individual risk-neutral distributions will modify the structure of
option prices (i.e, the smiles).
To get a ﬂavor of the skew laws outside of the single-factor model, consider Rnt = ant+bntRmt+cntF t+nt, which
incorporates a systematic factor, F , besides the market index. Assume the
independence of Rmt, F t, and nt. It can be shown that
SKEWnt = ntSKEWmt+ 
ntSKEWF t
+ntSKEWt
(25)
where n > 0, 
n > 0, and n > 0 are given in Equations (56)–(58) of the
appendix. Two parametric cases are of special appeal. Suppose SKEWF t
 < 0. Then, as in the single-factor characterization, n cannot be relatively
far left skewed with negative index skews. Next, when SKEWF t > 0,
then SKEWnt > SKEWmt with symmetry of n. Under the auxiliary
assumption that each systematic factor contributes equally to the variance of
Rn, we can see that SKEWnt > SKEWmt + SKEWF t/2, for
all n and all .
Our framework is sufﬁciently versatile to recover coskews between individual stocks and the market. The risk-neutral coskew is [Harvey and Siddique
(2000)]
COSKEWnt
∗
t Rnt−∗
t Rnt×Rmt−∗
t Rmt2
≡
(26)
∗
t Rnt−∗
t Rnt2×∗
t Rmt−∗
t Rmt2 1/2
=bnSKEWmt erVmt− 2
mt
n=1   N

(27)
erVnt− 2
nt
from the single-factor assumption of Equation (20). As before, V t and
t are known from option positioning Equations (7) and (39). However,
114

recognize that bnt is a risk-neutralized parameter and can be estimated
from individual equity option prices. We leave this application on coskews
to a future empirical examination.
Before closing this section we need to bridge one remaining gap: Can the
leverage effect reproduce risk-neutral skewness patterns, where the aggregate index is more negatively skewed than any individual stock. For this
purpose we parameterize, in the appendix, a model in which stock returns
and volatility correlate negatively at the individual stock level. In this setting
we demonstrate that the leverage effect does impart a negative skew to the
individual stock and to the aggregate index. But its predictions for the skew
magnitudes are sharply at odds with those asserted in Theorem 3. Specifically, leverage suggests that index skews will be less negative than some
individual stocks. The model’s implications for the joint behavior of riskneutral and physical distributions are unknown, and outside our scope. For
a different strand of the leverage argument, readers are referred to Toft and
Prucyk (1997).
2. The Structure of Option Prices and Skewness/Kurtosis
We can now merge theoretical elements of the risk-neutral distributions of
the market and the individual stocks on one hand, and the mapping that exists
between the structure of option prices and the risk-neutral moments on the
other. As such, this formalizes the empirical framework for exploring the
observed structure of option prices–individual equities or the stock market
index.
To ﬁx ideas, deﬁne the implied volatility as the volatility that equates the
market price of the option to the Black–Scholes value. Accordingly, for riskneutral density, qS, the implied volatility, , is obtained by inverting the
Black–Scholes formula

 e−rK −S+qSdS = Ke−r1− d2−St1− d1
(28)
2√, d2y = d1y−√ and moneyness y ≡
where d1y = −lnye−r
+ 1
√
K
S . Clearly, to know the implied volatility, one must know the form of qS
or the structure of option prices.
We will refer to the implied volatility curves as measuring the relation
among put option implied volatilities that differ only by their moneyness,
going from deep OTM puts to deep ITM puts. For a ﬁxed , write yt
to reﬂect its dependence on y, and deﬁne the slope of the implied volatility
curve as some notion of change in put-implied volatility with change in
moneyness. Intuitively a ﬂatter implied volatility curve implies that option
prices of adjacent strikes are spaced closer rather than far apart. The market
perception of the price of jump risk is embedded in the evolution of the
implied volatility curve [Rubinstein (1994)].
115

The following result—which relates the implied volatility function to the
risk-neutral moments—is borrowed with some modiﬁcation from Backus
et al. (1997). As in Longstaff (1995), it hinges on an approximate representation of any risk-neutral density in terms of the Gaussian.
Theorem 4.
Let yt denote Black–Scholes implied volatility [as recovered by solving Equation (28)]. Then, for a given moneyness, the implied
volatility is afﬁne in the risk-neutral moments that surrogate tail asymmetry
and tail size:
nyt ≈ny+nySKEWnt+nyKURTnt
n = 1   N
(29)
for functions y, y and y that can be obtained in closed form. For
a given (average) moneyness, the slope of the smile is afﬁne in the same
determinants.
The virtue of Theorem 4 is that it justiﬁes the use of simple econometric
speciﬁcations to analyze the relationship between the risk-neutral moments
and the structure of option prices.2 Theorem 4 is essentially a ﬁrst-order
approximation of individual implied volatility, at a given moneyness and
maturity, in terms of higher-order risk-neutral moments of the individual
risk-neutral density. As such, Equation (29) is robust to a wide variety of
speciﬁcations for the physical process of equity returns and the market price
of risk. Hence there is little economic content in the validity of Equation (29);
it just relates different statistics of the underlying risk-neutral density. Unlike
Equation (13) and (21), Equation (29) is not a model of risk-neutral skews.
The basic intuition for the coefﬁcients y and y is that ﬁrms with
higher negative skew have greater implied volatility at low levels of moneyness, while ﬁrms with greater kurtosis have higher implied volatilities for
both OTM and ITM puts. With regard to the effect of higher-order moments
on the shape of the implied volatility curve (at a ﬁxed maturity), we note that
skewness is a ﬁrst-order effect relative to kurtosis, and a higher negative skew
steepens the implied volatility curve. In contrast, kurtosis is a second-order
effect that symmetrically affects OTM call and put option prices, and this
2 There are cases where one cannot uniquely identify the density from the knowledge of all the moments,
including those for all powers above 4 (i.e., lognormal). Hence Equation (29) may not be true in general. We
can, at best, deduce that the correct option price equals the Black–Scholes price plus other terms surrogating
the price of higher risk-neutral moments. To get implied volatility, one has to pass through the inverse of the
Black–Scholes formula, which does not apply additively. In fact, we will get an abstract mapping of the type
yt = yV SKEW KURT. We may then take a ﬁrst-order approximation and attain Equation (29).
To emphasize reliance on one higher odd moment and one higher even moment, we have suppressed the
dependence of , , and  on return volatility. As an empirical matter, we did not ﬁnd smiles (its slope)
to be strongly inﬂuenced by risk-neutral volatility; its effect was already impounded in the denominators of
skewness and kurtosis.
116

should ﬂatten the slope of the implied volatility curve controlling for skewness. If the skew variable is omitted, one would expect kurtosis to proxy for
the ﬁrst-order effect and therefore steepen the implied volatility curve.
The discussion of the previous section along with Theorem 4 suggests the
following hypotheses that can be empirically investigated:
Hypothesis 1.
The implied volatility curves are less negatively sloped for
individual stock options than for stock index options.
Hypothesis 2.
The more negative the risk-neutral skewness, the steeper are
the implied volatility slopes. The more fat-tailed the risk-neutral distribution,
the ﬂatter are the smiles in the presence of skews.
Hypothesis 3.
Individual stock return (risk-neutral) distributions are, on
average, less negatively skewed than that of the market. Granted, the physical
distribution of the index is fat-tailed, the risk-neutral distribution of the index
is generally left skewed.
Hypothesis 1 lays the foundation of the investigation—is it true, as commonly asserted, that the structure of individual option prices is ﬂatter? Hypothesis 2 associates the slope of the smile to the moments, dynamically in the
time series, as well as in the cross section. Finally, Hypothesis 3 directly
follows from Theorem 3. The restriction it imposes on the price of individual skew relative to the price of market skew warrants an idiosyncratic
return component that is not heavily left skewed. These hypotheses are interrelated. For instance, individual slopes are ﬂatter than the market because
individual stocks are less negatively skewed. This implicitly requires index
risk-neutral distributions to be left-displaced versions of the physical counterparts. Having consolidated the big picture in theory, we now pursue our
empirical objectives in sufﬁcient detail.
3. Description of Stock Options and Choices
The primary data used in this study are a triple panel (in the three dimensions
of strike, maturity, and underlying ticker) of bid-ask option quotes written on
31 stocks and one index, obtained from the Berkeley Options Database. The
sample contains options on the S&P 100 index (the ticker OEX) and options
on the 30 largest stocks in the S&P 100 index. These options are American
and traded on the Chicago Board Options Exchange. For each day in the
sample period of January 1, 1991, through December 31, 1995, only the last
quote prior to 3:00 pm (CST) is retained.
For three reasons, we employ daily data to construct weekly estimates of
our variables. First, the use of daily data minimizes the impact of outliers by
allowing moments to be computed daily and then averaged over the calendar
week. Second, the estimation of the slope of the weekly smile for individual
equity options requires daily data over the week so that there are sufﬁcient
117

observations to estimate the smile. Third, the daily risk-neutral index skews
exhibit a Monday seasonality [Harvey and Siddique (1999)]. The exact procedure to build the time series of the smile and its slope will be outlined
shortly.
The requirement to sample options daily virtually limits the analysis to the
largest 30 stocks by market capitalization. Even with the existing choice, the
raw data contains more than 1.4 million price quotes, and additional stocks
would have made the empirical examination less manageable. The tickers and
names of the individual stock options are displayed in the ﬁrst two columns
of Table 1. The set includes, among others, such actively traded and familiar
stock options as IBM, General Electric, Ford, and General Motors.
Table 1
Description of OTM calls and puts
Number of
Midpoint of
option quotes
option quote
Short
Medium
Short
Medium
OEX
Ticker
Stock
Weight
Call
Put
Call
Put
Call
Put
Call
Put
1. AIG
American Int’l
2.32
3414
3884
1779
2471
1.26
0.99
2.34
1.47
2. AIT
Ameritech
1.24
1902
2199
1260
1570
0.62
0.58
0.96
0.89
3. AN
Amoco
1.09
2112
1942
1491
1435
0.49
0.48
0.79
0.76
4. AXP
American Express
1.27
2325
2367
1458
1696
0.41
0.40
0.66
0.60
5. BA
Boeing Company
1.27
2848
2624
1927
1896
0.56
0.48
0.93
0.71
6. BAC
BankAmerica Corp.
1.53
2640
3023
1576
2007
0.62
0.53
0.99
0.77
7. BEL
Bell Atlantic
1.90
2242
2335
1409
1600
0.47
0.47
0.71
0.74
8. BMY
Bristol-Myers
2.85
3040
3311
1927
2335
0.63
0.57
1.04
0.84
9. CCI
Citicorp
1.82
2545
2983
1512
2007
0.47
0.41
0.79
0.57
10. DD
Du Pont
2.33
2492
2639
1472
1731
0.57
0.53
0.98
0.79
11. DIS
Walt Disney Co.
2.04
4020
4677
2297
2905
1.06
0.87
2.00
1.40
12. F
Ford Motor
1.66
2924
3068
2062
2264
0.56
0.51
0.90
0.80
13. GE
General Electric
7.29
3323
4019
1857
2801
0.67
0.59
1.28
0.93
14. GM
General Motors
1.36
3021
3134
2107
2208
0.58
0.53
0.98
0.78
15. HWP
Hewlett-Packard
1.73
3973
5305
2168
3978
1.29
0.92
2.57
1.38
16. IBM
Int. Bus. Mach.
3.05
5605
4806
3514
2755
0.89
0.84
1.41
1.31
17. JNJ
Johnson & Johnson
2.48
2999
3256
1646
2148
0.81
0.70
1.40
1.00
18. KO
Coca Cola Co.
5.18
2438
3305
1450
2589
0.62
0.50
1.09
0.69
19. MCD
McDonald’s Corp.
1.21
2321
2285
1443
1814
0.51
0.40
0.89
0.60
20. MCQ
MCI Comm.
0.99
2437
2311
1503
1508
0.46
0.44
0.74
0.65
21. MMM
Minn Mining
1.01
3532
3730
1946
2175
0.80
0.75
1.32
1.21
22. MOB
Mobil Corp.
1.63
2573
2618
1795
2232
0.71
0.67
1.15
1.00
23. MRK
Merck & Co.
3.75
3283
4163
1865
2639
0.98
0.83
1.69
1.31
24. NT
Northern Telecom
0.89
1916
1788
1213
1176
0.60
0.53
0.94
0.72
25. PEP
PepsiCo Inc.
1.65
2091
2459
1285
1695
0.40
0.36
0.65
0.51
26. SLB
Schlumberger Ltd
1.04
2965
2678
1670
1699
0.77
0.71
1.34
1.06
27. T
AT&T Corp.
2.64
2423
2607
1498
1783
0.45
0.36
0.73
0.50
28. WMT
Wal-Mart Stores
3.31
2539
2959
1868
2036
0.49
0.42
0.80
0.63
29. XON
Exxon Corp.
4.64
2364
2502
1375
1556
0.46
0.44
0.73
0.66
30. XRX
Xerox Corp.
0.89
3665
4615
1927
2921
1.23
0.94
2.13
1.43
31. OEX
S&P 100 Index
12793
22755
10981
16828
2.15
1.86
4.98
4.47
The table reports the number of observations and the midpoint price as the average of the bid-ask quotes for short-term and
medium-term OTM calls and puts for 30 stocks and the S&P 100. The ticker, name, and recent weight of the stock in the index
(as of May 1998) are also reported. The call (put) is OTM if K/S > 1 (K/S < 1), where S denotes the contemporaneous stock
price and K is the strike. Short-term options have remaining days to expiration of between 9 and 60 days and medium term
between 61 and 120 days. Only the last daily quote prior to 3:00 p.m. CST of each option contract is used in our calculations.
The sample period extends from January 1, 1991, through December 31, 1995 for a total of 358,851 option quotes (162,046
calls and 196,805 puts).
118

To be consistent with the existing literature, the data were screened to
eliminate (i) bid-ask option pairs with missing quotes, or zero bids, and
(ii) option prices violating arbitrage restrictions that CtK < St or
CtK > St −PVDD −PVDK, for present value function PVD 
and dividends D. As longer- (and very short-) maturity stock option quotes
may not be active, options with less than 9 days and more than 120 days to
expiration were also discarded. Finally, as indicated by Theorem 1, we only
keep OTM calls and puts. As a result, puts have moneyness corresponding to
K
St < 1 , and calls have moneyness corresponding to K
K
K
St 
St 
St > 1 .
Although each series for skewness and kurtosis pertain to a constant ,
in practice, it is not possible to strictly observe these, as options are seldom
issued daily with a constant maturity. Therefore, in our empirical exercises, if
an OTM option has remaining days to expiration of 9 to 60 days, it is grouped
in the short-term option category; if the remaining days to expiration is 61
to 120 days, the option is grouped in the medium-term category. Thus only
two classiﬁcations of smiles and option portfolios are investigated.
Table 1 reports the option price as the average of the bid and ask quotes,
and the number of quotes, for both short-term and medium-term OTM calls
and puts. The table also reports the weight of each stock in the OEX. As
would be expected, the index has considerably more strikes quoted than
individual stock options, with puts more active than calls. In the combined
option sample, there are 358,851 OTM calls and puts.
Because each option under scrutiny has the potential for early exercise, the
treatment of the smile is arguably controversial. To probe this issue we also
calculate the volatility that equates the observed option price to the American
price. For estimating the price of the American option, we follow Broadie
and Detemple (1996). We construct a binomial tree where the Black–Scholes
price is substituted in the penultimate step. The American option price is estimated by extrapolating off the prices estimated from 50- and 100-step trees,
using Richardson extrapolation, and accounts for lumpy dividends. We then
estimate two separate implied volatilities: the volatility that equates the option
price to the American and the Black–Scholes price. In the latter calculations,
discounted dividends are subtracted from the spot stock price.
Table 2 compares the European and American implied volatilities. While
presenting this comparison, three decisions are made for conciseness. First,
options are divided into two moneyness intervals: [−10%−5%) and [−5%,
0), for calls and puts. Next, only the implied volatilities for a sample of
10 stocks and the OEX are shown. Finally, we focus on the 1995 sample
period, as averaging over the full ﬁve-year sample narrows the differences
even further. For the most part, the implied volatility curves tend to taper
downward from deep OTM put options to ATM, and then moves slightly
upward as the call becomes progressively OTM. Although the American
option implied volatility (denoted AM) is smaller than the Black–Scholes
(denoted BS) counterpart, this difference is negligible and within the bid-ask
119

& Poor’s and converted to a dividend yield for each date maturity combination. Following a common practice, when the Eurodollar interest rate matching the option maturity (datasource: Datastream) is unavailable,
option price, respectively. The American option price is estimated by Richardson extrapolation of 50- and 100-step binomial trees, accounting for lumpy dividends [see Broadie and Detemple (1996)]. The implied
puts to ITM puts. In all computations, discrete dividends for each stock are collected from CRSP and are assumed known over the life of the option. For the S&P 100, the daily dividends are drawn from Standard
Short-term options have remaining days to expiration of between 9 and 60 days, and medium term between 61 and 120 days. All numbers correspond to the period of January 1, 1995, through December 31, 1995.
For a sample of 10 stocks and the OEX, the table reports the Black–Scholes (denoted BS) and the American (denoted AM) option implied volatilities obtained by inverting the Black–Scholes and the American
As OTM call options have the same implieds as ITM puts at a given moneyness level, the four columns representing the implieds of OTM puts and calls may be also viewed as the entire smile ranging from OTM
volatilities of individual options are then averaged within each moneyness-maturity category and across days. Two categories of OTM options are used corresponding to the intervals [−10%, −5%) and [−5%, 0).
20.88
16.49
25.33
18.46
22.32
33.19
24.80
17.64
17.62
21.72
10.08
AM
−5% to −10%
20.89
16.50
25.33
18.46
22.32
33.19
24.80
17.64
17.62
21.72
10.08
BS
OTM calls
21.90
17.09
25.46
18.41
22.68
32.09
24.95
17.78
16.71
22.18
10.73
AM
0% to −5%
Medium-term options
21.93
17.10
25.49
18.41
22.68
32.09
24.95
17.78
16.71
22.18
10.73
BS
23.02
19.75
25.35
19.38
23.93
32.82
25.94
19.67
18.19
24.20
13.10
AM
−5% to 0%
23.39
20.11
25.83
19.84
24.33
33.31
26.42
20.13
18.65
24.68
13.31
BS
OTM puts
24.28
20.33
25.95
19.67
25.33
33.12
26.33
20.52
19.03
24.43
15.93
−10% to −5%
AM
24.50
20.53
26.23
19.88
25.54
33.42
26.59
20.74
19.27
24.69
16.01
BS
22.87
18.48
26.07
19.13
24.05
33.23
26.71
19.70
19.74
22.98
10.76
−5% to −10%
AM
22.87
18.48
26.24
19.13
24.04
33.23
26.71
19.72
19.81
22.97
10.76
Black–Scholes implied volatilities versus American option implied volatilities
BS
OTM calls
21.77
17.79
25.16
18.86
22.79
31.64
25.88
18.60
18.25
23.09
10.72
AM
0% to −5%
Short-term options
21.78
17.79
25.46
18.86
22.79
31.64
25.88
18.64
18.53
23.09
10.72
BS
23.41
19.85
25.17
19.79
23.76
32.89
27.03
20.03
20.00
24.58
13.36
AM
−5% to 0%
23.61
20.04
25.38
19.98
23.97
33.11
27.24
20.22
20.19
24.78
13.45
BS
OTM puts
26.64
22.70
27.10
21.51
26.31
34.16
28.67
22.37
21.26
26.24
18.49
−10% to −5%
AM
it is linearly interpolated.
26.73
22.78
27.20
21.59
26.40
34.26
28.76
22.45
21.35
26.32
18.52
BS
Table 2
MMM
Ticker
HWP
XRX
OEX
IBM
AIG
DIS
GM
JNJ
BA
GE
120

spread. With the assurance that the bias from adopting BS implied volatility
is small enough to be ignored, we adhere to convention and use only Black–
Scholes smiles to surrogate the pricing structure of options.
4. Skewness and the Structure of Option Prices: Empirical Tests
This section establishes the differential pricing of individual stock options
versus the market index and empirically relates it to the asymmetry and the
heaviness of the risk-neutral distributions. We also present a framework to
study the empirical determinants of risk-neutral index skews.
4.1 Quantifying the structure of option prices
To quantify the structure of option prices we use options of maturity  to
estimate the model,
lnyj = 0 + lnyj+ j
j = 1   J
(30)
across our sample of 30 stocks and the OEX, where, recall, y = K/S is
option moneyness (and deterministic). An advantage of the speciﬁcation in
Equation (30) is its potential consistency with empirical implied volatility
curves that are both decreasing and convex in moneyness. This suggests a
less than 0. We interpret as a measure of the ﬂatness of the implied
volatility curve and designate it as the sensitivity of the implied volatility
curve to moneyness. In economic terms, a ﬂatter implied volatility curve
simply states that prices of put options of nearby strikes are closer, while
those options that constitute a steeper curve have prices farther apart.
The model of Equation (30) is estimated weekly, and the estimated coefﬁcients are pooled over all the weeks in the sample. Brieﬂy the procedure is as
follows. Over each calendar day in the week we index the available options
by j and estimate the said model by least squares. Thus, for each stock, we
estimate Equation (30) for each of the 260 weeks for which sufﬁcient data
exist. Next, as in Fama and McBeth (1973), we time average the regression
T
1
t=1 t). Each reported t-statistic is computed under
coefﬁcients (say,
T
a ﬁrst-order serial correlation assumption for the coefﬁcient. The model is
estimated using OTM puts and calls. As in the money puts (K/S > 1) can be
proxied by OTM calls, this is tantamount to using all the strikes in the cross
section of puts.
Table 3 reports the average slope of the implied volatility curve for each
of the 30 stocks and the OEX. We also report the estimated ATM implied
volatility as exp 0. Consider ﬁrst, the results for short-term smiles. The
average ATM implied volatility for the OEX is 14%, while the average ATM
implied volatility over the 30 stocks is about 26%. With reference to the
estimate of , we can make three observations. First, on average, is negative for all the individual stocks and the OEX. The slopes are all statistically
121

Table 3
Quantifying the structure of option prices
Short-term options
Medium-term options
Slope of
Slope of
the smile,
the smile,
R2
R2
exp 0
<0
exp 0
<0
t
t
t
t
Ticker
Avg.
Avg.
Avg.
%
Avg.
Avg.
Avg.
%
32 12 −1 09 −13 01
119 84 −0 62
−7 61
0 22
43 57
0 22
38 2
1. AIG
97
76
38 45 −1 96 −14 34
108 39 −1 59 −15 22
0 19
55 41
0 19
31 9
2. AIT
96
57
25 61 −0 96
−8 25
80 11 −0 97
−6 60
0 19
36 08
0 19
41 4
3. AN
80
83
17 09 −0 26
−3 87
66 60 −0 32
−6 52
0 31
27 62
0 31
56 9
4. AXP
74
97
24 78 −0 69
−7 39
96 42 −0 57
−4 09
0 27
33 29
0 25
73 2
5. BA
80
97
18 27 −1 16 −13 03
93 15 −0 84
−8 30
0 30
56 81
0 29
74 7
6. BAC
95
98
23 70 −1 54 −10 14
89 94 −1 23
−7 98
0 21
48 12
0 20
59 0
7. BEL
86
95
22 70 −1 38
−7 78
93 39 −1 07
−5 02
0 21
46 55
0 20
71 5
8. BMY
89
98
12 87 −0 83 −10 20
58 59 −0 63
−6 79
0 35
42 32
0 35
75 8
9. CCI
90
97
30 96 −0 86 −15 39
129 37 −0 76 −14 08
0 24
42 01
0 23
48 8
10. DD
95
90
31 94 −0 91 −13 67
146 50 −0 69 −12 79
0 28
48 29
0 28
71 7
11. DIS
95
99
38 78 −0 62
−8 86
137 45 −0 50
−7 32
0 31
37 77
0 30
57 6
12. F
88
96
31 67 −1 85 −19 55
117 81 −1 55 −22 11
0 21
61 02
0 20
81 1
13. GE
99
98
26 48 −0 52
−8 27
138 09 −0 40
−5 22
0 31
34 86
0 30
76 7
14. GM
83
99
29 96 −0 83 −11 86
147 65 −0 50 −10 44
0 33
50 95
0 32
56 8
15. HWP
96
96
18 79 −0 36
−3 09
103 52 −0 28
−2 03
0 29
29 85
0 27
65 5
16. IBM
71
97
19 64 −1 00 −10 79
96 00 −0 88
−5 57
0 24
41 70
0 24
69 7
17. JNJ
93
99
28 06 −1 62 −20 64
113 41 −1 22 −10 15
0 24
62 87
0 22
77 6
18. KO
99
100
30 49 −1 16 −11 84
90 25 −0 99 −12 77
0 25
46 17
0 24
73 1
19. MCD
93
96
31 15 −0 53
−7 22
81 57 −0 32
−3 63
0 34
26 34
0 33
49 6
20. MCQ
74
68
60 43 −1 21
−6 19
151 90 −1 21 −11 52
0 21
42 65
0 19
67 5
21. MMM
90
96
30 92 −1 34 −14 75
124 79 −1 18 −13 29
0 19
44 17
0 18
44 9
22. MOB
94
80
17 46 −0 62
−3 51
98 47 −0 55
−3 49
0 27
38 67
0 26
76 1
23. MRK
72
98
17 38 −0 31
−3 05
69 44 −0 25
−3 77
0 31
28 40
0 29
34 6
24. NT
72
72
19 31 −1 13 −11 85
84 13 −0 92
−6 99
0 26
45 50
0 25
80 3
25. PEP
91
100
30 00 −0 54
−5 49
129 84 −0 55
−5 19
0 25
30 84
0 24
30 0
26. SLB
76
67
31 21 −1 44 −11 51
104 26 −1 11 −10 53
0 21
48 59
0 21
85 5
27. T
95
100
23 53 −0 95
−8 65
93 92 −0 50
−3 53
0 29
44 85
0 28
67 7
28. WMT
88
92
32 56 −1 47 −14 51
107 16 −1 43
−9 12
0 17
41 97
0 16
75 5
29. XON
91
99
36 39 −1 31 −17 38
162 13 −0 87 −18 17
0 26
55 73
0 25
49 8
30. XRX
98
88
24 80 −4 42 −22 32
84 31 −3 47 −20 31
0 14
86 08
0 14
93 8
31. OEX
100
100
For 30 stocks and the S&P 100, the table displays the average coefﬁcients for the speciﬁcation
lnj = 0 + lnyj+ j
j = 1   J
Here,  is the Black–Scholes implied volatility of option with moneyness y ≡K
S . The regression is estimated via OLS for each
of the 260 weeks in the period January 1, 1991, to December 31, 1995 in which there are a minimum of eight observations,
using OTM puts ( K
S < 1) and OTM calls ( K
S > 1). The table reports the estimated (i) ATM implied volatility corresponding
to K/S = 1 as exp 0, (ii) the slope of the smile, , and (iii) the coefﬁcient of determination, R2 (in %), as the time-series
average over all the weekly regressions [Fama and McBeth (1973)]. The reported t-statistic is the time-series average divided by
the standard deviation of the mean. We have computed the standard deviation of the mean under a ﬁrst-order serial correlation
assumption for the coefﬁcient, and used this assumption to adjust the reported t-statistics. The table also displays (in percentage)
the fraction of the weekly estimates of the slope that satisfy < 0.
signiﬁcant, and the R2 of the regression range from 26% (for MCQ) to 86%
(for the OEX). Second, the slope for the OEX is much steeper than that
for individual stocks. Compared to the short-term OEX slope of −4 42, the
average slope over the 30 stocks is −1 02 (the difference between OEX and
a representative individual implied volatility slope is almost seven standard
deviations away).
The difference between the slopes translates into a substantial difference in
pricing. For the OEX, the slope of −4 42 indicates that the implied volatility
122

of a 10% OTM put (y = 0 9) will be 22% as compared with the ATM implied
of 14%. In contrast, for the individual equity, the 10% OTM put will be priced
at 29% as compared with the ATM implied of 26%. Finally, the table reports
the statistic < 0, a counting indicator for the number of weeks in which
the slope of the implied volatility curve is negative. This statistic ranges from
71% in the case of IBM to 100% for the OEX. Although over this sample
period the slope is always downward sloping for the index, it is not always
so for individual equities. We also examined the slope of the smile in the
yearly subsamples and still found index smiles to be much steeper than any
individual equity smile. Table 3 also shows that the regression ﬁndings from
medium-term smiles are comparable.
As may be observed from Table 1, OTM puts are far more active than OTM
calls for the OEX. To investigate the pricing differential between individual
stocks and the OEX for OTM puts alone, we also estimated Equation (30) by
trimming the option data to include only OTM puts. The average (short-term)
slope coefﬁcient for the OEX is −5 00, as compared to an average of −2 04
over the 30 stocks. The conclusion from the one-sided smile is essentially
the same—that OTM puts are relatively more expensive than ATM puts for
OEX than in the individual option markets.
In summary, two conclusions emerge. First, the slope of the OEX smile is
persistently more negative than individual equity slopes. Second, unlike the
OEX, the slopes of individual smiles are not always negative. Thus OTM
puts are consistently and substantially more expensive than OTM calls for
the index. In contrast, the difference between OTM puts and OTM calls is
smaller for the individual equity, and may, in fact, change signs. But why
are index smiles always downward sloping? What causes the slope of the
individual smiles to reverse its sign? The differential pricing in the cross
section of strikes and in the cross section of stocks is puzzling.3
4.2 Explaining the behavior of options in the stock cross section
Although, as in the previous subsection, it is possible to establish that the
implied volatility curve is ﬂatter for the individual equity than for the OEX,
it is difﬁcult to provide an economic rationale for the differential pricing
of individual equity options. In this subsection and the next, we investigate
3 To verify the results, we also model the implied volatility curve as quadratic in moneyness: j = 0 +
1Kj/S −1 + 2Kj/S −12 + jj = 1   J [see Heynen (1994) and Dumas, Fleming, and Whaley
K
S = 1) is consistently more
(1998)]. Empirically we ﬁnd that the 1 of the index (slope of the smile at
negative than the individual counterparts. In addition, the convexity parameter, 2, is persistently positive in
the cross section of stocks. Consequently the quadratic speciﬁcation has in common with its log predecessor
the feature that the ﬁrst-order (second-order) derivative of the implied volatility function with respect to
moneyness is negative (positive). Toft and Prucyk (1997) and Dennis and Mayhew (1999) adopt an alternative
measure where the slope is standardized to impute the distance between the implied volatilities of 10% ITM
and OTM options. This measure of the implied volatility slope is particular to just two option strikes that
are themselves almost two standard deviations OTM for short-term options, and hence constitutes a crude
measure of volatility skews.
123

whether we can parsimoniously relate the structure of option prices to the
respective risk-neutral moments, and, if so, what judgments can be drawn
from the analysis.
Unlike the implied volatility curve, the risk-neutral moments are intrinsically unobservable. Here we make use of our model-free characterizations in
Theorem 1 to estimate each moment. Consider, as an example, the estimation
of the skew. This requires ﬁrst replicating the cubic contract in Equation (8),
and we do this by constructing positions in both OTM calls and puts that
approximate the corresponding integral. The long position in the calls is discretized as
K−St

K
wSt+jKCtSt+jKK
lim
(31)
K→
j=1
2
St−3ln K
St
6ln K
where wK ≡
, and the short position in the puts as
K2
St−K

K
wjKPtjKK
(32)
j=1
2
St
St
K +3ln
K 
6ln
where now wK ≡
. We similarly discretize and estimate
K2
the volatility contract and the quartic contract, and next, using the formulas
in Equations (5) and (6), we estimate the risk-neutral skewness and kurtosis.
The moments are estimated daily, separately for both short-term and mediumterm options.
Motivated by Theorem 4, we investigate whether a stock with a greater
absolute skew has a steeper smile. To this end we estimate an ordinary least
squares regression
SLOPEnt=+SKEWnt+KURTnt+ n
n=1   N
(33)
where the series for the slope of the smile are the weekly estimates of the
coefﬁcient obtained from regressing log implied volatility on log moneyness. As we have compiled weekly estimates of slopes and the corresponding
moments for each of the 30 stocks, we estimate the cross-sectional regression
weekly for each of the 260 weeks (January 1991 to December 1995). In so
doing, we follow the standard procedure of averaging the estimated regression coefﬁcients and their R2. As before, the t-statistic is computed under
a ﬁrst-order serial correlation assumption for the regression coefﬁcient. We
report, in Table 4, results for both the multivariate regression, as well as the
univariate regressions.
Irrespective of the sample period, and regardless of the maturity structure
of the options, the coefﬁcient for skewness, , is positive and statistically
124

estimated by OLS for each week in the sample period. The table reports the coefﬁcients and the coefﬁcient of determination (R2, in percent), as the time-series average over all the weekly regressions [as in Fama
risk-neutral skewness and kurtosis are estimated from the cross section of OTM calls and puts (as in Theorem 1). The weekly estimate is then derived as the time average of the daily estimates. The regression is
where, corresponding to stock n, SLOPEn is the slope of the smile, n, as described in Table 3, and SKEWn and KURTn are the risk-neutral skews and kurtosis, respectively. For each day in the week, the
and McBeth (1973)] for both restricted and unrestricted regressions. The reported t-statistics are computed under the assumption of ﬁrst-order serial correlation for the regression coefﬁcients. Nt is the number of
stocks in the cross section in week t. Each row of the table shows the results for a speciﬁc maturity (short or medium) and time period. “Full” refers to the entire period from January 1, 1991, through December
Avg.
5.6
3.7
3.2
9.2
9.2
7.5
5.4
9.3
R2
−10 07
−1 19
−5 31
−7 96
2 74
2 77
2 41
−6 65
t
Restricted  ≡0
(kurtosis alone)

−0 08
−0 02
−0 08
−0 14
0 07
0 10
0 10
−0 10
Avg.
−25 30
−10 44
−14 31
−9 01
−16 88
−10 29
−8 44
−9 74
t

−0 79
−0 98
−0 81
−0 61
−0 72
−1 13
−1 18
−1 25
Avg.
Avg.
46.5
43.2
48.0
44.7
48.1
47.0
50.1
45.0
R2
For short-term and medium-term options on 30 stocks and the S&P 100, the table reports the average coefﬁcients of weekly cross-sectional regression,
35.44
13.08
19.66
14.49
27.88
19.78
17.14
12.06
t
n = 1   Nt
(skewness alone)
Restricted  ≡0

Avg.
1.26
1.11
1.40
1.24
1.01
0.81
1.10
0.96
−50 59
−10 26
−20 72
−27 73
−19 76
−23 28
−37 54
−39 50
t
SLOPEn = +SKEWn + KURTn + n

−0 75
−0 77
−0 57
−0 57
−0 53
−0 74
−0 72
−0 60
Avg.
Avg.
51.3
49.7
52.8
47.3
56.2
60.4
54.3
48.3
R2
12 86
6 21
7 64
3 18
8 45
7 84
5 24
1 03
t
Structure of option prices and moments in the stock cross section

0 46
0 48
0 63
0 21
0 55
0 74
0 47
0 12
Avg.
Unrestricted regression
40.93
21.89
20.90
22.05
32.27
40.94
19.79
12.46
t

Avg.
1.45
1.29
1.62
1.37
1.04
0.88
1.10
1.03
−23 04
−9 95
−12 07
−8 65
−13 52
−11 27
−8 78
−4 28
t

−0 78
−1 56
−1 56
−1 83
−1 56
−1 87
−1 41
−1 12
Avg.
Medium-1991
Medium-1993
Medium-1995
Medium-Full
Short-1991
Short-1993
Short-1995
Short-Full
31, 1995.
Table 4
Year
125

signiﬁcant. Thus, as premised, each week, a more negatively skewed stock
displays a steeper smile. Over the entire sample, the average coefﬁcient for
skewness is 1.45 (t-statistic of 55.88), while that of kurtosis is 0.46 (t-statistic
of 16.54), for short-term smiles. Subperiod results for each year are consistent
with those of the overall sample period: the estimate of  is in the range of
1.29 to 1.62, and  in the range of 0.21 to 0.63. The results are stable across
both option maturities, and the ﬁt of the regression has an average R2 of
51.37% for short-term options and 56.29% for medium-term options.
To determine the individual explanatory powers of skewness and kurtosis,
we performed two separate univariate regressions where we constrain  ≡0
and  ≡0, respectively. These restricted regressions support two additional
ﬁndings. First, the cross-sectional behavior of equity options is primarily
driven by the degree of asymmetry in the risk-neutral distributions; the average R2 in the short-term univariate regression is 46.54% with skewness alone,
as compared to 5.6% with kurtosis alone. Therefore the model performance
worsens substantially when a role for skews is omitted. We infer from this
reduction in performance that the ﬁrst-order effect on the implied volatility slopes is driven by risk-neutral skews. The second point to note is that
although the sign on  remains unaltered between the restricted and the
unrestricted regressions, the coefﬁcient on kurtosis reverses sign and turns
negative. Thus, consistent with our hypotheses, in the presence (absence) of
negative skewness, the kurtosis makes the smile ﬂatter (steeper).
A possible explanation of the estimation results for  is that a fatter tail
is accompanied by a greater negative skew and a steeper smile, but that
the marginal effect of kurtosis is to ﬂatten the smile. Indeed, for our sample of individual stocks and the index, the average time-series correlation
between (risk-neutral) skew and kurtosis is −0 48. Thus the negative covariation between skew and kurtosis will downward bias  when skewness is
left uncontrolled in the estimation of Equation (33). To examine the role of
kurtosis separate from its covariation with the skew, we linearly project kur-

tosis onto skewness, KURTt = a0 + a1SKEWt +
KURTt, and

KURTt. Repeating
extracted the orthogonalized component of kurtosis,
the cross-sectional regression of Equation (33), we get the following results
for short-term options (all coefﬁcients are signiﬁcant):
R2 =49 98%
SLOPEn =−0 81+1 29SKEWn+0 10 
KURTn+ n
and
R2 =5 91%
SLOPEn =−1 11+0 12 
KURTn+ n
As our evidence veriﬁes, the orthogonal component of kurtosis also ﬂattens
the smile. This is also true across each of the annual subsamples. To sum up,
skewness does not completely subsume the effect of kurtosis, and individual
skew variation is responsible for explaining the bulk of the variation in the
cross section of individual equity option prices. We will provide an economic
explanation for these results shortly.
126

4.3 Explaining dynamic variations in individual option prices
We next research the link between the risk-neutral moments and the individual option prices in the time series (suppressing dependence on  in each
entity):
SLOPEt = +SKEWt+ KURTt+ SLOPEt −1+ t (34)
which involves a time-series regression of the slope of the smile on individual name risk-neutral skew and kurtosis. The SLOPEt −1 is included to
accommodate the possibility of serial correlation in the dependent variable,
SLOPE. Equation (34) is estimated by ordinary least squares (OLS), and the
standard errors are computed using the Newey–West procedure (with a lag
length of 8).
Panel A of Table 5 presents the unrestricted regression results for shortterm options. For all stocks and the OEX,  is positive and statistically
signiﬁcant. Thus, as anticipated, the smile steepens when the risk-neutral
skew becomes more negative from one week to another. The sensitivity of
the slope to risk-neutral skewness is by far the highest for the OEX which has
Table 5
Variation in individual equity option prices across time
Panel A: Unrestricted regressions
LR test
R2
21

t

t
t 
p value
Ticker
7 80
0 03
0 83
7 18
0 68
1. AIG
0.75
0.44
46.0
.41
6 70
0 24
4 52
2 20
23 12
2. AIT
1.42
0.21
46.1
.00
−0 06
−2 23
6 05
3 81
23 12
3. AN
0.73
0.21
44.6
.00
3 59
0 01
0 95
3 13
2 00
4. AXP
0.35
0.33
43.7
.16
10 21
0 03
1 99
4 14
6 56
5. BA
0.95
0.26
66.6
.01
10 42
0 04
2 95
7 73
8 53
6. BAC
0.68
0.39
68.1
.00
12 11
0 13
4 51
4 22
31 83
7. BEL
1.24
0.28
64.3
.00
10 06
0 05
2 15
7 69
8 00
8. BMY
1.05
0.37
71.1
.00
−0 01
−1 25
9 50
8 78
1 22
9. CCI
0.58
0.42
63.3
.27
9 26
0 04
3 04
4 60
11 27
10. DD
0.57
0.30
43.8
.00
6 58
0 04
2 47
10 18
6 13
11. DIS
0.52
0.52
55.8
.01
5 97
0 02
2 31
8 25
7 25
12. F
0.41
0.45
57.6
.01
11 76
0 10
5 62
9 51
30 01
13. GE
1.07
0.46
62.3
.00
−0 01
−0 79
6 90
9 22
0 97
14. GM
0.49
0.46
58.9
.33
8 10
0 06
2 57
8 54
10 02
15. HWP
0.47
0.52
61.5
.00
−0 03
−1 12
6 47
8 77
2 57
16. IBM
0.80
0.53
74.8
.11
4 13
0 01
0 90
6 74
1 60
17. JNJ
0.49
0.43
49.5
.21
10 30
0 08
4 57
4 55
37 00
18. KO
0.86
0.27
58.6
.00
11 10
0 09
4 62
3 81
36 67
19. MCD
0.87
0.29
57.5
.00
7 63
0 03
1 56
3 10
3 61
20. MCQ
0.81
0.18
47.0
.06
5 14
0 08
1 96
8 17
3 45
21. MMM
0.87
0.63
47.2
.06
8 96
0 05
2 02
6 31
6 43
22. MOB
0.95
0.31
54.2
.01
7 67
0 07
5 34
5 77
32 59
23. MRK
0.77
0.45
74.6
.00
5 74
0 04
1 53
6 04
5 10
24. NT
0.58
0.27
48.6
.02
9 65
0 04
3 43
6 02
13 61
25. PEP
0.78
0.28
58.6
.00
10 43
0 10
4 25
7 64
22 21
26. SLB
0.95
0.27
60.7
.00
10 03
0 08
4 85
5 09
33 58
27. T
1.00
0.27
71.3
.00
13 24
0 04
2 88
6 65
11 09
28. WMT
0.59
0.43
66.3
.00
9 17
0 08
4 13
3 40
22 14
29. XON
1.11
0.15
54.4
.00
4 50
0 08
2 71
10 62
9 79
30. XRX
0.57
0.51
43.0
.00
5 65
0 21
5 02
7 68
28 43
31. OEX
1.83
0.58
74.8
.00
127

Table 5
(continued)
Panel B: Restricted regressions
Restricted  ≡0
Restricted  ≡0
(skewness alone)
(kurtosis alone)
R2
R2

t
t 

t
t 
Ticker
−0 12
−3 03
7 22
7 12
8 69
1. AIG
0.71
0.44
45.9
0.53
32.5
−0 04
−1 39
4 19
3 28
4 19
2. AIT
0.77
0.29
34.2
0.37
15.1
2 87
4 32
0 00
0 09
4 90
3. AN
0.60
0.24
38.9
0.33
10.9
−0 02
−2 39
3 85
3 92
5 34
4. AXP
0.32
0.34
43.2
0.50
25.9
−0 05
−2 36
9 16
4 28
7 39
5. BA
0.88
0.27
65.7
0.54
33.5
−0 07
−4 93
10 32
8 23
11 05
6. BAC
0.58
0.39
67.0
0.57
46.6
−0 11
−5 32
10 70
4 38
5 99
7. BEL
0.84
0.29
59.4
0.44
36.5
−0 09
−3 29
7 17
7 56
10 58
8. BMY
0.91
0.37
70.2
0.61
53.2
−0 07
−5 31
10 85
8 76
10 16
9. CCI
0.59
0.43
63.2
0.57
45.5
−0 01
−1 80
7 71
4 58
6 08
10. DD
0.47
0.31
41.2
0.44
20.9
6 48
10 67
0 12
0 94
14 92
11. DIS
0.49
0.52
54.8
0.64
42.4
−0 01
−1 09
4 78
8 45
14 54
12. F
0.36
0.47
56.4
0.63
40.2
−0 06
−3 30
7 87
9 83
11 82
13. GE
0.74
0.49
57.7
0.58
38.7
−0 03
−2 81
7 02
9 01
13 39
14. GM
0.49
0.45
58.7
0.63
41.2
7 14
9 30
0 00
0 09
12 67
15. HWP
0.41
0.54
59.9
0.69
48.8
7 40
9 16
0 00
0 18
19 31
16. IBM
0.78
0.54
74.6
0.77
63.7
−0 04
−2 74
4 58
6 99
10 88
17. JNJ
0.45
0.44
49.2
0.58
37.5
−0 02
−0 88
10 01
4 00
7 83
18. KO
0.63
0.25
52.2
0.51
29.5
−0 04
−3 05
5 97
4 67
6 67
19. MCD
0.61
0.32
50.8
0.47
25.8
−0 03
−1 32
7 33
3 15
4 32
20. MCQ
0.77
0.19
46.2
0.35
13.2
−0 03
−1 22
5 78
8 73
9 11
21. MMM
0.70
0.65
46.5
0.66
42.2
−0 05
−2 53
8 83
6 38
7 80
22. MOB
0.87
0.32
53.2
0.48
24.3
−0 03
−1 80
8 35
11 36
13 77
23. MRK
0.53
0.58
71.1
0.77
58.1
−0 07
−5 89
8 56
6 61
6 84
24. NT
0.47
0.28
47.4
0.39
28.8
−0 04
−3 88
8 58
5 18
6 01
25. PEP
0.66
0.28
56.3
0.45
27.8
−0 07
−2 15
6 60
8 79
12 71
26. SLB
0.77
0.31
57.2
0.52
29.9
−0 07
−5 84
10 53
6 43
8 60
27. T
0.65
0.32
67.3
0.53
49.3
−0 03
−1 33
11 68
8 25
14 83
28. WMT
0.51
0.47
64.8
0.68
47.1
−0 06
−4 24
7 33
3 65
6 95
29. XON
0.85
0.17
50.4
0.35
21.3
−0 01
−0 59
3 70
10 18
12 13
30. XRX
0.42
0.51
40.9
0.57
33.3
−0 06
−3 82
5 38
9 97
14 57
31. OEX
0.69
0.64
71.9
0.76
68.7
For each of the 30 stocks and the S&P 100, the table reports the results of a time-series regression: SLOPEt = +SKEWt+
KURTt+ SLOPEt −1+ t, where SLOPE(t) is the (weekly) slope of the smile (i.e., the previously computed t in
Table 3). SKEW(t) and KURT(t) are the risk-neutral skew and kurtosis for each of the 260 weeks in the sample period, January
1, 1991, to December 31, 1995. We include SLOPE(t −1) to correct for the autocorrelation of the dependent variable. The
method of estimation is OLS. The t-statistics are computed using the Newey–West (with a lag length of 8 weeks) methodology
that corrects for heteroscedasticity and serial correlation. Standard errors with lag length up to 20 are virtually similar. R2 is the
coefﬁcient of determination (in %). The reported 21 is the likelihood ratio test statistic for the null hypothesis that  = 0.
The corresponding p value is presented under the column “p value.” Only the results using short-term smiles are shown here.
a  of 2.44, in contrast to a range of 0.35 to 1.42 for the individual stocks.
The kurtosis coefﬁcient, , is typically small and positive, with 21 signiﬁcant
t-statistics. As in the case of the cross-sectional regressions, an increase in
risk-neutral kurtosis ﬂattens the smile in the time series as well. Overall, all
regressions appear to have a reasonable ﬁt. The serial correlation coefﬁcient,
, is positive and statistically signiﬁcant (all names and the OEX).
Two additional tests are performed to better appreciate the role of riskneutral skew and kurtosis. First, we perform the restricted regressions and
examine the ﬁt of each model (see panel B of Table 5). For the vast majority
of the stocks, risk-neutral skewness tracks the dynamic movements in the
slope of the smile fairly well (on average, the R2 is 55.40%). When kurtosis
128

is included by itself in Equation (34), there is some deterioration in model
ﬁt (on average, the R2 is 36.57%). While not shown in a table, the key
conclusions are unchanged with medium-term options. Therefore, as hypothesized, the tail asymmetry and the tail size of the risk-neutral distribution are
reﬂected in the asymmetry of the implied volatility curves.
Second, returning to panel A of Table 5, we also present the likelihood
ratio test statistic for the exclusion restriction that  = 0. As is standard
[Hamilton (1994)], this statistic is distributed 2(1). From the last two columns of panel A of Table 5, we can observe that most of the chi-square
statistics are large in magnitude. In fact, 23 of the p values are lower than
.05 and only 6 p values exceed .10. Based on this test, we can conclude that,
even in the presence of negative skew, risk-neutral kurtosis is important in
explaining dynamic movements in the slope of the smile. The marginal effect
of omitting risk-neutral kurtosis is strongest for the market index.
One concern with the regression results that we just presented is that
the slope of the smile as well as the risk-neutral moments are based on
the same set of options. To verify our results, we perform integrity checks
from two angles. First, consistent with the term structure of risk-neutral
skews, we regress the medium-term slope of the smile on short-term skewness: SLOPEmedt = ˆ+ ˆSKEWsht+ ˆ SLOPEmedt−1+ t, and, second, we regress the medium-term slope on lagged medium-term skewness:
SLOPEmedt = ˜+ ˜SKEWmedt −1+ ˜ SLOPEmedt −1+ t. For each
regression, the slope and the risk-neutral skew are now estimated from a
collection of option prices with no overlap. If the results of Table 5 are
not spurious, then using either the lagged medium-term skew or the shortterm skew as an instrumental variable for the medium-term skew should give
qualitatively similar (albeit weaker) results. In the ﬁrst candidate speciﬁcation, the index and 22 of the 30 stocks show signiﬁcant positive coefﬁcients.
For the second speciﬁcation, all 30 stocks and the index show signiﬁcant
positive coefﬁcients, with comparable goodness-of-ﬁt R2 statistics. Both sets
of regressions indicate that increasing the absolute magnitude of risk-neutral
skewness makes puts more expensive relative to calls.
If there are strong cross-sectional comovements in the estimated slope of
the smile and the risk-neutral moments, then a multivariate version of Equation (34) may be more informative. Therefore, as an additional check, we
also estimate a multivariate multiple regression across 31 individual names.
This seemingly unrelated regression (SUR) equation system not only allows
regression disturbances to be correlated, but also permits a joint test for
n = 0 for n = 1   31. While not shown, the results of the SUR are
similar to those reported in Table 5. For instance, all the estimated  are
positive and signiﬁcant, while only 21 of the 31 estimated  are signiﬁcant.
Moreover, a (multivariate) likelihood ratio test that  ≡0 is rejected with a
p value < 001 ( 231 = 239 11.
129

Equation (34) and Equation (13), which relate risk-neutral index skews
to physical index higher moments via risk aversion, are part of the same
underlying economic equilibrium, and may be combined. In the one-factor
generating structure, one may view the implied volatility slope as reﬂecting
risk-neutral index skews, with the idiosyncratic component providing a perturbation. On the other hand, one can think of individual risk-neutral skew
and kurtosis as noisy proxies for the respective index moments. Following
the derivation of Theorem 2, one may relate the risk-neutral index kurtosis
to risk aversion and the physical moments by
KURTm ≈KURTm −2 KURTm +2SKEWm +PKEWmSTDm
(35)
where PKEW is the ﬁfth (physical) moment normalized by the variance
raised to the power 5/2; other physical moments are as previously deﬁned.
We thereby observe that individual-name implied volatility curves are related,
in a one-factor setting, to normalized physical moments up to order ﬁve. As
already stated, if risk aversion is strong and there is considerable excess kurtosis, it leads to strong negative risk-neutral index skew. Consistent with this
notion, as corroborated in Tables 4 and 5, risk-neutral skews account, to a
ﬁrst order, for the observed steepness of the implied volatility curves. Conditional on negative risk-neutral skewness, the effect of risk-neutral kurtosis
is of second order, as reﬂected in the relative small magnitudes of .
If risk-neutral skewness is not controlled, then risk-neutral kurtosis proxies
for the fundamental effect of risk-neutral skewness. The ﬁndings in Tables 4
and Table 5 remain broadly consistent with the viewpoint that the primary
action on the structure of option prices is aversion to market risk and the
existence of fat-tailed physical distributions. It follows then that to understand
the relative structure of individual equity options and the market index, one
must equivalently characterize their relative risk-neutral skews.
4.4 Skewness patterns for individual stocks
Our goal here is to describe the empirical properties of the risk-neutral
moments, and present the relationship that exists between the skew of the
individual equities and the stock market index. Let us start with the average
short-term skew for individual stocks and the OEX (shown in Table 6). In
comparison with its 30 stock components, the OEX is substantially more
negatively skewed, with an average skewness of −1 09 (over the entire
1991–1995 sample). In contrast, the skewness of GE, HWP, and XRX are
−0 53−0 17, and −0 33, respectively. For each of the stocks, the difference
between individual and OEX skews is statistically signiﬁcant, with a minimum t-statistic of 5.72 (not reported). We also incorporate estimates for (i)
the fraction of weeks in which the individual skew is higher than the index
skew (i.e., the occurrence frequency for the event SKEWn > SKEWm), and
(ii) the fraction of weeks in which the individual/index skews are negative
130

Table 6
The character of individual and index risk-neutral skewness
Sign of
Univariate regression
skewness
SKEWnt = 0 +1SKEWmt+ t
Price of moments
SKEWn >
SKEWn
√
R2
0
t0
1
t1
V
SKEW
KURT
< 0
Ticker
SKEWm
−0 21
0 11
1 43
0 29
4 46
7 2
7 98
1. AIG
68
96
2.20
−0 54
−3 77
−0 65
0 11
0 85
0 3
6 59
2. AIT
83
77
4.18
−0 38
0 35
1 79
0 67
3 92
5 9
6 59
3. AN
69
84
5.00
−0 08
−0 50
−0 12
0 04
0 28
0 0
10 93
4. AXP
48
90
4.51
−0 14
0 17
1 65
0 29
3 21
3 8
9 16
5. BA
58
94
4.54
−0 44
0 13
1 13
0 52
5 29
9 9
10 48
6. BAC
77
88
3.99
−0 89
−4 86
−0 21
−1 28
−0 68
0 7
7 09
7. BEL
79
72
5.62
−0 46
0 22
1 73
0 63
5 68
11 1
7 42
8. BMY
74
86
4.46
−0 01
−0 06
−0 28
0 25
2 98
3 3
12 71
9. CCI
69
92
3.88
−0 00
−0 04
−0 26
0 24
2 77
2 9
8 39
10. DD
69
92
3.87
−0 09
−1 28
−0 13
0 04
0 61
0 2
10 17
11. DIS
62
98
3.18
−0 13
0 05
0 39
0 16
1 55
0 9
11 02
12. F
58
93
3.98
−0 08
−0 97
−0 53
0 41
5 37
10 0
7 60
13. GE
88
87
3.90
−0 01
−0 15
−0 09
0 07
1 00
0 4
11 07
14. GM
56
95
3.53
−0 17
0 18
2 48
0 32
5 06
9 0
11 85
15. HWP
61
96
2.33
0 27
3 92
0 20
3 47
4 5
10 49
0 04
16. IBM
43
98
2.89
−0 30
0 28
2 36
0 52
5 20
9 6
8 49
17. JNJ
65
91
4.12
−0 21
−1 93
−0 56
0 32
3 44
4 4
8 27
18. KO
87
82
4.48
−0 34
−2 22
−0 41
0 07
0 51
0 1
8 51
19. MCD
71
85
5.18
−0 09
−0 81
−0 15
0 05
0 48
0 1
12 18
20. MCQ
53
91
3.78
−0 36
0 03
0 40
0 36
5 55
10 7
7 27
21. MMM
85
95
3.28
−0 15
−1 43
−0 39
0 22
2 54
2 4
6 47
22. MOB
77
88
3.47
−0 43
−2 65
−0 24
−1 76
−0 16
1 2
9 38
23. MRK
51
86
4.41
−0 04
0 16
1 07
0 18
1 40
0 8
10 44
24. NT
37
93
4.03
−0 04
−0 26
−0 39
0 33
2 78
2 9
8 67
25. PEP
72
87
5.87
−0 07
0 13
1 11
0 19
1 82
1 3
8 74
26. SLB
50
94
3.09
−0 76
−4 75
−0 14
−1 01
−0 61
0 4
7 28
27. T
78
76
6.10
−0 38
0 20
1 53
0 53
4 78
8 2
10 34
28. WMT
70
88
4.18
−0 25
−1 42
−0 58
0 31
2 07
1 6
5 93
29. XON
83
82
5.49
−0 09
−1 19
−0 33
0 22
3 40
4 3
9 27
30. XRX
77
93
2.50
−1 09
5 56
31. OEX
100
3.99
For each of the 30 stocks and the S&P 100, the table reports three sets of numbers relating to the weekly risk-neutral moments
estimated. In the ﬁrst two columns, we report (i) the percentage of observations for which SKEWn < 0, and (ii) the percentage
of observations for which the risk-neutral skewness of the stock, SKEWn, is more than the risk-neutral skewness of the market,
SKEWm (i.e., less negative than the risk-neutral index skewness). The next ﬁve columns present the results of an OLS regression:
SKEWnt = 0 +1SKEWmt+ t, where 0, 1 are the intercept and sensitivity coefﬁcients, respectively; t0t1
are the t-statistics, and R2 is the coefﬁcient of determination (in percent). The last three columns display the average estimate
of the risk-neutral volatility, skew, and kurtosis (with one exception, all moments are statistically signiﬁcant and omitted). The
volatility is the square root of the variance contract, reported in percent. All moments used are of short-term maturity. The
sample period is January 1, 1991, to December 31, 1995.
(that is, SKEWn < 0). Together these statistics again highlight the dichotomy
between the market index and the individual stocks. Unlike any individual stock return distribution, the OEX risk-neutral distribution is persistently
skewed to the left in each of the 260 weeks in the sample. Finally, on average across the 30 stocks, the individual skew is less negative than the market
89% of the time. Only occasionally do individual stocks have skews that are
more negative than the OEX (13% and 2% for GE and IBM, respectively).
How do we interpret the fact that individual skews are almost always less
negative than that of the market index? In light of the underlying theory,
there are at least three explanations. First, if there is indeed a market component in the individual return, then our characterizations indicate that the
131

idiosyncratic return component is, most likely, not heavily negatively skewed.
Second, if a market component is nonexistent, then idiosyncratic skewness
decides the skewness of the individual stock. In this hypothetical case, the
small negative skew of the individual stock may simply reﬂect that of the
idiosyncratic return component. However, amongst our sample, all stocks
have a sizable market component to its return—in a (weekly) regression of
stock return on the market return, each stock has a signiﬁcant bt. Thus
the less negative skew of the individual stock appears to be a symptom of an
unsystematic return component that is either positive, symmetric, or mildly
negatively skewed. Third, the leverage explanation implies that at least some
stocks are more negatively skewed than the market index, which we do not
empirically detect. While the feedback between return and volatility is sufﬁcient to produce negative individual skews, it is inadequate for creating an
index distribution that is overly left skewed.
To isolate the contribution of market skews for individual return skews,
consider the regression
SKEWnt = 0 +1 SKEWmt+ nt
(36)
In essence this regression follows from the skew laws in Equation (21) of
Theorem 3 and assesses time variations in the individual risk-neutral skew
via time variations in the risk-neutral market skew (the idiosyncratic skew is
unidentiﬁed). The regression will be well speciﬁed, for instance, if the relation between Vmt and Vnt (or equivalently Vt) is stable, so that
the coefﬁcient 1 can be assumed constant over this sample period. Again
exploiting short-term options, Table 6 reports the results of this regression.
The following observations can be made. First, each 1 that is signiﬁcantly
greater than zero at the 5% level is also signiﬁcantly less than 1. This is
broadly in line with our theory that the individual risk-neutral skew is a
weighted combination of the risk-neutral market skew and the idiosyncratic
skew, with weights that are bounded between 0 and 1. However, the coefﬁcient 1 should not be interpreted as the coefﬁcient of coskewness [which
is properly deﬁned in Harvey and Siddique (2000)]. The latter captures the
covariation between the ﬁrst moment in the individual names and the second
moment of the market, as per Equation (26). Equation (36), on the other
hand, assesses the covariation between third moments.
Second, about one-third of the stocks do not show a signiﬁcant dynamic
relation between the market and the individual skew. Even for the stocks
that have a meaningful relation, the R2 of the regression is small, with only
three stocks having R2 greater than 10%. One possible interpretation of these
results is that the time-variation in the idiosyncratic skew is more important
than that of the market skew in determining the risk-neutral individual skew.
Alternatively, the idiosyncratic skew may be directionally offsetting the negative market skew. Finally, the results for medium-term options are comparable
132

(both quantitatively and quantitatively), with 21 of the 22 signiﬁcant coefﬁcients being positive and less than 1 (not reported here).4
The results of this subsection point to substantial differences in the riskneutral distributions of individual stocks and the stock market index. While
the volatility (see the price of volatility contracts in Table 6) of individual
return distributions is greater than that of the index, the individual stock riskneutral skew is less negative than the market skew. The price of individual
kurtosis can be higher or lower than the market (the t-statistics are omitted,
as all moments except one are statistically signiﬁcant).
That the ﬁrst two higher moments of the risk-neutral distribution of individual stocks can be so radically different from the index distribution has
important implications. In particular, it indicates that we can make limited
inference about the risk-neutral distribution of the individual stock by tracking only the risk-neutral distribution of the market. Although the single-factor
model postulated in Equation (20) is consistent with our ﬁndings, the nature
of individual multivariate risk-neutral return distributions remains unresolved.
Speciﬁcally, under what economic conditions can each marginal return distribution possess a low negative skew and yet a portfolio represented by the
market index be heavily left skewed?
4.5 Determinants of risk-neutral index skews
In this ﬁnal subsection, we test the market skew equation [Equation (13)]
using Hansen’s (1982) generalized method of moments (GMM). Fix the horizon  and deﬁne the disturbance, ˆ , from Theorem 2 as
ˆ t +1 ≡SKEWmt +1−SKEWmt +1
+ KURTmt +1−3STDmt +1
(37)
where  is the risk aversion parameter and STDmt +1, SKEWmt +1, and
KURTmt+1 are the higher-order t+1-conditional moments of the physical
index distribution. Equation (37) can be potentially viewed as a model for
risk-neutral skews when ˆ t + 1 is independent of the physical moments.
Allowing for possible dependencies, we rely merely on the orthogonality
of ˆ t + 1 with time t-determined instrumental variables, t. Under the
null hypothesis of a power utility stochastic discount factor [and those in the
class of Equation (15)] and identifying orthogonality conditions, we must
have E ˆ t +1⊗t = 0.
4 So far we have not discussed the preciseness of our weekly estimates for risk-neutral return skew and kurtosis.
How much of the cubic and quartic contract price comes from outside of the available strike price range (say,
±20% range)? To see whether this area is negligible in general, let us compute the fourth moment in a (riskneutral) Gaussian setting with standard deviation h (keeping r = 0). The reader can verify that the area in the
 
0 20 R4 exp−R2/2h2dR, is relatively small (as a fraction of the total) for plausible values of h.
1
tail,
√
h
2!
Thus despite the absence of a continuum of strikes [and our discretizations in Equations (31) and (32)], the
results with ﬁnite strikes appear reliable on a theoretical basis. In any case, the commonality of our ﬁndings
across the OEX (for which we have abundant strikes) and the individual stocks suggest that even a few strikes
are reliable for mimicking skew and kurtosis. Our conclusions are, mostly, robust.
133

As our intent is to estimate a single coefﬁcient, , and test the restrictions
embedded within Equation (37), the GMM appears to be an attractive estimation method for several reasons. First, unlike return volatility, the estimates
of physical skews and kurtosis require a fairly long time series and will be
measured with error [Merton (1980) and Harvey and Siddique (2000)]. Therefore the market skew formulation of Equation (37) is susceptible to an errors
in variables problem. Second, the return standard deviation and the excess
kurtosis enter nonlinearly in Equation (37) and may be correlated with ˆ .
Finally, the minimized GMM criterion function (multiplied by T ), T , offers
a convenient approach to assess misspeciﬁcations in Equation (37). The T
statistic is chi-square distributed with L −1 degrees of freedom (given L
instruments).
Before turning to a discussion of GMM estimation results reported in
panels A and B of Table 7, some clariﬁcations are in order. First, Theorem 2
applies for a particular . We therefore generate a nonoverlapping series of
risk-neutral index skews from options with maturities of 58 and 86 days.
Second, estimates of physical skews and kurtosis are sensitive to the choice
Table 7
GMM tests of the market skew equation
E ˆ t +1⊗t = 0
E ˜ t +1⊗t = 0
Size
T
t
T
p
0
t(0)
p

t()
(days)
df
Panel A: Risk-neutral OEX skews from 86-day options
2 26
7 60
12 01
SET 1
350
1
2.11
0.005
4.46
7.33
.006
2 08
4 69
11 20
400
1
2.32
0.030
2.93
4.87
.027
1 76
3 77
9 82
450
1
2.48
0.052
3.09
3.99
.045
2 29
10 93
15 99
SET 2
350
2
1.97
0.004
2.66
8.86
.011
2 25
6 96
12 08
400
2
2.22
0.030
2.85
6.52
.038
1 99
4 26
10 85
450
2
2.40
0.118
3.01
4.52
.104
11 39
7 01
22 32
SET 3
350
3
2.67
0.071
2.78
7.44
.059
1 76
11 15
20 23
400
3
2.16
0.010
2.95
6.17
.103
1 89
6 70
11 52
450
3
2.35
0.082
2.97
5.59
.133
Panel B: Risk-neutral OEX skews from 58-day options
2 09
13 97
11 95
SET 1
350
1
2.64
0.000
3.63
8.90
.000
1 91
7 81
9 35
400
1
2.80
0.005
3.64
6.66
.009
1 36
8 90
7 25
450
1
3.05
0.052
3.99
7.77
.005
3 21
14 63
16 78
SET 2
350
2
2.60
0.000
3.76
7.53
.023
2 12
14 23
12 29
400
2
2.67
0.000
3.67
8.56
.013
1 44
11 20
8 01
450
2
2.93
0.003
3.85
9.04
.010
5 98
9 48
20 87
SET 3
350
3
2.66
0.023
3.90
5.66
.129
2 60
16 95
16 51
400
3
2.60
0.000
3.77
7.65
.053
1 59
11 40
8 84
450
3
2.89
0.009
3.78
8.75
.032
Consider the restrictions imposed by the power utility pricing kernel: ˆ t + 1 ≡SKEWmt + 1 −SKEWmt + 1 +
KURTmt +1−3STDmt +1, which is another way to express Equation (13) of Theorem 2. The risk aversion parameter,
, is estimated by generalized method of moments (GMM). In panels A and B, we report the GMM results when the riskneutral market skew, SKEWm, is recovered from 86-day and 58-day options, respectively. Over the entire sample of January
1988 through December 1995 there are thus 32 (48) nonoverlapping observations for 86- (58-) day options. We build the time
series of higher-order physical return moments, STD, SKEW, and KURT, from daily returns on the OEX. Thus a sample size
(denoted Size) of 350 days means that we go backward 350 days to construct the moments. For consistency, each variable has
been annualized. The degrees of freedom, df, are the number of instruments, t, minus one. In SET 1, the instrumental variables are a constant plus SKEWmt. Likewise, SET 2 (SET 3), contains SET 1 (SET 2) plus SKEWmt−1 (SKEWmt−2).
For robustness, other information sets were tried; they yielded similar implications. The minimized value (multiplied by T ) of
the GMM criterion function, T , is chi-square distributed with df. The impact of physical skews on risk-neutral skews is studied
by considering the ad hoc speciﬁcation ˜ t +1 ≡SKEWmt +1−0SKEWmt +1.
134

of histories. We experiment with moments estimated from OEX returns using
sample sizes of 350 days, 400 days, and 450 days (in the column marked
Size). All inputs into Equation (37) are annualized for consistency. Over the
1988–1995 sample period (we have added three more years) there are thus
48 (32) matched observations for 58-day (86-day) index skews. Moreover,
as theory offers little direction on the choice of instrumental variables to be
used in the GMM estimation, three different sets were tried. SET 1 contains
a constant and SKEWm lagged once; SET 2 (SET 3) contains a constant
and two (three) lags of SKEWm. Each information set is picked to keep the
number of orthogonality conditions manageable relative to the sample size.
Proceed now to the estimation results for 86-day skews (in panel A). Supportive of Theorem 2 predictions, the estimate of  are reasonable and in the
range 1.76 and 2.26 for SET 1, in the range 1.99 to 2.29 for SET 2, and in the
range 1.76 to 11.39 for SET 3. Each estimate of  is statistically signiﬁcant.
With sample size set to 450, the overidentifying restrictions imposed by the
model are not rejected (as reﬂected in p values higher than 5%). Otherwise
the model may be incomplete in that it has omitted higher-order terms in the
ﬁrst-order approximation. To appreciate the point that employing a longer
sample size will possibly improve the quality of the estimation, notice that
with sample size set to 450 days, the daily (sample average) STDm = 16 32%,
SKEWm = −1 26, and KURTm = 19 12. In contrast, for sample size set to
300 days, STDm = 17 76%, SKEWm = −0 96, and KURTm = 14 08. With
shorter sample size, the skew and kurtosis may be underestimated.
If we choose  = 0 in Equation (37), it trivially imposes the constraint
0 = 1 in ˜ t + 1 ≡SKEWmt + 1 −0 SKEWmt + 1. Although ad hoc,
this alternative speciﬁcation helps evaluate the relation between the physical
and the risk-neutral skews. As our GMM results demonstrate, the estimate
of 0 is always more than 9.82 and signiﬁcant. In other words, the statistical
skews are too small and must be multiplied by a factor of at least 10 to be
consistent with risk-neutral index skews. This conﬁrms our earlier claim that
the risk-neutral skew magnitudes are not sustainable without risk aversion
and fat-tailed physical index distributions.
The inferences that we have drawn are not too different with 58-day riskneutral skews. Future work should extend the estimation methodology to
include state-dependent stochastic discount factors. As risk aversion may be
stochastically time varying in that context, it may impose more stringent
testable restrictions on the dynamics of risk-neutral index skews.
5. Concluding Remarks and Possible Extensions
It has been noted that risk-neutral moments inﬂuence the relative pricing of
an option of a particular strike to another. But basic questions like how to
quantify the relationship between the risk-neutral density and the moments of
135

the physical return distribution have not been addressed. The central contributions of this article can be summarized as follows. First, we theoretically reconcile when negative risk-neutral skews are feasible from symmetric physical
distributions. For a large class of utility functions, we show that risk-neutral
index skews are a consequence of risk aversion and fat-tailed physical distributions. Next, we formalize the skew laws of individual equities, and propose
a framework to recover risk-neutral moments from option prices. It is shown
that the individual risk-neutral stock distributions are qualitatively distinct
from the index counterpart.
Empirically we demonstrate the differential pricing of individual equity
options. The slope of the individual smiles is ﬂatter than that of the market index. This ﬁnding is consistent with the idiosyncratic component of the
return being less negatively skewed (risk neutrally) than that market. Furthermore, a more negative risk-neutral skew is related to a steeper negative slope
of the implied volatility curve. In large part, the empirical analysis suggests
that when negative risk-neutral skew is internalized, a higher risk-neutral
kurtosis produces a ﬂatter volatility smile.
Our framework allows us to understand and reconcile two stylized facts
of economic signiﬁcance: that the index option smile is highly skewed,
and the differential pricing of individual equity options versus the market
index. Overall our ﬁndings remain consistent with the belief that the primary
action on the structure of equity options is fat-tailed physical distributions
and risk aversion. The econometric tests provide support for this economic
argument.
The verdict is still out on a number of related research questions. First,
future research should examine the nature of risk-neutral skews from other
models. One possibility is to study the interaction of biased beliefs and the
pricing of puts and calls [David and Veronesi (1999)], suggestive of generalizations to the marginal-utility tilting of the physical density studied in this
article. Second, spanning the characteristic function with the option basis and
then inferring the risk-neutral density is a natural extension to our work on
moments. At an abstract level, our approach of directly pricing risk-neutral
moments from option portfolios can serve as a useful check in evaluating
parametric methods for jointly estimating the physical and the risk-neutral
densities [Ferson, Heuson, and Su (1999), Chernov and Ghysels (2000), and
Harvey and Siddique (2000)]. Finally, a large body of literature [e.g., Canina
and Figlewski (1993), Lamoureux and Lastrapes (1993), Fleming (1998), and
Christensen and Prabhala (1998)] has attempted to determine whether ATM
implied volatilities are unbiased predictors of future return volatility. Since
we have designed option positioning to infer volatility, forecasting exercises
can be performed without taking any stand on the parametric option model
or on the form of the volatility risk premium. This study has provided the
incentive to expand research on individual stock options.
136

Appendix
Setting S ≡St in Equation (2) and performing standard differentiation
Proof of Theorem 1.
steps, we can observe that

21−lnK/St

volatility contract
K2
6lnK/St−3lnK/St2
HSSK =
(38)
cubic contract

K2
12lnSt/K2 +4lnSt/K3
quartic contract
K2
Equations (7)–(9) of Theorem 1 follow from substituting Equation (38) into Equation (2). For the

 e−rSqSdS = St (by the martingale property). Therefore
mean stock return, we note that
St +

er = ∗
= ∗
t expRt
t
St
t Rt+ 1
t Rt2+ 1
t Rt3+ 1
= 1+∗
2 ∗
6∗
24 ∗
t Rt4
since expR = 1+R+R2/2+R3/6+R4/24+oR4. Reorganizing,
St +

= er −1−er
2 V t−er
6 Wt−er
t ≡∗
24 Xt
t ln
(39)
St
The ﬁnal pricing formulas for risk-neutral skewness and kurtosis in Equations (5) and (6) now
■
follow by using Equation (39), and expanding on their deﬁnitions.
Proof of Equations (11) and (12).
Strictly, the Radon–Nikodym theorem is a statement about
two equivalent probability measures, Q and P, on some measurable space (recall we have
reserved P for the put price). In general, we have measures on a sigma ﬁeld of subsets of 
and the Radon–Nikodym theorem allows us to assert
Qd" = "Pd"
(40)
where " is an 1 measurable function with respect to the underlying sigma ﬁeld [Halmos
(1974)]. For any (Borel measurable) test function f S, the density of the stock price (if it


f SPd". Analogously the risk-neutral
f SpSdS =
exists) is deﬁned by the condition


f S "Pd". Armed with this result, deﬁne the condif SqSdS =
density satisﬁes
tional expectation of , given the ﬁltration generated by the stock price as E  S by the
condition that (for all test functions f Sm)



f Sm "Pd" =
f SmE  SmPd" =
f SmE  Sm pSmdSm
(41)

f Sm ×
Applying this property of conditional expectations to the above equation, we get

qSmdSm =
f SmE  Sm pSmdSm. Thus we may deduce qSm = E  Sm ×pSm. As
is traditional, one conjectures a form for the unnormalized Radon–Nikodym derivative, and in
this case
E  Sm ×pSm

qSm =

(42)
E Sm ×pSmdSm
where can be interpreted as a general unnormalized change-of-measure pricing kernel. Under
the maintained hypothesis of a power utility function in wealth, we may specialize the stochastic
137

discount factor to E  Sm = S−
m = e− lnSm. Then dividing the denominator and numerator
by S−
m t and making a change of variable, we derive Equation (11). For recent applications of
Equation (11), check Amin and Ng (1993), Chernov and Ghysels (2000), Harrison and Kreps
■
(1979), Stutzer (1996), and Jackwerth (2000).
Proof of Theorem 2: Exponential Tilting of the Physical Measure can Introduce Skew in the
Risk-Neutral Measure.
We wish to relate the skewness of qR to that of pR (suppressing
the subscript on Rm). Without loss of generality, we may suppose that the parent density, pR,
has been mean shifted and has zero mean (i.e., suppose ¯#1 = 0). Let the ﬁrst three successive
higher moments of pR be
 
− R2pRdR
¯#2 ≡
(43)
 
− R3pRdR
¯#3 ≡
(44)
 
− R4pRdR
¯#4 ≡
(45)
As is standard, deﬁne the moment-generating function, 
$, of pR, for any real number $,
by
 

− e$RpRdR
$ ≡
= 1+ $2
2 ¯#2 + $3
6 ¯#3 + $4
24 ¯#4 +o$4
(46)
and can thus be expressed in terms of its uncentered moments.
Now consider the moment-generating function, $, of qR. From the relation qR =
e−R×pR
e−R×pRdR , it holds that

 
 
− e$Re−RpRdR
− e$RqRdR =
 
$ ≡
(47)
− e−RpRdR

$−
=
−
(48)

Hence $ can be recovered from the (parent) moment-generating function of pR.
Using the properties of moment-generating functions, up to a ﬁrst-order effect of , we see
that the moments of qR satisfy a recursive relationship. Thus we have
 
#1 ≡
− RqRdR ≈¯#1 − ¯#2
(49)
 
− R2qRdR ≈¯#2 − ¯#3
#2 ≡
(50)
 
− R3qRdR ≈¯#3 − ¯#4
#3 ≡
(51)
and 
− = 1+o. Now we are ready to compute the risk-neutral index skew, which is,
 
−R−#13qRdR
 
SKEWmt ≡
−R−#12qRdR3/2 

= ¯#3 − ¯#4 −3 ¯#2
2
+o
(52)
¯#3/2
2
Simplifying the resulting expression, and noting KURT ×#2
2 = #4, the theorem is proved.
138

 
For our generalization to marginal utilities in the class of U ′Rm =
0 e−zRmdz, we
 
 
can note that up to a ﬁrst-order in  that #1 ≈¯#1 − 
0 zdz ¯#2, #2 ≈¯#2 − 
0 zdz ¯#3,
 
and #3 ≈¯#3 − 
0 zdz ¯#4. From the same argument as in the derivation of Equation (52),
 
we have SKEWm ≈SKEWm − 
0 zdz  KURTm −3STDm.
■
Proof of Parts (a) and (b) of Theorem 3.
Recall that the stock return follows a single-index
return-generating process. Suppressing time arguments, write Rt as R and the risk-neutral
density of stock return (idiosyncratic risk) as qR (q. Impose the square-integrability conditions Vt ≡e−r 
2qd <  and Vmt ≡e−r 
R2
mqRmdRm < , which bound
the price of idiosyncratic volatility and index volatility. The risk-neutral skewness of the index
must be
 
−Rm − m3 qRmdRm
SKEWmt ≡
3/2
(53)
 
−Rm − m2 qRmdRm
Exploiting the return-generating process in Equation (20), and using the independence of  and
Rm,
 
 
−Rm − m3 qRmdRm +
b3
− 3
n qd
n
SKEWnt =
(54)

3/2
 
 
− Rm − m2qRmdRm +
b2
nt
− 2
n qd
since the coskews, E nRm − m2 and E 2
nRm − m , vanish. Rearranging Equation (54),
we obtain (for n = 1   N)
∗
t nt3
SKEWnt = ntSKEWmt+nt
(55)
∗
t nt2 3/2
with nt and nt, as displayed in Equations (22) and (23) of the text. If the density
q is symmetric around the origin, ∗
t t3 = 0. Inserting this restriction into Equation (55)
proves this element of the theorem.
This procedure can be extended to the two-factor context: Rnt = ant+bntRmt
 + cntF t + nt, which decomposes the systematic part of the individual return
into two forces. Repeating the above steps, we derive Equation (25) with
−3/2
ntVF t−e−r 2
1+ c2
F t+Vt
nt ≡

(56)
ntVmt−e−r 2
b2
mt
−3/2
ntVmt−e−r 2
1+ b2
mt+Vt

nt ≡

and
(57)
ntVF t−e−r 2
c2
F t
−3/2
ntVmt−e−r 2
ntVF t−e−r 2
1+ b2
mt+c2
F t
nt≡

Vt
(58)
■
which is the ﬁnal step of the proof.
Proof that Leverage Implies Index Skew is Less Negative than Some Individual Skews.
Before
presenting the proof, we need a result on the moment-generating function of vector standard
normal variates and its derivatives. That is, ∗ expℓ1 &1 +ℓ2 &2 = exp0 5ℓ2
1 +0 5ℓ2
2 +'ℓ1ℓ2,
which is exponential afﬁne in the variance-covariance matrix.
139

To stay focused on this counterexample, we adopt a two-period and two-stock setting. Fix
N = 2 and hypothesize the two-period return evolution (with (n > 0)
Rn1 = r +&n1
&n ∼ 01
(59)
Rn2 = r +&n2+&n1)n2
)n ∼ 01
(60)
&n1 = (n exp−&n1
(61)
for n = 12. Equation (61) goes to the heart of the leverage argument: the volatility of the secondperiod return increases (decreases) as lagged return innovations goes down (up) [see Cox and
Ross (1976) and Beckers (1980)]. Let &nt be independent of )n2, ' ≡covt &1t&2t,
and * ≡covt )1t)2t. Note that second-period volatilities are correlated across stocks and
the individual return process is autocorrelated. This model yields
6(2
n exp2
SKEWn2 = −
n = 12
(62)
1+(2
n exp23/2
Therefore leverage produces negative skewness in individual names. Now cross-sectionally
aggregate the second-period return equally to get the return on the market (basket): Rm2 =
R12+R22
. With some algebraic manipulation we arrive at the leverage implied index skew:
2
2
SKEWm2 = +0 +
+n ×SKEWn2
(63)
n=1
where
6* 1+'(1 (2 exp1+'
+0 ≡−
2 exp2+2* (1 (2 exp1+'
(64)
21+'+(2
1 exp2+(2
0 501+'1+(n exp2
+n ≡
n = 12
2 exp2+2* (1 (2 exp1+' < 1
(65)
21+'+(2
1 exp2+(2
Thus the market skew is just a convex combination of the individual skews and imposes the
restriction that at least one of the individual skews be more negative than the market skew. To
see this, set ' = 0 and * = 0. In this special case, +0 is identically zero. Now set * > 0 and
reexamine Equation (63). In sum, while leverage generates negative skew, its implications for
index skewness are diametrically opposite to those originating from risk aversion and fat-tailed
■
physical distributions.
Proof of Equation (29) in Theorem 4.
Although the proof is available in Backus et al. (1997),
we sketch the basic steps to make our analysis self-contained. To justify the functional form of
Equation (29), standardize stock returns so that they have mean zero and unit variance. Accord-

ingly, let x ≡Rt−
, where, as before, ≡∗
t Rt, and ¯ ≡
∗
t Rt−∗
t Rt 2.
¯
Now return to Equation (28) and redeﬁne the exercise region as  ≡ lnK−lnSt−
> x . As a
¯
consequence

 e−r K −Stexpx ¯ +  qxdx = Ke−r 1− d2−St1− d1
(66)
From probability theory, a robust class of density functions can be approximated in terms of its
moments and the Gaussian density [see Johnson, Kotz, and Balakrishnan (1994, p. 25)], as in
-3,x
-4,x
qx ≈,x−1
×SKEWt+ 1
× KURTt−3
(67)
3!
4!
-x3
-x4
140

2! e−x2/2 denotes the standard normal density function. Thus the left-hand side
1
where ,x =
√
of Equation (66) becomes

 e−r K −Stexpx ¯ +  qxdx

 e−r K −Stexpx ¯ +  ,xdx
=

 e−r K −Stexpx ¯ +  -3,x
−1
3! SKEWt×
dx
-x3

 e−r K −Stexpx ¯ +  -4,x
+ 1
4!  KURTt−3×
dx
(68)
-x4
which gives the theoretical put price linearly in terms of the Black–Scholes price (evaluated at
the true volatility), the risk-neutral skewness, and (excess) risk-neutral kurtosis.
Two remaining steps need some explanation. First, take a Taylor series of  d1 around ¯,
and use the Leibnitz differentiation rule to simplify the expression

Ke−r 1− d2−St1− d1−
 e−r K −Stexpx ¯ +  ,xdx
(69)
Second, -3,x
and -4,x
can be directly computed by differentiating the normal density function.
-x3
-x4
That is,
-3,x
1
3x −x3e−x2/2
=
√
-x3
2!
-4,x
1
3x −6x2 +x4e−x2/2
=
√
-x4
2!
Collecting the remaining terms, and exploiting the moment-generating function of the Gaussian
(i.e., its translates and derivatives), we achieve the desired result in Equation (29). This result
is, however, not observationally equivalent to the counterpart one (i.e., Proposition 2) in Backus
et al. (1997) (it is unnecessary to approximate y, y, and y). As the closed forms for
y, y, and y are not particularly instructive, they are omitted here. This completes the
proof that the structure of option prices, as represented through the Black–Scholes implied
■
volatility curve, is afﬁne in risk-neutral skewness and kurtosis.
References
Ait-Sahalia, Y., and A. Lo, 1998, “Nonparametric Estimation of State-Price Densities Implicit in Financial
Prices,” Journal of Finance, 53, 499–548.
Amin, K., and V. Ng, 1993, “Option Pricing With Systematic Stochastic Volatility,” Journal of Finance, 48,
881–910.
Backus, D., S. Foresi, K. Lai, and L. Wu, 1997, “Accounting for Biases in Black-Scholes,” mimeo, New York
University.
Bakshi, G., C. Cao, and Z. Chen, 1997, “Empirical Performance of Alternative Option Pricing Models,”
Journal of Finance, 52, 2003–2049.
Bakshi, G., and D. Madan, 2000, “Spanning and Derivative Security Valuation,” Journal of Financial Economics, 55, 205–238.
Bates, D., 1991, “The Crash of 87: Was it Expected? The Evidence From Options Markets,” Journal of
Finance, 46, 1009–1044.
141

Bates, D., 2000, “Post-’87 Crash Fears in the S&P 500 Futures Option Market,” Journal of Econometrics,
94, 181–238.
Beckers, S., 1980, “The Constant Elasticity of Variance Model and its Implications for Option Pricing,”
Journal of Finance, 35, 661–673.
Broadie, M., and J. Detemple, 1996, “American Option Valuation: New Bounds, Approximations, and a
Comparison of Existing Models,” Review of Financial Studies, 9, 1211–1250.
Canina, L., and S. Figlewski, 1993, “The Information Content of Implied Volatilities,” Review of Financial
Studies, 6, 659–681.
Carr, P., and D. Madan, 2001, “Optimal Positioning in Derivative Securities,” Quantitative Finance, 1, 19–37.
Chernov, M., and E. Ghysels, 2000, “A Study Towards a Uniﬁed Approach to the Joint Estimation of Objective
and Risk-Neutral Measures for the Purpose of Option Valuation,” Journal of Financial Economics, 56, 407–
458.
Christensen, B., and N. Prabhala, 1998, “The Relation Between Implied and Realized Volatility,” Journal of
Financial Economics, 50, 125–150.
Cox, J., and S. Ross, 1976, “The Valuation of Options for Alternative Stochastic Processes,” Journal of
Financial Economics, 3, 145–166.
David, A., and P. Veronesi, 1999, “Option Prices With Uncertain Fundamentals: Theory and Evidence on the
Dynamics of Implied Volatilities,” mimeo, Federal Reserve Board and the University of Chicago.
Dennis, P., and S. Mayhew, 1999, “Implied Volatility Smiles: Evidence From Options on Individual Securities,”
mimeo, Purdue University and University of Virginia.
Dufﬁe, D., J. Pan, and K. Singleton, 2000, “Transform Analysis and Asset Pricing for Afﬁne Jump-Diffusions,”
Econometrica, 68, 1343–1376.
Dumas, B., J. Fleming, and R. Whaley, 1998, “Implied Volatility Smiles: Empirical Tests,” Journal of Finance,
53, 2059–2106.
Fama, E., and J. McBeth, 1973, “Risk, Return, and Equilibrium: Empirical Tests,” Journal of Political Economy, 81, 607–636.
Ferson, W., A. Heuson, and T. Su, 1999, “How Much Do Expected Stock Returns Vary Over Time? Answers
From the Options Markets,” mimeo, University of Washington and University of Miami.
Fleming, J., 1998, “The Quality of Market Volatility Forecasts Implied by S&P 100 Index Option Prices,”
Journal of Empirical Finance, 5, 317–345.
Halmos, P., 1974, Measure Theory, Springer Verlag, New York.
Hamilton, J., 1994, Time Series Analysis, Princeton University Press, Princeton, New Jersey.
Hansen, L., 1982, “Large Sample Properties of Generalized Method of Moments Estimators,” Econometrica,
50, 1029–1084.
Harrison, M., and D. Kreps, 1979, “Martingales and Arbitrage in Multiperiod Securities Markets,” Journal of
Economic Theory, 20, 381–408.
Harvey, C., and A. Siddique, 1999, “Autoregressive Conditional Skewness,” Journal of Financial and Quantitative Analysis, 34, 465–487.
Harvey, C., and A. Siddique, 2000, “Conditional Skewness in Asset Pricing Tests,” Journal of Finance 55,
1263–1295.
Heynen, R., 1994, “An Empirical Analysis of the Observed Smile Patterns,” Review of Futures Markets, 13(2),
317–353.
Kraus, A., and R. Litzenberger, 1976, “Skewness Preference and the Valuation of Risk Assets,” Journal of
Finance, 31, 1085–1100.
142

Jackwerth, J., 2000, “Recovering Risk Aversion From Options Prices and Realized Returns,” Review of Financial Studies, 13, 433–451.
Johnson, N., S. Kotz, and N. Balakrishnan, 1994, Continuous Univariate Distributions, Vol. 1, Wiley, New
York.
Kahneman, D., and A. Tversky, 1979, “Prospect Theory: An Analysis of Decision Under Risk,” Econometrica,
47, 263–292.
Lamoureux, C., and W. Lastrapes, 1993, “The Information Content of Implied Volatilities,” Review of Financial Studies, 6, 659–681.
Longstaff, F., 1995, “Option Pricing and the Martingale Restriction,” Review of Financial Studies, 8, 1091–
1124.
Madan, D., P. Carr, and E. Chang, 1998, “The Variance Gamma Process and Option Pricing,” European
Journal of Finance, 1, 39–55.
Merton, R., 1976, “Option Pricing When Underlying Stock Returns Are Discontinuous,” Journal of Financial
Economics, 3, 125–144.
Merton, R., 1980, “On Estimating the Expected Return on the Market: An Exploratory Investigation,” Journal
of Financial Economics, 8, 323–361.
Pan, J., 1999, “The Jump-Risk Premia Implicit in Options: Evidence From an Integrated Time-Series Study,”
forthcoming in Journal of Financial Economics.
Revuz, D., and M. Yor, 1991, Continuous Martingales and Brownian Motion, Springer Verlag, New York.
Rubinstein, M., 1973, “The Fundamental Theory of Parameter-Preference Security Valuation,” Journal of
Financial and Quantitative Analysis, 8, 61–69.
Rubinstein, M., 1985, “Nonparametric Tests of Alternative Option Pricing Models Using All Reported Trades
and Quotes on the 30 Most Active CBOE Options Classes From August 23, 1976 Through August 31, 1978,”
Journal of Finance, 40(2), 455–480.
Rubinstein, M., 1994, “Implied Binomial Trees,” Journal of Finance, 49, 771–818.
Stutzer, M., 1996, “A Simple Nonparametric Approach to Derivative Security Valuation,” Journal of Finance,
51, 1633–1652.
Toft, K., and B. Prucyk, 1997, “Options on Leveraged Equity: Theory and Empirical Tests,” Journal of
Finance, 52, 1151–1180.
143

## Tables

### Table 1

*Caption:* Table 1

|  |  |  |  | Number of |  |  |  |  | Midpoint of |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | option quotes |  |  |  |  | option quote |  |
|  |  |  | Short |  | Medium |  |  | Short |  | Medium |
|  |  | OEX |  |  |  |  |  |  |  |  |
| Ticker | Stock | Weight | Call | Put | Call | Put | Call | Put | Call | Put |
| 1. AIG | American Int’l | 2.32 | 3414 | 3884 | 1779 | 2471 | 1.26 | 0.99 | 2.34 | 1.47 |
| 2. AIT | Ameritech | 1.24 | 1902 | 2199 | 1260 | 1570 | 0.62 | 0.58 | 0.96 | 0.89 |
| 3. AN | Amoco | 1.09 | 2112 | 1942 | 1491 | 1435 | 0.49 | 0.48 | 0.79 | 0.76 |
| 4. AXP | American Express | 1.27 | 2325 | 2367 | 1458 | 1696 | 0.41 | 0.40 | 0.66 | 0.60 |
| 5. BA | Boeing Company | 1.27 | 2848 | 2624 | 1927 | 1896 | 0.56 | 0.48 | 0.93 | 0.71 |
| 6. BAC | BankAmerica Corp. | 1.53 | 2640 | 3023 | 1576 | 2007 | 0.62 | 0.53 | 0.99 | 0.77 |
| 7. BEL | Bell Atlantic | 1.90 | 2242 | 2335 | 1409 | 1600 | 0.47 | 0.47 | 0.71 | 0.74 |
| 8. BMY | Bristol-Myers | 2.85 | 3040 | 3311 | 1927 | 2335 | 0.63 | 0.57 | 1.04 | 0.84 |
| 9. CCI | Citicorp | 1.82 | 2545 | 2983 | 1512 | 2007 | 0.47 | 0.41 | 0.79 | 0.57 |
| 10. DD | Du Pont | 2.33 | 2492 | 2639 | 1472 | 1731 | 0.57 | 0.53 | 0.98 | 0.79 |
| 11. DIS | Walt Disney Co. | 2.04 | 4020 | 4677 | 2297 | 2905 | 1.06 | 0.87 | 2.00 | 1.40 |
| 12. F | Ford Motor | 1.66 | 2924 | 3068 | 2062 | 2264 | 0.56 | 0.51 | 0.90 | 0.80 |
| 13. GE | General Electric | 7.29 | 3323 | 4019 | 1857 | 2801 | 0.67 | 0.59 | 1.28 | 0.93 |
| 14. GM | General Motors | 1.36 | 3021 | 3134 | 2107 | 2208 | 0.58 | 0.53 | 0.98 | 0.78 |
| 15. HWP | Hewlett-Packard | 1.73 | 3973 | 5305 | 2168 | 3978 | 1.29 | 0.92 | 2.57 | 1.38 |
| 16. IBM | Int. Bus. Mach. | 3.05 | 5605 | 4806 | 3514 | 2755 | 0.89 | 0.84 | 1.41 | 1.31 |
| 17. JNJ | Johnson & Johnson | 2.48 | 2999 | 3256 | 1646 | 2148 | 0.81 | 0.70 | 1.40 | 1.00 |
| 18. KO | Coca Cola Co. | 5.18 | 2438 | 3305 | 1450 | 2589 | 0.62 | 0.50 | 1.09 | 0.69 |
| 19. MCD | McDonald’s Corp. | 1.21 | 2321 | 2285 | 1443 | 1814 | 0.51 | 0.40 | 0.89 | 0.60 |
| 20. MCQ | MCI Comm. | 0.99 | 2437 | 2311 | 1503 | 1508 | 0.46 | 0.44 | 0.74 | 0.65 |
| 21. MMM | Minn Mining | 1.01 | 3532 | 3730 | 1946 | 2175 | 0.80 | 0.75 | 1.32 | 1.21 |
| 22. MOB | Mobil Corp. | 1.63 | 2573 | 2618 | 1795 | 2232 | 0.71 | 0.67 | 1.15 | 1.00 |
| 23. MRK | Merck & Co. | 3.75 | 3283 | 4163 | 1865 | 2639 | 0.98 | 0.83 | 1.69 | 1.31 |
| 24. NT | Northern Telecom | 0.89 | 1916 | 1788 | 1213 | 1176 | 0.60 | 0.53 | 0.94 | 0.72 |
| 25. PEP | PepsiCo Inc. | 1.65 | 2091 | 2459 | 1285 | 1695 | 0.40 | 0.36 | 0.65 | 0.51 |
| 26. SLB | Schlumberger Ltd | 1.04 | 2965 | 2678 | 1670 | 1699 | 0.77 | 0.71 | 1.34 | 1.06 |
| 27. T | AT&T Corp. | 2.64 | 2423 | 2607 | 1498 | 1783 | 0.45 | 0.36 | 0.73 | 0.50 |
| 28. WMT | Wal-Mart Stores | 3.31 | 2539 | 2959 | 1868 | 2036 | 0.49 | 0.42 | 0.80 | 0.63 |
| 29. XON | Exxon Corp. | 4.64 | 2364 | 2502 | 1375 | 1556 | 0.46 | 0.44 | 0.73 | 0.66 |
| 30. XRX | Xerox Corp. | 0.89 | 3665 | 4615 | 1927 | 2921 | 1.23 | 0.94 | 2.13 | 1.43 |
| 31. OEX | S&P 100 Index |  | 12793 | 22755 | 10981 | 16828 | 2.15 | 1.86 | 4.98 | 4.47 |
| The table reports |  | the number of observations and the midpoint price as |  |  | the average of |  | the bid-ask quotes | for |  | short-term and |
| medium-term OTM calls and puts for 30 stocks and the S&P 100. The ticker, name, and recent weight of the stock in the index |  |  |  |  |  |  |  |  |  |  |
| (as of May 1998) are also reported. The call (put) is OTM if K/S > 1 (K/S < 1), where S denotes the contemporaneous stock |  |  |  |  |  |  |  |  |  |  |
|  | price and K is the strike. Short-term options have remaining days to expiration of between 9 and 60 days and medium term |  |  |  |  |  |  |  |  |  |
|  | between 61 and 120 days. Only the last daily quote prior |  |  | to 3:00 p.m. CST of each option contract |  |  |  | is used in our calculations. |  |  |
|  | The sample period extends from January 1, 1991, |  | through December 31, 1995 for a total of 358,851 option quotes (162,046 |  |  |  |  |  |  |  |
| calls and 196,805 puts). |  |  |  |  |  |  |  |  |  |  |

Raw CSV: `assets/table_001.csv`

### Table 2

*Caption:* Table 1

<table>
  <tr>
    <th>The Review of Financial Studies / v 16 n 1 2003</th>
  </tr>
  <tr>
    <td>observations to estimate the smile. Third, the daily risk-neutral index skews</td>
  </tr>
  <tr>
    <td>exhibit a Monday seasonality [Harvey and Siddique (1999)]. The exact pro-</td>
  </tr>
  <tr>
    <td>cedure to build the time series of the smile and its slope will be outlined</td>
  </tr>
  <tr>
    <td>shortly.</td>
  </tr>
  <tr>
    <td>The requirement to sample options daily virtually limits the analysis to the</td>
  </tr>
  <tr>
    <td>largest 30 stocks by market capitalization. Even with the existing choice, the</td>
  </tr>
  <tr>
    <td>raw data contains more than 1.4 million price quotes, and additional stocks</td>
  </tr>
  <tr>
    <td>would have made the empirical examination less manageable. The tickers and</td>
  </tr>
  <tr>
    <td>names of the individual stock options are displayed in the ﬁrst two columns</td>
  </tr>
  <tr>
    <td>of Table 1. The set includes, among others, such actively traded and familiar</td>
  </tr>
  <tr>
    <td>stock options as IBM, General Electric, Ford, and General Motors.</td>
  </tr>
</table>

Raw CSV: `assets/table_002.csv`

### Table 3

*Caption:* Table 1 reports the option price as the average of the bid and ask quotes,

<table>
  <tr>
    <th>Individual Equity Options</th>
  </tr>
  <tr>
    <td>To be consistent with the existing literature, the data were screened to</td>
  </tr>
  <tr>
    <td>eliminate (i) bid-ask option pairs with missing quotes, or zero bids, and</td>
  </tr>
  <tr>
    <td>(ii) option prices violating arbitrage restrictions that C(cid:1)t(cid:3) (cid:5)(cid:7) K(cid:2) &lt; S(cid:1)t(cid:2) or</td>
  </tr>
  <tr>
    <td>C(cid:1)t(cid:3) (cid:5)(cid:7) K(cid:2) &gt; S(cid:1)t(cid:2) − PVD(cid:6)D(cid:8) − PVD(cid:6)K(cid:8), for present value function PVD(cid:6)(cid:10)(cid:8)</td>
  </tr>
  <tr>
    <td>and dividends D. As longer- (and very short-) maturity stock option quotes</td>
  </tr>
  <tr>
    <td>may not be active, options with less than 9 days and more than 120 days to</td>
  </tr>
  <tr>
    <td>expiration were also discarded. Finally, as indicated by Theorem 1, we only</td>
  </tr>
  <tr>
    <td>keep OTM calls and puts. As a result, puts have moneyness corresponding to</td>
  </tr>
  <tr>
    <td>(cid:2) (cid:2)</td>
  </tr>
  <tr>
    <td>S(cid:1)t(cid:2) S(cid:1)t(cid:2) &lt; 1(cid:11), and calls have moneyness corresponding to (cid:9) K S(cid:1)t(cid:2) S(cid:1)t(cid:2) &gt; 1(cid:11).</td>
  </tr>
  <tr>
    <td>Although each series for skewness and kurtosis pertain to a constant (cid:5),</td>
  </tr>
  <tr>
    <td>in practice, it is not possible to strictly observe these, as options are seldom</td>
  </tr>
  <tr>
    <td>issued daily with a constant maturity. Therefore, in our empirical exercises, if</td>
  </tr>
  <tr>
    <td>an OTM option has remaining days to expiration of 9 to 60 days, it is grouped</td>
  </tr>
  <tr>
    <td>in the short-term option category; if the remaining days to expiration is 61</td>
  </tr>
  <tr>
    <td>to 120 days, the option is grouped in the medium-term category. Thus only</td>
  </tr>
  <tr>
    <td>two classiﬁcations of smiles and option portfolios are investigated.</td>
  </tr>
  <tr>
    <td>Table 1 reports the option price as the average of the bid and ask quotes,</td>
  </tr>
  <tr>
    <td>and the number of quotes, for both short-term and medium-term OTM calls</td>
  </tr>
  <tr>
    <td>and puts. The table also reports the weight of each stock in the OEX. As</td>
  </tr>
  <tr>
    <td>would be expected, the index has considerably more strikes quoted than</td>
  </tr>
  <tr>
    <td>individual stock options, with puts more active than calls. In the combined</td>
  </tr>
  <tr>
    <td>option sample, there are 358,851 OTM calls and puts.</td>
  </tr>
  <tr>
    <td>Because each option under scrutiny has the potential for early exercise, the</td>
  </tr>
  <tr>
    <td>treatment of the smile is arguably controversial. To probe this issue we also</td>
  </tr>
  <tr>
    <td>calculate the volatility that equates the observed option price to the American</td>
  </tr>
  <tr>
    <td>price. For estimating the price of the American option, we follow Broadie</td>
  </tr>
  <tr>
    <td>and Detemple (1996). We construct a binomial tree where the Black–Scholes</td>
  </tr>
  <tr>
    <td>price is substituted in the penultimate step. The American option price is esti-</td>
  </tr>
  <tr>
    <td>mated by extrapolating off the prices estimated from 50- and 100-step trees,</td>
  </tr>
  <tr>
    <td>using Richardson extrapolation, and accounts for lumpy dividends. We then</td>
  </tr>
  <tr>
    <td>estimate two separate implied volatilities: the volatility that equates the option</td>
  </tr>
  <tr>
    <td>price to the American and the Black–Scholes price. In the latter calculations,</td>
  </tr>
  <tr>
    <td>discounted dividends are subtracted from the spot stock price.</td>
  </tr>
  <tr>
    <td>Table 2 compares the European and American implied volatilities. While</td>
  </tr>
  <tr>
    <td>presenting this comparison, three decisions are made for conciseness. First,</td>
  </tr>
  <tr>
    <td>options are divided into two moneyness intervals: [−10%(cid:3) −5%) and [−5%,</td>
  </tr>
  <tr>
    <td>0), for calls and puts. Next, only the implied volatilities for a sample of</td>
  </tr>
  <tr>
    <td>10 stocks and the OEX are shown. Finally, we focus on the 1995 sample</td>
  </tr>
  <tr>
    <td>period, as averaging over the full ﬁve-year sample narrows the differences</td>
  </tr>
  <tr>
    <td>even further. For the most part, the implied volatility curves tend to taper</td>
  </tr>
  <tr>
    <td>downward from deep OTM put options to ATM, and then moves slightly</td>
  </tr>
  <tr>
    <td>upward as the call becomes progressively OTM. Although the American</td>
  </tr>
  <tr>
    <td>option implied volatility (denoted AM) is smaller than the Black–Scholes</td>
  </tr>
  <tr>
    <td>(denoted BS) counterpart, this difference is negligible and within the bid-ask</td>
  </tr>
  <tr>
    <td>119</td>
  </tr>
</table>

Raw CSV: `assets/table_003.csv`

### Table 4

*Caption:* Table 3 reports the average slope of the implied volatility curve for each

<table>
  <tr>
    <th>Individual Equity Options</th>
  </tr>
  <tr>
    <td>spread. With the assurance that the bias from adopting BS implied volatility</td>
  </tr>
  <tr>
    <td>is small enough to be ignored, we adhere to convention and use only Black–</td>
  </tr>
  <tr>
    <td>Scholes smiles to surrogate the pricing structure of options.</td>
  </tr>
  <tr>
    <td>4. Skewness and the Structure of Option Prices: Empirical Tests</td>
  </tr>
  <tr>
    <td>This section establishes the differential pricing of individual stock options</td>
  </tr>
  <tr>
    <td>versus the market index and empirically relates it to the asymmetry and the</td>
  </tr>
  <tr>
    <td>heaviness of the risk-neutral distributions. We also present a framework to</td>
  </tr>
  <tr>
    <td>study the empirical determinants of risk-neutral index skews.</td>
  </tr>
  <tr>
    <td>4.1 Quantifying the structure of option prices</td>
  </tr>
  <tr>
    <td>To quantify the structure of option prices we use options of maturity (cid:5) to</td>
  </tr>
  <tr>
    <td>estimate the model,</td>
  </tr>
  <tr>
    <td>j = 1(cid:3) (cid:4) (cid:4) (cid:4) (cid:3) J (cid:3) (30) + (cid:28) ln(cid:1)yj (cid:2) + (cid:29)j (cid:3) ln(cid:1)(cid:16)(cid:6)yj (cid:8)(cid:2) = (cid:28)0</td>
  </tr>
  <tr>
    <td>y = K/S across our sample of 30 stocks and the OEX, where, recall, is</td>
  </tr>
  <tr>
    <td>option moneyness (and deterministic). An advantage of the speciﬁcation in</td>
  </tr>
  <tr>
    <td>Equation (30) is its potential consistency with empirical implied volatility</td>
  </tr>
  <tr>
    <td>curves that are both decreasing and convex in moneyness. This suggests a</td>
  </tr>
  <tr>
    <td>(cid:28) less than 0. We interpret (cid:28) as a measure of the ﬂatness of the implied</td>
  </tr>
  <tr>
    <td>volatility curve and designate it as the sensitivity of the implied volatility</td>
  </tr>
  <tr>
    <td>curve to moneyness. In economic terms, a ﬂatter implied volatility curve</td>
  </tr>
  <tr>
    <td>simply states that prices of put options of nearby strikes are closer, while</td>
  </tr>
  <tr>
    <td>those options that constitute a steeper curve have prices farther apart.</td>
  </tr>
  <tr>
    <td>The model of Equation (30) is estimated weekly, and the estimated coefﬁ-</td>
  </tr>
  <tr>
    <td>cients are pooled over all the weeks in the sample. Brieﬂy the procedure is as</td>
  </tr>
  <tr>
    <td>follows. Over each calendar day in the week we index the available options</td>
  </tr>
  <tr>
    <td>by j and estimate the said model by least squares. Thus, for each stock, we</td>
  </tr>
  <tr>
    <td>estimate Equation (30) for each of the 260 weeks for which sufﬁcient data</td>
  </tr>
  <tr>
    <td>exist. Next, as in Fama and McBeth (1973), we time average the regression</td>
  </tr>
  <tr>
    <td>(cid:16)</td>
  </tr>
  <tr>
    <td>1 T T t coefﬁcients (say, =1 (cid:28)(cid:1)t(cid:2)). Each reported t-statistic is computed under</td>
  </tr>
  <tr>
    <td>a ﬁrst-order serial correlation assumption for the coefﬁcient. The model is</td>
  </tr>
  <tr>
    <td>estimated using OTM puts and calls. As in the money puts (K/S &gt; 1) can be</td>
  </tr>
  <tr>
    <td>proxied by OTM calls, this is tantamount to using all the strikes in the cross</td>
  </tr>
  <tr>
    <td>section of puts.</td>
  </tr>
  <tr>
    <td>Table 3 reports the average slope of the implied volatility curve for each</td>
  </tr>
  <tr>
    <td>of the 30 stocks and the OEX. We also report the estimated ATM implied</td>
  </tr>
  <tr>
    <td>the results for short-term smiles. The volatility as exp(cid:1)(cid:28)0(cid:2). Consider ﬁrst,</td>
  </tr>
  <tr>
    <td>average ATM implied volatility for the OEX is 14%, while the average ATM</td>
  </tr>
  <tr>
    <td>implied volatility over the 30 stocks is about 26%. With reference to the</td>
  </tr>
  <tr>
    <td>estimate of (cid:28), we can make three observations. First, on average, (cid:28) is nega-</td>
  </tr>
  <tr>
    <td>tive for all the individual stocks and the OEX. The slopes are all statistically</td>
  </tr>
</table>

Raw CSV: `assets/table_004.csv`

### Table 5

*Caption:* Table 3

|  |  | Short-term options |  |  |  | Medium-term options |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | Slope of |  |  |  | Slope of |  |  |
|  |  | the smile, |  |  |  | the smile, |  |  |
|  | exp(cid:1)(cid:28)0(cid:2) | (cid:28) | R2 | (cid:28) < 0 | exp(cid:1)(cid:28)0(cid:2) | (cid:28) | R2 | (cid:28) < 0 |
| Ticker | Avg. | t t Avg. | Avg. | % | Avg. | t t Avg. | Avg. | % |
| 1. AIG | 0(cid:10)22 | 32(cid:10)12 −1(cid:10)09 −13(cid:10)01 | 43(cid:10)57 | 97 | 0(cid:10)22 | 119(cid:10)84 −0(cid:10)62 −7(cid:10)61 | 38(cid:10)2 | 76 |
| 2. AIT | 0(cid:10)19 | 38(cid:10)45 −1(cid:10)96 −14(cid:10)34 | 55(cid:10)41 | 96 | 0(cid:10)19 | 108(cid:10)39 −1(cid:10)59 −15(cid:10)22 | 31(cid:10)9 | 57 |
| 3. AN | 0(cid:10)19 | 25(cid:10)61 −0(cid:10)96 −8(cid:10)25 | 36(cid:10)08 | 80 | 0(cid:10)19 | 80(cid:10)11 −0(cid:10)97 −6(cid:10)60 | 41(cid:10)4 | 83 |
| 4. AXP | 0(cid:10)31 | 17(cid:10)09 −0(cid:10)26 −3(cid:10)87 | 27(cid:10)62 | 74 | 0(cid:10)31 | 66(cid:10)60 −0(cid:10)32 −6(cid:10)52 | 56(cid:10)9 | 97 |
| 5. BA | 0(cid:10)27 | 24(cid:10)78 −0(cid:10)69 −7(cid:10)39 | 33(cid:10)29 | 80 | 0(cid:10)25 | 96(cid:10)42 −0(cid:10)57 −4(cid:10)09 | 73(cid:10)2 | 97 |
| 6. BAC | 0(cid:10)30 | 18(cid:10)27 −1(cid:10)16 −13(cid:10)03 | 56(cid:10)81 | 95 | 0(cid:10)29 | 93(cid:10)15 −0(cid:10)84 −8(cid:10)30 | 74(cid:10)7 | 98 |
| 7. BEL | 0(cid:10)21 | 23(cid:10)70 −1(cid:10)54 −10(cid:10)14 | 48(cid:10)12 | 86 | 0(cid:10)20 | 89(cid:10)94 −1(cid:10)23 −7(cid:10)98 | 59(cid:10)0 | 95 |
| 8. BMY | 0(cid:10)21 | 22(cid:10)70 −1(cid:10)38 −7(cid:10)78 | 46(cid:10)55 | 89 | 0(cid:10)20 | 93(cid:10)39 −1(cid:10)07 −5(cid:10)02 | 71(cid:10)5 | 98 |
| 9. CCI | 0(cid:10)35 | 12(cid:10)87 −0(cid:10)83 −10(cid:10)20 | 42(cid:10)32 | 90 | 0(cid:10)35 | 58(cid:10)59 −0(cid:10)63 −6(cid:10)79 | 75(cid:10)8 | 97 |
| 10. DD | 0(cid:10)24 | 30(cid:10)96 −0(cid:10)86 −15(cid:10)39 | 42(cid:10)01 | 95 | 0(cid:10)23 | 129(cid:10)37 −0(cid:10)76 −14(cid:10)08 | 48(cid:10)8 | 90 |
| 11. DIS | 0(cid:10)28 | 31(cid:10)94 −0(cid:10)91 −13(cid:10)67 | 48(cid:10)29 | 95 | 0(cid:10)28 | 146(cid:10)50 −0(cid:10)69 −12(cid:10)79 | 71(cid:10)7 | 99 |
| 12. F | 0(cid:10)31 | 38(cid:10)78 −0(cid:10)62 −8(cid:10)86 | 37(cid:10)77 | 88 | 0(cid:10)30 | 137(cid:10)45 −0(cid:10)50 −7(cid:10)32 | 57(cid:10)6 | 96 |
| 13. GE | 0(cid:10)21 | 31(cid:10)67 −1(cid:10)85 −19(cid:10)55 | 61(cid:10)02 | 99 | 0(cid:10)20 | 117(cid:10)81 −1(cid:10)55 −22(cid:10)11 | 81(cid:10)1 | 98 |
| 14. GM | 0(cid:10)31 | 26(cid:10)48 −0(cid:10)52 −8(cid:10)27 | 34(cid:10)86 | 83 | 0(cid:10)30 | 138(cid:10)09 −0(cid:10)40 −5(cid:10)22 | 76(cid:10)7 | 99 |
| 15. HWP | 0(cid:10)33 | 29(cid:10)96 −0(cid:10)83 −11(cid:10)86 | 50(cid:10)95 | 96 | 0(cid:10)32 | 147(cid:10)65 −0(cid:10)50 −10(cid:10)44 | 56(cid:10)8 | 96 |
| 16. IBM | 0(cid:10)29 | 18(cid:10)79 −0(cid:10)36 −3(cid:10)09 | 29(cid:10)85 | 71 | 0(cid:10)27 | 103(cid:10)52 −0(cid:10)28 −2(cid:10)03 | 65(cid:10)5 | 97 |
| 17. JNJ | 0(cid:10)24 | 19(cid:10)64 −1(cid:10)00 −10(cid:10)79 | 41(cid:10)70 | 93 | 0(cid:10)24 | 96(cid:10)00 −0(cid:10)88 −5(cid:10)57 | 69(cid:10)7 | 99 |
| 18. KO | 0(cid:10)24 | 28(cid:10)06 −1(cid:10)62 −20(cid:10)64 | 62(cid:10)87 | 99 | 0(cid:10)22 | 113(cid:10)41 −1(cid:10)22 −10(cid:10)15 | 77(cid:10)6 | 100 |
| 19. MCD | 0(cid:10)25 | 30(cid:10)49 −1(cid:10)16 −11(cid:10)84 | 46(cid:10)17 | 93 | 0(cid:10)24 | 90(cid:10)25 −0(cid:10)99 −12(cid:10)77 | 73(cid:10)1 | 96 |
| 20. MCQ | 0(cid:10)34 | 31(cid:10)15 −0(cid:10)53 −7(cid:10)22 | 26(cid:10)34 | 74 | 0(cid:10)33 | 81(cid:10)57 −0(cid:10)32 −3(cid:10)63 | 49(cid:10)6 | 68 |
| 21. MMM | 0(cid:10)21 | 60(cid:10)43 −1(cid:10)21 −6(cid:10)19 | 42(cid:10)65 | 90 | 0(cid:10)19 | 151(cid:10)90 −1(cid:10)21 −11(cid:10)52 | 67(cid:10)5 | 96 |
| 22. MOB | 0(cid:10)19 | 30(cid:10)92 −1(cid:10)34 −14(cid:10)75 | 44(cid:10)17 | 94 | 0(cid:10)18 | 124(cid:10)79 −1(cid:10)18 −13(cid:10)29 | 44(cid:10)9 | 80 |
| 23. MRK | 0(cid:10)27 | 17(cid:10)46 −0(cid:10)62 −3(cid:10)51 | 38(cid:10)67 | 72 | 0(cid:10)26 | 98(cid:10)47 −0(cid:10)55 −3(cid:10)49 | 76(cid:10)1 | 98 |
| 24. NT | 0(cid:10)31 | 17(cid:10)38 −0(cid:10)31 −3(cid:10)05 | 28(cid:10)40 | 72 | 0(cid:10)29 | 69(cid:10)44 −0(cid:10)25 −3(cid:10)77 | 34(cid:10)6 | 72 |
| 25. PEP | 0(cid:10)26 | 19(cid:10)31 −1(cid:10)13 −11(cid:10)85 | 45(cid:10)50 | 91 | 0(cid:10)25 | 84(cid:10)13 −0(cid:10)92 −6(cid:10)99 | 80(cid:10)3 | 100 |
| 26. SLB | 0(cid:10)25 | 30(cid:10)00 −0(cid:10)54 −5(cid:10)49 | 30(cid:10)84 | 76 | 0(cid:10)24 | 129(cid:10)84 −0(cid:10)55 −5(cid:10)19 | 30(cid:10)0 | 67 |
| 27. T | 0(cid:10)21 | 31(cid:10)21 −1(cid:10)44 −11(cid:10)51 | 48(cid:10)59 | 95 | 0(cid:10)21 | 104(cid:10)26 −1(cid:10)11 −10(cid:10)53 | 85(cid:10)5 | 100 |
| 28. WMT | 0(cid:10)29 | 23(cid:10)53 −0(cid:10)95 −8(cid:10)65 | 44(cid:10)85 | 88 | 0(cid:10)28 | 93(cid:10)92 −0(cid:10)50 −3(cid:10)53 | 67(cid:10)7 | 92 |
| 29. XON | 0(cid:10)17 | 32(cid:10)56 −1(cid:10)47 −14(cid:10)51 | 41(cid:10)97 | 91 | 0(cid:10)16 | 107(cid:10)16 −1(cid:10)43 −9(cid:10)12 | 75(cid:10)5 | 99 |
| 30. XRX | 0(cid:10)26 | 36(cid:10)39 −1(cid:10)31 −17(cid:10)38 | 55(cid:10)73 | 98 | 0(cid:10)25 | 162(cid:10)13 −0(cid:10)87 −18(cid:10)17 | 49(cid:10)8 | 88 |
| 31. OEX | 0(cid:10)14 | 24(cid:10)80 −4(cid:10)42 −22(cid:10)32 | 86(cid:10)08 | 100 | 0(cid:10)14 | 84(cid:10)31 −3(cid:10)47 −20(cid:10)31 | 93(cid:10)8 | 100 |
|  | For 30 stocks and the S&P 100, |  | the table displays the average coefﬁcients for |  |  | the speciﬁcation |  |  |
|  |  |  | ln(cid:1)(cid:16)j (cid:2) = (cid:28)0 + (cid:28) ln(cid:1)yj (cid:2) + (cid:29)j |  | j = 1(cid:3) (cid:4) (cid:4) (cid:4) (cid:3) J (cid:10) |  |  |  |
|  | Here, (cid:16) is the Black–Scholes implied volatility of option with moneyness y ≡ K |  |  |  |  | S . The regression is estimated via OLS for each |  |  |
| of | the 260 weeks in the period January 1, 1991, |  | to December 31, 1995 in which there are a minimum of eight observations, |  |  |  |  |  |

Raw CSV: `assets/table_005.csv`

### Table 6

*Caption:* Table 5

|  | Panel A: Unrestricted regressions |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  | LR test |
| Ticker | (cid:25) | t(cid:1)(cid:25)(cid:2) | (cid:26) | t(cid:1)(cid:26)(cid:2) | (cid:31) | t(cid:1)(cid:31)(cid:2) | R2 | 2(cid:1)1(cid:2) | p value |
| 1. AIG | 0.75 | 7(cid:10)80 | 0(cid:10)03 | 0(cid:10)83 | 0.44 | 7(cid:10)18 | 46.0 | 0(cid:10)68 | .41 |
| 2. AIT | 1.42 | 6(cid:10)70 | 0(cid:10)24 | 4(cid:10)52 | 0.21 | 2(cid:10)20 | 46.1 | 23(cid:10)12 | .00 |
| 3. AN | 0.73 | 6(cid:10)05 | −0(cid:10)06 | −2(cid:10)23 | 0.21 | 3(cid:10)81 | 44.6 | 23(cid:10)12 | .00 |
| 4. AXP | 0.35 | 3(cid:10)59 | 0(cid:10)01 | 0(cid:10)95 | 0.33 | 3(cid:10)13 | 43.7 | 2(cid:10)00 | .16 |
| 5. BA | 0.95 | 10(cid:10)21 | 0(cid:10)03 | 1(cid:10)99 | 0.26 | 4(cid:10)14 | 66.6 | 6(cid:10)56 | .01 |
| 6. BAC | 0.68 | 10(cid:10)42 | 0(cid:10)04 | 2(cid:10)95 | 0.39 | 7(cid:10)73 | 68.1 | 8(cid:10)53 | .00 |
| 7. BEL | 1.24 | 12(cid:10)11 | 0(cid:10)13 | 4(cid:10)51 | 0.28 | 4(cid:10)22 | 64.3 | 31(cid:10)83 | .00 |
| 8. BMY | 1.05 | 10(cid:10)06 | 0(cid:10)05 | 2(cid:10)15 | 0.37 | 7(cid:10)69 | 71.1 | 8(cid:10)00 | .00 |
| 9. CCI | 0.58 | 9(cid:10)50 | −0(cid:10)01 | −1(cid:10)25 | 0.42 | 8(cid:10)78 | 63.3 | 1(cid:10)22 | .27 |
| 10. DD | 0.57 | 9(cid:10)26 | 0(cid:10)04 | 3(cid:10)04 | 0.30 | 4(cid:10)60 | 43.8 | 11(cid:10)27 | .00 |
| 11. DIS | 0.52 | 6(cid:10)58 | 0(cid:10)04 | 2(cid:10)47 | 0.52 | 10(cid:10)18 | 55.8 | 6(cid:10)13 | .01 |
| 12. F | 0.41 | 5(cid:10)97 | 0(cid:10)02 | 2(cid:10)31 | 0.45 | 8(cid:10)25 | 57.6 | 7(cid:10)25 | .01 |
| 13. GE | 1.07 | 11(cid:10)76 | 0(cid:10)10 | 5(cid:10)62 | 0.46 | 9(cid:10)51 | 62.3 | 30(cid:10)01 | .00 |
| 14. GM | 0.49 | 6(cid:10)90 | −0(cid:10)01 | −0(cid:10)79 | 0.46 | 9(cid:10)22 | 58.9 | 0(cid:10)97 | .33 |
| 15. HWP | 0.47 | 8(cid:10)10 | 0(cid:10)06 | 2(cid:10)57 | 0.52 | 8(cid:10)54 | 61.5 | 10(cid:10)02 | .00 |
| 16. IBM | 0.80 | 6(cid:10)47 | −0(cid:10)03 | −1(cid:10)12 | 0.53 | 8(cid:10)77 | 74.8 | 2(cid:10)57 | .11 |
| 17. JNJ | 0.49 | 4(cid:10)13 | 0(cid:10)01 | 0(cid:10)90 | 0.43 | 6(cid:10)74 | 49.5 | 1(cid:10)60 | .21 |
| 18. KO | 0.86 | 10(cid:10)30 | 0(cid:10)08 | 4(cid:10)57 | 0.27 | 4(cid:10)55 | 58.6 | 37(cid:10)00 | .00 |
| 19. MCD | 0.87 | 11(cid:10)10 | 0(cid:10)09 | 4(cid:10)62 | 0.29 | 3(cid:10)81 | 57.5 | 36(cid:10)67 | .00 |
| 20. MCQ | 0.81 | 7(cid:10)63 | 0(cid:10)03 | 1(cid:10)56 | 0.18 | 3(cid:10)10 | 47.0 | 3(cid:10)61 | .06 |
| 21. MMM | 0.87 | 5(cid:10)14 | 0(cid:10)08 | 1(cid:10)96 | 0.63 | 8(cid:10)17 | 47.2 | 3(cid:10)45 | .06 |
| 22. MOB | 0.95 | 8(cid:10)96 | 0(cid:10)05 | 2(cid:10)02 | 0.31 | 6(cid:10)31 | 54.2 | 6(cid:10)43 | .01 |
| 23. MRK | 0.77 | 7(cid:10)67 | 0(cid:10)07 | 5(cid:10)34 | 0.45 | 5(cid:10)77 | 74.6 | 32(cid:10)59 | .00 |
| 24. NT | 0.58 | 5(cid:10)74 | 0(cid:10)04 | 1(cid:10)53 | 0.27 | 6(cid:10)04 | 48.6 | 5(cid:10)10 | .02 |
| 25. PEP | 0.78 | 9(cid:10)65 | 0(cid:10)04 | 3(cid:10)43 | 0.28 | 6(cid:10)02 | 58.6 | 13(cid:10)61 | .00 |
| 26. SLB | 0.95 | 10(cid:10)43 | 0(cid:10)10 | 4(cid:10)25 | 0.27 | 7(cid:10)64 | 60.7 | 22(cid:10)21 | .00 |
| 27. T | 1.00 | 10(cid:10)03 | 0(cid:10)08 | 4(cid:10)85 | 0.27 | 5(cid:10)09 | 71.3 | 33(cid:10)58 | .00 |
| 28. WMT | 0.59 | 13(cid:10)24 | 0(cid:10)04 | 2(cid:10)88 | 0.43 | 6(cid:10)65 | 66.3 | 11(cid:10)09 | .00 |
| 29. XON | 1.11 | 9(cid:10)17 | 0(cid:10)08 | 4(cid:10)13 | 0.15 | 3(cid:10)40 | 54.4 | 22(cid:10)14 | .00 |
| 30. XRX | 0.57 | 4(cid:10)50 | 0(cid:10)08 | 2(cid:10)71 | 0.51 | 10(cid:10)62 | 43.0 | 9(cid:10)79 | .00 |
| 31. OEX | 1.83 | 5(cid:10)65 | 0(cid:10)21 | 5(cid:10)02 | 0.58 | 7(cid:10)68 | 74.8 | 28(cid:10)43 | .00 |
|  |  |  |  |  |  |  |  |  | 127 |

Raw CSV: `assets/table_006.csv`

### Table 7

*Caption:* Table 5

|  | Panel B: Restricted regressions |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | Restricted (cid:26) ≡ 0 |  |  |  |  | Restricted (cid:25) ≡ 0 |  |  |
|  |  |  | (skewness alone) |  |  |  |  | (kurtosis alone) |  |  |
| Ticker | (cid:25) | t(cid:1)(cid:25)(cid:2) | (cid:31) | t(cid:1)(cid:31)(cid:2) | R2 | (cid:26) | t(cid:1)(cid:26)(cid:2) | (cid:31) | t(cid:1)(cid:31)(cid:2) | R2 |
| 1. AIG | 0.71 | 7(cid:10)22 | 0.44 | 7(cid:10)12 | 45.9 | −0(cid:10)12 | −3(cid:10)03 | 0.53 | 8(cid:10)69 | 32.5 |
| 2. AIT | 0.77 | 4(cid:10)19 | 0.29 | 3(cid:10)28 | 34.2 | −0(cid:10)04 | −1(cid:10)39 | 0.37 | 4(cid:10)19 | 15.1 |
| 3. AN | 0.60 | 2(cid:10)87 | 0.24 | 4(cid:10)32 | 38.9 | 0(cid:10)00 | 0(cid:10)09 | 0.33 | 4(cid:10)90 | 10.9 |
| 4. AXP | 0.32 | 3(cid:10)85 | 0.34 | 3(cid:10)92 | 43.2 | −0(cid:10)02 | −2(cid:10)39 | 0.50 | 5(cid:10)34 | 25.9 |
| 5. BA | 0.88 | 9(cid:10)16 | 0.27 | 4(cid:10)28 | 65.7 | −0(cid:10)05 | −2(cid:10)36 | 0.54 | 7(cid:10)39 | 33.5 |
| 6. BAC | 0.58 | 10(cid:10)32 | 0.39 | 8(cid:10)23 | 67.0 | −0(cid:10)07 | −4(cid:10)93 | 0.57 | 11(cid:10)05 | 46.6 |
| 7. BEL | 0.84 | 10(cid:10)70 | 0.29 | 4(cid:10)38 | 59.4 | −0(cid:10)11 | −5(cid:10)32 | 0.44 | 5(cid:10)99 | 36.5 |
| 8. BMY | 0.91 | 7(cid:10)17 | 0.37 | 7(cid:10)56 | 70.2 | −0(cid:10)09 | −3(cid:10)29 | 0.61 | 10(cid:10)58 | 53.2 |
| 9. CCI | 0.59 | 10(cid:10)85 | 0.43 | 8(cid:10)76 | 63.2 | −0(cid:10)07 | −5(cid:10)31 | 0.57 | 10(cid:10)16 | 45.5 |
| 10. DD | 0.47 | 7(cid:10)71 | 0.31 | 4(cid:10)58 | 41.2 | −0(cid:10)01 | −1(cid:10)80 | 0.44 | 6(cid:10)08 | 20.9 |
| 11. DIS | 0.49 | 6(cid:10)48 | 0.52 | 10(cid:10)67 | 54.8 | 0(cid:10)12 | 0(cid:10)94 | 0.64 | 14(cid:10)92 | 42.4 |
| 12. F | 0.36 | 4(cid:10)78 | 0.47 | 8(cid:10)45 | 56.4 | −0(cid:10)01 | −1(cid:10)09 | 0.63 | 14(cid:10)54 | 40.2 |
| 13. GE | 0.74 | 7(cid:10)87 | 0.49 | 9(cid:10)83 | 57.7 | −0(cid:10)06 | −3(cid:10)30 | 0.58 | 11(cid:10)82 | 38.7 |
| 14. GM | 0.49 | 7(cid:10)02 | 0.45 | 9(cid:10)01 | 58.7 | −0(cid:10)03 | −2(cid:10)81 | 0.63 | 13(cid:10)39 | 41.2 |
| 15. HWP | 0.41 | 7(cid:10)14 | 0.54 | 9(cid:10)30 | 59.9 | 0(cid:10)00 | 0(cid:10)09 | 0.69 | 12(cid:10)67 | 48.8 |
| 16. IBM | 0.78 | 7(cid:10)40 | 0.54 | 9(cid:10)16 | 74.6 | 0(cid:10)00 | 0(cid:10)18 | 0.77 | 19(cid:10)31 | 63.7 |
| 17. JNJ | 0.45 | 4(cid:10)58 | 0.44 | 6(cid:10)99 | 49.2 | −0(cid:10)04 | −2(cid:10)74 | 0.58 | 10(cid:10)88 | 37.5 |
| 18. KO | 0.63 | 10(cid:10)01 | 0.25 | 4(cid:10)00 | 52.2 | −0(cid:10)02 | −0(cid:10)88 | 0.51 | 7(cid:10)83 | 29.5 |
| 19. MCD | 0.61 | 5(cid:10)97 | 0.32 | 4(cid:10)67 | 50.8 | −0(cid:10)04 | −3(cid:10)05 | 0.47 | 6(cid:10)67 | 25.8 |
| 20. MCQ | 0.77 | 7(cid:10)33 | 0.19 | 3(cid:10)15 | 46.2 | −0(cid:10)03 | −1(cid:10)32 | 0.35 | 4(cid:10)32 | 13.2 |
| 21. MMM | 0.70 | 5(cid:10)78 | 0.65 | 8(cid:10)73 | 46.5 | −0(cid:10)03 | −1(cid:10)22 | 0.66 | 9(cid:10)11 | 42.2 |
| 22. MOB | 0.87 | 8(cid:10)83 | 0.32 | 6(cid:10)38 | 53.2 | −0(cid:10)05 | −2(cid:10)53 | 0.48 | 7(cid:10)80 | 24.3 |
| 23. MRK | 0.53 | 8(cid:10)35 | 0.58 | 11(cid:10)36 | 71.1 | −0(cid:10)03 | −1(cid:10)80 | 0.77 | 13(cid:10)77 | 58.1 |
| 24. NT | 0.47 | 8(cid:10)56 | 0.28 | 6(cid:10)61 | 47.4 | −0(cid:10)07 | −5(cid:10)89 | 0.39 | 6(cid:10)84 | 28.8 |
| 25. PEP | 0.66 | 8(cid:10)58 | 0.28 | 5(cid:10)18 | 56.3 | −0(cid:10)04 | −3(cid:10)88 | 0.45 | 6(cid:10)01 | 27.8 |
| 26. SLB | 0.77 | 6(cid:10)60 | 0.31 | 8(cid:10)79 | 57.2 | −0(cid:10)07 | −2(cid:10)15 | 0.52 | 12(cid:10)71 | 29.9 |
| 27. T | 0.65 | 10(cid:10)53 | 0.32 | 6(cid:10)43 | 67.3 | −0(cid:10)07 | −5(cid:10)84 | 0.53 | 8(cid:10)60 | 49.3 |
| 28. WMT | 0.51 | 11(cid:10)68 | 0.47 | 8(cid:10)25 | 64.8 | −0(cid:10)03 | −1(cid:10)33 | 0.68 | 14(cid:10)83 | 47.1 |
| 29. XON | 0.85 | 7(cid:10)33 | 0.17 | 3(cid:10)65 | 50.4 | −0(cid:10)06 | −4(cid:10)24 | 0.35 | 6(cid:10)95 | 21.3 |
| 30. XRX | 0.42 | 3(cid:10)70 | 0.51 | 10(cid:10)18 | 40.9 | −0(cid:10)01 | −0(cid:10)59 | 0.57 | 12(cid:10)13 | 33.3 |
| 31. OEX | 0.69 | 5(cid:10)38 | 0.64 | 9(cid:10)97 | 71.9 | −0(cid:10)06 | −3(cid:10)82 | 0.76 | 14(cid:10)57 | 68.7 |
|  | For each of the 30 stocks and the S&P 100, the table reports the results of a time-series regression: SLOPE(cid:1)t(cid:2) = (cid:24)+(cid:25)SKEW(cid:1)t(cid:2)+ |  |  |  |  |  |  |  |  |  |
|  | (cid:26)KURT(cid:1)t(cid:2) + (cid:31)SLOPE(cid:1)t − 1(cid:2) + (cid:29)(cid:1)t(cid:2), where SLOPE(t) |  |  |  | is the (weekly) slope of |  | the smile (i.e., | the previously computed (cid:28)(cid:1)t(cid:2) in |  |  |
|  | Table 3). SKEW(t) and KURT(t) are the risk-neutral skew and kurtosis for each of the 260 weeks in the sample period, January |  |  |  |  |  |  |  |  |  |
| 1, 1991, | to December 31, 1995. We include SLOPE(t − 1) |  |  |  | to correct | for | the autocorrelation of |  | the dependent variable. The |  |
|  | method of estimation is OLS. The t-statistics are computed using the Newey–West (with a lag length of 8 weeks) methodology |  |  |  |  |  |  |  |  |  |
| that corrects for heteroscedasticity and serial correlation. Standard errors with lag length up to 20 are virtually similar. R2 is the |  |  |  |  |  |  |  |  |  |  |
|  | coefﬁcient of determination (in %). The reported 2(cid:1)1(cid:2) is the likelihood ratio test statistic for |  |  |  |  |  |  |  | the null hypothesis that (cid:26) = 0. |  |
|  | The corresponding p value is presented under |  |  | the column “p value.” Only the results using short-term smiles are shown here. |  |  |  |  |  |  |

Raw CSV: `assets/table_007.csv`

### Table 8

*Caption:* Table 6

|  |  | Sign of |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | skewness |  |  |  | Univariate regression |  |  |  |  |  |
|  |  |  |  |  | SKEWn(cid:1)t(cid:2) = (cid:21)0 | + (cid:21)1SKEWm(cid:1)t(cid:2) + (cid:29)(cid:1)t(cid:2) |  |  |  | Price of moments |  |
|  | SKEWn |  | SKEWn > |  |  |  |  |  | √ |  |  |
| Ticker | < 0 |  | SKEWm | (cid:21)0 | t(cid:1)(cid:21)0(cid:2) | (cid:21)1 | t(cid:1)(cid:21)1(cid:2) | R2 | V |  | SKEW KURT |
| 1. AIG | 68 |  | 96 | 0(cid:10)11 | 1(cid:10)43 | 0(cid:10)29 | 4(cid:10)46 | 7(cid:10)2 | 7(cid:10)98 | −0(cid:10)21 | 2.20 |
| 2. AIT | 83 |  | 77 | −0(cid:10)54 | −3(cid:10)77 | 0(cid:10)11 | 0(cid:10)85 | 0(cid:10)3 | 6(cid:10)59 | −0(cid:10)65 | 4.18 |
| 3. AN | 69 |  | 84 | 0(cid:10)35 | 1(cid:10)79 | 0(cid:10)67 | 3(cid:10)92 | 5(cid:10)9 | 6(cid:10)59 | −0(cid:10)38 | 5.00 |
| 4. AXP | 48 |  | 90 | −0(cid:10)08 | −0(cid:10)50 | 0(cid:10)04 | 0(cid:10)28 | 0(cid:10)0 | 10(cid:10)93 | −0(cid:10)12 | 4.51 |
| 5. BA | 58 |  | 94 | 0(cid:10)17 | 1(cid:10)65 | 0(cid:10)29 | 3(cid:10)21 | 3(cid:10)8 | 9(cid:10)16 | −0(cid:10)14 | 4.54 |
| 6. BAC | 77 |  | 88 | 0(cid:10)13 | 1(cid:10)13 | 0(cid:10)52 | 5(cid:10)29 | 9(cid:10)9 | 10(cid:10)48 | −0(cid:10)44 | 3.99 |
| 7. BEL | 79 |  | 72 | −0(cid:10)89 | −4(cid:10)86 | −0(cid:10)21 | −1(cid:10)28 | 0(cid:10)7 | 7(cid:10)09 | −0(cid:10)68 | 5.62 |
| 8. BMY | 74 |  | 86 | 0(cid:10)22 | 1(cid:10)73 | 0(cid:10)63 | 5(cid:10)68 | 11(cid:10)1 | 7(cid:10)42 | −0(cid:10)46 | 4.46 |
| 9. CCI | 69 |  | 92 | −0(cid:10)01 | −0(cid:10)06 | 0(cid:10)25 | 2(cid:10)98 | 3(cid:10)3 | 12(cid:10)71 | −0(cid:10)28 | 3.88 |
| 10. DD | 69 |  | 92 | −0(cid:10)00 | −0(cid:10)04 | 0(cid:10)24 | 2(cid:10)77 | 2(cid:10)9 | 8(cid:10)39 | −0(cid:10)26 | 3.87 |
| 11. DIS | 62 |  | 98 | −0(cid:10)09 | −1(cid:10)28 | 0(cid:10)04 | 0(cid:10)61 | 0(cid:10)2 | 10(cid:10)17 | −0(cid:10)13 | 3.18 |
| 12. F | 58 |  | 93 | 0(cid:10)05 | 0(cid:10)39 | 0(cid:10)16 | 1(cid:10)55 | 0(cid:10)9 | 11(cid:10)02 | −0(cid:10)13 | 3.98 |
| 13. GE | 88 |  | 87 | −0(cid:10)08 | −0(cid:10)97 | 0(cid:10)41 | 5(cid:10)37 | 10(cid:10)0 | 7(cid:10)60 | −0(cid:10)53 | 3.90 |
| 14. GM | 56 |  | 95 | −0(cid:10)01 | −0(cid:10)15 | 0(cid:10)07 | 1(cid:10)00 | 0(cid:10)4 | 11(cid:10)07 | −0(cid:10)09 | 3.53 |
| 15. HWP | 61 |  | 96 | 0(cid:10)18 | 2(cid:10)48 | 0(cid:10)32 | 5(cid:10)06 | 9(cid:10)0 | 11(cid:10)85 | −0(cid:10)17 | 2.33 |
| 16. IBM | 43 |  | 98 | 0(cid:10)27 | 3(cid:10)92 | 0(cid:10)20 | 3(cid:10)47 | 4(cid:10)5 | 10(cid:10)49 | 0(cid:10)04 | 2.89 |
| 17. JNJ | 65 |  | 91 | 0(cid:10)28 | 2(cid:10)36 | 0(cid:10)52 | 5(cid:10)20 | 9(cid:10)6 | 8(cid:10)49 | −0(cid:10)30 | 4.12 |
| 18. KO | 87 |  | 82 | −0(cid:10)21 | −1(cid:10)93 | 0(cid:10)32 | 3(cid:10)44 | 4(cid:10)4 | 8(cid:10)27 | −0(cid:10)56 | 4.48 |
| 19. MCD | 71 |  | 85 | −0(cid:10)34 | −2(cid:10)22 | 0(cid:10)07 | 0(cid:10)51 | 0(cid:10)1 | 8(cid:10)51 | −0(cid:10)41 | 5.18 |
| 20. MCQ | 53 |  | 91 | −0(cid:10)09 | −0(cid:10)81 | 0(cid:10)05 | 0(cid:10)48 | 0(cid:10)1 | 12(cid:10)18 | −0(cid:10)15 | 3.78 |
| 21. MMM | 85 |  | 95 | 0(cid:10)03 | 0(cid:10)40 | 0(cid:10)36 | 5(cid:10)55 | 10(cid:10)7 | 7(cid:10)27 | −0(cid:10)36 | 3.28 |
| 22. MOB | 77 |  | 88 | −0(cid:10)15 | −1(cid:10)43 | 0(cid:10)22 | 2(cid:10)54 | 2(cid:10)4 | 6(cid:10)47 | −0(cid:10)39 | 3.47 |
| 23. MRK | 51 |  | 86 | −0(cid:10)43 | −2(cid:10)65 | −0(cid:10)24 | −1(cid:10)76 | 1(cid:10)2 | 9(cid:10)38 | −0(cid:10)16 | 4.41 |
| 24. NT | 37 |  | 93 | 0(cid:10)16 | 1(cid:10)07 | 0(cid:10)18 | 1(cid:10)40 | 0(cid:10)8 | 10(cid:10)44 | −0(cid:10)04 | 4.03 |
| 25. PEP | 72 |  | 87 | −0(cid:10)04 | −0(cid:10)26 | 0(cid:10)33 | 2(cid:10)78 | 2(cid:10)9 | 8(cid:10)67 | −0(cid:10)39 | 5.87 |
| 26. SLB | 50 |  | 94 | 0(cid:10)13 | 1(cid:10)11 | 0(cid:10)19 | 1(cid:10)82 | 1(cid:10)3 | 8(cid:10)74 | −0(cid:10)07 | 3.09 |
| 27. T | 78 |  | 76 | −0(cid:10)76 | −4(cid:10)75 | −0(cid:10)14 | −1(cid:10)01 | 0(cid:10)4 | 7(cid:10)28 | −0(cid:10)61 | 6.10 |
| 28. WMT | 70 |  | 88 | 0(cid:10)20 | 1(cid:10)53 | 0(cid:10)53 | 4(cid:10)78 | 8(cid:10)2 | 10(cid:10)34 | −0(cid:10)38 | 4.18 |
| 29. XON | 83 |  | 82 | −0(cid:10)25 | −1(cid:10)42 | 0(cid:10)31 | 2(cid:10)07 | 1(cid:10)6 | 5(cid:10)93 | −0(cid:10)58 | 5.49 |
| 30. XRX | 77 |  | 93 | −0(cid:10)09 | −1(cid:10)19 | 0(cid:10)22 | 3(cid:10)40 | 4(cid:10)3 | 9(cid:10)27 | −0(cid:10)33 | 2.50 |
| 31. OEX | 100 |  |  |  |  |  |  |  | 5(cid:10)56 | −1(cid:10)09 | 3.99 |
|  | For each of the 30 stocks and the S&P 100, |  |  |  | the table reports three sets of numbers relating to the weekly risk-neutral moments |  |  |  |  |  |  |
| estimated. In the ﬁrst |  |  | two columns, we report (i) the percentage of observations for which SKEWn < 0, and (ii) the percentage |  |  |  |  |  |  |  |  |
|  | of observations for which the risk-neutral skewness of the stock, SKEWn, |  |  |  |  |  | is more than the risk-neutral skewness of the market, |  |  |  |  |
|  | SKEWm (i.e., less negative than the risk-neutral index skewness). The next ﬁve columns present the results of an OLS regression: |  |  |  |  |  |  |  |  |  |  |
|  | SKEWn(cid:1)t(cid:2) = (cid:21)0 + (cid:21)1SKEWm(cid:1)t(cid:2) + (cid:29)(cid:1)t(cid:2), where (cid:21)0, (cid:21)1 are the intercept and sensitivity coefﬁcients, respectively; t(cid:1)(cid:21)0(cid:2)(cid:3) t(cid:1)(cid:21)1(cid:2) |  |  |  |  |  |  |  |  |  |  |
|  | are the t-statistics, and R2 |  | is the coefﬁcient of determination (in percent). The last |  |  |  |  | three columns display the average estimate |  |  |  |
| of | the risk-neutral volatility, skew, and kurtosis (with one exception, all moments are statistically signiﬁcant and omitted). The |  |  |  |  |  |  |  |  |  |  |
| volatility is | the square root of |  |  | the variance contract, |  | reported in percent. All moments used are of |  |  |  | short-term maturity. The |  |

Raw CSV: `assets/table_008.csv`

### Table 9

*Caption:* Table 7

|  |  |  |  |  |  |  | E(cid:9) ˆ(cid:29)(cid:1)t + 1(cid:2) ⊗ (cid:4)(cid:1)t(cid:2)(cid:11) = 0 |  |  |  |  | E(cid:9) ˜(cid:29)(cid:1)t + 1(cid:2) ⊗ (cid:4)(cid:1)t(cid:2)(cid:11) = 0 |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | Size |  |  |  |  |  |  |  |  |  |  |  |  |
| (cid:4)(cid:1)t(cid:2) |  |  |  |  | (cid:15) |  |  |  | (cid:5) | p |  |  | (cid:5) | p |
|  |  | (days) | df |  |  |  | t((cid:15)) |  | T |  | (cid:15)0 | t((cid:15)0) | T |  |
|  | Panel A: Risk-neutral OEX skews from 86-day options |  |  |  |  |  |  |  |  |  |  |  |  |  |
| SET 1 |  | 350 | 1 |  | 2(cid:10)26 |  | 2.11 |  | 7(cid:10)60 | 0.005 | 12(cid:10)01 | 4.46 | 7.33 | .006 |
|  |  | 400 | 1 |  | 2(cid:10)08 |  | 2.32 |  | 4(cid:10)69 | 0.030 | 11(cid:10)20 | 2.93 | 4.87 | .027 |
|  |  | 450 | 1 |  | 1(cid:10)76 |  | 2.48 |  | 3(cid:10)77 | 0.052 | 9(cid:10)82 | 3.09 | 3.99 | .045 |
| SET 2 |  | 350 | 2 |  | 2(cid:10)29 |  | 1.97 |  | 10(cid:10)93 | 0.004 | 15(cid:10)99 | 2.66 | 8.86 | .011 |
|  |  | 400 | 2 |  | 2(cid:10)25 |  | 2.22 |  | 6(cid:10)96 | 0.030 | 12(cid:10)08 | 2.85 | 6.52 | .038 |
|  |  | 450 | 2 |  | 1(cid:10)99 |  | 2.40 |  | 4(cid:10)26 | 0.118 | 10(cid:10)85 | 3.01 | 4.52 | .104 |
| SET 3 |  | 350 | 3 |  | 11(cid:10)39 |  | 2.67 |  | 7(cid:10)01 | 0.071 | 22(cid:10)32 | 2.78 | 7.44 | .059 |
|  |  | 400 | 3 |  | 1(cid:10)76 |  | 2.16 |  | 11(cid:10)15 | 0.010 | 20(cid:10)23 | 2.95 | 6.17 | .103 |
|  |  | 450 | 3 |  | 1(cid:10)89 |  | 2.35 |  | 6(cid:10)70 | 0.082 | 11(cid:10)52 | 2.97 | 5.59 | .133 |
|  | Panel B: Risk-neutral OEX skews from 58-day options |  |  |  |  |  |  |  |  |  |  |  |  |  |
| SET 1 |  | 350 | 1 |  | 2(cid:10)09 |  | 2.64 |  | 13(cid:10)97 | 0.000 | 11(cid:10)95 | 3.63 | 8.90 | .000 |
|  |  | 400 | 1 |  | 1(cid:10)91 |  | 2.80 |  | 7(cid:10)81 | 0.005 | 9(cid:10)35 | 3.64 | 6.66 | .009 |
|  |  | 450 | 1 |  | 1(cid:10)36 |  | 3.05 |  | 8(cid:10)90 | 0.052 | 7(cid:10)25 | 3.99 | 7.77 | .005 |
| SET 2 |  | 350 | 2 |  | 3(cid:10)21 |  | 2.60 |  | 14(cid:10)63 | 0.000 | 16(cid:10)78 | 3.76 | 7.53 | .023 |
|  |  | 400 | 2 |  | 2(cid:10)12 |  | 2.67 |  | 14(cid:10)23 | 0.000 | 12(cid:10)29 | 3.67 | 8.56 | .013 |
|  |  | 450 | 2 |  | 1(cid:10)44 |  | 2.93 |  | 11(cid:10)20 | 0.003 | 8(cid:10)01 | 3.85 | 9.04 | .010 |
| SET 3 |  | 350 | 3 |  | 5(cid:10)98 |  | 2.66 |  | 9(cid:10)48 | 0.023 | 20(cid:10)87 | 3.90 | 5.66 | .129 |
|  |  | 400 | 3 |  | 2(cid:10)60 |  | 2.60 |  | 16(cid:10)95 | 0.000 | 16(cid:10)51 | 3.77 | 7.65 | .053 |
|  |  | 450 | 3 |  | 1(cid:10)59 |  | 2.89 |  | 11(cid:10)40 | 0.009 | 8(cid:10)84 | 3.78 | 8.75 | .032 |
| Consider | the | restrictions |  | imposed | by | the | power | utility | pricing | kernel: | (cid:29)(cid:1)t + 1(cid:2) ≡ SKEWm(cid:1)t + 1(cid:2) − SKEWm(cid:1)t + 1(cid:2) + |  |  |  |
|  | (cid:15)(cid:1)KURTm(cid:1)t + 1(cid:2) − 3(cid:2)STDm(cid:1)t + 1(cid:2), which is another way to express Equation (13) of Theorem 2. The risk aversion parameter, |  |  |  |  |  |  |  |  |  |  |  |  |  |
| (cid:15), | is estimated by generalized method of moments |  |  |  |  |  |  | (GMM). |  | In panels A and B, we report |  | the GMM results when the risk- |  |  |
|  | neutral market skew, SKEWm, |  |  |  | is recovered from 86-day and 58-day options, |  |  |  |  |  | respectively. Over |  | the entire sample of January |  |
|  | 1988 through December 1995 there are thus 32 (48) nonoverlapping observations for 86- |  |  |  |  |  |  |  |  |  |  | (58-) day options. We build the time |  |  |
|  | series of higher-order physical |  |  |  | return moments, STD, SKEW, and KURT, |  |  |  |  |  | from daily returns on the OEX. Thus a sample size |  |  |  |
|  | (denoted Size) of 350 days means that we go backward 350 days to construct |  |  |  |  |  |  |  |  |  | the moments. For consistency, each variable has |  |  |  |
|  | been annualized. The degrees of freedom, df, are the number of instruments, (cid:4)(cid:1)t(cid:2), minus one. In SET 1, |  |  |  |  |  |  |  |  |  |  |  | the instrumental vari- |  |
|  | ables are a constant plus SKEWm(cid:1)t(cid:2). Likewise, SET 2 (SET 3), contains SET 1 (SET 2) plus SKEWm(cid:1)t −1(cid:2) (SKEWm(cid:1)t −2(cid:2)). |  |  |  |  |  |  |  |  |  |  |  |  |  |
| For | robustness, other |  | information sets were tried; |  |  |  |  | they yielded similar |  |  | implications. The minimized value (multiplied by T ) of |  |  |  |
| the GMM criterion function, (cid:5)T , |  |  |  |  | is chi-square distributed with df. The impact of physical skews on risk-neutral skews is studied |  |  |  |  |  |  |  |  |  |
|  | by considering the ad hoc speciﬁcation ˜(cid:29)(cid:1)t + 1(cid:2) ≡ SKEWm(cid:1)t + 1(cid:2) − (cid:15)0SKEWm(cid:1)t + 1(cid:2). |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 134 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

Raw CSV: `assets/table_009.csv`

### Table 10

*Caption:* Table 7

<table>
  <tr>
    <th>The Review of Financial Studies / v 16 n 1 2003</th>
  </tr>
  <tr>
    <td>As our intent is to estimate a single coefﬁcient, (cid:15), and test the restrictions</td>
  </tr>
  <tr>
    <td>embedded within Equation (37), the GMM appears to be an attractive estima-</td>
  </tr>
  <tr>
    <td>tion method for several reasons. First, unlike return volatility, the estimates</td>
  </tr>
  <tr>
    <td>of physical skews and kurtosis require a fairly long time series and will be</td>
  </tr>
  <tr>
    <td>measured with error [Merton (1980) and Harvey and Siddique (2000)]. There-</td>
  </tr>
  <tr>
    <td>fore the market skew formulation of Equation (37) is susceptible to an errors</td>
  </tr>
  <tr>
    <td>in variables problem. Second, the return standard deviation and the excess</td>
  </tr>
  <tr>
    <td>ˆ</td>
  </tr>
  <tr>
    <td>kurtosis enter nonlinearly in Equation (37) and may be correlated with (cid:29).</td>
  </tr>
  <tr>
    <td>Finally, the minimized GMM criterion function (multiplied by T ), (cid:5) T , offers</td>
  </tr>
  <tr>
    <td>a convenient approach to assess misspeciﬁcations in Equation (37). The (cid:5) T</td>
  </tr>
  <tr>
    <td>statistic is chi-square distributed with L − 1 degrees of freedom (given L</td>
  </tr>
  <tr>
    <td>instruments).</td>
  </tr>
  <tr>
    <td>Before turning to a discussion of GMM estimation results reported in</td>
  </tr>
  <tr>
    <td>panels A and B of Table 7, some clariﬁcations are in order. First, Theorem 2</td>
  </tr>
  <tr>
    <td>applies for a particular (cid:5). We therefore generate a nonoverlapping series of</td>
  </tr>
  <tr>
    <td>risk-neutral index skews from options with maturities of 58 and 86 days.</td>
  </tr>
  <tr>
    <td>Second, estimates of physical skews and kurtosis are sensitive to the choice</td>
  </tr>
</table>

Raw CSV: `assets/table_010.csv`

## Figures

No figures extracted.

## Extraction Notes

- camelot lattice produced no usable tables; using stream output
- camelot stream failed on page 20 region 32.40,281.81,615.60,89.41: cannot unpack non-iterable NoneType object
- camelot stream failed on page 25 region 32.40,248.41,615.60,56.01: max() iterable argument is empty
