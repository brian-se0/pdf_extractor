---
paper_id: "s00780-005-0162-y"
source_file: "s00780-005-0162-y.pdf"
title: "FS162.DVI"
authors: ["Katharina Steingraeber Heidelberg 1107 1999 Jun 19 15:23:21"]
year: 2005
doi: "10.1007/s00780-005-0162-y"
page_count: 16
extracted_at: "2026-02-07T06:52:30.526161+00:00"
status: "success"
---

# FS162.DVI

## Metadata

- **Source File:** `s00780-005-0162-y.pdf`
- **Authors:** Katharina Steingraeber Heidelberg 1107 1999 Jun 19 15:23:21
- **Year:** 2005
- **DOI:** 10.1007/s00780-005-0162-y

## Abstract

Not found.

## Main Text

Finance Stochast. 9, 477–492 (2005)
DOI: 10.1007/s00780-005-0162-y
c⃝Springer-Verlag 2005
### Local martingales, bubbles and option prices
Alexander M.G. Cox1, David G. Hobson2
1 Department of Mathematics, University of York, Heslington, York YO10 5DD, UK
(e-mail: amgc500@york.ac.uk)
2 Department of Mathematical Sciences, University of Bath, Claverton Down, Bath, BA2 7AY, UK
and Department of Operations Research and Financial Engineering, Princeton University,
Princeton, NJ 08544, USA (e-mail: dgh@maths.bath.ac.uk)
Abstract. In this article we are interested in option pricing in markets with bubbles. A bubble is deﬁned to be a price process which, when discounted, is a local
martingale under the risk-neutral measure but not a martingale. We give examples
of bubbles both where volatility increases with the price level, and where the bubble
is the result of a feedback mechanism. In a market with a bubble many standard
results from the folklore become false. Put-call parity fails, the price of an American call exceeds that of a European call and call prices are no longer increasing
in maturity (for a ﬁxed strike). We show how these results must be modiﬁed in the
presence of a bubble. It turns out that the option value depends critically on the
deﬁnition of admissible strategy, and that the standard mathematical deﬁnition may
not be consistent with the deﬁnitions used for trading.
Key words:
Bubbles, feedback, local martingales, derivative pricing, put-call
parity
JEL Classiﬁcation: G13, D84
Mathematics Subject Classiﬁcation (2000): 91B70, 60G44, 60G40
1 Introduction
The last few decades have seen a spectacular growth in the trading of ﬁnancial
securities and derivatives, and a spectacular growth in the sophistication of the
mathematical tools used by traders. They have also been associated with a series
The second author is supported by an Advanced Fellowship from the Epsrc. Thanks are due to Matt
Davison, Jonathan Evans and Walter Schachermayer and an anonymous referee for helpful comments
and for suggesting references to the literature.
Manuscript received: August 2004; ﬁnal version received: March 2005

478
of bubbles and crashes where systematic over-pricing was followed by market
corrections, often with serious adverse consequences for investors. The purpose of
this article is to consider a class of models of a pricing bubble, and more importantly
to consider the implications for option pricing within that class.
In economic terms a bubble is a deviation between the trading price of an asset
and its underlying value. The problem with this deﬁnition, and the reason why
bubbles are difﬁcult to spot until they have burst, is that it depends on the elusive
concept of underlying value. In his classic text ‘A random walk down Wall Street’
Malkiel [20] outlines two basic theories which describe how ﬁnancial assets are
assigned value. The ﬁrst, called the ‘ﬁrm-foundation’ theory, attempts to deﬁne an
intrinsic value for a share via an analysis of the balance sheet, the expected future
dividends and the growth prospects of a company. The second, sometimes called
the ‘castle-in-the-air’ or ‘greater-fool’ theory, says that an asset is worth whatever
another investor will pay for it.
Within this framework there have been numerous attempts to explain why bubbles may arise. Some explanations fall under the general heading of ‘Irrational
exuberance’ (Shiller [21]), and attempt to explain the mispricing in terms of investor psychology and herd behaviour. Indeed Shiller [22] also takes issue with the
description of such behaviour as ‘irrational’, preferring to place the emphasis on
human shortcomings rather than human error. One explanation he gives for speculative bubbles is that price increases in a stock lead to increased enthusiasm for,
and attention upon, that stock, which in turn leads to increased demand. Further
price increases follow in a feedback mechanism. Alternatively the price bubble can
be seen as desirable for risk-loving (compared to the rest of the market) investors
since there is the potential for much larger gains to be made.
In this work we are interested in the consequences of bubbles for derivative
pricing. We want to remain within the mathematical paradigm of no-arbitrage,
and for this reason we will assume the existence of an equivalent local martingale
measure.The key fact is that we will assume that under the pricing measure the asset
price is a strict local martingale. This is the sense in which our price process satisﬁes
a bubble – the current price exceeds the expected discounted future price (under the
risk-neutral measure). To a certain extent this work is expository in nature, and the
new mathematics is conﬁned to Theorem 4.3 and LemmaA.2. Instead the emphasis
is on interpretation and re-interpretation of existing models and results.
Let S denote the discounted trading price of an asset. Suppose that under the
pricing measure Q, the price process is a local martingale. Since S is non-negative
it is a supermartingale. We are interested in the consequences of assuming that S is
not a martingale. In particular, we want to consider whether some basic properties of
derivative prices remain valid: does put-call parity hold, areAmerican and European
prices the same for convex payoffs, do call prices tend to zero as strike increases
to inﬁnity, and, for diffusion models, are call prices convex in the underlying? The
counter-intuitive answer to each of the above questions turns out to be no.
Some of the above questions were asked in the book by Lewis [19] and a paper of
Heston et al. [15]. Lewis makes an extensive study of the option pricing PDE when
the underlying is a local martingale, and makes the key observation that this PDE
may have multiple solutions. Heston et al. [15] place an economic interpretation

479
on these results and our deﬁnition of a bubble is taken from that paper. The main
distinction between this paper and [19] and [15] is that we deﬁne the option price
(in the standard mathematical fashion) as the cheapest initial fortune with which
it is possible to super-replicate the option. In contrast, Lewis asserts that the price
is given by a different formula, whereas Heston et al. propose a range of prices at
which the option might trade. A further difference is that Lewis and Heston et al.
use a PDE approach in a Markovian setting, whereas we express results in terms
of local martingales and stochastics.
In Sect. 2 we give some examples of bubbles, both from ﬁnancial history and
in mathematical terms via strict local martingales. One of the examples has a direct
interpretation in terms of a bubble via a feedback mechanism.
In Sects. 3, 4 and 5 we review some of the implications of our deﬁnitions and
give several characterisations of the presence of a bubble. In Sect. 3 we show that
many standard results from the folklore (such as put-call parity) fail to hold when
there is a bubble. We then discuss some of the interesting conclusions which can
be derived. In Sect. 4 we show that although call prices are not strictly increasing
in maturity (for ﬁxed strike) it is possible to derive static no-arbitrage restrictions
which relate prices for calls with maturity T to calls with maturity T ′.
One of the key ideas is the notion of an admissible strategy, and in Sect. 5
we discuss the ways in which the price of a derivative depends on the rules for
option trading imposed by internal or external regulation. Some of these issues also
arise in martingale models, including the Black-Scholes model, but they are much
more apparent in a strict local martingale model where the prices of American and
European options differ. For this reason the study of models with bubbles is very
useful for the light it throws upon the issues of admissibility and arbitrage.
2 Examples
2.1 Examples of bubbles from history
There are many famous episodes in ﬁnancial history of bubbles in prices. One of the
earliest examples was the Dutch tulip mania in the 17th century. Speculative trading
in tulip bulbs led ﬁrst to astronomical increases in prices (there was a twenty-fold
increase in prices in January 1637) and then, in February 1637, to a massive crash.
See Malkiel [20] for more details on this and other examples.
In the 20th century ﬁnancial markets (and other markets such as property)
were subject to a series of bubbles and crashes. The Roaring Twenties, the sixties
technology bubble, the roaring eighties, the Internet bubble of the 1990s – in each
case (over)-optimism about a new era of progress and wealth generation led to
a speculative growth in stock prices and a subsequent market correction. Recent
instances of pricing bubbles leading to violations of, for example, put-call parity
include Palm and RJR Nabisco.We refer the reader to Heston et al. [15] for a further
discussion.

480
2.2 Examples of bubbles from mathematics
Let S be the discounted price of a ﬁnancial security. We assume throughout that
S is continuous, though it is clear that many of the arguments can be extended
to the jump case. No-arbitrage theory tells us that S is a local martingale under
the pricing measure. More precisely, for locally bounded semi-martingale price
processes, there is no-free-lunch-with-vanishing-risk if and only if there exists an
equivalent local martingale measure (Delbaen and Schachermayer [10]). Note that
we specify models under the pricing measure rather than the physical measure. In
this way we sidestep the issue of whether an equivalent local martingale measure
exists.
For most examples (such as the Black-Scholes model) S is a martingale. However, for some models the price process is a local martingale, but not a true martingale. We will use the term strict local martingale to refer to the fact that S is a local
martingale, but not a martingale. Note that, since S is non-negative we must have
that S is a supermartingale.
Deﬁnition 2.1 The price process S has a bubble if S is a strict local martingale
under the risk-neutral measure Q.
The key fact is that simply because S is a strict local martingale does not mean
that there are arbitrage opportunities. In particular, the strategy of selling the asset
short may not be admissible, since the liability is unbounded.
2.2.1 Time inhomogeneous models
Throughout we suppose that t is the current time. Suppose St = s > 0 and
Su
dSu =
T −udBu.
√
Then Su = s exp( ˜BAu −Au/2) where ˜B is a Brownian motion with ˜Bt = 0, and
Au = −ln(1 −(u −t)/T). The process is a true martingale over [t, u] for each
u < T, but ST = 0, almost surely.
2.2.2 CEV models
Let S solve St = s > 0, dSu = Sα
u dBu for α > 1. As Lewis [19] observes, in this
case S is a strict local martingale.
If α = 2 then it is possible to write down simple expressions for the transition
density of the process. (When α = 2, we have that S is the reciprocal of the
radial part of 3-dimensional Brownian motion. This is the classical example, due
to Johnson and Helms, of an L2-bounded strict local martingale, and some of
the implications for no-arbitrage pricing theory have already been investigated by
Delbaen and Schachermayer [9].) We have
P(ST ∈dz) = s
dz

z3
2π(T −t)





−(1/z + 1/s)2
−(1/z −1/s)2
.
−exp
×
exp
2(T −t)
2(T −t)

481
It follows that



1
1 −2Φ
E[ST |Su] = ∆(Su, u) = Su
.
√
−
Su
T −u
Note that ∆(Su, u) is a true martingale, and moreover



1
d∆(Su, u) =
dSu = ∆(Su, u)SudBu.
1 −2Φ
√
−
Su
T −u
2.2.3 Stochastic volatility models
Consider the following stochastic volatility model, ﬁrst proposed by Hull and
White [18], under which the non-negative volatility process follows an exponential
Brownian motion:
dSu = SuVudBS
u ,
dVu = ηVudBV
u + µVudu.
Here the dynamics are speciﬁed under a risk-neutral measure Q, BS and BV are
Brownian motions with correlation ρ, and the initial values St and Vt are known
positive constants. (The original Hull-White model took ρ = 0, but the extension to

constant ρ is straight-forward.)Write BV = ρBS+ρ⊥B⊥where ρ⊥= +
1 −ρ2
and B⊥is a Brownian motion orthogonal to BS.
This model is incomplete, except when |ρ| = 1, and to that extent it falls outside
the general philosophy of this article, but it still gives interesting examples of strict
local martingales when ρ is positive, as we now show.
The following argument is essentially due to Sin [23], and can be applied to
other stochastic volatility models. We want to decide whether S is a true martingale
or a strict local martingale. Suppose S is a true martingale. Then we can deﬁne
a probability measure P, equivalent to Q, via dP/dQ = ST /St. By Girsanov’s
theorem, under P, the process BS,P deﬁned via dBS,P
= dBS
u −Vudu is a Brownian
u
motion. Further, under P, V solves
dVu = ηVu(ρdBS,P
+ ρ⊥dB⊥
u ) + (µVu + ηρV 2
u )du.
u
If ηρ > 0 then this process explodes to plus inﬁnity in ﬁnite time. Since V does
not explode under Q, this contradicts the assumption that P and Q are equivalent.
Hence, when ηρ > 0, S is a strict local martingale.
2.2.4 Complete-market models of stochastic volatility
Consider the case of a complete stochastic volatility model (Hobson and
Rogers [17], Davis [8]) where the underlying and the volatility are driven by the
same Brownian motion.
As a ﬁrst and simple example, suppose that under the pricing measure Q
dSu = SuVudBu,
dVu = V 2
u dBu

482
and St = Vt = s. Then (one solution is) Su = Vu, for all u ≥t, and since V is a
strict local martingale, so is S (this is the CEV model of Sect. 2.2.2).
The next example is adapted from [17] and is a model of a speculative feedback
bubble. Suppose that dSu = SuVudBu where Vu = η(Σu) and Σ is given by
 ∞
 ∞
λe−λr ln(Su/Su−r)dr = Su −
λe−λr ln(Su−r)dr.
Σu =
0
0
The idea is that Σ is a measure of the displacement between the current price level
and its past average, and that the volatility of future stock price movements are a
function of this displacement. (Here Σ is a proxy for the amount of attention the
stock receives.) Then,


λΣu + 1
2η(Σu)2
du.
dΣu = η(Σu)dBu −
If S is a true martingale under Q then ST /St is the density with respect to Q of an
equivalent measure P, and then under P,


λΣu −1
2η(Σu)2
dΣu = η(Σu)dBP
du.
u −
If η(Σ)2 = (1 + Σ2) the behaviour of Σ is different under the two sets of
dynamics: in one case it explodes to minus inﬁnity, and in the other it explodes to
plus inﬁnity. Hence Q and P are not equivalent, S is not a true martingale, and the
price process S has a speculative feedback bubble.
2.2.5 Bubbles in the Black-Scholes world
Suppose that S is an exponential Brownian motion with unit volatility.
For real x and positive r deﬁne

x2n
v(x, r) =
(2n)!h(n)(r).
n≥0
Here h(n) denotes the nth derivative of h, and h is any non-negative (and not
identically zero) function for which h and and all its derivatives at 0 are zero. The
canonical example is h(r) = e−1/r. Note that v as deﬁned solves the heat equation
vxx = vr with zero initial condition v(x, 0) = 0. Now set


ln Su, T −u
,
Yu = Λ(Su, u) = S1/2
e−(T −u)/8v
(1)
u
2
so that dYu = Λ′(Su, u)dSu where Λ′ denotes the space derivative. The process
Y is a local martingale for which YT = 0, almost surely.
We can think of Y as a degenerate price for the derivative security with payoff
zero at expiry. Further it is possible to add Y to the price process of any derivative to
create a new price process with bubble-like characteristics.We return to a discussion
of this example at the end of Sect. 5.

483
2.3 Alternative deﬁnitions of bubbles
Although Deﬁnition 2.1 captures many of the essential features of bubbles, it is not
the only deﬁnition used in the literature. For example, Andersen and Sornette [1]
propose a model with exponential growth followed by a downward jump (or crash)
at an unpredictable stopping time. Much closer in spirit to this work is the paper
by Cassese [6]. Recall that we work under the risk neutral measure Q, which we
assume to exist and to be equivalent to the real-world measure, here denoted R.
Cassese works under R, and considers the situation where Z is a strict local Rmartingale, where Z is the candidate change of measure density. In particular,
there is no equivalent local martingale measure Q: instead Z can be used to deﬁne
a ﬁnitely additive measure. In that sense the paper of Cassese might be described as
a discussion of the no-arbitrage condition rather than bubbles (see Sect. 5 of [6]).
However, many of the conclusions which we derive have parallels in situations
considered by Cassese. For example, Theorem 3.4(iii) should be compared with
Example 9.2 of Fernholz et al. [13]. In their model of a weakly diverse market
Fernholz et al. show that put-call parity fails. However, this is a consequence of
the fact that the candidate Girsanov change of measure martingale is a strict local
martingale, and that the model contains a free-lunch-with-bounded-risk, rather than
a bubble in the sense of Deﬁnition 2.1.
3 European and American options
We work on a probability space (Ω, F, Ft, Q), where T∞is the terminal date of
the economy and FT∞= F. Deﬁned on this space there is a complete market
model of a traded asset with continuous (discounted) price process S, so that by
assumption any Q-local martingale can be written as a stochastic integral of a
predictable process θ with respect to S.
Consider an option on the traded asset with non-negative payoff H ≡H(ST ),
and expiry T < T∞. We are interested in the problem of pricing the derivative H
from the point of view of a ﬁnancial institution which is considering the sale of the
derivative.
We begin by deﬁning the set of admissible strategies available to this institution.
Deﬁnition 3.1 An admissible wealth process is a self-ﬁnancing process W of the
form Wu = Wt +(θ ·S)u, where θ is a predictable S-integrable process, such that


k kQ
u∈[t,T ] Wu < −k
= 0.
lim
inf
The set W of admissible wealth processes contains as subsets the sets
W+ = {Wu : Wu ≥0, ∀u ∈[t, T], a.s.},

{Wu : Wu ≥−a, ∀u ∈[t, T], a.s.},
Wf =
a
Wmg = {Wu : Wu ≥Mu, ∀u ∈[t, T], for some martingale M }.

484
Each of these sets has been proposed as an appropriate deﬁnition of admissibility
(Harrison and Pliska [14], Dybvig and Huang [11],Ansel and Stricker [2]).The need
for some restriction to rule out doubling strategies was ﬁrst observed in [14]. Our
formulation is due to Strasser [24]. The key point is that by any of these deﬁnitions
an admissible wealth process is a Q-supermartingale.
Given a deﬁnition of admissible strategies, it is now possible to deﬁne (in
the standard mathematical fashion) the fair price for a derivative. We recall this
deﬁnition here, since later we will discuss alternative deﬁnitions.
Deﬁnition 3.2 The fair price of a derivative security is the smallest initial fortune
required to ﬁnance an admissible super-replicating wealth process.
t (H) of a European option with payoff H is
Theorem 3.3 The time-t fair price V E
given by
V E
t (H) = Et[H(ST )]
and the fair price V A
t (H) of an American option is given by
V A
t (H) =
Et[H(Sτ)].
sup
t≤τ≤T
u (H) = Eu[H(ST )] is a (super)-
Proof The proof is based on the fact that V E
martingale which super-replicates the option payout, and can be shown to be the
smallest such process. Since H is non-negative it is admissible by the complete
□
market assumption. The American option can be treated similarly.
When H(x) = (x−K)+ for some K ≥0 we write CE
t (K) and CA
t (K) for the
European and American call prices. Similarly, we denote the prices of put options
by P E
t (K) and P A
t (K).
Suppose, temporarily, that S is a true martingale. It follows from the identity
(ST −K)+ −(K −ST )+ = ST −K
(2)
that put-call parity holds:
CE
t (K) −P E
t (K) = St −K.
(3)
Now consider options with a general non-negative convex payoff H. Jensen’s inequality tells us that it is never optimal to exercise the American option before
maturity, and that
V E
t (H) = V A
t (H)
∀H ≥0, H convex.
(4)
If S is a strict local martingale, then both of the statements (3) and (4) are false.
Instead we have the following result:
Theorem 3.4 The local martingale S has a bubble if and only if any of the following
conditions holds:

485
S is a strict supermartingale;
(i)
(ii) Et[ST ] < St, so that the forward price is below the current price;
(iii) CE
t (K) −P E
t (K) < St −K for some K, so that put-call parity fails;
(iv) limK↑∞P E
t (K) −K + St > 0;
CE
t (K) < CA
t (K) for some K, so that American calls are more expensive
(v)
than their European counterparts;
(vi) limK↑∞CA
t (K) > 0.
In all these cases CA
t (K) −CE
t (K) = St −Et(ST ) > 0 which is independent of
K, so that if (iii) or (v) holds for some K then it holds for all K.
Another necessary and sufﬁcient condition for a bubble is that
kQ
Su > k
> 0,
lim sup
sup
(5)
k
u∈[t,T ]
Proof By deﬁnition S has a bubble if (i) holds. Further, if S is a non-negative
local martingale then S is a supermartingale and (ii) is a necessary and sufﬁcient
condition for S to be a strict supermartingale. The equivalence of (ii) and (iii)
follows on taking expectations in (2).
Note that P E
t (K)−K +St = St −Et[ST ]+CE
t (K). By deﬁnition CE
t (K) =
Et[(ST −K)+] which tends to zero as K ↑∞, so that (iv) if and only if (ii).
The ﬁnal condition is taken from Az´ema et al. [3].
To complete the proof, and to prove (v) ⇔(ii) ⇔(vi) it is sufﬁcient to apply
Theorem A.1 with G(x) = (x −K)+.
□
Example 3.5 ConsidertheexamplegiveninSect.2.2.1.ThenST = 0almostsurely,
and CE
t (K) = 0, P E
t (K) = K. Hence put-call parity fails. Also, by comparison
with holding the stock we immediately see that CA
t (K) ≤s; equality follows from
considering the ﬁrst-hitting times of levels n.
Example 3.6 Suppose dSt = S2
t dBt. Then
E[(ST −K)+] = St {Φ(κ −δ) −Φ(−δ) + Φ(δ) −Φ(δ + κ)}
Φ(κ + δ) −Φ(δ −κ) + δ−1 [Φ′(κ + δ) −Φ′(κ −δ)]
−K
√
√
where δ−1 = St
T −t, κ−1 = K
T −t and Φ and Φ′ are the cumulative normal
distribution and density respectively.
Note that


2
1
s↑∞E[(ST −K)+] =
.
−K
2Φ

√
T −t −1
lim
K
2π(T −t)
so that the price of a call option is bounded when considered as a function of St.
Example 3.6 can also be used as a counter-example to another standard result
from the folklore of option pricing. Suppose S is a diffusion process. There are
several proofs (Bergman et al. [4] via PDEs, El Karoui et al. [12] via stochastic
ﬂows, Hobson [16] via coupling) that subject to certain regularity conditions, the
price of an option with a convex payoff is convex in S. Example 3.6 shows that this
can fail when S is a strict local martingale; the European price of an option with
convex payoff H(ST ) = ST is not convex in s.

486
4 Prices at intermediate times
Given time-t call prices with maturity T, what are the possible call prices at time
T ′ consistent with no arbitrage? Rather than specify a model and ﬁnding a modelspeciﬁc solution, we will consider the problem from the point of view of a ﬁnancial
institution which observes traded call prices. The only assumption we make is that
these observed prices are consistent with some model and are deﬁned according to
the formulas in Theorem 3.3.
Since call prices are now also a function of the maturity of the option we write
CE
= CE
t (K, T). For a ﬁxed time T, if call prices are given by Deﬁnition 3.2,
t
then CE
t (K, T) is decreasing and convex in K. If these conditions fail then there
is a simple static strategy (e.g. a spread or a butterﬂy spread) which can be used to
generate arbitrage. Conversely, if there is a model under which the asset price is a
local martingale and under which the expected call payoffs are given by CE
t (K, T),
then there is no static portfolio of investments in the calls which can be used to
generate arbitrage.
Deﬁnition 4.1 There is no static arbitrage in the family of call prices
{CE
t (Kα, Tα); α ∈A} if there is a model for which S is a non-negative local
martingale, and under which call prices with strikes Kα and maturities Tα are
given by CE
t (Kα, Tα).
If S is a true martingale then call prices are increasing in T. It is well known
that if t < T ′ < T then a necessary and sufﬁcient condition for there to be no static
arbitrage in the pair of call price functions
t (K, T); K′ ≥0, K ≥0}
t (K′, T ′), CE
{CE
t (K′′, T ′′) – for T ′′ equal to each of T, T ′ – is a decreasing, convex funcis that CE
tion of K′′ with CE
t (0, T ′′) = St and limK′′↑∞CE
t (K′′, T ′′) = 0, and together
they satisfy (St −K)+ ≤CE
t (0, T ′) ≤CE
t (0, T). However, it is easy to see from
the example of a call with strike zero that this is no longer true when S is a strict
supermartingale.
Instead the following result is true:
Theorem 4.2 Fix t < T ′ < T. There is no static arbitrage provided CE
t (K, T ′)
and CE
t (K, T) are decreasing convex functions of K with zero limit at strike inﬁnity,
0 ≤CE
t (0, T) ≤CE
t (0, T ′) ≤St and
(St−K)+−St+CE
t (0, T ′) ≤CE
t (K, T ′) ≤CE
t (K, T)−CE
t (0, T)+CE
t (0, T ′),
or equivalently
(St −K)+ −St ≤CE
t (K, T ′) −Et(ST ′) ≤CE
t (K, T) −Et(ST ).
Given the relationships between puts and calls, the theorem will follow immediately from the following theorem.

487
Theorem 4.3 Fix t < T ′ < T. There is no static arbitrage provided P E
t (K, T ′)
and P E
t (K, T) are non-negative, increasing, convex functions of K with
(K −St)+ ≤P E
t (K, T ′) ≤P E
t (K, T) ≤K.
(6)
Proof We need to show that (6) is both necessary, and, in combination with the
other conditions, sufﬁcient. Necessity follows from the following argument using
monotonicity and Jensen:
P E
t (K, T ′) = Et[(K −ST ′)+] ≤Et[(K −ET ′[ST ])+] ≤Et[(K −ST )+],
together with an equally trivial argument for the lower bound.
Now we need to show sufﬁciency.To do this we give a model which is consistent
with the given put price functions. We are going to do this over the interval [T ′, T],
but it is clear we could repeat the construction over [t, T ′] and by concatenation we
have a model which prices correctly at t, T ′ and T.
t (K,T)=Et[(K−ST )+]
BytheresultsofBreedenandLitzenberger[5],givenP E
it is possible to infer the time-T law of S from the relationship P E
t (K, T) =
Et[(K −ST )+]. Denote the laws of ST ′ and ST by µ0 and µ1 respectively. Let mi
 ∞
denote the mean of µi, so that m1 ≤m0. Deﬁne Pi(k) =
0 (k −x)+µi(dx), so
that P0(k) = P E
t (k, T ′) for example. We are going to construct a local martingale
process Yu deﬁned on [0, 1] such that Y0 ∼µ0 and Y1 ∼µ1.
If m0 = m1 then P0(k) ≤P1(k), uniformly in k, and this is exactly the
necessary and sufﬁcient condition for there to exist a martingale with the desired
initial and terminal laws. Indeed there are many solutions to the Skorokhod embedding problem (for an example see Chacon and Walsh [7]) which describe how to
construct a martingale (speciﬁcally a time-change of Brownian motion) for which
Y0 ∼µ0 and Y1 ∼µ1.
So suppose m1 < m0. Let z be the unique positive root of F where F(k) =
k −m1 −P0(k). Fix ϵ ∈(0, 1) and deﬁne the increasing convex function Pϵ by

P0(k)
k < z
Pϵ(k) =
k ≥z
k −m1
Let µϵ be the probability measure associated with Pϵ in the sense of Breeden and
Litzenberger.
We plan to construct Y such that Y is a non-negative local martingale, Y0 ∼µ0,
Yϵ ∼µϵ and Y1 ∼µ1.
Let B be a Brownian motion with B0 ∼µ0 and deﬁne τ = inf{r : Br ≤z}.
Then Bτ ∼µϵ, and, for u ≤ϵ we set Yu = Bτ∧(ϵ−u)−1.
For the ﬁnal part, note that mϵ = m1 and Pϵ(k) ≤P1(k). Hence, we can
use any martingale solution to the Skorokhod embedding problem to generate a
suitable continuation Yu.
□

488
5 European calls with collateral requirements
When the underlying price process is a local martingale, but not a martingale, the
price process is necessarily unbounded above. Indeed, it must be the case that
lim sup xQ(sup0≤t≤T St > x) > 0, recall (5). In these cases Heston et al. [15]
argue that the standard mathematical deﬁnition of the European option price of
Deﬁnition 3.2 is not the economically meaningful one.
Consider a call option in one of the models described in Sect. 2.2. In a strict
local martingale model there is a probability of order 1/n that the value of the
underlying will rise to n, at which point the intrinsic value of the option will be
large. Most exchanges require traders who are short options to post collateral in
such circumstances. Even though the trader may be following a trading strategy
corresponding to a super-replicating wealth process, it may not generate sufﬁcient
wealth to cover these collateral requirements. Thus, for a wealth process W to
describe a super-replicating strategy, in practice it must satisfy both the terminal
condition WT ≥H(ST ) and a collateral condition at intermediate times.
A related phenomenon was applicable during the Internet bubble. European call
options on stocks cannot be exercised before maturity, but the terms and conditions
of options on Internet stocks often included the proviso that if the ﬁrm was subject
to a take-over at time T ′ < T, then the option paid (ST ′ −K)+. In order to superreplicate the call option it is necessary to have a wealth process which satisﬁes both
a condition at maturity and this condition at intermediate times. (Note that if S is
a true martingale then a super-replicating wealth process for a call automatically
satisﬁes Wu ≥Eu[(ST −K)+] ≥(Su −K)+, but if the underlying is a local
martingale this need not be the case.)
Deﬁnition 5.1 Consider a contingent claim with maturity T. The fair price of an
option with payoff H and collateral requirement G is the smallest initial fortune
which is required to construct a self-ﬁnancing wealth process W satisfying the
super-replication condition WT ≥H(ST ) and the collateral condition Wu ≥
G(Su).
Essentially the above deﬁnition involves redeﬁning the set of admissible strategies to be the set of self-ﬁnancing wealth processes which satisfy Wu ≥G(Su).
It is clear that any super-replicating wealth process W for H(ST ) which also
satisﬁes Wu ≥G(Su) is also a super-replicating wealth process for an Americanstyle claim which pays H(ST ) if exercised at time T, and G(Su) if exercised at
time u < T. The converse also holds in that a super-replicating wealth process for
theAmerican claim is also a super-replicating wealth process satisfying a collateral
requirement. Hence there is an equivalence between the price of a contingent claim
with collateral requirement, and the price of American options where the payoff
depends on the time of exercise.
Let Vt(G, H) denote the smallest fortune with which it is possible to superreplicate the claim. Note that Vt(0, H) = V E
t (H) and Vt(H, H) = V A
t (H). The
following result is proved in the appendix.
Theorem 5.2 Suppose G is a positive convex function, with lim sup G(x)/x = β,
and that H ≥G is arbitrary. Then Vt(G, H) = Et[H(ST )] + β(St −Et[ST ]).

489
Corollary 5.3 Consider a European call option and suppose that the exchange
requires collateral of α(Su −K)+, with α ∈(0, 1], to be posted when the option
t (K) + αCA
is in the money. Then the fair price of the option is (1 −α)CE
t (K) =
t (K) + α(St −Et[ST ]).
CE
Consider now the actual price (rather than the fair price) of the option. Lewis [19,
p.295] asserts that this price should be CA
t (K), but does not give a convincing reat or CA
son for his choice. In contrast, Heston et al. [15] argue either CE
t could be
the traded price, amongst others, and that without some additional conditions it is
not possible to determine the true price. We have shown that the correct additional
condition is related to the notion of admissible strategy. Given a zero collateral requirement the unique, arbitrage-free fair price of a European call option is CE
t (K),
and with a collateral requirement of (Su −K)+ the fair price is CA
t (K).
Now consider a similar question, but from a different perspective. Suppose that
the option trades for price CT r
t . Is it possible to make arbitrage proﬁts?
Again, the correct answer depends on the notion of admissibility, and this phenomenon is not a byproduct of a strict local martingale model, but rather is to be
found in almost any model. Consider the Black-Scholes model, and consider a
claim with zero payoff. Suppose the time-t traded price of this claim is given by
V T r
= Λ(St, t), where Λ is as given by (1), and suppose moreover that the traded
t
price process of the claim is V T r
= Λ(Su, u). Consider an agent who sells such a
u
claim, for price V T r
, and who makes no effort to hedge the claim. At maturity the
t
agent has a fortune V T r
, and an arbitrage.
t
Now suppose the agent is required to keep his net wealth positive, where net
wealth includes the obligation resulting from the claim sold short. In particular the
agent must have ˜Wu ≥0 where
˜Wu = V T r
+ (θ · S)u −V T r
u .
t
Since this net wealth process is a non-negative local martingale, started at zero, it
must be identically zero, and the agent cannot generate an arbitrage. This argument
extends easily to net wealth processes satisfying WT ≥0 (super-replication) and
an admissibility condition on net wealth of the form


˜Wu < −k
k kQ
= 0.
inf
lim
u∈[t,T ]
In summary, even though there is an apparent arbitrage which results from
the claim with zero payoff trading at a positive price, it may not be possible to
make proﬁts from this situation. It is observations such as this which underpin the
importance of Deﬁnitions 3.2 and 5.1.
6 Conclusion
Most examples of stock prices are such that the stock is a martingale under the riskneutral measure. In such a model many simple properties such as put-call parity
follow trivially. However, the general no-arbitrage pricing theory does not require

490
the stock price to be a true martingale; instead it merely presupposes that the stock
price is a local martingale.
Following Heston et al. [15], we give an economic interpretation to this strict
local martingale property in terms of a bubble. There are several examples from
the literature where, wittingly or otherwise, the proposed dynamics correspond to a
strict local martingale; similarly there are repeated examples from economic history
of pricing bubbles.
Great care is needed when pricing options under such a model as many intuitively obvious statements turn out to be false – the presence of a bubble requires us
to be careful about the deﬁnitions of admissible strategies. It may be that the standard mathematical deﬁnition is not the appropriate ﬁnancial deﬁnition if collateral
restrictions are imposed.
Appendix: Optimisation for local martingales
Suppose M0 = 1 and that (Mt)0≤t≤1 is a continuous non-negative (Q, Ft)-local
martingale. Let m1 = E[M1]; then m1 ≤1 with equality if M is a true martingale,
otherwise M is a strict supermartingale.
Theorem A.1 Let G
R+
:
→
R be a convex function such that
lim supx↑∞G(x)/x = β ∈(−∞, ∞]. Then, for τ a stopping time,
E[G(Mτ)] = E[G(M1)] + β+(1 −m1)
sup
(7)
τ≤1
In the true martingale case where m1 = 1 the result follows easily from an
application of a conditional Jensen’s inequality. Hence it is sufﬁcient to consider
the case where m1 < 1 and the local martingale M is a strict supermartingale.
For x > 0 deﬁne Hx = inf{u : Mu ≥x} where the inﬁmum of the empty set
is taken to be 1. To cover the case where we start at time t, let Θt denote the shift
operator, so that Hx ◦Θt = inf{u > t : Mu ≥x} ∧1. Then (Mu∧(Hx◦Θt))t≤u≤1
is a bounded local martingale and hence a a true martingale. Hence, for t < 1,
Mt = Et[MHx◦Θt]
= MtI(Mt>x) + xQt(t < Hx ◦Θt < 1) + Et[M1I(Hx◦Θt=1)].
Taking limits and rearranging we ﬁnd
Mt −Et[M1] = lim
x↑∞xQt(Hx ◦Θt < 1) = lim
x↑∞xQt
Mu ≥x
.
sup
u∈[t,1]
Write γt = Mt −Et[M1]. Then γt = 0 if M is a true martingale, whereas in
the case we are considering γt ≥0.
Theorem A.1 follows on taking t = 0 and F = G in the following lemma,
however we need this more general form in Sect. 5.

491
Lemma A.2 Suppose that G is convex and lim supx↑∞G(x)/x = β. Let F be
any function with F ≥G and let J(x, t) be deﬁned via
J(x, t) = G(x)I(t<1) + F(x)I(t=1).
Then
Et[J(Mτ, τ)] = Et[F(M1)] + β+γt.
sup
(8)
t≤τ≤1
Proof Suppose β ≤0 whence G is a decreasing convex function. The result then
follows easily using Jensen’s inequality, and the fact that M is a supermartingale.
So suppose β > 0. Fix ϵ > 0 and let xn ↑∞be a sequence such that
G(xn)/xn > β −ϵ. Write Hn as shorthand for Hxn ◦Θt. Then, for n large
enough so that Mt < xn,
Et[J(Mτ, τ)] ≥Et[J(MHn, Hn)]
sup
t≤τ≤1
= Et[F(M1)I(Hn=1)] + G(xn)Qt(Hn < 1).
Taking limits, and since ϵ is arbitrary, we conclude that
Et[J(Mτ, τ)] ≥Et[F(M1)] + βγt.
sup
t≤τ≤1
Now we wish to prove the reverse inequality. (Note that there is nothing to
prove if β = ∞.) Let Y F , Y G be the martingales given by Y F
u = Eu[F(M1)] and
u = Eu[G(M1)]. Suppose we can show that
Y G
J(Mu, u) ≤Y F
u + βγu
(9)
foralluincludingu = 1.Theright-hand-sideofthisexpressionisasupermartingale
and if (9) holds for all u then we have J(Mτ, τ) ≤Y F
τ + βγτ for all stopping
times τ. It follows that
Et[J(Mτ, τ)] ≤Et[Y F
τ + βγτ] ≤Y F
+ βγt,
t
and we are done.
Clearly (9) holds when u = 1. For u < 1 we show G(Mu) ≤Y G
u + βγu from
which (9) follows instantly.
Deﬁne Gβ(x) = βx −G(x). Then Gβ is an increasing concave function with
lim infx↑∞Gβ(x)/x = 0. By Jensen’s inequality
Eu[Gβ(M1)] ≤Gβ(Eu[M1]) ≤Gβ(Mu).
Rewriting this in terms of G we ﬁnd
G(Mu) ≤β(Mu −Eu[M1]) + Eu[G(M1)] = βγu + Y G
u ,
□
and the result is proved.

492
References
1. Andersen, J.V., Sornette, D.: Fearless versus fearful speculative ﬁnancial bubbles. Physica A 337,
565–585 (2004)
2. Ansel, J.P., Stricker, C.: Couverture des actifs contingents et prix maximum.Ann. Inst. H. Poincar´e:
Probab. Statist. 30, 303–315 (1994)
3. Az´ema, J., Gundy, R.F., Yor, M.: Sur l’integrabilit´e uniforme des martingales continues. (Springer
Lecture Notes in Mathematics 784) S´eminaire de Probabilit´es XIV, 53–61 (1980)
4. Bergman,Y.Z., Grundy, B.D., Wiener, Z.: General properties of option prices. J. Finance 51, 1573–
1610 (1996)
5. Breeden, D.T., Litzenberger, R.H.: Prices of state-contingent claims implicit in option prices. J.
Bus. 51, 621–651 (1978)
6. Cassese, G.: A note on asset bubbles in continuous time. Inter. J. Theoret. Appl. Finance (2005)
(forthcoming)
7. Chacon, R.V.,Walsh, J.B.: One-dimensional potential embedding. (Springer Lecture Notes in Mathematics 511) S´eminaire de Probabilit´es X, 19–23 (1976)
8. Davis, M.H.A.: Complete-market models of stochastic volatility. Proc. Roy. Soc. (A) 460, 11–26
(2004)
9. Delbaen, F., Schachermayer, W.: Arbitrage and free lunch with bounded risk for unbounded continuous processes. Math. Finance 4, 343–348 (1994)
10. Delbaen, F., Schachermayer, W.: A general version of the fundamental theorem of asset pricing.
Math. Ann. 300, 463–520 (1994)
11. Dybvig, P.H., Huang, C.: Nonnegative wealth, absence of arbitrage, and feasible consumption plans.
Rev. Financial Stud. 1, 377–401 (1988)
12. El Karoui N., Jeanblanc, M., Shreve, S.E.: Robustness of the Black-Scholes formula. Math. Finance
8, 93–126 (1998)
13. Fernholz, R., Karatzas, I., Kardaras, C.: Diversity and relative arbitrage in ﬁnancial markets. Finance
Stochast. 9, 1–27 (2005)
14. Harrison, J.M., Pliska, S.R.: Martingales and stochastic integrals in the theory of continuous trading.
Stochast. Proc. Appl. 11, 251–260 (1981)
15. Heston, S., Loewenstein, M., Willard, G.A.: Options and bubbles. Preprint (2004)
16. Hobson, D.G.: Volatility misspeciﬁcation, option pricing and superreplication by coupling. Ann.
Appl. Probab. 8, 193–205 (1998)
17. Hobson, D.G., Rogers, L.C.G.: Complete models with stochastic volatility. Math. Finance 8, 27–48
(1998)
18. Hull, J., White, A.: The pricing of options on assets with stochastic volatilities. J. Finance 42,
281–299 (1987)
19. Lewis, A.L.: Option valuation under stochastic volatility. Newport Beach, USA: Finance Press
2000
20. Malkiel, B.G.: A random walk down Wall Street. New York: Norton 2003
21. Shiller, R.J.: Irrational exuberance. Princeton: Princeton University Press 2000
22. Shiller, R.J.: Bubbles, human judgement and expert opinion. Yale University (Preprint) (2001)
http://viking.som.yale.edu/ﬁnance.center/pdf/wpshiller.pdf
23. Sin, C.A.: Complications with stochastic volatility models.Adv.Appl. Probab. 30, 256–268 (1998)
24. Strasser, E.: Necessary and sufﬁcient conditions for the supermartingale property of a stochastic
integral with respect to a local martingale. (Springer Lecture Notes in Mathematics 1832) S´eminaire
de Probabilit´es XXXVII, 385–393 (2004)

## Tables

No tables extracted.

## Figures

![Figure 1: Figure 1](assets/fig_001.jpeg)

## Extraction Notes

- No warnings.
