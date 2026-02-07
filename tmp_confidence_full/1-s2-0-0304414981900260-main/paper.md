---
paper_id: "1-s2-0-0304414981900260-main"
source_file: "1-s2.0-0304414981900260-main.pdf"
title: "PII: 0304-4149(81)90026-0"
authors: []
year: 1981
doi: null
page_count: 46
extracted_at: "2026-02-07T06:48:39.893917+00:00"
status: "success"
---

# PII: 0304-4149(81)90026-0

## Metadata

- **Source File:** `1-s2.0-0304414981900260-main.pdf`
- **Authors:** Unknown
- **Year:** 1981
- **DOI:** Unknown

## Abstract

Not found.

## Main Text

Stochastic Processes and their Applications 11 (1981) 215-260
North-Holland Publishing Company
NGALES AND STOCHASTIC INTEGRALS
IN THE THEORY OF CONTINUOUS TRA
J. Michael HARRISON
Graduate School of Business, Stanford University, Stanford, CA 94305, U.S.A.
Stanley R. PLISKA
Northwestern University, Evanston, IL 20601, U.S.A.
Received 18 July 1980
Revised 22 December 1980
This paper develops a general stochastic model of a frictionless security market with continuous
trading. The vector price process is given by a semimartingale of a certain clr;zss, and the general
stochastic integral is used to represent capital gains. Within the framework of this model, we discuss
the modern theory of contingent claim valuation, including the celebrated option pricing formula
of Black and Scholes. It is shown that the security market is complete if and only if its vector price
process has a certain martingale representation property. A multidimensional generalization of the
Black-Scholes model is examined in some detail, and some other examples are discussed briefly.
Contingent claim valuation
representation of martingales
continuous trading
semimartingales
1
diffusion processes
stochastic integrals
option pricing
1. Introductim
This paper is intended partly as a tutorial, partly as a survey, and partly as a forum
for new results. Its subject is the theory of security markets with continuous trading, a
‘~~~r+~nt topic in financial economics. ‘We
highly specialized but nonetheless
IIU~.,. .-___
develop a general stochastic model of a frictionless market with continuous trading,
hereafter called simply a continuous market, and then discuss the modern theory of
contingent claim valuation
(option pricing) in the context of that model. The
mathematical
structure developed
here is also flotentially
useful for study of
consumption-investment
problems, but that subject will not be dealt with directly.
In mentioning the modern theory of contingent claim valuation, we refer primarily
to the option pricing formula of Black and Scholes [2]. It was a desire to better
understand their formula which originally P 1 otivated our study, so we introduce this
rief account of the BlackScholes
theory and some questions that it
naturally suggests. For purposes of introduction,
certain terms will be used in a
0304-4149/ 81/0000-0000/$02.50
@ North-Holland
Publishing Company

216
temporary
narrow sense and some of the mathematical
definitions will be stated
informally
or even deleted
altogether.
Also, to give a more or less concrete
motivation for the general theory, excessive emphasis is placed on a single economic
issue, involving what we call completeness
of the market.
1.1. TIze opticn pricing formula
Let W = { Wl; 0 s t G T} be a standard
(zero drift and unit variance) Brownian
motion on scme probability
space (a, 9, P). Let r, I_C and CT be real constants with
L+ > 0. It will be natural to think in terms of the case p > r > 0, blut this restriction is
not necessary. Mow define
s:
0 6 t G T,
=z S; exp(aW, +l(p~ +*)t),
(1.2)
where the initial values Sz and SA ilre positive constants. (This notational
system is
used through,out. The time parameter
of a process is given by a subscript, and the
components
of the vector security price process S are indexed by a superscript
k =0, 1,. . . , K. The distinction between superscripts and exponents will always be
clear lrom context.) Interpret Sp as the price at time t of a riskless bond, with r being
the associated riskless interest rate. Interpret Sf as the price at time t, in dollars per
share., of a stock which pays no dividends. In more general terms we might call So and
S’ the price processes for a riskless security and a risky security, respectively. For our
purposes, a unit of security k can be viewed simply as, a piece of paper which is
exchangeable
for S: dollars at any time f (k = 0,I). The market value of the bond
grows exponentially
at rate r, while that of the stock fluctuates randomly.
Applying Ito’s Formula to (1 .l) and (1 .a.), it is seen that our price processes So and
S1 satisfy the stochastic differential equations
dS; = rSp dt,
(1.3)
dS; =c&
dW,+&
dt.
(1.4)
One can paraphrase (1.2) and (1.4) by saying that S’ is a geometric Brownian motion
with rc$te of return dS:/S:
= u d Wt + p dt. This terminology is a bit sloppy since W is
nond;ITerentiable,
and in the body of the paper we will simply call cr Wt + pt the return
process for the stock.
Consider an investor, hereafter
called you, palrticipating in a securities market
where this stock and this bond are traded. Assume that you are allowed to trade
continuously,
that there are no transaction costs (like brokerage fees) in this market,
and that you can sell short without restriction
(selz below). We summarize these
assumptions by saying that this is a frictionless market with continuous trading. Now
consider a ticket which entitles its bearer to buy one share of stock at the terminal
date T, if he wishes, for a specified price of c dollars. ‘This is a European calloption on
tlhe stock, with exercise price c and expiration date 1: If Sk < c (stock price is below

217
exercise price at expiration date), then the bearer of the ticket will not exercise his
option to buy, meaning that the ticket is worthless in the end, But if Sk 2 c, the bearer
can buy one share of stock for c dollars, then ‘turn around and sell it for Sk dollars,
making a profit of Si - c. Thus we see that the cad1 option is completely equivalent to
a ticket which entitles the bearer to a payment of X = (Sk-c)’
dollars at time T.
Now, how much would you be willing to pay for such a ticket at time zero? Put
another way, what is your valuation of the option? On the surface of things it seems
perfectly reasonable that different people might give different answers, depending on
their attitudes toward risk bearing, since purchase of the option is unquestionably
a
risky investment.
But Black and &holes [2] asserted that there is a unique rational
value for the option, independent
of one’s risk attitude. Specifically, defining
### f<x, t) = x@(g(x, t)) -c e-“@(h(x, t)),
(1.5)
where
g(x, t) = [ln(x/c) + (r + $2)b]/~ J;,
h(x, t) = g(x, t)-m/t,
### and @( l
) is the standard normal distribution
function, this unique rational value is
f(SA, T). Obse rve that the valuation formula (1.5) involves the current stock price x,
the expiration
date t, the exercise price c, the return variance g2 and the riskless
interest rate r, but not the mean rate of return 1~ for the stock.
Before we discuss the reasoning behind this formula, some historical remarks are
in order. The first mathematical
description
of the stochastic process now called
Brownian motion was given by Bachelier [l] in a thesis submitted to the Academy 0:
Paris in 1900. Proposing this process as a model of security price fluctuations, his goal
was to develop theoretical
values for various types of options, and compare these
against the observed market prices of the options. Thus the problem of option
valuation motivated the very first research on what we now call diffusion processes.
(Bachelier’s work was apparently unknown to Einstein and Wiener when they later
deveioped the mathematical
theory of Brownian motion.) From a modern perspective, Bachelier’s mathematics and economics were both flawed, so there is no point in
describing the valuation theory at which he finally arrived. But he did solve a number
of problems correctly, and the paper makes interesting reading.
More than 50 years later, the search for a mathematical
theory of option valuation
was taken up by Samuelson [34] and others. They replaced Bachelier’s ordinary (or
arithmetic)
Brownian
motion
with the geometric
Brownian
motion
(1.2), the
simplest argument in favor of this change being that stock prices cannot go negative
because of limited liability. Using geometric Brownian motion as their model of
stock price movement,
various authors obtained liarious valuation theories under
various sorts of assumptions. But these theories, developed between 1956 and 1
and they *zft even their creators feelin
all contained
ad hoc elements,
that, in t
dissatisfied. Then Black and Scholes made the dazzling observation
idealized market described above, investors can actually duplicate the cash flow (or
payoff stream) from a call option by adroitly managing a portfolio that contains only

J.M. Harrison, S.R. Pliska / Martingales, stuchastk integrals and continuous trading
218
stock and bond. Since possession
of this portfolio
is completely
equivalent
to
possession of the call option, the market value of its constituent
securities at time
zero is the unique rational value for the option. This argument will be made precise
and connected with the valuation formula (1.5) shortly.
The mathematical
argument
given by Black and !;choles in support of their
formula is not entirely satisfactory, but there are several alternate explanations
and
derivations now available in the literature of financial economics. (In fact, explaining
the valuation formula has become a minor industry.) The best of these from our
perspective and the one uniqluely consistent with the general theory developed here,
is the argument by Merton [3Q] which we now present. For more on the history of
option theory, see the surveys by Samuelson [3S] and Itmith [37].
1.2, Portfolio theory and option valuation
It is easy to verify that the function f(x, t) defined I~y (1.5) satisfies the partial
differential equation
a2
X9 = lazx*--$ f(x, t) + rx; f(x, t) -rf(n, t)
$f(
t)
(1.6)
(with initial condition
f(x, 0) = (x - c)‘.
(13
In fact, Black and Scholes originally obtained their valua:ion formula by solving (1.6)
and (1.7). Now define stochastic processes
v,=f(S,‘, T-t),
Qst<T,
(W
### 4: -;f(S:,
T-t),
OwsT,
(1.9)
(1X))
Interpret the vector process & = (&, 4;) as a tradingstrateg!), with & specifying the
number of units of security k to be held at time t. Simply put, & is the portfolio of
securities held at time t. From (1.10) we see that the market value of the portfolio
held at time t is
= Vt,
&s’: +4X
(1.11)
Osts
T.
Thus, using (1.8) and (1.7), the initial value of the portfolio is Vo = f (S& T), and the
terminal value
VT = f(S& 0) = (Sk-c)’
is precisely equal to the terminal value of the call option. Finally, app1yitr.g Ito’s
Formula to (1 .EJ), we obtain
dV, =:f(S:,
T-t)dS:
T-s)(dS:)2+zf(S;,
+&$f(S:,
T-t)dt.
at
(1.12)

219
Using (1.3), (1.4), (1.6) and (1.8)-(l.lO), we ultimately reduce (1.12) to
dV, = 4; dS; +4: dSf.
(1.13)
I t
In its precise integral form, (1.13) is
### vt- v()=
### a$: dS”, +
I ’ 4: dS;,
(1.14)
Ost<T.
0
0
The right-hand side represents the total earnings, or capital gains, which you realize
on your holdings up to time t (see Section 3). Thus (1.14) says that all changes in the
value of your portfolio are due to capital gains, as opposed to withdrawal of cash or
infusion of new funds. In the language of Harrison and Kreps [13], this is a
self-financing strategy.
The justification of the valu8Gon formula (1 S) is now complete. We have located a
trading strategy which requires initial investment r = f(S& T) and thereafter
produces exactly the same pattern of cash flows as the call option. In brief, the option
is attainable in this market, at a time zero price of rr, by dealing only in stock and
bond. In the economics literature it is customary to go further, arguing that arbitrage
profits could be made if options were sold in a parallel market at any price other than
n, and that existence of arbitrage opportunities is inconsistent with equilibrium in the
total economic system. See, for example, the original papea of Black and Scholes [I23
or the recent article by Cox, Ross and Rubinstein [6]. To reduce verbiage and to get a
self-contained mathematical theory, we shall simply stop with the statement of
attainability. Throughout this paper, we focus on an isolateld market in which certain
securities are traded, assuming that no arbitrage opportunities exist internal to this
market (see Section 2). We seek to characterize the class of contingent claims that
investors can attain, and the prices at which they can attain them, by dealing only in
the designated securities. In discussing the valuation formula (1.5), for example, we
have focused on a market where only the stock and bond are traded, and we have
discovered that investors can manufacture call options for themselves in this market
at the price specified in the formula. No comparison is made with the price at which
options do sell, imight sell, or should sell outside OUK market, although it is obviously
possible to do so.
Beginning with the statement of the critical balance condition (1.13), our treatment has diverged somewhat from Merton’s [30] proof of the valuation formula. In
particular, his defense of (1.13 j as a zero-net-new-investment condition relies on his
own theory of portfolio management with diffusion price :processes [26,27].
As a final point, let us return to the assumption of unrestricted short sales. From
the standpoint of our formal theory this means simply that either portfolio
component 4: can be negative. In the case of the bond, short selling amounts to
borrowing (rather than lending) money at the riskless interest rate
particular trading strategy 4 defined by (1.9) _ qd (I e IO), it can be verified
4 1 are positive but 4’ can go negative. Thus, in order to duplicate the cas
the call option, you will always hold a positive amount of stock, but it may be

J.M. Harrison, S’.R. Bliska / Martingales, stochastic integrals and continuous trading
220
necessary to finance some of your stock purchases with riskless borrowing (selling
bonds short). In particular, the valuation formula (1.5) for call options does not
actually require the assumption that stock can be sold short without restriction, but
short sale of stock may be necessary in order to attain other types of options. See [36]
for an explanation of short sales.
I. 3. Compieteness of the market
In the preceding section we have defended the valuation formula (1.5) without
ever suggesting how it was obtained in the first place. The derivation of the formula,
Ior rather our approach to its derivation, will be explained later in Section 5, where we
also show that the attainability result of the previous subsection can be greatly
generalized. Roughly, the story is as follows. Let
meaning that zF~ consists of all events whose occurrence 33: nonoccurrence can be
determined from the stock price history through time T. Define a contingent claim as
a nonnegative random variable X which is measurable with respect to P+ (hereafter
written X E 9r). This is our formal representation-.: for a ticket which entitles the
bearer to a payment, at time T, whose size depends (in an arbitrary way) on the price
history up through T. Olre can of course expand this definition to consider claims
payable at other times, but doing so complicates notation and the added generality is
essentially trivial. The European call option discussed above is represented by
X=(&- - c)‘. Generalizing the ideas in Subsection 1.2, a contingent claim X is said
to be attainable atprice ,ar in our security market if there exists a self-financing trading
strategy # with associated market value process V, such that V0 = v and VT =X,
almost surely. To make this precise, one of course needs a general definition of a
self-financing strategy (and the associated value process), but wc trust that the spirit
of the definition is clear. A remarkable property of the diffusion model described in
Subsection I .l is that every contingent claim is attainable, and one can even write
down a general (but ratner abstract) valuation formula for the price 7r associated with
a given claim X. The valuation formula is
r = exp( - rrli’)E*l;X),
(1.15)
where E*( . ) is the expect:ation operator associated with a (very particular) probability measure P* on (Q9).
This measure P” is equivalent to P, meaning that
P*(A) = 0 if and only if P(A) = 0 (the two measures have the same null sets). The
Black-Scholes formula t 1.5) is a special case of (1.15).
Loosely adopting a standard term in economic theory, we say that a security
market model is complete if every contingent claim is attainable. (See Section 3 for
precise definitions.) The completeness of the Black-Scholes model, in a somewhat
different sense, and the general valuation formula (1.15) were proved by Harrison
and Kreps [ 131, although the origin of (1.15) lies in an observation by Cox and Ross
### 151 .

J.M. Harrison, SR. Pliska / Martingales, stochastic integrals alrld continuous trading
221
1.4. An open question
It can be argued that the important and interesting, feature of the model in
Subsection 1.1 is its completeness, not the fact that it yields the explicit valuation
formula (1.5) for call options. We shall adopt precisely thi,s point of view throughout
most of this paper, investigating the structural features of different models, rather
than emphasizing explicit computation. (In the end, however, it is the explicit
calculation which give the subject its vitality.) From this viewpoint, the following
question is both natural and fundamental:
Suppose the vector price process in Subsection 1.1 is replaced by
some other positive vector process S = {S, ; 0 =Z t s T} with all
(1.169
other assumptions and1 definitions unchanged. What processes S
yield a complete market?
A significant amount of our attention is directed to this question. A satisfactory
general answer will not be obtGned, but matters will at least be brought to a point
where the question is given a precise mathematical form and then reduced to an
equivalent problem in martingale theory, for which a substantial literature exists.
The general question (1.16) probably has a very sharp answer, although much
debate is possible over the appropriate criterion of sharpness, and we hope our paper
will stimulate interest in this and related mathematical problems. For the moment,
we simply wish to make two observations. First, despite the impression one often gets
in reading the academic finance literature, it is neither necessary nor sufficient for
completeness of the market that the price process S has continuous sample paths. In
particular, the attainability of call options in the model of Subsection 1.1 requires
much more than continuity of the stock price process, allthough one can certainly
relax the precise distributional assumptions imposed there. See Subsection 6.3 for an
example, and compare this against the introductory passiage in the survey by Smith
[37]. Second, the Markov property is completely irrelevant to the question posed in
(1.16). In fact, a much stronger statement can be made. Consider a market model
whose securities price process S is defined on some proba’bility space (a, 9; P). Now
consider a second inodel identical in all regards except that P is replaced by an
equivalent probability measure Q. Then a contingent claim is attainable at price z in
the first model if and only if it is attainable at this same lprice in the second model.
Consequently, the first model is complete if anld only if the second o/le is. These
statements may not be obvious, since precise definitions hlave not been given, but we
hope they are at least plausible at this point. Putting the assertion another way, only
the null sets of the distribution of S are relevant to the question (1.16). In asking
whether every contingent claim derived from S is attainable in the mar
oniy interested in which sets of sample paths do and do not have positive p
Thus the parts of probability theory most relt.vant to the general question
those results, usually abstract in appearance and French in origin, which a
under substitution of an equivalent measure.

222
J.M. Harrison, S.R. Pliska / Mqrtingales,
stochastic
r’ntegrals and corltirruous tradhg
I .5. The proba bilistir setting
Before the completeness question (1.16) can even be state,31 precisely, one must
have a general model of a market with continuous trading. In tb is section we describe
the minimal model structure necessary for a study of completeness, suppressing some
features of the theory actually developed later. Our first task is to resolve the
following modeling issues:
What class of vector processes S might conceivably be used to
(1.17)
represent security price fluctuations?
How should one define a trading strategy in general and then,
(1.18)
what is the proper definition of a self-financing strategy?
To keep things simple, consider only price proc:(:sses S with Sy = exp(rt), meaning
that the riskless interest rate is both deterministic and constant. Let & = exp( - rt)
and call p the intrinsic discountprocess for S. It will be argued that, if we are to obtain
and internally consistent theory, we need only consider S such that
the discounted vector price process PS is a martingale under some
(1.19)
probability measure P* equivalent to F’.
It is this P*, called the reference measure, which enters in the general valuation
formula (1.15) discussed earlier. One implicat:on of (1.19) is that S must be what is
called a semimartingale, and we are fortunate to have available a well developed
theory dealing with change of measure for semimartingales. This theory, which has
evolved from Girsanov’s Theorem [ 121 for Ito processes, is precisely what is needed
to verify or refute the condition (1.19) for any given model.
Turning to the modeling issue (1.18), we define a trading strategy 4 as a
predictable vector process. We define the capital gains under strategy 4 as the
stoch!astic integral of 4 with respect to the vector price process S, and then we define
a self-financing strategy exactly as in (1.14). Because the price process is a semimartingale, the necessary general theory of stochastic integration is readily available. In
the en3, we find that our model is complete if and only if every process which is a
martingale under P* can be written as a stochastic integral with respect to the process
PS in (1.19). In the language of martingale theory, the model is complete if and only
if /3S has the martingale representation property under our reference measure P*.
All of this is intended to suggest that the modern theory of martingales and
stochastic integrals provides exactly the mathematical framework needed for a
theory of continuous trading. As our development unfolds, there will be still more
examples of general results in the mathematical theory that look as if they were
created for this application. We have started to feel that all the standard problems
studizl in martingale theory and all the major results must have interpretations and
appGcations in our setting. Be this as it may, the
recess of searching for such
connections has barely even

J.M. Harrison, 5X. Hiska / Martingales, stochastic integrals and continuous trading
223
1.6. Outline of the paper
This paper is aimed at readers with a good command of probability and stochastic
processes, but no particular knowledge of economics. On the former dimension, we
assume familiarity with the Strasbourg theory of martingales and stochastic integration, as developed in the definitive treatise by Meyer [32]. ‘This assumption is perhaps
unrealistic, but we cannot provide a systematic tutorial on stochastic integrals and an
adequate treatment of our nominal subject matter in a reasonable amount of space.
(Also, the former task is best left to others. We ire working dangerously close to the
boundaries of our knowledge as things stand.) Most of this paper will be accessible to
those who know about stochastic integrals with respect to Brownian motion, and the
rest should come into focus after a little study of the relevant foundational material.
(On first reading, specialize general results to the case where S is an Ito process.) To
facilitate such study, we consistently refp ,r to Meyer [32] by page number for basic
definitions and standard results, and his notation and terminology are used wherever
possible. For a nide overview of the Strasbourg approach to stochastic integration,
plus some new results and illuminating commentary, see the recent survey by
Dellacherie [9] in this journal. A comprehensive treatment of stochastic calculus is
given by Jacod [18], and it appears that the second volume of Williams [38] will be
another good sourcebook on martingales and stochastic integrals in the Strasbourg
style. A somewhat different approach to stochastic integrals is developed by MeGvier
and Pallaumail [31], and their theory is also discussed briefly by Dellachericf [
Some, but not all, of the results used here can be found in the English edition of
Liptser and Shiryayev [24].
The heart of this paper is Section 3 which contains the general theory of continuous
markets, alluded to earlier. This is preceded by a partial development of the
analogous theory for finite markets in Section 2. (A finite market is one where trading
takes place at discrete points in time, and the underlying probability space is finite.)
Both the formulation and the central results of Section 2 are taken from the paper by
Harrison and Kreps [ 131, which is in all respects the intellectual progenitor of this
work. By treating the finite case first, we are able to ease the exposition in several
respects. First, the necessary economic notions are introduced in a simple setting.
Having interpreted or defended a definition in the finite case, we typically state its
formal analog and proceed without furthe. r cornnient in development of the general
theory. Second, we are able to give an adequate treatment in the finite case of certain
foundational issues that will be essentially glossed over in development of the general
theory. In particular, a key assumption of Section 3 is defended principally on
the basis of its formal similarity to a condition derived from more primitive co
siderations in Section 2. Finally, the technical complexity that one encounters
with a continuous time parameter obscureE the basic structure of the mathematical
theory. By treating the finite case first, we hope to establish the natura
martingale technology, and thus motivate the rat&r intricate develo
Section 3.

224
Section 4 serves as a complement to Section 3, discussing the general relationship
between security price processes and their associated return processes. Section 5
analyzes in some detail a multi-dimensional version of the Black-Scholes model.
Section 6 contains further examples relating to completeness of markets, and Section
7 contains some miscellaneous concluding remarks.
We conclude this section with some general comments on terminology and
notation u The term positive is used hereafter in the weak sense, as opposed to strictly
positive, and similarly for increasing versus strictly increasing. When we write X = Y
for random variables X and Y, this is understood to be an almost sure relationship,
ar.d simila1,l.v for X 2 Y. In the case of processes, X 3 Y means Xt a Yt for all t. As
examples 0: these conventions, we will have frequent occasion to write X = 0 or
X 2 0, where X may be either a random variable or a process. The symbol = is used
to mean equals by definition.
2. The finite theory
This section introduces a number of basic concepts by examining the case where
time is discrete and the sample space is finite. This presentation is intended not as a
comprehensive, systematic study of the finite case, but rather as a device for
motivating and facilitating understanding of the continuous trading model that
follows in Section 3. Most of what transpires here can be traced back to the paper by
Harrison and Kreps [ 131.
2.1. Formulation of the market model
The probability space (L&9, P) is specified and fixed. The sample space L? has a
finite number of elements, each of which is interpreted as a possible state of the
world. We assume P(W) > 0 for all or) E 0, and this is the only role of the probability
measure. We envision a community of investors who agree on which states of the
world are possible but who do not necessarily agree further on their probability
assessments. All of our definitions and results remain the same if P is replaced by any
equivalent probability measure,
Also specified are a time horizon T, which is a terminal date for all economic
activity under consideration, and a filtration IF = {so, Fr, . . . , PT}. By this we mean
each 9t is an algebra of subsets of L! with SO E l 0 l c FT. Without any real loss of
generality, we assume 9$ = {C&O} and 9+ = 9 is the set of all subsets.
Securities are traded at time t = 0, 1, . . . , T, and the filtration ff describes how
information is revealed to the investors. Each Pl corresponds to a unique partition 9$
of 0, and at time t the investors know which cell of this partition contains the true
state of the world, but they do not know more than this.
Taken as primitive in our model is a K + 1 dimensional stochastic process
S={S,: t=o,
1,. . , 9
T} with component processes s”, S’, . . . I SK. It is required that
I

J.M. Hmrison, S.R. Pliska / Martingales, stochastic integrals and continuous trading
225
each comporient
:S” be strictly positive and adapted to IF. The latter means that the
function (r) + S:(w) is measurable with respect to 9’1 (written S,” E St) for each k and
t. Interpret $‘ as the price at time t of security k, so S adapted means that investors
know at time t thle past and current prices of the K + 1 securities.
The 0th security plays a somewhat special role because we also assume, and this
can be done withlout loss of generality,
that Sz = 1. We call this security the bond,
even though we :make no assumptions
which really distinguish
it from Khe other
securities. In the continuous theory, the bond will have solme special features which
set it apart from other securities. We define a process /3 by setting & = (l/S:)
and call
it the discount process. The reader should think in terms of the special case where
Sy = (1 + ~1’ with r (the riskless interest rate) constant and1 positive.
Define a trading strategy tfo be a predictable
vector p;rocess 4 = (4, ; t = I, . . . , T}
with components
c$‘, C$ ‘, . . . , @.
Predictable means & E 9t_l for t = 1, . . . , T.
Interpret 4: as the quantity of security k (in physical unit:s, like shares) held by the
investor between times t - 1 and t. The vector c$( will be called the investor’s portfolio
at time t, anld its components
may assume negative as wlell as positive values. In
particular,
w7e are permitting
unrestricted
short sales. By requiring
that 4 be
predictable,
we are allowing the investor to select his time 8 portfolio after the prices
St+ are observed. However, the portfolio 4t must be established before, and held
until after, announcement
of the prices S,.
We pause to introduce some notation. If X and Y are two vector-valued,
discrete
ti,me, stochastic processes of the same dimension,
then let XtY, denote the innerproduct Xf Y,'
+XfYf
-to l l
, and let XY denote the real-valued
process whose
value at time t is XtYt. In addition, let AX, denote the vector X, - Xt-- l., and let AX
denote the process whose value at time t is 3X,.
Clearly &St_1 represents the market value of the pal tfolio & just after it has been
established at time t - 1, whereas &S, is its market value just after time t prices are
Hence &AS, is the
observed, but before any changes are made in the portfolio.
change in market value due to the changes in security prices which occur between
times t - I and t, If an investor uses trading strategy #, therefore, we see that
cw
G?(4)= i &iASi, tll,...,T,
i = 1
represents the cumulative earnings or capital gains which the investor realizes on his
holding
up through
time
t. We set Go(~) = 0 and call G(4) the gains process
.+,. Pu’ote that G(4) is an adapted, real-valued,
stochastic process.
associated with A
It is important to notice that a general trading strategy 4 may require the addition
of new funds after time zero or allow the withdrawal of funds for consumption.
In
contrast, we say a trading str&gy
# is self-financing if
(2.2
t=l,...,
&s’,=&+,S,,
T-l.
This means thl?t no funds are added to or withdrawn from the value of t
at
OPf
to check that (2.2)
T - 1. Using (2.1), it is straightforward
anyofthetimest=l,...,

226
is equivalent to
(2.3)
t = ‘1,. . . ? T.
q&s, = a$&+G,(4),
Thus a trading strategy is szlf-financing if and only if all changes in the value of the
portfolio are due to the net gains realized on investments.
We want to add one more restriction. A trading strategy 4 is called admissible if it
is self-financing and V(#) is a j?ositive process (hereafter written V(4) 3 0) where
ift=l,,..,,T,
(2.4-Q
if t = 0.
We call V(4) the value process for 4 since Vr(4) represents the market value of the
portfolio held just before time f transactions. By requiring that V(4) be positive we
are saying not only that theinv?stor must start with positive wealth, but also that his
investments must be such that he is never put into a position of debt. This constraint is
fairly common in the finance literature. Since security prices are positive, it has the
effect of prohibiting certain kinds of short sales. Let Qi denote the set of all admissible
trading strategies.
A contingent claim is simply a nonnegative random variable X. It can be thought of
as a contract or agreement which pays X(w) dollars at time T if state o pertains.
Letting X denote the set of all such contingent claims, it is easy to see tha: X is a
convex cone. ,A contingent claim X is said to be attainable if there exists some 4 E @
such that I+-(&) = X. In this case we say that 4 generatesx and that v = Vo(4) is the
(time-zero) price associated with this contingent claim. Is this price unique, or can a
contingent claim be generated by two different trading strategies with the initial
value V0 being diEerent in each case? This is our next subject.
2.2. Vkbility of the model
An arbitmge opportunity is some 4 E @ such that Vo(4) = 0 and yet E( VT(~)) > 0.
Such a strategy, if *one exists, represents a riskless plan for making profit without any
investment. It does not require either initial funds or new funds in succeeding
periods, but, since L+(4) 2 0, it yields, through some combination of buying and
selling, a positive gain in some circumstances without a countervailing threat of loss
in other circumstances. A security market containing arbitrage opportunities cannot
be one in which an economic equilibrium exists.
The purpose of this subsection is to derive two co:nditions which are equivalent to
the assertion that there are no arbitrage opportunities. We begin by defining a price
system for contingent claims to be a map v :
+ [O,, 00) satisfying
) = 0 if and only if X = 0,
(2Sa)
and
‘) for all a, b 2 0 and all X, X’ E
(2Sb)

J.M. Harrison, S.R. PA!ska / Martingales, stochastic integrals and continuous trading
227
Such a price system v is said to be consistent with the market model if V( VT(&) =
VO(q5) for all 4 E @. Let II denote the set of all price sys8telms consistent with the
model.
Let IFJ bc the set of all probability measures Q which are equivalent to P and are
such that the discounted price process PS is a (vector) martingale under Q. The
relationship between IP and I7 is established in the following (where Eo is the
expectation oper star under Q E P).
2.6. Proposition. There is a one-to-one correspondence between price systems IT E Ll
and probability memures Q cz Up via
(i) V(X) = E&.&X)
and
(ii) Q(A) = ~(s$lJ,
A E 9.
Proof., Let Q E IP and define 7~ by (i). Clearly v is a price system. To show it is
consistent with the market model, let 4 E Q) be arbitrary and notice by (2.2) that
+Til (4i-&i+l)piSi=
; ~i(piS;i-pi-lSi_,)+~,p,S,.
PTVTW+'I-~TST
j = 1
i=2
Hence
Now PS is a martingale under Q and 4 is predictable, so the first term on the
right-hand side equals zero. For the second term we compute E&&St)
=
= &&SO = Vo(@), thereby verifying that n is consistent and thus an
&E&?&)
element of II.
For the converse, let 72 E II and define Q by (ii). For each o E 1(2 we have
Q(w) = &&,)
HI since $4,
# 0 and v satisfies (2Sa). Now consider the strategy
K (hold one bond throughout). Since w
&E@with@‘=land~k=Ofork=l,...,
is consistent vwith the model, we have V&I) = w(VT(~)), or I= &&),
or
Q(0) = 1. Thus G is a probability measure equivalent to P, and it follows directly
from (2.5) that W(X) = Eo(&X) for any X EX. Next, let k 2 1 be arbitrary, let r s T
be a stopping time, and consider the strategy 4 E @ defined by
and 4’ = 0 for all other i. This is the strategy which holds one share of stock k up until
(through) the stopping time 7, then sells that share of stock and invests1 all the
proceeds in bonds (check that 4 is predictable). Then V&) = S$ and VT(&) =
= S$&SF, and the consistency of 7~ gives us
cs:/s’l)s;
since 81 and T are arbitrary, this means that @S is a vector martingale under C), an
hence that Q is an element of P.

J.M. Harrison, S. R. Pliska / Martingales, stochastic integrals and continuous trading
228
We now return to the notion of arbitrage opportunities and present the central
result of this subsection.
### .7. Theorem. The market model contains no arbitrage opportunities if and only if P
(or equivale,rztly IT) is nonempty.
efinitio:a. Hereafter we say that the n&c 3 is viable if the three equivalent
conditions of (2.7) hold.
orollary. If the model is viable, then there is a single price w associated with any
attainable contingent claim X, and it satisfies n = E&TX)
for each Q E P.
emark. This resolves the uniqueness issue raised at the end of Subsection 2.1. It
has also been shown that knowledge of any one Q E IP allows us to compute (at least
in principle) the prices of all attainable claims.
Proof. Suppose P is nonempty. By (2.6) this is equivalent to Z7 nonempty. Fix v E L!
and let 4 E @ be-such that V&) = 0. Then ?I( V&5))
= V&j) = 0 because 72 is
consistent with the model, and hence V&$) = 0 by (2.5). Thus no arbitrage opportunities exist. To prove the converse we need the following preliminary proposition,
because we have demanded that admissible strategies have positive value processes.
emma. If there exists a self-financing strategy C$ (not necessarily admissible) with
V0C4) = 0, VT@) a 0, and E( V&#J)) > 0, then there exists an arbitrage opportunity.
roof. If V(b) 2 0, then 4 is admissible and hence is an arbitrage opportunity itself,
so we are done. If not, there must exist a t < T, A E 9t and a < 0 such that #$ = a on
A and c#&, G 0 on A for all u > t. Define a new trading strategy # by setting #, = 0
forust,&(W)=Oifu>tandwlSA,andifu>tandoEA
+k(
)
fork
=o,
uo
=
for k = 1,2, . . . , K.
Clearly ~5 is predictable. For o E A we have
by (2.2) and 1 he definition of a, so it follows that $ is self-financing. For u :> t and
we have
UEA
SO V($) 3 0 and $ E @. But; Si* > 0 implies V,(e) > 0 on A, so 9 is an arbitrage
opportunity. This completes the proof of the 1e:mma.

J.iW. Harrison, S.R. Pliska / Martingales, stochastic integrals and continuous trading
229
Back to proving Theorem 2.7. Let
be the set of all
random variables X on Jt such tha
or some self-fi
cing strategy &
(not necessarily admissible) with Vo(4) = 0. Suppose no arbitrage opportunities
exist. Then it follows directly from the lemma above that
’ and X’ are disjoint
(remember that
contains only positive random variables). Now X’ is a closed and
convex subset
Rn, while X0 is a linear subspace. Thus by the Separating
Hyperplane Theorem there exists a linear functional L on lRn such that L(X) = 0 for
all IX E ’ and L(X) > 0 for all X E JK’. From the latter property (and the linearity)
we have L(1,) > 0 for all o E 0. Normalizing, we take n(X) = L(X)/L(St).
lt is
immediate that v satisfies (2.9, so it is a price system. To see that it is consistent with
the model (rr E n), pick t$ E @ and define
if k = 0,
(4: - V&$)
ifk=l,...,K.
Then ~5 is a self-financing strategy (not necessarily admissible) with V&)
= 0 and
V&b) = l&-(4$) - V&b)S$. Since VT($) E X0, v(X) := 0 for all X E X0, 7r is linear,
and v(S$) = 1 by normalization, we have
### v,(dso,)
0 = ar( V&f+)) = dvT@)-
So r( I&(@) = I&(#) for all C$ E @, meaning that 7r E Z7. So no arbitrage opportunities implies II nonempty, hence Dp nonempty by Proposition 2.6, and the theorem
is prove J.
A close look at this proof, and particularly at the intermediate l,emma, reveals the
following. Suppose we had defined admissibility of self-financing strategies by the
weaker restriction VT(+) 3 0, meaning that the investor’s wealth may go negative at
times t c T under plan 4, but he must be able to cover all debts in the end. Defining
arbitrage opportunities in terms of admissible strategies just as before, Theorem 2.7
would still hold and in the end we would find that V(4) 3 0 for all admissible 4 in a
viable model. Thus the weaker definition of admissibility is equivalent to the stronger
one if we eventually restrict attention to viable models (as we shall).
0f the three equivalent conditions defining viability, the least abstract and the
most meaningful economically is the absence of arbitrage opportunities. Put another
way, this condition is the one that justifies our use of the term viable. However, it is
the existenct: of a martingale measure Q E P which is usually easiest to verify i
examples.
We have seen in Subsection 2.2 that a 3r each attainable claim
market price rr satisfies :r~ =
claim X for attainability’? First some preliminaries.

230
### roposition. If C$ E @, then the discounted value process p V(4) is a martingale
2.
under each measure Q E IF?
Prq .A Since 4 is self-financing, it is easy to check that A@ V(4)), = x:=1 & A$@),
(see the proof of Proposition 2.6j. Then Proposition 2.8 follows from the predictability of 4 and the fact that PS is (by definition) a martingale under each Q E P.
roposition. If X E
is attainable, then
wt(~)=&?(PTXl%),
t=O,L..J9
for any 4 E. @ which generates Xand each Q E I%.
roof. Just observe that VT(~) =X for any 4 which generates X, and then use
Proposition 2.8.
An immediate implication of Proposition 2.9 is the following. If a contingent claim
X is attainable, then the value process V = V(4) for any # E @ which generates X
must be
(2.10)
VI=(IIWWPTX~~),
t=O, I,...,
T,
where Q E P is arbitrary. Furthermore, if V is computed from X by (2.10), and if
C$ E @ generates X, then
(2.11)
A(pV), z= ; c$;A(/?S~)~, t = 1,. . . , T,
k=l
11s one can easily verify. Note that the bond coml:Dnent 4’ does not enter in (2.11).
Finally, one can prove the converse statement as well. The contingent claim X is
ilttainable if and only if there exist predictable processes #,
. . . , dK such that (2.11)
holds, as we will show in the more general setting of Section 3. The verification (or
,;efutation) of (2.11) can in principle be done with a separate calculation for each
cell of the partition 9$_1 and each t = 1, . . . , T. Because this story is quite specific to
the finite setding, we will not continue it, but there is one important qualitative point
to understard about the procedure. Its content lies in the fact that V is computed
using (2.10) and any Q E B, before we know whether or not X is attainable. The
,$uestion of attainability then comes down to the indicated representation problem.
2.4. Complete markets
The security market model is said to be complete if every contingent claim is
attainable. In Section 3 it will be shown that completeness is equivalent, in the
general mode.1, to a certain martingale representation property. Here we wish to state
a much sharper characterization of completeness which is entirely specific to the
finite case. To eliminate trivial complications, we first impose a nondegeneracy
ecall that & is the partition of 0 underlying 9’. The price process S is
said to contzlin a redundancy if
= 0 ] A) = 1 for some nontrivial vector a, some
t+l

J.M. Harrison, S.R. Pliska / Martingales, stochastic integra1.s and contimous trading
231
t<T,and
some A E Pr. If such a redundancy
exists, then there is an event
A possible
one security over the corn
at time t which makes possession of some
ing period
completely equivalent to possession of a linear combination of the other securities
over that same period. If no such circumstances exist, then we say that the securities
are nonredundant.
For each cell A of 9& (t = 0, 1, . . . , T - l), let K,(A) be the number of cells of g,+ E
which are contained in A. This might be called the splitting index of A. Assuming that
the securities are nonredundant, and (as always) that the model is viable, we must
have K,(A) 2 K + 1 (the total number of securities) for all I! and A. (This fact may nos
be obvious, but neither is it hard to prve.)
2.12. Proposiition. hf the securities are nonredundant, then the model is complete if
andonlyifK,(A)=P~+lforaZZA~~,andt=O,l,...,T-1.
A precise proof of this, in its more general form without the nonredundancy
assumption, is given by Kreps [20], and we shall not reproduce the argument here,
The interested reader should be able to piece together a proof, starting with the
single period case T = 1. If 0 has n elements, then the space X of contingent claims is
just the positive orthant of Iw”, and with T = 1 each security k consists of a constant S,”
and a vector SF E R” whose components specify S:(o) for different o E f2. For
completeness it is necessary that each X E X be representable as a linear combination of Sy, S:, . . . , SF. In the nonredundant case (where Sy, S:, . . . , SF are linearly
independent) this comes down precisely to the requirelmerlt that n = K + 1. This
argument can then be extended by induction to prove Proposition 2.12 for general T.
Thus we see that completeness is a matter of dimension. Speaking very loosely,
Proposition 2.12 says that in each circumstance A that may prevail at time t, investors
must have available enough linearly independent securities to span the space of
contingencies which may prevail at time t + 1. For a model with many trading dates t
and many states w, completeness depends critically on the way uncertainty resolves
itself over time, this being reflected by the splitting indices K,(A). Again, we refer to
Kreps [20] for further discussion.
With continuous trading no characterization of completeness even remotely
similar to Proposition 2.12 is known, but a second characterization of completeness
for the finite case does have a lcnown general analog. It was observed by Harrison and
Kreps [13] that a finite model is complete if and only if P is a singleton, and a similar
result is known to hold in a more general setting, as we will discuss in Subsection 3.4
2.5. A random walk model
For a concrete example, consider a finite model with Sy = (I+ t)‘, S: = * . 4 =
1, and
fort=1 ,...,
Tandk=l,...,
K
Sf= h (l+a’&
S= 1

232
are independent sequences of i.i.d. binary random variables
where {xi }, . . . , {xf}
taking values f 1 with equal probability, and r, a *, . . . , a K are constants satisfying
k price processes are then independent geometric random
e s oc
Ocr-<rzk<l.Th
t
walks;, while security zero is a riskless bond paying interest rate t each period. The
reade ,r shquld have no trouble determining a martingale mc-psure Q E IFD
for this
model (there are many such Q if # > 1, but only if K = 1). Taking IF to be the
filtrat:on induced by the price process S itself, we see that K,(A) = 2K for all A and t.
It is e:asy to verify that these securities are non-redundant, so Proposition 2.12 says
that SJGS
random walk model is complete if and only if K = 1. See [6] for an extensive
discussion of the K = 1 model and its various generalizations. This same paper
provides a good introduction to and overview of the modern theory of option pricing,
all in the simple setting of a finite model with one stock and one bond.
3. Continuous trading
This section presents a general model of a frictionless security market where
investors are allowed to trade continuously up to some fixed planning horizon T. The
theory closely parallels that developed in Section 2, so we shall be brief and to the
point, pausing only to discuss issues that have no counterparts in the finite case.
We begin now with a probability space (0,9, P) and a filtration (increasing family
of sub-as-algebras) IF = (Ff; 0 G t G T) satisfying the usual conditions:
ykc contains all the null sets of P,
(3.1)
IF is right-continuous, meaning that 5$ = n 9s
for 0 s t < T.
(3.2)
s>t
In fact, without significant loss of generality, .it will be assumed that 90 contains only
Cn and the null sets of f, and that .9+ = 5 It will ultimately be seen that P plays no
role in our theory except to specify the null sets. Hereafter we shall speak of the
fii’tered probability space (a, IF, P).
Let S = {St; 0~ t s T} be a vector process whose clomponents So, S’, . . . , SK are
adapted (meaning SF E Yl for 0 s t G T), right continuous with left limits (hereafter
abbreviated RCLL), and strictly positive. Most of what w’il be done requires only
nonnegative prices, but by assuming strict positivity one avoids various irritating
complications. *
We assume that S” has finite variation and is continuous, interpreting this to mean
that security zero (called the bond) is Zocaiiy riskless. As a convenient normalization,
let St = 1 throughout. If So was absolutely continuous, then we could write
SP = exp
OatsT,
for some process y, and then y, would be interpreted as the riskless interest rate at
time t.
owever, we have found that absolute continuity does not significantly

233
simplify any aspect of the theory, so we do not assume it. Instead, defining
06 t c T,
(3.3)
at = log(S:),
we simply call cy the return process for So, or the locally riskless return process. Also, let
&=l/S?=exp(-a,),
(3.4)
Ost=sT,
calling p the intrinsic discount pwcess for S. We nclw interrupt our development of
the market model to review some aspects of martingale thetory.
3.1. Martingales and stochastic integrals
A supermartingale is an adapted RCLL process X := {Xt ; 0 G t s T} such that Xt is
integrable and E(Xt 1 gs) =Z Xs for 0 s s < t s T. ‘?~Yhe process X is said to be a
if both X and -X
are supermartingales. All our martingales are
martin&e
uniformly integrable because they are stopped at time T c 03. This should be kept in
mind, comparing our later definitions with those in the general literature. We shall
later use the fact that
a positive process X is a martingale if and only if it is a supermartingale and E(XT) = X0,
(3.5)
cf. Lemma 7.10 of Jacod [ 181. An adapted RCLL process M is said to be a local
martingale [32, p. 2911 if there exists an increasing sequence of stopping times (T,,}
suc11 that
W-n =T}+l
asn+a,
(3.6)
and
the stopped process {M(t A T,); 0 s t G T) is a martingale for each n,
(3.7)
in which case the sequence {T,,} is said to reduce M. As (3.7) illustrates, we shall write
the time parameter of a process as a functional argument (rather than a subscript) if
this is necessary to avoid clumsy typography.
Clearly, every martingale is a local martingale, and it follows easily from Fatou’s
Lemma that
every positive local martingale is also a supermartingale.
Combining this with (3.9, we see that
a positive local martingale M is a martingale if and only if E(
A process A = (r4,: 0 s t s T) is said to de in the class b.‘F (for oa
simply a VF process, if it is adapted, RCLL, and has sample paths o
[32, p. 2491. A process X is called a semimartingale [32, p. 2981 if it admits

234
decomposition X = M + A where M is a local martingale and A is a VF process. This
cafweicail decomposition is not generally unique.
We say that H = {Hr; 0 s t s T) is a simple predictable process if there exist times
= T and bounded random variables &E &J,& E Z&,, . . . , &-I
E
Q=t*al<-*<t,
S+$,_, such that
(i=O, 1,. . .,n-1).
Hl=ei
if tictsti+l
Thus simple predictable processes are bounded, adapted, left-continuous, and
piecewise constant. The predictable o-algebra on a x [0, T] is defined to be the one
generated by the simple predictable processes (a variety of equivalent definitions can
be found in the literature). A process H = {Ht ; 0 G t s T) is said to be predictable if it
is measurable with respect to the predictable a-algebra. Every predictable process is
adapted.
Meyer [32, p. 2991 says that a process H is locally bounded if
there exist constants {C,,} and stopping times {T,} satisfying (3.6)
(3.11)
suchthatlH,IaC,
forO<tsT,
andn=1,.2,...,.
In his ldiscussion of the Lebesgue Stochastic Integral, Dellacherie [9] defines local
boundedness by the weakerrequirement
(3.12)
but the discrepancy is resolved (for our purposes) by the following result, which
Dellacherie [9] cites in a footnote and attributes to Lenglart.
Conditions (3.11) and (3.12) are equivalent for predictable processes.
(3.13)
Also, it is well known that
an adapted process which is left-continuous with right limits
(3.14)
(LCRL) is both predictable and locally bounded.
Now consider a semimartingale X together with a simple predictable process H
satisfying (3.10). The stochastic integral 2 = j H dX is then defined path-by-path in
the Lebesgue-Stieltjes sense, meaning (remember that H is left-continuous while X
is right-continuous) Z. = 0 and
i- 1
## zt ‘= C tj(pY,+,
-Xti)+ei(Xt-Xti)
if ti<tsti+i.
j-0
Now, if H is a general localiy bounded and predictable process, the stochastic
integral Z = 1 H dX can be defined by continuously extending what we have for
simple predictable processes, cf. [9] or [32, Chapter 41. Incidentally, when *Ne write
Z=jHdXwemeanZo=Oand
I t
zt =
H, dX, =
H, d
0

235
Observe that predictability and local boundedness are both preserved under substitution of an equivalent measure, and the semimartingale property is also invariant to
such substitutions [32, p. 3761. Finally, the stochastic: integral j H dX described
above enjoys this same invariance. The fact that all these definitions depend only on
the null setq of the underlying probability measure is important in our setting.
The definition of stochastic integrals in terms of predictable integrands is precisely
what is needed for economic modeling, and it yields the following key result [32, p.
2991.
If H is locally bounded and predictable and M is a local martin-
### gale, then J II dM is a local martingale as well.
(3.15)
### If we further assume that M is a martingale, it may not be true that J H dM is a
martingale (there are familiar counterexamples in the Ito theory where M is
Brownian motion). It cannot be emphasized too strongly that (3.15) only holds when
one restricts attention to predictable integrals H.
### If 2 is the stochastic integral J II dX as above, then 2 itself is a semimartingale
(hence RCLL) with
AZ,=H,AXt,
OGtsT
(3.16)
where we use the standard notation AZ’t = Zl -Zl_ for the jump of 2 at t. We shall
write AZ and Z- to denote the processes {AZ,; 0 =S t 6 T} and {ZI_ ; 0 < t G T},
### respectively. Incidentally, the definition of the general stochastic integral J H dX
agrees with the Ito integral in the case where X is Brownian motion (although we are
restricting ourselves to a slightly smaller class of integrands than is customary in
developing the Ito theory), and it amounts to a path-by-path Lebesgue-Stieltjes
integral when X is a VF process.
Let X and Y be semimartingales. Since X- and Y- are LCRL and adapted, (3.14)
shows that it is meaningful to define a new process C&X,
Y] by
## [X Y]t=Xy,-I1x,
(3.17)
dY,-I’Ys_dX&
OstsT.
0
0
An equivalent definition is the following [9]. Let tl = it/2” for II = I, 2, . . . and
i = 0, 1, . . . ,2”. Then
[X, Y], =XoYo+lim C (X(ty+,)-X(ty))(
Y(ty+,)- Y(C))
n
i
where the convergence is in probability. This latter definition explains why [X, Y) is
called the @itit variation of X and Y, with [X, X] called the quadratic vaiation of X.
This is yet another detinition which is invariant to substitution of an equiv
ility measure.
re are a few more properties of the joint variation which will be use
] is always a VF process [32, p. 2671 and moreover
[X, Y] = C AX, A Ys if either X or Y is VF.
ssr

Harmon, S.R. Pliska / Martingales, stochastic integrals and continuous trading
JM.
236,
In particular, if X (say) is continuous and VF, then (3.18) gives [X, Y] = 0 for any
semimartingale
Y. Finally, from (3.17) and the finite variation of [X, “/] it is
immediate that
the product of two semimartingales is itself a semimartingale.
(3.19)
A process X is said to be ivttegrable (under P) if E(lX,/) < 00,0 c t 6 !K It is said to
be locally integrable if there exist stopping times {T,} satisfying (3.6) such that
{X(t A T,,); OC t c T} is integrable for each it.
3.2. A preliminary market model
Picking up where we left off before Subsection 3.1, it will be convenient to define a
by setting
discounted price process 2 = (Z’,
. . . , ZK)
Note that Z has only K components. Let IP be the set of probability measures Q on
(0,s)
whiich are equivalent to P and s.uch that 2 is a (vector) martingale under Q.
This is of course the same as requiring that PS be a martingale under Q, since PS” = 1
is a martingale under any measure equivalent to P. Elements of P are called
martingale measures. We shall henceforth impose the following.
3.20. Assumption. P is nonempty.
The primitive acceptance of Assumption 3.20 constitutes a major difference in our
treatment of the finite and continuous cases. All of Subsection 2.2, culminating in
Theorem 2.7, was devoted to proving that in a finite setting Assumption 3.20 is
equivalent to the nonexistence of arbitrage opportunities, which is an economically
palatable assumption. For the continuous case one can in fact prove a general version
of Theorem 2.7, buf the proper definition of an arbitrage opportunity and the
ensuing mathe.natica! development are extremely complex. A proper treatment of
viability for continuous models requires a paper in itself, so we just rely here on the
formal analogy with the finite theory, referring interested readers to [ 131 for more on
viability in a general setting.
We have that So is a VF process (and thus a semimartinga e), that Zk is a
martingale under any Q E P, and that S” = Zk/fl = S”Zk. Then from (3.19) it follows
that Sk is a semimartingale under Q, and thus also under P (recall that the
semimartingale property is invariant under substitution of an equivalent measure).
Hence S is a vector semimartingale.
In order to verify Assumption 3.20, and later to compute the prices of attainable
contingent claims (see subsection 3.3), it is necessary to actually determine at least
one martingale measure Q E P. This will be done later for some concrete examples,
but it should also be noted that there exists a well developed general theory on
change of measure for semimartingales. ? ire general form of Cirsanov’s Theorem
[32, ppa 376-3791 sho*:vs that to find a Q E P one must find a strictly positive

237
martingale M which bears a certain relationship (involving jfoint variation) to the
discounted price process 2. A nice account of this general theory is given in the
second volume of Dellacherie and Meyer [IO], for which an English translation
should soon be available.
A trading strategy is (temporarilg) defined as a K + 1 dimensional process 4 =
{&;O<f6T)whosecomponents@,#1,...,4K
are locally bounded and predictable (see Subsection 3.1). With each such strategy 4 we associate a value process
V(4) and a gains process G(4) by
## W4)=4tSt= c”
4X
(3.21)
OstsT
9
k=O
## G,(4~=~‘9udS;
## = f i’m:
## dSku,
(3.22)
0 c t ‘s T.
0
k=O
0
As in the finite theory, we interpret Vt(#) as the market value of the portfolio &, and
G,(4) as the net capital gains realized under strategy 4 through time t. But why
should trading strategies be predictable, and why does the stochastic inte:gral give the
right definition of capital gains? Continuing our practice of ducking foundational
issues, we shall say rather little on this important subject. It is obvious that simple
predictable strategies (see Subsection 3.1) should be allowed, and that G( l ) pives the
right notion of capital gains for such strategies. In fact, the definition of G(d) for
simple predictable 4 essentially reduces to that used earlier in the finite theory. The
ultimate defense of our set-up must then rely on the fact that each predictable
strategy 4 can be approximated (in a certain sense) by a sequence of sirnpk
predictable strategies {&} such that G(d) = j 4 dS is the limit (in a certain sense) of
G(&) = 5 & dS. The restriction to predictable strategies serves to limit in an
essential way what $investors can do at jumps times of the prices process. If S is
continuous, one need not worry about predictability at all: using the same forwardlooking (or nonanticipating) definition of the stochastic integral, one could allow all
trading strategies which are optional (adapted and just a bit mlore).
We say that a trading strategy 4 is self-financing if
(3.23i
06 t< T.
= V,(4)+Gt(4),
vt(4)
Since the stochastic integral G(4) is adapted and RCLL, we see that V(4) is adapted
and RCLL for any self-financing 4. Now let @ be the class of all self-financing
strategies 4 such that V(4) 2 0. This is the precise continuous counterpart to what
we had as the set of admissible trading strategies in the finite theory. Unfortunately,
@ will not do as the set of admissible strategies in the continuous theory. Shortlv we
c
shall discuss the problems with db, and thie necessary modifications will be made later.
But first a preliminary result is needed. For any trading strategy 4, let us a
write
G*(+-+$dZ=
f I(bkdZk,
k=l

1 M. Harrison, S.R. Pliska / Martingales, stochastic integrals and continuous trading
238
with the bond component & playing no role. We also introduce the notation
### v*(qb)=pv(&=l$“+ : qbkZk,
k=l
calling G”(4) and V’(4) the discounted gains process and discounted value process,
respectively, for strategy 4.
roposition. Let q!~
be any trading strategy. Then q5 is self-financing if and only if
V*(4) == V,” (4)+ G*(4), and of course V(#) 2 0 if and only if V*(4) 2 0.
.emark. Thus all our essential definitions can be equivalently recast in terms
of discounted quantities. Henceforth we shall deal exclusively in terms of the more
convenient discounted formulation. See Remark 3.27 below.
3.26. Corollary. If q5 E @, then V*(4)
is a positive local martingale, and also a
supermartingale, under each Q E Op.
Proof. For Proposition 3.24, first suppose that 4 is self-financing, meaning that
V( $) = V&5) + G(4). Then d V(4) = AG(q5) = 4 A§ and hence
V_(&=
V(4)-AV(&=@-4AS=@-.
Since 8 is a continuous VF process, (3.18) gives [p, V(#)] = 0, and then from the
definition (3.17) of the joint variation (and the continuity of /3)
dV*@) = d(flV(4)) = & dV(& + V-(4) d@
=@ dV(@+ V-(q5)dp =p dG(@++S-d@
=&$dS+@-dp=4(,GdS+S_dfl).
But sjmilarly dZ = d(PS) = /3 dS f S- dp, so we have d V*(4) = 4 dZ which means
precisely that V*(4)
+f 4 dZ = V,” (4) + G”(4), the desired conclusion.
= V,"
(4)
The proof of the converse is virtually identical, so we delete it. Corollary 3.26 is
immediate from (3.19, the fact that V*(4) 2 0, and (3.8).
3.27.
. Recall that G*(4) does not depend on the bond component 4’=
Thus (3.24) shows that a self-financing strategy 4 is completely determined by its
initial value V,” (4) and its stock components. More particularly, any set of locally
bounded and predictable processes 4 ‘, . . . ) qSK can be uniquely {extended to a
self-financing strategy 4 with specified initial value V:(4) = v by setting
k=l
smce this is the unique choice of 4’ that will give us V*(4) = v + G*(&. Obviously
if and only if v + G*(4) 2 0.

239
NOW what happens if we declare all strategies C$ E @ to be admissible? lf one
defines an arbitrage opportunity as a strategy 4 E @ for which Vu(~)
= 0 but
VT@) > 0 with ositive probability, then it follows from Corollary 3.26 that none of
these exist. Because V*(#) is known to be a positive supermartingale under any
Q E P, it must remain at zero if it starts there. So there are no strategies in @ which
turn nothing into something, but there may be (and generally are) strategies which
turn something into nothing. In Subsection 6.1 we will give an example (for the
Black-Scholes model of Subsection 1.1) of a suicide strategy & E @, such that
V&J) = 1 but VT@) = 0. If all strategies ~#5
E CP were allowed, the prices of attainable
contingent claims in the Black-Scholes model would therefore never be unique.
Having determined that a claim X is attainable at price T using some #, we can
always add to 4 the suicide strategy and thus attain X at price T + 1. (Attainable
claims and their associated prices have not been formally defined in this section, but
we trust that the spirit of these remarks is clear from all that has gone before.) So the
first problem with @ is that it contains too many strategies, since we want each
attainable claim to have a unique associated price. We are going to remedy this by
fixing a reference measure P* E P and restricting attention to strategies 4 for which
V*(4) is a martingale, not just a local martingale, under P*. This will of course
eliminate the suicide strategy alluded to above.
Although 43 is slightly too large in the ltnense just discussed, it is slightly too small in
a different sense. Roughly stated, the space of Zocally bounded predictable strategies
lacks a sort of closure property which we need to get a clean result on completeness.
If one wants all contingent claims (or even all bounded claims) to be attainable in the
Black-&holes model, for example, one must allow some strategies which are not
locally bounded. We now introduce a set Q* of admissible strategies which is just
right for our purposes.
3.3. T%e ,final formulation
Let US select and fix a reference measure
P* E P, denoting by E*( l ) the associated
expectation operator. Until further notice, when we speak of martingales and local
martingales, the underlying probability measure is understood to be P? We define
Z(Z) as the set of all predictable processes H = (H’, . . . , HK j such that the
increasing process
## t&J2 Wk, z”l,)“*,
(jar
OstsT,
is locally integrable (see Subsection 3.1) under P* for each k = 1, . . . ,
verified that L??(Z) contains all locally bounded and predictable I!!& a
I H dZ is still a local martingale for these mtegrands [32, p. 341
We now expand our definition of a trading strategy to include all pr
such that (&, . . . , c$I~)E~~(Z).
With I?#)
=:
d, = (#O, 4’ , . . . , c$~)
G*(4) = 14 dZ as before, a trading strategy 4 is said to be admissibk if

240
### V”(4) = V,” (4) + G*W, and
(3.29)
is a martingale (under P*).
V*(4)
Let @* be the class of all admissible trading strategies. The last condition (3.29) looks
awful, but verifying (or refuting) it is not a problem that ever arises if one is interested
only in contingent claim valuation. See Remark 3.33 below. Obviously (3.29) is
equivalent to requring that G*(4) = [ 4 dZ be a martingale and by (3.9) it is also
equivalent to the simple condition
## E”[Wd41= vi?
w*
(3.30)
A contingent claim is formally defined as a positive random variable X (remember
9 = J??$ by convention). Such a claim is said to be attainable if there exists 4 E @*
such that V”, (4) = &X, in which case 4 is said to genera&X and 7~ = V,” (4) is called
the price associated with X.
3.31. Proposition. The unique price v associated with an attainable claim X is
7T = E*&x).
This is of course immediate from (3.30). Hereafter we shall say that a claim X is
integrable if E*(pTX) c 00, and similarly bounded means that PTX is bounded. From
the definition it is immediate that only integrable claims can be attainable. We now
give a more or less concrete test for attainability.
3.32. Proposition. Let X be an integrable contingent claim and let V* be the ROLL
modification of
Then X 3 attainable if and only if V” can be represented in the form V* =
Vg +I H dZ for some HE .2(Z), in which case V*(4) = F’* for any C$ E Cp” which
gen era tcs X.
## process v* is computed before we know
mark. Note
that the candidate value
whether 6~ not
X is attainable.
roof, Suppose X is attainable, generated by some # E a”‘. Let Hk = 4k for
Fc=l,...
, K SO that j H dZ = G*(d). Since pTX = V’*,(4) and V*(@ is a martingale by (3.29), we have that
ut v:(cQ’i= V$(#)+GF(#)=
because +~a*,
so we have the
Vg(&+JiHdZ
desired representation.
For the converse, let X be an integrable claim, define V* as indicated, and suppose
that V* = V~+fHdZforH~~(Z).Set#‘=H’,...,+~-H~,andthendefine

211
Q!? as in Remark 3.27, with v = V,“, thus yielding a trading strategy 4 with
Obviously V* is a positive martingale by its very definition, so 4 is an admissible
strategy with V%(4) = &X. Thus X is attainable, generated by 4.
3.33. Remark. Note that the trading strategy 4 constructed in the second half of the
proof, starting with the integrand H which appears in the representation, automatically satisfies the stickly condition (3.29), because of the way we defined V* in the
first place.
3.4. Complete markets (representation of martingales)
We say that the market model of Subsection 3.3’is complete if every integrable
claim is attainable. Before proceeding with the analysis of complete markets, let us
establish that nothing is added to this definition by considering claims payable &$OM
the terminal date T. Suppose we define a (wide sense) contingent claim as a pair (I, X)
with 0 6 t s T and X E gt, making the obvious interpretations. We say that (t, X) is
attainable if there exists q5 E @* such that VF (4) = &X. Defining integrability of
(t, X) by the requirement E*(&X)< a>, we then say that the model is (wide sense)
complete if every integrable (wide sense) claim is attainable. Suppose the model is
complete according to our original definition, fix (t, X) and consider the pair (T, X’)
where X’ = &XSt. Obviously E*&X’)
= E*(&X) c ts, so X’ is an integrable claim
(payable at T). Letting 4 E @* be a strategy which atta,ins X’ (remember we assumed
completeness in the narrow sense), we know that V*(4) is a margingale under P’
with V”, (4) = @TX’. Thus
## vr (4) = E*( I+(#) I9t) = E*&X’I%)
= E”(&Xl%)
= @tX,
so ~5 also attains (t, X), and we conclude that (wide sense) completeness is equivalent
to completeness in the original narrow sense.
All notation and conventions established in the last section remain in force. In
particular, the term martingale implicitly refers to the reference measure P*. Let &
be the set of all martingales, and let A(Z) consist of all M E Jc& representable in the
form
(3.35
M = MO + I H dZ
for some H E LZ’iZ).
If JU = &(Z), thlen we say that Z has the martingt;le representation property for
(0, IF, P*). This definition of course involves the filtration IF in a fundamental w
Roughly speaking, it says that Z provides a basis for the space J# or that
with stochastic integrals playing the role of liriear combinations.
3.35. Theorem. The model is complete if and only if .ti = &(Z).
3.36. CosolPary, If IFb is a singleton, then the model ,r’.s
complete.

242
J.M. Havison, S.R. Pliska / Martingales, stochastic integrals and continuous trading
Theorem 3.35 follows immediately from Proposition 3.32, using the fact that any
can be expressed as the difference of two positive martingales. Corollary
martingale
3.36 comes from the general theory of representation of martingales. Specifically it
follows from the results on pp. ?3?-345of Jacod [18], using the fact that if P* is the
sole element P, then P* is an extreme point of the set of all probability measures
under which 2 is a martingale. Using the general theory in [18, Chapter XI],
Corolilary ? ,36 can actually be strengthened to say that the model is complete if and
only if P* is an extreme point of a certain set. To state this result precisely requires
some additional, rather technical deficitions, so we shall not pursue the matter
further, Jacod’s general theorems on representation of martingales have an obvious
aesthetic appeal, and they provide a potential means of establishing the completeness of any given market model, but there is nothing comparable to the very explicit
characterization of complete finite markets which was given in Subsection 2.4. Tlhat
result makes one feel that the ultimate characterization of complete conticuous
markets should involve the fine structure of the filtration IF.
Moving on to more concrete issues suppose that D: = lFs, the minimal filtration
(satisfying the usual conditions) with respect to which S is adapted. This is intIerpreted to mean that investors only have access to (or at leasr are obliged to base their
trading decisions solely on) p:ast and present price information. Let us further assulme
that So (the bond price process) is deterministic, this giving Fs = IF z because 2 = 13s.
In the general set-up, completeness is a joint propertqof (0, IF, P*) and 2, but now
2 actually determines the filtration, so there is no need to mention the underlytng
space at all. Thus we are led to say that a martingale 2 is complete if every ot%ler
martingale
M over IF2 can be represented
as M = MO +I H dZ with H
predictable.
We shall now discuss some martingales which are known to be complete in at least
rclughly the sense of the last paragraph. Certainly the oldest known result of this type
concerns the completeness of one-dimensional Brownian motion (which implies that
every (contingent claim is attainable in the Black-Scholes model). Clarke [4] attributes this to Ito [ 141, and different proofs have been given by Kunita and Watanabe
[23], Dellacherie [8], and doubtless many others. Multidimensional Brownian
motion is also complete, as we will discuss in Section 5, although its natural analog in
discrete time is not (see Subsection 2.5). Jacod [17] says that more general types
of diffusion processes are known to be complete, as one can easily deduce from
the result for Brownian motion itself, but we do not know a good reference
on that subject. The Poisson martingale cN, -cAt where c is a real constant
and N is a Poisson process of intensity A, is also known to be complete.
This result is usually ascribed to Munita and Watanabe [23], and it has been
generalized to arbitrary point processes [lS]. Finally, it is well known, although
we cannot produce 21 reference, that the Wiener and Poisson martingales are
the only complete one-dimensional martingales having stationary, independent
I
increments.

J&i. Harrison, S. R. Pliska / Murtinga&
stochastic intd,grals and continuous trading
243
eturn processes and the semimartingale expo
It is customary in financial economics to specify not price processes themselves but
rather the corresponding return processes (see Subsection 1.1). In this section we
describe briefly the general mathematical nature of that correspondence.
4.1. Exponentiation
Let X = {Xl; 0 6 t =Z T} be a semimartingale and consider the equation
&=I&+
‘U..dX,,
(4.1)
@=t~?‘,
I
0
where UU E F. is aivu given. We would like to find a semimartingale U satisfying this
equation. It turns out [32, p. 3041, that (4.1) always has a (semimartingale) solution; it
is unique, and it is given by
f%,(X) = exp(X, -X o - $[X, Xlt) n (1 + AX,) exp( - dX, + $(AXs)*).
(4.3)
sst
‘This process g(X) is called the exponentiul of Xin the semimartinyale sense. Note that
go(X) = 1. A key property of the semimartingale exponential is [32, p. 3051
zqX)8( Y) = 55(X + Y + [X, Y])
(4.4)
for auy two semimartingales X and Y. Since [X, Y] ‘- 0 if either X or Y is continuous
and VF (see Subsection 3.1), this means
8(X)8(Y)
= 8(X + Y) if X is any semirnartingale
and Y is continuous and VF.
(4.5)
Let % be the set of se:mimartingales X such that 1 + AX a 0, and let #
be those
semimartingales X satisfying the stronger condition that 1 -t AX > 0. Then from (J.3)
it follows that
8(X) 2 0 if and only if X E 3,
and
4.2. Return processes
0ur price proces
’ and its corresponding retur
other via (4.1) with ’ instead of U’ and Rk instead

244
J t
R’ expressed in terms of Sk by
## (l/d_) ds:, OasT,
R;=
(4.7)
k=O,l,...,
K.
0
In the case of the continuous VF bond, this simplifies to
RP
(4.8)
OaGT.
=log(S;)=a,,
We set R = (R’, R’, . . . , RK), and call RK the return process for security k.
The following argument shows that (4.7) really does 8 Jine R” unambiguously in
Lliiwhi * xt). The discounted
terms of Sk (remember that we assume IP non-em;+
price process Zk (see Subsection 3.2) is a strictly positive martingale under each
(2 E P, so Z! is strictly positive and left-continuous, implying that (l/S!
) is locally
bounded. So the stochastic integral in (4.7) is well defined, the integrand being locally
bounded and the integrator being a semimartingale?
Since (4.7) is equivalent to the statement that dSk == Sk dRk, we see from
Subsection 4.1 that Sk and 14’ are also related by the semimartingale exponential.
That is,
k=O,l,...,K.
(4.9)
Sk=S$(Rk),
By (4.6) and the strict positivity of Sk we see that Rk E 9!’ for k = 0, . . . , K.
Consider now the discounted price process ZK. We have /3 = exp( - a) = %‘( -a),
so (4.5) gives
Zk =, psk s
fg( -a)S$(Rk)=Zgk%‘(Rk-a).
(4.10)
Defining the discounted return process Y = ( Y ‘, . . . 9 Y K, by
Y,” == R,k -at,
(4.11)
OwsT,
k=l,...,K,
(4.10) gives
### Zk = Z,kS( F).
(4.12)
Thus Yk plays the same role for Zk as R k does for Sk. We emphasize that the tidy
relationship (4.11) depends crucially on our assumption that cy is continuous and VF,
so that [Rk, -a]=O.
5.
We now consider a generalization of the Black-Scholes model (see Subsection Is, 1)
which has a bon:1 and K correlaled stocks. The bond price process is Sy = exp(rt),
0 c t -G T with r a real constant as before, and each individual stock price process
s’, . . . s SK is to be a geometric Brownian motion. To specify the model precisely it
will be convenient to construct first the discounted return process Y (see Subsection
4.2), then the discounted stock price :ocess Z (see Subsection 3.2), and finally the
.

245
processes Sk themselves. We continue to denote components of vectors by superscripts, except in a few isolated instances where doing so is hopelessly impractical.
Let A = (hii) be a non-singular K x K matrix, and define a covariance matrix
(symmetric and positive definite) A = (aij) by setting A ‘-= AA’, meaning that
## @i z fAli
ik ik fori,j=l,...,K.
(5.1)
Er=1
Let p=(&...,
pK) be a vector of real constants. Next, let W’, . . . , WK be
independent standard Brownian motions with Wlj = l
l = W,” = 0, defined on some
l
probability space (a,$, P). Then set
Y,=AWt+pt,
@=tsT,
i5.2)
meaning
## Yf = f hkiW;+pkt,
k=l,...,
K.
(5.3)
OstsT,
j=l
Thus Y is a vector Brownian motion with covariance matrix A and drift vector e.
### Now let 20, . . . , 2,” be strictly positive constants and set
1
## 2: =i?$exp(Y:--$~?k~l),
k=l,...,K.
(5.4)
OstsT,
Ito’s Formula gives us
### so zk = Z&8( Yk) as in Subsection 4.2. Furthermore,
d[Z’, Z’]t = Ziz’ d[ Y’, Yi]t = ziZ’a, dt.
(5.6)
The first equality in (5.6) follows from (5.5) and the basic joint variation property of
stochastic integrals [32, p. 2711, the second is a well-known property of Brownian
motion. Now define
SF = SyZF =ertZf
forOst<T,
k=l,...,
K,
so that Zk =pSk as in Subsection 3.2. From (5.5)-(5.7) we see that SE,. . . ) S” are
correlated geometric Brownian motions as promised, the return process for Sk being
R+
‘ff + rt (a Brownian motion with variance akl: er,d drift p” + r
information structure, we take IF = IF w = IF y = IF2 = IFS (see Subsection 3
investors are required to base their trading decisions on past and present pric
~nform;rtion only.
For the explicit calculations of Subsectie I 5.3, the following observatio
helpful. Let h = (h ‘, . . . , hK) be the function defined by
C5.W
k=l,...,K,
hk(x, y, t)=xkexp(yk-&t),

246
h (20, Yl, t). Furthermore, it is easily
for X, y E IRK and t 2 0. Then (5.4) says that Zt =
.
verified that
for Osts
7 47. = h(Z,, YT - Yt, T-t)
T.
(5.9)
5: 1. The reference measure
Because A (and hence A) is non-singular by assumption, there exists a unique
M-vector y satisfying
(5.10)
ny=p.
Now it will be convenient to define a vector process 6 = (tl,.
. . , tK) by
(5.11)
&= W,+yt,
OstsT,
so that (5.2) can be restated as
Y, = A&, 0 s t s T.
(5.12)
Mow define the martingale (under P)
M,=exp I - f
y”WF -i
5 (yk)*t ,
OctsT,
I
k-l
k=l
and let the reference measure P* be given by
dP* := MT dP.
(5.13)
Because M is a strictly positive martingale with MO = 1, we see that P* i; a
priobabihty m:=asure equivalent to P. The following proposition, sometimes Cal ted
the likelihood ratio formula for Brownian motion, is a special
case of the o.riginal
Gjirsanov Theorem [ 121,
. Proposition. The processes el, . . . , tK are independent
standard Brownian
motions under P*.
From this and (5.12) we have that Y is a Brownian motion with zero drift and
covariance matrix A under P*, and then from (5.4) that 2 is a (vector) martingale
under P* as required. From Theorem 3.35 and the representation theorem cited in
the next subsection, it foll*Jws that P* is in fact the unique element of a9, but we will
ma.ke no direct use of this fact. We fix P* as our reference measure and then define
admissible trading strategies in terms of it as in Subsection 3.3.
5.2. Completeness
We now replace P by P*, so the terms integrable, martingale and local martingale
implicitly refer to P*. From the definition (5.11) of 6 i: is clear that IF = 0:” = ff’,
meaning that the filtration in our market model is that generated by the standard
Brownian motior, 8. Let A? (the space of all martingales) and A(Z) be defined as in

247
Subsection 3.4. We want to show that A(Z) =A, and hence by Theorem X35 that
the model under discussion is complete.
First suppose
E A is square integrable, meaning that E*(1MT12) < 00. It is well
known [32, pp. 911-9131 that Al can be represented in the form
‘&d&,
(5.15)
Mt=Mo+
OstsT,
I
0
where 9 = (0i, . . . , 19~) is a predictable process satisfying
## E*( ~oT~h~2
(5.16)
dt) coo.
Furthermore, every martingale M on the Brownian filtration ff is continuous, hence
bcally sacare integrable, and it then follows easily that each MEA
can be
represeatcd in the form (5.15) with 8 satisfying (5.16) locally, *which means simply
that
(5.17)
P*
= 1.
=l&I'dt-)
From (5.11) and the non-singularity of A, this is obviously equivalent to the
following. Each M E 4 can be represented in the form
(5.18)
‘q5dY,,
OsssT,
Mt=Mo+
I
0
is predictable and satisfies
where q = ($,
. . . , $)
## P* (I Tlqt~2dt<m)
=
(5.19)
1.
0
Now let us define H = (H’, . . . , Hx) by
## Hf = qw forO<tsT,
(5.20)
k=l,...,K.
Using (5.5), we can then rewrite (5.18) as
(5.21)
Mt=MO+
‘HsdZ,,
OasT.
I
0
Furthermore, the increasing process (3.28) occurring in the definition of Z(Z) is, by
## k .k \
(5.6),
## (H:)2d[Z , Z Is = (dhc ds .
t
l/2
)
t
## l/Z I (I
U
0
0
This process is continuous, so it is locally i. tegrable (under P*) by
can be repres
EA?(Z). ‘ll’o repeat, every
conclude that
dZ for some H E d?(Z), so A! = A(Z) and hence the model
Theorem 3.35.

248
One can greatly generalize the diffusion model discussed in this section and still
have completeness. The diffusion coefficients aij can be made to depend on past and
in a more or less arbitrary way, and the drift coefficients pk may
present
prices
depend on even more than that. (We will not attempt to even make these statements
let alone justify them.) But it appears that the riskless interest rate must be
precise,
deterministic if one is to get completeness, although it may vary with time, and that
the diffusion coefficients may not depend on more than past and present prices. We
are not sure how one even states this latter property precisely, but s.?e the example of
Subsection 6.3.
.
5.3, Explicit computations
We now consider a class of contingent claims X for which one can calculate quite
explicitly the associated price 7~ = E*(#3TX) and a trading strategy 4 which generates
X. Specifically, we assume in this section that
(5.23)
X=erf+(&)
forsome~:R~+R+.
Since Z”, = exp( - rT)Sk, for k = 1 , c . . , K, this means simply that X is a function of
the final stock prices only. As usual, though, it is more convenient to speak in terms of
the discounted price process 2 throughout. It is easy to verify that the European call
option discussed in Subsection 1.1 corresponds to the function
$(x) = [x1 - ce-“I+,
assuming that we are talking about a call option on stock k = 1 (with exercise price c
and expiration date T).
Let X be given by (5.23) and assume hereafter that it is integrable, meaning that
7~ = E*(&X) = E*(e-‘*X) = E*[:$(ZT)] < 00,
Then we know from the completeness result of Subsection 5.2 that X is attainable at
price r. Moreover, we know from Subsection 3.3 that the discounted value process
V* = V*(4) for any 4 generating X is given by
VT =E*(PTXI~~)=E*[*(ZT)I~~~],
(5.24)
OGtST.
our objective now is to calculate V* and hence 7~ (since 72 = V,” ). First let’s define
the normal density function
C(z) = (2nt)-K’2
exp( -$1*)
(5.25)
for t>O
and z E RK. Observe that
(5.26)
p*{(z;.
-- 6)
E dz
1%)
= rT-r(Z)
dz,
meaning that & - & is indepenclent of %t and has density r&
0) under P*. This, of
course, follows from Proposition 5.14 and the fact that IF = ff’. Now (5.9) and (5.12)
give us
zT= h(Z~,A(&-&),
(5.27)
r-t),
f&tGT,

J.M. Harrison, S.R. PIriska / Martingales, stochastic integrals and continuous trading
249
so combining (5.24)-(5.27) we have
## vf = E*MWt,
### At&T - 6th T- t)) 1 %I
AZ, T - #k-i--t(Z) dz
(5.28)
= I #(h(Zt,
where the integral is over RK. Defining
f*(x, t) = 1 9(h(x, AZ, t))W)
dz
(5.29)
for x E Wf and t a 0, (5.28) is more compactly stated as
(5.30)
V,” =f*(Z;, T-t),
OasT.
In particular, our final valuation formula for X is
(5.31)
TT = V,” = f*(&, T).
Obviously (5.29) and (5.3 1) give the most explicit valuation formula possible without
further information on the payoff function +.
To determine the trading strategy 4 which generates X, we compute the differential of V* from (5.30) and Ito’s Formula, observing that p has the necessary
regularity by its definition (5.29). Letting @/au)f * denote the partial derivative off”
with respect to its second argument, and using (5.6) we have
K
## cw; = c ---i;f*(&
a
(5.32)
f*(& T - t) dt
T-t)dZ,k
+
k=l ax
where L* is the linear partial differential operator
K
K
a2
L* = 3 c c &-&&j
ad
ad'
i=l
j=l
Starting from the fact that r((z) satisfies the heat equation
and fighting through all the tr&nsformations which define f” in (5.29), it can be
verified that (a/au)f* = L*f*. Thus, taking
k t =$f*(&T-t),
4
(5.33;
OstsT,
k=l,...,
K..
we see that (5.32) gives
t
VT = v,” + ;
OstsT.
4,” dZ,k,
I
k=ll 0
Then F’ ropssition 3.32 shows that strategy 4 = (4*, c$‘, . . . , &K) generates X, where

250
the bond component 4” is given by
From the general representation result (Proposition 3.32) and the completeness
result of Subsection 5.2, we knew that our process VF = f *(Zr, T - t) was going to be
representable in the form (5.39, and from (5.32) we see that thiis is the case if and
only if f* satisfies the differential equation (a/au)f* = L*f*. T:hus the differential
equation has arisen here as a logical consequence of various general propositions. In
contrast, it was by solving an analogous differential equation that Black and Scholes
[24 originally obtained their option pricing formula.
Because all the calculations of this section have been done in discounted terms, they
do not mesh precisely with the earlier discussion of option pricing in Section 1. The
interested reader should have no trouble making the linkage, however, by recasting
the earlier discussion in discounted terms. In particular, the function f (x, t) defined
by (1.5) can be gotten by evaluating QS.29) for
### bw=bl - c exp( - rT)]+,
as we have indicated earlier.
We collect in this section four concrete examples which illustrate the diversity, and
some of the intricacy, that one encounters in models with continuous trading. The
first example is of a trading strategy which turns something into nothing. The
remaining three are chosen to shed light on the important subject of completeness.
We make no attempt to connect these examples with any realistic problems, and the
analyses are neither systematic nor rigorous.
6-l. A bad strategy
Consider the Black-Scholes model of Subsection 1.1, specialized to the case r = 0
(so that So= l), T=l,
and SA= 1. As before, we call So and S1 the bond price
process and stodk price process respectively. As a first step in constructing the suicide
strategy alluded to in Subsection 3.2, suppose b > 0 and consider the strategy
ifk=OandO<t<r(b),
‘L+b
if k = 1 and Osts7(b),
otherwise
where
T(b) = inf{t: S: = I+ l/b) = inf{l: Vt(4) = 0).

J.M. Harrison, S.R. Pliska / Marlingales, stochastic integrals and continuous trading
251
The investor starts with one dollar of wealth, he sells b shares of stock short and buys
1 + b bonds, holding this portfolio up until d = 1 or he is ruined, whichever comes first.
The probability of ruin under this strategy is p(b) = (r(b) < I), and it’s clear that
p(b) increases from zero to one as b increases from zero to infinity. By selling short a
very large amount of stock, the investor makes his own ruin almost certain, but he
will probably make a great deal of money if he survives.
The chance of survival can be completely eliminated, however, by escalating the
### amount of !$ock sold short in the following way. On the time interval [0, 11 we follow
the strategy of the last paragraph with parameter b = 1. The probability of ruin
### during [0, 3.1
is then p = P(T(~) s 4). If ~(1) > $, we adjust the amount of stock sold
short to a new level bl at time 3, simultaneously changing the amount of bond held in
a self-financing fashion. Specifically, the number bl is chosen so as to make the
conditional probability of ruin during the interval ($,$J equal to p again. In general, if
at any time tn = 1 - ($)” we still have positive wealth, then we readjust (typically
increas;) the amount of stock sold short so that the conditional probability of ruin
during (t,,, r;t+J is again p. To keep the strategy self-financing, the amount of bond
held must be adjusted at each time tn as well, of course. The probability of survival
through time tn is then (1 -p)“, which vanishes as n + 00 (t, -) 1). Thus we obtain a
piecewise constant, self-financing strategy q5 with V&)
= 1, V(4) 3 0, and VI(&) =
0. This is closely related to an example presented by Kreps [20].
6.2. A point process model
Consider the model with M = 1, So = 1, and
Sf = SA exp(bN, -gt)
(6.1)
where N = {N,; 0 s t s T} is a Poisson process with intensity A > 0, and b and p are
positive constants. This is the model of Cox and Ross [S], specialized to the case of
zero riskless interest rate. Corresponding to S1 is the return process (see Subsection
4.2)
I--: = (exp(b)-I)N,-+t.
(6.2)
For the filtration F we take the one generated by S’ itself.
Let
(6.3
A*=&(exp(b)-1)
and
### I@ = (A*/AI~~ exp((A -h*)t),
0~ t s T.
is a strictly positive m
gale with MO = 1, we de
Observirlg that
dP”. rorn the chan
equivalent probability measure P* by d?* =
theorem for point processes [3, pp. 377-3791 we have thalt N is a Poisson process
with intensity A* under P *. It follows from (6.2) and (6.5) that R’ is a martin

J.&f. Harrisori, S.R. Pliska / Martingales, stochastic integrals and continuous trading
252
under P*, and then from (6.1) that S1 is one too. Hence we can (and do) adopt P* as
our reference measure.
It is well known, cf. Jacod [18, p. 3471, that R ’ has the martingale representation
property for (a, P, P*), and it is straightforward to verify that the same must be true
of S’, Thus this model is complete (see Subsection 3.4). and the price associated with
any integrable contingent claim X is
r = E*(x)
because p = 1. In particular, consider the call option
### x =[S&cl’.
LJsing the fact that N has intensity A* under P*, we have the valuation formula
n- = E*([S; -cl+)
= E*([SA exp(bNT - p*T) - c]‘)
=~f-&I*T)“[S~
exp(bn-pT)-cl+.
=
.
This is a special case (the riskless interest rate is zero) of the formula obtained by Cox
and Ross [SJ. The precise trading strategy which generates this contingent claim X
can be computed as in Subsection 5.3.
6.3. A model which is rrot complete
Let (J2,9, P) be a probability space on which is defined a standard Brownian
motion W = { Wt; 0 s t s T} and an independent process CT = {a,; 0 s t 6 T} such that
2 for 0 G t c $T with probability 1,
a; = 1 for ;T G t s T with probability $,
3 for $T G t s T with probability $.
Let K = 1, assume So =
- 1 (the riskless interest rate is zero throughout), and define
t
a,dW,,
Ost<T.
R:
=
I
0
Thus the return process R ’ for the stock evolves as a driftless Brownian motion with
variance parameter a: = 4 over the interval [0, $T), and then a coin is flipped. If a
head is observed, the variance parameter increases to & = 9, but if a tail is observed
it decreases to U: = 1. @bserve that
## CR’, R’], = I’u:
ds,
OasT.
(6.4)
0
Let the filtration F be that generated by R’, or equivalently by S’, so investors have
access only to past and present price information. The filtration 6 is the same as that

253
generated by PV except that, by (6.4) and the right continuity of IF, 9. is augmented by
the outcome of the coin flip for $T 6 t s T. Obviously R ’ is a martingale, and it is easy
to check that the same is true for S1 = %(R ‘) = exp(R’ -&I?
I, R ‘1). Of course
Z1 = S1 because p = 1. Thus we can (and do) adopt P itself as our reference measure.
It is easy to prove, using the fact that u/ has the martingale representation
property for its own filtration, that every martingale on (In, IF, P) has the form
(6.5)
where # and $* are predictable. Since Z1 = S’ is continuous, only continuous
martingales M can be represented as stochastic integrals with respect to 2’. So by
Theorem 3.35 this model is not complete. The investors do not have available
enough financial instruments to span all sources of ?zncertainty.
This model can be made complete, however, by the introduction of another
security. Let
1 for Oat<$T,
for$Tst<TandgT=l,
sf = 0
2 for$Tst<TandcT=3.
I
This is the price process for a ticket which can be bought (or sold) at a price of one
dollar at any time before $T. If a head (a variance increase) is then observed, the
ticket becomes worth two dollars, but the ticket becomes worthless if a tail is
observed. The tickets represent an institutionalize
means of betting on the outcome
of the coin flip, and we impose the strong assumption that the price of the tickets is
certain to remain constant up until the time of the coin toss (this assumption is not
essential, but it eliminates a lot of complexity). Clearly S* = 2* is a martingale, so P
remains a valid reference measure.
Now from (6.5) and the definitions of CT and S* we have that every martingale
satisfies
dM=$&lS’+J12dS2=+1dZ1+~2dZ2
for some predictable integrands $’ and $*, so the model is now complete by
Theorem 3.35.
This example suggests another natural sort of question which one might ask about
security markets with continuous trading. Given only a filtered probability space
(0, IF, p*), what is the minimal number of securities adapted to IF with which one can
create a complete market, and what is their form. 3 See [7] for a discussion of this
question (cast i:? purely mathematical terms).
6.4. A mod4 of mixed type
This subsection is devoted to yet anotl -r example with a b
= 1). We believe, but cannot rove, that this model is compl~t
(
this example provides a vehicle for discussion of several importan

254
price process is So = 1, so the riskless interest rate is zero. To simplify notation, the
stock price process will be denoted by S rather than S’, and the corresponding return
process by R rather than R ‘. Because P = 1, there is no distinction between S and
Z ;= pS9 or between R and Y = R -ar, so we are free to (and shall) reuse the letters Y
and Z with completely new meanings. The time parameters of various processes will
appe;ar as subscripts at some points and as functional arguments at others, depending
on which is more convenient.
Begin with a probability space (U, 9, P) on which is defined a standard (zero drift
and unit variance) Brownian motion W = ( Wt; t 3 0}, a Poisson process N =
{N(t); t 3 0) with intensity A > 0, and an i.i.d. sequence of binary random variables
l .} such that xn = * 1 with equal probability. We assume that W, N and (xIt}
(X1, x2,
l
are also indepndent of one antoher, with Wo = N(0) = 0.
Let 2 = (1,; t 2 0) be the focal time of W at the origin, meaning that
(6.6)
From this definition it is apparent that
2 increases only at times t where W, = 0,
(6.7)
and it is well known that 2 is continuous but not absolutely continuous. In fact,
because the set {t: Wt = 0) has zero Lebesgue measure (almost surely), we have from
(6.6) that I is flat except on a set of measure zero. Next let 70 = 0,
rn =inf{tH):
forrz=1,2,...
(6.3)
Wt=n}
and
M(t) = sup{rz so:
y=t},
tiNI.
Finally, let y be a coristant (0 C 2’ < 1) and define
RI= Wt+Xt+
Yt
(6.9)
where
X, = N(1,) -Al,
and
YC = y[xl + l 9 * + xMctj].
(6.10)
Note that each of the jump times Ti, T2, . . . of X must be a point of increase for Z, and
thus Ftp(?‘,) = 0 for all n by (6.7). In contrast, Y jumps by ‘yxl, ‘yx2, . . . at the hitting
times 71, 3~2,
. . . respectively, so the two sequences of jump tilmed are disjoint. Also, I
is a continuous VF process. Thus (see Subsection 3.1) we have
## I[ w Wlr =: t,
## Xlr = I: tAXA = NW
sst
### y2 (t)
1p.J Y-jr = 1 (AYs)2=
and
[W9
Y]=[X,
Y]=O.
Sst
We now set S = 5?(R), taking So = 1 for convenience. From the preceding equations
and Subsection 4.1 we see that S = 8’(R) = #?( W)%‘(X)S?( Y). The general formula

J.M. Harrison, S.R. Pliska / Martingales,
stochastic integrals and continuous tmding
255
(4.3) for the semimartingale exponential then gives us
M(r)
S, = exp( Wt - it)2 N(‘o
(6.11)
exp(--~~~) n (I+ .YX~)~
Observe that our stock price process S satisfies dS = S d W when the underlying
Brownian motion W is not at an integer level. At each of the times rn whiere W hits a
positive integer level II for the first time, S either jumps to (1 + y) times its previous
value or else drops to (1 - y) times its previous value (with equal probalbility). Also,
there are times T,, Tz, . . . at which S jumps to double its previous value, but these
only occur when W is in state zero, and it is at just such times that the factor
exp(-Al,) is pulling the stock price down (in a continuous fashion).
We take the filtration for our example to be IF = lFR = IFS (see Subsection 3.4),
meaning that investors have access only to past and present stock price information.
It is apparent that W, X, Y and hence ,q are martingales over IF, so S = Z?(R) Is at least
a local martingale. Direct calculation shows that S is moreover a martingale, so we
can (and shall) take Ip itself as our reference measure.
Readers familiar with martingale theory will recognize (6.9) as the decomposition
of R into its continuous martingale part (W), the sum of its predictable jumps ( Y),
and the compensated sum of its totally inaccessible jumps (X). MIeyer [32, pp.
261-2671 explains how an arbitrary martingale can be so decomposed, and we shall
review here just the two essential definitions. A stopping time r is said to be
pred&zbZe if there exists an increasing sequence of stopping times {TV} such that 7 fr
almost surely as kToo, in which case the sequence {,Tk) is said to announce r. Each of
the hitting, times TV in (6.8) is predictable because we can construct a sequence {TV)
announcing ~1 (for example) by taking
TK =inf{taO:
WI=l-l/k},
k=l,2,....
At the other extreme, a stopping time 7 is said to be totaily inaccessible if P(T = 7’) = 0
for every predictable stopping time 7’. The jump times of a Poisson process are the
canonical examples of totally inaccessible stopping times, and from this one can quite
easily show that the jump times Tl, Tz9. . . above ;are totally inaccessible. This
categorization of stopping times is of fundamental importance in martingale the
and the definitions also seem natural and useful for ptrrposes of economic modeli
The return process R (or equivalently S) in this elxample was devised so as
exhibit both predictable and totally inaccessible jumps plus a nontrivial continuous
martingale part, and in this sense it is representative of the most general
possible. However, our example also has the feature that R (or S) can have on1
finitely many jumps in a finite amount of time, and in this regard it Is q
general martingale may have a countably infinite number of jumps in
of time, a.nd it is this feature which geneY ltes most of the difficulties in the
theory of stochastic integration.
Now what is the general form of a predictable trading strategy in this model?
is a very long story, which we will not go into here. The reader with a serious interest

256
in the general theory of continuous trading will find further analysis of this example
an educatilonal exercise, however, and we will say just a few more words to facilitate
such a study. If f, g and h are any three predictable processes, then the process C$
defned by
(h(o)
if w(w)=O,
if T&0)= t for some n,
&(o)={g,(o)
## I h,(w) otherwise,
is also predictable because the sets {(t, w): W&o) = 0} and {(t, CO): T,(O)
= t for some
n) are elements of the predictable a-algebra. Furthermore, with 4 defined in this
way we have
J’t#,ds=j4s_dR=[ga-(dW+dX+dY)
J
## = hs-ciw+lfS_cix+(
### gs-cwusing the fact that 4 = h except on a set of time points having zero Lebesgue
measure. What this ultimately means is that investors are able to use completely
different trading strategies relative to the three components (W, X and Y) of the
return process R. From the known completeness of Brownian motion, the Poisson
martingale N(t)
- At, and the one-dimensional random walk in discrete time, we then
conjecture that this model is complete.
7. Uonclndimg aemwks
This section presents a list of unresolved questions which, we think, merit further
study by probabilists and/or ecsnomists. It may be that some of the answers are
already known, or that they can be gotten by straightforward application of existing
theory. At the end, we discuss briefly the questions of why one ought to study
continuous trading at all.
In Section 3 we sidestepped the whole question of viability with continuous
trading. How does one justify the critical assumption (3.20) from more primitive
economic considerations, or is Assumption 3.20 even the right expression of
viability? Should we replace the assumption by the weaker requirement that Z be
just a local martingale under some equivalent measure Q, or perhaps by the stronger
requirement that 2 be a square integrable martingale under some of such Q? Again
we refer the interested reader to [20] for more on this very complex subject.
The definition of an attainable contingent claim depends directly on the definition
of a self4inancing strategy, which in turn depends on how one defines the gains
operator G. In Section 3 we have not defended our restriction to predictable trading

J.M. Hurrison, S.R. Pliska / Martingales, stochastic integrals and continuoux trading
257
strategies, nor our definition of G as a stochastic integral. We have no doubt that
these are the right definitions, but a careful study of this issue is certainly
needed.
It
should be possible to show, for example, rhat a claim is attainable according
to our
definition if and only if it is the limit (in some appropriiate sense) of claims generated
by simple (see Subsection 3.1) self -financing strategies.
In Subsection 3.2 we temporarily restricted attention to locally bounded predictable strategies. For any integrand CP of this class, and any semimartingale S, the
stochastic integral 14 dS is well defined; this definition depending on the underlying
probability measure only through its null sets. There is furthermore a well developed
stochastic calculus for locally bounded integrands [32, Chapter IV], and we used
parts of this calculus to show that all our essential definitions could be recast in terms
of discounted quantities. Then we fixed a reference measure P* and used it to define a
new class of strategies @*, some of whose members are not locally bounded, Can the
undiscounted gains process G(4) = j 4 dS be meaningfully defined for each 4 E @*?
If so, can the final formulation of Subsection 3.3, which was expressed entirely
in terms of discounted
quantities,
be equivalently
recast in undiscounted
terms?
Another important question concerns the extent to which our choice of reference
measure (when there is a choice) affects the set of contingent claims which are
ultimately found to be attainable and the prices associated with these claims. There is
of course some effect, but we believe it is relatively small. More particularly, we
conjecture (but cannot prove) that the following two statements are true. First, a
bounded claim is attainable with one choice of reference measure if and only if it is
attainable with any choice of reference measure. Second, if a claim is attainable
under two different choices of reference measure, then it has the same associated
price under each. Resolution of these issues is a matter of highest priority.
Th.e definition of @* in Subsection 3.3 retains only those self-financing strategies c;b
for which V*(4) is a martingale, this ensuring that the price associated with each
attainable claim is unique. One would like to know that in making this definition we
have discarded only b~gically dominated strategies. This requires a result of the
following type. Let X ge a contingent claim, and let a(X)
be the set of all
self-financing strategies 4 such that V*(4)
2 0 and V%(4) :I= &X0
9.1. Conjecture. If @X) is nonempty, then Q(X) n @* is nonempty.
We know from Corollary 3.26 that V*(4) is a local martingale, and hence a
superma.rtingale, undci:r P* for each 4 E Q(X). So a proof oE Conjecture 7.1 woul
show that we have reliiained only that strategy (or perhaps those strategies) Q~hi~h
attain X at the lowest possible price.
In the first paragraph of Section 1 we said that the imathematical str
developed here is potentially useful for z ‘udy of consumptio
First consider the purle investment problem where one start
and wishes to find a self-financing strategy 4 such that

J.M. Harrison, S.R. Pliska / Martingales,
stochastic
integrals and continuous
trading
258
maximal expected utility. In this problem the choice set is essentially the set of all
claims attainable at price 7r, so our conceptual framework is precisely
contingent
For a true consumpltion-investment problem, however, one must allow
appropriate:.
investors to withdraw wealth for consumption over the interval [0, T]. Roughly
this requires that the formulation of Section 3 be generalized in the
speaking,
following way.
The set of admissible trading strategies would be enlarged to include those 4 for
which V(4) 2 0, and I(& = Vo(#) + G(#) - V(4) is an increasing process (rather
than just identically zero) where V(4) G c#& and G(4) = I& dS as before. We would
interpret I,(& as the cumulative amount of wealth withdrawn from the portfolio
over the interval [0, t] for consumption, calling I(& the consur~lption stream or cash
pow generated by strategy (6. An investor starting with wealth v would then choose
among those admissible strategies cfi with Vu@) = w, making his section in such a way
that I($) and V&5) jointly maximize some measure of felicity. Here we are thinking
in terms of the case where there is utility associated both with consumption during
[0, T] and with terminal wealth. For a treatment of consumption-investment
problems with diffusion price processes, see [26,27].
We have observed in Subsection 3.4 that existing general results on the martingale
representation property do not give much insight as to the conditions that yield
complete markets. More specifically, the result cited in Subsection 2.4 for discrete
models suggests that the ultimate characterization of completeness with continuous
trading ought to involve the fine structure of the filtration IF. Perhaps the relationships
between completeness and the martingale representation
property
(see Subsection 3.4) will suggest new lines of attack nn the mathematical problem itself. Be
that as it majr, one of our central conclusions is that there exists potential benefit
for financial economics in continued F,tudy of the martingale representation
property.
Finally, let’s consider the question of why bother with continuous trading, focusing
solely on the problem of contingent claim valuation. Recall from Subsection 2.5 that
a finite market with a deterministic bond and two independent stocks following
,geometric random walks is not complete. In contrast, we have seen in Section 5 that
the continuous limit of this model, having a deterministic bond and two independent
stocks fohlowing geometric Brownian motions, is complete. It should then be possible
to demonstrate that, under the usual conditions justifying a diffusion approximation,
the finite market is in some sense nearly complete, or that each contingent claim is in
some sense newly attainable. This point of view has been discussed by Kreps 5201,
who quite rightly observes that making these statements precise is a mathematical
task of imposing proportions. Still we feel confident that a satisfactory convergence
theory can be developed, and the notion of asymptotic completeness, if accompanied
by a reasonable understanding of how and when it occurs, is of great potential
jimportance. The Black-Scholes model and its various generalizations are important
precisely because they may approximate so many other types of models which are not
complete themselves.

259
This work was done while the second author was on sabbatical leave at the
Graduate School of Business, Stanford University, and he was partially supported by
the National Science Foundation under Grant ENG76-09004 AOl. We are indebted
to -Rick Durrett for his assistance and companionship in our study of stochastic
calculus, to Kristen Harrison for her help with translations, and to David Kreps,
whose ideas permeate this paper.
References
L. Bachelier, Theory of speculation,
in: The Random Character of Stock Market Prices P.H.
111
Cootner Ed., (M.I.T. Press, Cambridge, MA, 1964).
121
F. Black and M. Scholes, The pricing of opttons and corporate liabilities, J. Polit. Econom. 81 ( 1973)
637-659.
P. Bremaud and J. Jacod, Processus ponctucls et martingales: Resultats recents sur la’modelisation et
131
la filtrage, Advances in Appl. Probability 9 (1977) 362-416.
J.M.C. Clarke, The representation
of functionals of Brownian motion by stochastic integrals, Ann.
[41
Math. Statist. 41 (1970) 1282-1295; Correction, Ann. Math. Statist. 42 (1971).
J. Cox and S. Ross, The valuation of options for alternative stochastic processes, J. Fin. Econom. 3
PI
(1976) 145-166.
J.C. COX, S.A. Ross and M. Rubenstein, Option pricing: A simplified apprq-:h. J. Fin. Econom. 7
051
(1979) 229-263.
M.H.A. Davis and P.P. Varaiya, The multiplicity of an increasing family of cr-fields, Ann. P&ah.
II71
2 (1974) 958-963.
C. Dellacherie,
Integrales stochastique par rapport aux Frrocessus de Wiener et de Poisson, in:
ra
Seminaire de ProbabilitC VIII and IX, Lecture h otes in Mzthcmatics 381, pp. 25-26 and 465, p. 495
(Springer, New York, 1975).
Stochastic Process. Appl. 10
C. Dellacherie, Un iurvol de la theorit: de I’integrale sto&astique,
PI
(1980) 115-144.
C. Dellacherie and P.-A. Meyer, Probs jilities and Potentials (North-Holland,
New York, 1978).
DO1
R.M. Dudley, Wiener functionals as Itcrt integrais, Ann. Probab. 5 (1977) 140-141.
WI
1.1. Girsanov, On transforming a certain class of stochastic processes by absolutely continuous
WI
substitution of measures, Theory ProbaS. Appl. 5 (1960) 285-301.
J.M. Harrison and D.M. Kreps, Martingales and arbitrage in multiperiod securities markets, J.
[I31
Econom. Theory 20 (1979) 381-408.
K. Ito, Multiple Wiener integral, J. M;ith. Sot. Japan 3 (1951) 158-169.
1141
J. Jacod, Multivariate
point processes:
Predictable
projection,
Radon-Nikudym
derivative.
WI
representation
of martingales, Z. Wahrscheinlichkeitstheorie
und Verw. Gebiete 3 1 (1s 75 1 235253.
J. _Jaeod, Un theorbme de representation
pour les martingales discontinues, Z. Wahrscheinlich1161
keitstheorie und Verw. Gebiete 35 (1976) l-37.
J. Jacod, A general theorem of representation
for martingales, Proc. Symp. Pure Math. Vol. 3%
El71
(American Mathematical Society, Providence, i977) 37-53.
J. Jacod, C&u1 Stochastique et Probl&nes de Martingales, Lecture Notes in Mathemati~
7fi
WI
(Springer, New York, 1979).
J. Jacod and M. Yor, Etudes des solutions extre Iales et representation
integrale des soiutiQ~s pour
WI
iete t
F
certains problkmes de martingales,
2. Wahrscaleinlichkeitstheorie
und Verw.
83-125.
D.M. Krlzps, Multiperiod securities and the efficient allocation of risk: A comment on the
E201
Scholes option pricing model, U-NBER
Conference
on the Economics of Information
and
Uncertainty, Boston, U.S.A., 1979.

260
[21] DM. Kreps, Three essays on capital markets, Tech. Rept. No. 298. Institute for Mathematical
Studies in the Social Sciences, Stanford Univ., Stanford, CA (1979).
[22] D.M. Kreps, Arbitrage and equilibrium in economies with infinitely many commodities, 1. Math.
Econom., to appear.
[23 ] H. Kunita and S. Watanabe, On square integrable martingales, Nagoya Math. J. 30 (1967) 209-245.
[24] R.S. Liptser and A.N. Shiryaev, Statistics of Random Processes Vol. I (Springer, New York, 1977).
[25] M. Magi11 and G. Constantinides, Portfolio selection with transaction costs, J. Econom. Theory 13
(1976) 245-263.
[26] R.C. Merton, Lifetime portfolio sehxtion under uncertainty, the continuous-time
case, Rev.
Econom. Stud. LI (1969) 247-257.
[27] R.C. Merton, Optimum consumption and portfolio rules in a continuous-time model, J. Econom.
Theory 3 (1971) 373-413.
[28] R.C. Merton, Theory of rational option pricing, Bell J. Econom. Management Sci. 4 (1973)
141-183.
[29] R.C. Merton, Option pricing when underlying stock returns are discontinuous, J. Fin. Econom. 3
(1976) 125-144.
[30] R.C. Merton, On the pricing of contingent claims and the Modigliani-Miller theorem, J. Fin.
Econom. 5 (1977) 241-249.
[31] M. Metivier and J. Pellaumail, Stochastic Integration (Academic Press, New York, 1980).
1321 P.-A. Meyer, Un tours sur les integrales stochastiques, in: Seminaire de Probabilid X, Lecture
Notes in Mathematics 5 11 (Springer, New York, 1976) 245-400.
1331 P.-A. Meyer, Introduction au calcul differentiel stochastique, Contrib. en Prob. y Est. Mat. Ens. de la
Mat. y Analisis, Univ. de Granada (1979) 91-108.
[34] P.A. Samuelson, Rational theory of warrant pricing, Ind. Management Rev. 6 (1965) 13-39.
[35] P.A. Samuelson, Mathematics of speculative price, SIAM Rev. xx (1973) l-42.
[36] W. Sharpe, Investments (Prentice-Hall, Englewood Cliffs, NJ, 1978).
[37] C.W. Smith, Jr., Option pricing: A review, J. Fin. Econom. 3 (1976) 3-51.
[38] D. Williams, Diffusions, Markov Processes and Martingales Vol. 1 (Wiley, New York, 1979).
[39] M. Yor, Sous-espaces denses dans L’ ou H’ et representation des martingales, in: Seminaire de
Probabilite XII, Lecture Notes in Mathematics 649 (Springer, New York, 1978) 265-309.

## Tables

No tables extracted.

## Figures

No figures extracted.

## Extraction Notes

- discarded 1 tiny-placement embedded figure(s)
- discarded 2111 dense-page embedded figure candidate(s)
