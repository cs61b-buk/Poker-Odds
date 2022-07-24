# Drop your proofs and solutions here:
https://www.wyzant.com/resources/answers?filter=unanswered&sort=newest
# Statistics questions for Ashley on Tuesdays or Saturdays:
(1) Consider the following statement:
    If n = 100 random samples of water from the lake were taken and the 95% CI 
    on µ computed, and this process were repeated 1000 times, 950 of the CIs would
    contain the true value of µ. Is this statement correct? Explain your answer.
(2) An article in the Journal of Agricultural Science ["The Use of Residual Maximum 
    Likelihood to Model Grain Quality Characteristics of Wheat with Variety,
    Climatic and Nitrogen Fertilizer Effects" (1997, Vol. 128, pp. 135-142)]
    investigated means of wheat grain crude protein content (CP) and Hagberg
    falling number (HFN) surveyed in the UK. The analysis used a variety of
    nitrogen fertilizer applications (kg N/ha), temperature (°C), and total monthly
    rainfall (mm). The data shown below describe temperatures for wheat grown at
    Harper Adams Agricultural College between 1982 and 1993. The temperatures
    measured in June were obtained as follows:
        15.2, 14.2, 14.0, 12.2, 14.4, 12.5, 14.3, 14.2, 13.5, 11.8, 15.2
    Assume that the standard deviation is known to be σ = 0.5.
    (a) Construct a 99% two-sided confidence interval on the mean temperature.
    (b) Construct a 95% lower-confidence bound on the mean temperature.
    (c) Suppose that we wanted to be 95% confident that the error in 
        estimating the mean temperature is less than 2 degrees Celsius.
        What sample size should be used?
    (d) Suppose that we wanted the total width of the two-sided confidence interval 
        on mean temperature to be 1.5 degrees Celsius at 95% confidence. 
        What sample size should be used?
(3) Let X1, X2, X3, ... Xn denote independent and identically distributed random 
    variables from a Pareto distribution with parameters α and ẞ, where ẞ is known. 
    Then if α > 0, fx(x;α,ẞ) = α * ẞ^α * x^-(α+1) if x ≥ ẞ else 0 otherwise. 
    (a) Show that E[X] = αβ / (α-1) if α > 1 and E[X] is undefined if 0 < α < 1.
    (b) Derive the method of moment estimator for α where E[X] is defined.
# Determine all quadratic residues mod 13, 16, and 17:
     x           | 1 | 2 | 3 | 4 |  5 |  6
-------------------------------------------
a == x² (mod 13) | 1 | 4 | 9 | 3 | 12 | 10
So, all quadratic residues mod 13 are 1, 3, 4, 9, 10, and 12.
     x           | 1 | 3 | 5 | 7 | 9 | 11 | 13 | 15
----------------------------------------------------
a == x² (mod 16) | 1 | 9 | 9 | 1 | 1 |  9 |  9 |  1
So, all quadratic residues mod 16 are 1 and 9.
     x           | 1 | 2 | 3 |  4 |  5 |  6 |  7 |  8 
-------------------------------------------------------
a == x² (mod 17) | 1 | 4 | 9 | 16 |  8 |  2 | 15 | 13 
So, all quadratic residues mod 17 are 1, 2, 4, 8, 9, 13, 15, and 16.
# Evaluate the following:
(24 / 19) == (4 / 19) * (6 / 19) == 1 * 6^(19-1)/2 == 6^(18/2)
          == 6^9 == (6^2)^4 * 6^1 == 36^4 * 6 == (-2)^4 * 6 
          == 16 * 6 == -3 * 6 == -18 == 1 (mod 19)
(18 / 11) == (9 / 11) * (2 / 11) == 1 * 2^(11-1)/2 == 2^(10/2)
          == 2^5 == 32 == -1 (mod 11)
# Find, and then prove, each limit, using the epsilon-delta (ε-ẟ) definition:
These problems are from the video on blackpenredpen's YouTube channel 
linked here: youtube.com/watch?v=luiJmucU7lI and these answers are based on 
blackpenredpen's technique from his YouTube channel, a video of an example 
[ of which is linked here: youtube.com/watch?v=DdtEQk_DHQs.
 1. lim as x ->  1 of 6x - 2 = 6*(1) - 2 = 6 - 2 = 4, because
    if we let f(x) = 6x - 2, L = 4, and a = 1, then we have the following:
    Given ε > 0, choose ẟ = ε/6. Suppose 0 < |x - a| = |x - 1| < ẟ, 
    and check: |f(x) - L| = |(6x - 2) - 4| = |6x - 6| = |6 * (x - 1)|,
    so we now have |f(x) - L| = |6| * |x - 1| < 6 * ẟ = 6 * (ε/6) = ε. [[QED]
 2. lim as x -> -2 of (2x + 7) = 2*(-2) + 7 = -4 + 7 = 3, because
    if we let f(x) = 2x + 7, L = 3, and a = -2, then we have the following:
    Given ε > 0, choose ẟ = ε/2. Suppose 0 < |x - a| = |x - (-2)| = |x + 2| < ẟ,
    and check: |f(x) - L| = |(2x + 7) - 3| = |2x + 4| = |2 * (x + 2)|,
    so we now have |f(x) - L| = |2| * |x + 2| < 2 * ẟ = 2 * (ε/2) = ε. [QED]
 3. lim as x ->  3 of (2x/3 - 5) = 2*(3)/3 - 5 = 2 - 5 = -3, because
    if we let f(x) = 2x/3 - 5, L = -3, and a = 3, then we have the following:
    Given ε > 0, choose ẟ = 3ε/2. Suppose 0 < |x - a| = |x - 3| < ẟ,
    and check: |f(x) - L| = |(2x/3 - 5) - (-3)| = |2x/3 - 2| = |2/3 * (x - 3)|,
    so we now have |f(x) - L| = |2/3| * |x - 3| < 2/3 * ẟ = 2/3 * (3ε/2) = ε. [QED]
 4. lim as x ->  4 of √(x) = √(4) = 2, because
    if we let f(x) = √(x), L = 2, and a = 4, then we have the following:
    Given ε > 0, choose ẟ = ε. Suppose 0 < |x - a| = |x - 4| < ẟ, and
    check: |f(x) - L| = |√(x) - 2| = |√(x) - 2| * |√(x) + 2| / |√(x) + 2|,
    so we now have |f(x) - L| = |x - 4| / |√(x) + 2| < |x - 4| < ẟ = ε, 
    because |√(x) + 2| > 1 for all x >= 0. [QED]
 5. lim as x ->  6 of √(3x - 2) = √(3*(6) - 2) = √(18 - 2) = √(16) = 4, because
    if we let f(x) = √(3x - 2), L = 4, and a = 6, then we have the following:
    Given ε > 0, choose ẟ = ε/3. Suppose 0 < |x - a| = |x - 6| < ẟ, and
    check: |f(x) - L| = |√(3x - 2) - 4| = |√(3x - 2) - 4| * |√(3x - 2) + 4| / A,
    where A = |√(3x - 2) + 4|, which is > 1 for all 3x - 2 > 0, so we now have 
    |f(x) - L| = |3x - 2 - 16| / A < |3x - 18| = 3|x - 6| < 3ẟ = 3*(ε/3) = ε. [QED]
 6. lim as x ->  3 of (2x² + 1) = 2*(3)² + 1 = 2*9 + 1 = 18 + 1 = 19, because
    if we let f(x) = 2x² + 1, L = 19, and a = 3, then we have the following:
    Given ε > 0, choose ẟ = min(1, ε/14). Suppose 0 < |x - a| = |x - 3| < ẟ,
    and check: |f(x) - L| = |(2x² + 1) - 19| = |2x² - 18| = 2 * |x + 3| * |x - 3|,
    so if we let ẟ be <= 1, then |x - 3| < ẟ means that |x - 3| < 1, so we have:
    -1 < x - 3 < 1, so 5 < x + 3 < 7, so |x + 3| < 7, so we now have:
    |f(x) - L| = 2 * |x + 3| * |x - 3| < 2*7*ẟ = 14 * ẟ <= 14 * (ε/14) = ε. [QED]  
 7. lim as x -> -2 of (x² - 3x) = (-2)² - 3*(-2) = 4 - (-6) = 4 + 6 = 10, because
    if we let f(x) = x² - 3x, L = 10, and a = -2, then we have the following:
    Given ε > 0, choose ẟ = min(1, ε/8).
    Suppose 0 < |x - a| = |x - (-2)| = |x + 2| < ẟ, and check: 
    |f(x) - L| = |(x² - 3x) - 10| = |x - 5| * |x + 2|, so if we let ẟ be <= 1, 
    then |x + 2| < ẟ means that |x + 2| < 1, so we have:
    -1 < x + 2 < 1, so -8 < x - 5 < -6, so |x - 5| < 8, so we now have: 
    |f(x) - L| = |x - 5| * |x + 2| < 8 * ẟ <= 8 * (ε/8) = ε. [QED]
 8. lim as x ->  2 of (x³) = (2)³ = 8, because
    if we let f(x) = x³, L = 8, and a = 2, then we have the following:
    Given ε > 0, choose ẟ = min(1, ε/19). Suppose 0 < |x - a| = |x - 2| < ẟ, 
    and check: |f(x) - L| = |x³ - 8| = |x² + 2x + 4| * |x - 2| <=
        (|x²| + |2x + 4|) * |x - 2| = (|x²| + 2 * |x + 2|) * |x - 2|, 
    so if we let ẟ be <= 1, then |x - 2| < ẟ means that |x - 2| < 1, so we have:
    -1 < x - 2 < 1, so 1 < x < 3 and 3 < x + 2 < 5, so |x²| < 3² = 9 and 
    |x + 2| < 5, so we now have: |f(x) - L| = (|x²| + 2 * |x + 2|) * |x - 2| <
        (9 + 2 * 5) * ẟ = (9 + 10) * ẟ = 19 * ẟ <= 19 * (ε/19) = ε. [QED]
 9. lim as x ->  2 of (1 / x) = 1/2, because:
    if we let f(x) = 1/x, L = 1/2, and a = 2, then we have the following:
    Given ε > 0, choose ẟ = min(1, ε). Suppose 0 < |x - a| = |x - 2| < ẟ, & check:
    |f(x) - L| = |1/x - 1/2| = |2/(2x) - x/(2x)| = |2 - x| / |2x| = |x - 2| / |2x|,
    so if we let ẟ be <= 1, then |x - 2| < ẟ means that |x - 2| < 1, so we have:
    -1 < x - 2 < 1, so 1 < x < 3, so 2 < 2x < 6, so |2x| > 1, so we now have:
    |f(x) - L| = |x - 2| / |2x| < |x - 2| < ẟ = ε. [QED]
10. lim as x ->  1 of 1 / (2x + 1) = 1 / (2*(1) + 1) = 1 / (2 + 1) = 1/3, because
    if we let f(x) = 1 / (2x + 1), L = 1/3, and a = 1, then we have the following:
    Given ε > 0, choose ẟ = min(1, 3ε/2). Suppose 0 < |x - a| = |x - 1| < ẟ, and
    check: |f(x) - L| = |1/(2x+1) - 1/3| = |3/[3*(2x+1)] - (2x+1)/[3*(2x+1)]| 
        = |3 - (2x+1)| / [3*|2x+1|] = |2 - 2x| / [3 * |2x + 1|]
        = 2 * |1 - x| / [3 * (2x + 1)] = 2 * |x - 1| / [3 * |2x + 1|],
    so if we let ẟ be <= 1, then |x - 1| < ẟ means that |x - 1| < 1, so we have:
    -1 < x - 1 < 1, so 0 < x < 2, so 0 < 2x < 4, so 1 < 2x + 1 < 5,
    so |2x + 1| > 1, so we now have:
    |f(x) - L| = 2 * |x - 1| / [3 * |2x + 1|] < 2 * ẟ/3 <= 2 * (3ε/2)/3 = ε. [QED]
### Order Modulo n Warmups:
# Find ord_10(7) and ord_25(9):
ord_10(7) = N <===> 7^N = 1 (mod 10), so we list the powers of 7^n (mod 10):
n = 1 ==> 7^n = 7^1 = 7 (mod 10)
n = 2 ==> 7^n = 7^2 = 49 (mod 10) = 9 (mod 10)
n = 3 ==> 7^n = 7^3 = 343 (mod 10) = 3 (mod 10)
n = 4 ==> 7^n = 7^4 = 343*7 (mod 10) = 3*7 (mod 10) = 21 (mod 10) = 1 (mod 10)
Therefore, N = ord_10(7) = 4.
ord_25(9) = N <===> 9^N = 1 (mod 25), so we list the powers of 9^n (mod 25):
n = 1 ==> 9^n = 9^1 = 9 (mod 25)
n = 2 ==> 9^n = 9^2 = 81 (mod 25) = 6 (mod 25)
n = 3 ==> 9^n = 9^3 = 6*9 (mod 25) = 54 (mod 25) = 4 (mod 25)
n = 4 ==> 9^n = 9^4 = 4*9 (mod 25) = 36 (mod 25) = 11 (mod 25)
n = 5 ==> 9^n = 9^5 = 11*9 (mod 25) = 99 (mod 25) = -1 (mod 25)
n = 10 ==> 9^n = 9^10 = (9^5)^2 (mod 25) = (-1)^2 (mod 25) = 1 (mod 25)
Therefore, N = ord_25(9) = 10.
# Find all primitive roots mod 11, 13, and 17:
2 is a primitive root mod 11 <===> ord_11(2) = phi(11) = 10 <===> 2^10 = 1 (mod 11),
so we list the powers of 2^n (mod 11):
n = 1 ==> 2^n = 2^1 = 2 (mod 11)
n = 2 ==> 2^n = 2^2 = 4 (mod 11)
n = 3 ==> 2^n = 2^3 = 8 (mod 11)
n = 4 ==> 2^n = 2^4 = 16 = 5 (mod 11)
n = 5 ==> 2^n = 2^5 = 32 = -1 (mod 11)
n = 10 ==> 2^n = 2^10 = (2^5)^2 = (-1)^2 = 1 (mod 11)
Therefore, N = ord_11(2) = 10, so 2 is a primitive root mod 11.
3 is a primitive root mod 11 <===> ord_11(3) = phi(11) = 10 <===> 3^10 = 1 (mod 11),
so we list the powers of 3^n (mod 11):
n = 1 ==> 3^n = 3^1 = 3 (mod 11)
n = 2 ==> 3^n = 3^2 = 9 (mod 11)
n = 3 ==> 3^n = 3^3 = 27 = 5 (mod 11)
n = 4 ==> 3^n = 3^4 = 5*3 = 15 = 4 (mod 11)
n = 5 ==> 3^n = 3^5 = 4*3 = 12 = 1 (mod 11)
Therefore, N = ord_11(3) = 5, so 3 is NOT a primitive root mod 11.
4 is a primitive root mod 11 <===> ord_11(4) = phi(11) = 10 <===> 4^10 = 1 (mod 11),
so we list the powers of 4^n (mod 11):
n = 1 ==> 4^n = 4^1 = 4 (mod 11)
n = 2 ==> 4^n = 4^2 = 16 = 5 (mod 11)
n = 3 ==> 4^n = 4^3 = 64 = 9 (mod 11)
n = 4 ==> 4^n = 4^4 = 9*4 = 36 = 3 (mod 11)
n = 5 ==> 4^n = 4^5 = 3*4 = 12 = 1 (mod 11)
Therefore, N = ord_11(4) = 5, so 4 is NOT a primitive root mod 11.
5 is a primitive root mod 11 <===> ord_11(5) = phi(11) = 10 <===> 5^10 = 1 (mod 11),
so we list the powers of 5^n (mod 11):
n = 1 ==> 5^n = 5^1 = 5 (mod 11)
n = 2 ==> 5^n = 5^2 = 25 = 3 (mod 11)
n = 3 ==> 5^n = 5^3 = 3*5 = 15 = 4 (mod 11)
n = 4 ==> 5^n = 5^4 = 4*5 = 20 = 9 (mod 11)
n = 5 ==> 5^n = 5^5 = 9*5 = 45 = 1 (mod 11)
Therefore, N = ord_11(5) = 5, so 5 is NOT a primitive root mod 11.
6 is a primitive root mod 11 <===> ord_11(6) = phi(11) = 10 <===> 6^10 = 1 (mod 11),
so we list the powers of 6^n (mod 11):
n = 1 ==> 6^n = 6^1 = 6 (mod 11)
n = 2 ==> 6^n = 6^2 = 36 = 3 (mod 11)
n = 3 ==> 6^n = 6^3 = 3*6 = 18 = 7 (mod 11)
n = 4 ==> 6^n = 6^4 = 7*6 = 42 = 9 (mod 11)
n = 5 ==> 6^n = 6^5 = 9*6 = 54 = -1 (mod 11)
n = 10 ==> 6^n = 6^10 = (6^5)^2 = (-1)^2 = 1 (mod 11)
Therefore, N = ord_11(6) = 10, so 6 is a primitive root mod 11.
7 is a primitive root mod 11 <===> ord_11(7) = phi(11) = 10 <===> 7^10 = 1 (mod 11),
so we list the powers of 7^n (mod 11):
n = 1 ==> 7^n = 7^1 = 7 (mod 11)
n = 2 ==> 7^n = 7^2 = 49 = 5 (mod 11)
n = 3 ==> 7^n = 7^3 = 5*7 = 35 = 2 (mod 11)
n = 4 ==> 7^n = 7^4 = 2*7 = 14 = 3 (mod 11)
n = 5 ==> 7^n = 7^5 = 3*7 = 21 = -1 (mod 11)
n = 10 ==> 7^n = 7^10 = (7^5)^2 = (-1)^2 = 1 (mod 11)
Therefore, N = ord_11(7) = 10, so 7 is a primitive root mod 11.
8 is a primitive root mod 11 <===> ord_11(8) = phi(11) = 10 <===> 8^10 = 1 (mod 11),
so we list the powers of 8^n (mod 11):
n = 1 ==> 8^n = 8^1 = 8 (mod 11)
n = 2 ==> 8^n = 8^2 = 64 = 9 (mod 11)
n = 3 ==> 8^n = 8^3 = 9*8 = 72 = 6 (mod 11)
n = 4 ==> 8^n = 8^4 = 6*8 = 48 = 4 (mod 11)
n = 5 ==> 8^n = 8^5 = 4*8 = 32 = -1 (mod 11)
n = 10 ==> 8^n = 8^10 = (8^5)^2 = (-1)^2 = 1 (mod 11)
Therefore, N = ord_11(8) = 10, so 8 is a primitive root mod 11.
9 is a primitive root mod 11 <===> ord_11(9) = phi(11) = 10 <===> 9^10 = 1 (mod 11),
so we list the powers of 9^n (mod 11):
n = 1 ==> 9^n = 9^1 = 9 (mod 11)
n = 2 ==> 9^n = 9^2 = 81 = 4 (mod 11)
n = 3 ==> 9^n = 9^3 = 4*9 = 36 = 3 (mod 11)
n = 4 ==> 9^n = 9^4 = 3*9 = 27 = 5 (mod 11)
n = 5 ==> 9^n = 9^5 = 5*9 = 45 = 1 (mod 11)
Therefore, N = ord_11(9) = 5, so 9 is NOT a primitive root mod 11.
10 is a primitive root mod 11 <===> ord_11(10) = phi(11) = 10 <===> 10^10 = 1 (mod 11),
so we list the powers of 10^n (mod 11):
n = 1 ==> 10^n = 10^1 = 10 (mod 11)
n = 2 ==> 10^n = 10^2 = 100 = 1 (mod 11)
Therefore, N = ord_11(10) = 2, so 10 is NOT a primitive root mod 11.
So, all of the primitive roots mod 11 are in the following set: {2, 6, 7, 8}.
2 is a primitive root mod 13 <===> ord_13(2) = phi(13) = 12 <===> 2^12 = 1 (mod 13),
so we list the powers of 2^n (mod 13):
n = 1 ==> 2^n = 2^1 = 2 (mod 13)
n = 2 ==> 2^n = 2^2 = 4 (mod 13)
n = 3 ==> 2^n = 2^3 = 8 (mod 13)
n = 4 ==> 2^n = 2^4 = 16 = 3 (mod 13)
n = 5 ==> 2^n = 2^5 = 3*2 = 6 (mod 13)
n = 6 ==> 2^n = 2^6 = 6*2 = 12 = -1 (mod 13)
n = 12 ==> 2^n = 2^12 = (2^6)^2 = (-1)^2 = 1 (mod 13)
Therefore, N = ord_13(2) = 12, so 2 is a primitive root mod 13.
3 is a primitive root mod 13 <===> ord_13(3) = phi(13) = 12 <===> 3^12 = 1 (mod 13),
so we list the powers of 3^n (mod 13):
n = 1 ==> 3^n = 3^1 = 3 (mod 13)
n = 2 ==> 3^n = 3^2 = 9 (mod 13)
n = 3 ==> 3^n = 3^3 = 27 = 1 (mod 13)
Therefore, N = ord_13(3) = 3, so 3 is NOT a primitive root mod 13.
4 is a primitive root mod 13 <===> ord_13(4) = phi(13) = 12 <===> 4^12 = 1 (mod 13),
so we list the powers of 4^n (mod 13):
n = 1 ==> 4^n = 4^1 = 4 (mod 13)
n = 2 ==> 4^n = 4^2 = 16 = 3 (mod 13)
n = 3 ==> 4^n = 4^3 = 64 = -1 (mod 13)
n = 6 ==> 4^n = 4^6 = (4^3)^2 = (-1)^2 = 1 (mod 13)
Therefore, N = ord_13(4) = 6, so 4 is NOT a primitive root mod 13.
5 is a primitive root mod 13 <===> ord_13(5) = phi(13) = 12 <===> 5^12 = 1 (mod 13),
so we list the powers of 5^n (mod 13):
n = 1 ==> 5^n = 5^1 = 5 (mod 13)
n = 2 ==> 5^n = 5^2 = 25 = -1 (mod 13)
n = 4 ==> 5^n = 5^4 = (-1)^2 = 1 (mod 13)
Therefore, N = ord_13(5) = 4, so 5 is NOT a primitive root mod 13.
6 is a primitive root mod 13 <===> ord_13(6) = phi(13) = 12 <===> 6^12 = 1 (mod 13),
so we list the powers of 6^n (mod 13):
n = 1 ==> 6^n = 6^1 = 6 (mod 13)
n = 2 ==> 6^n = 6^2 = 36 = 10 (mod 13)
n = 3 ==> 6^n = 6^3 = 10*6 = 60 = 8 (mod 13)
n = 4 ==> 6^n = 6^4 = 8*6 = 48 = 9 (mod 13)
n = 5 ==> 6^n = 6^5 = 9*6 = 54 = 2 (mod 13)
n = 6 ==> 6^n = 6^6 = 2*6 = 12 = -1 (mod 13)
n = 12 ==> 6^n = 6^12 = (6^6)^2 = (-1)^2 = 1 (mod 13)
Therefore, N = ord_13(6) = 12, so 6 is a primitive root mod 13.
7 is a primitive root mod 13 <===> ord_13(7) = phi(13) = 12 <===> 7^12 = 1 (mod 13),
so we list the powers of 7^n (mod 13):
n = 1 ==> 7^n = 7^1 = 7 (mod 13)
n = 2 ==> 7^n = 7^2 = 49 = 10 (mod 13)
n = 3 ==> 7^n = 7^3 = 10*7 = 70 = 5 (mod 13)
n = 4 ==> 7^n = 7^4 = 5*7 = 35 = 9 (mod 13)
n = 5 ==> 7^n = 7^5 = 9*7 = 63 = 11 (mod 13)
n = 6 ==> 7^n = 7^6 = 11*7 = 77 = -1 (mod 13)
n = 12 ==> 7^n = 7^12 = (7^6)^2 = (-1)^2 = 1 (mod 13)
Therefore, N = ord_13(7) = 10, so 7 is a primitive root mod 13.
8 is a primitive root mod 13 <===> ord_13(8) = phi(13) = 12 <===> 8^12 = 1 (mod 13),
so we list the powers of 8^n (mod 13):
n = 1 ==> 8^n = 8^1 = 8 (mod 13)
n = 2 ==> 8^n = 8^2 = 64 = -1 (mod 13)
n = 4 ==> 8^n = 8^4 = (8^2)^2 = (-1)^2 = 1 (mod 13)
Therefore, N = ord_13(8) = 4, so 8 is NOT a primitive root mod 13.
9 is a primitive root mod 13 <===> ord_13(9) = phi(13) = 12 <===> 9^12 = 1 (mod 13),
so we list the powers of 9^n (mod 13):
n = 1 ==> 9^n = 9^1 = 9 (mod 13)
n = 2 ==> 9^n = 9^2 = 81 = 3 (mod 13)
n = 3 ==> 9^n = 9^3 = 3*9 = 27 = 1 (mod 13)
Therefore, N = ord_13(9) = 3, so 9 is NOT a primitive root mod 13.
10 is a primitive root mod 13 <===> ord_13(10) = phi(13) = 12 <===> 10^12 = 1 (mod 13),
so we list the powers of 10^n (mod 13):
n = 1 ==> 10^n = 10^1 = 10 (mod 13)
n = 2 ==> 10^n = 10^2 = 100 = 9 (mod 13)
n = 3 ==> 10^n = 10^3 = 9*10 = 90 = -1 (mod 13)
n = 6 ==> 10^n = 10^6 = (10^3)^2 = (-1)^2 = 1 (mod 13)
Therefore, N = ord_13(10) = 6, so 10 is NOT a primitive root mod 13.
11 is a primitive root mod 13 <===> ord_13(11) = phi(13) = 12 <===> 11^12 = 1 (mod 13),
so we list the powers of 11^n (mod 13):
n = 1 ==> 11^n = 11^1 = 11 (mod 13)
n = 2 ==> 11^n = 11^2 = 121 = 4 (mod 13)
n = 3 ==> 11^n = 11^3 = 4*11 = 44 = 5 (mod 13)
n = 4 ==> 11^n = 11^4 = 5*11 = 55 = 3 (mod 13)
n = 5 ==> 11^n = 11^5 = 3*11 = 33 = 7 (mod 13)
n = 6 ==> 11^n = 11^6 = 7*11 = 77 = -1 (mod 13)
n = 12 ==> 11^n = 11^12 = (11^6)^2 = (-1)^2 = 1 (mod 13)
Therefore, N = ord_13(11) = 12, so 11 is a primitive root mod 13.
12 is a primitive root mod 13 <===> ord_13(12) = phi(13) = 12 <===> 12^12 = 1 (mod 13),
so we list the powers of 12^n (mod 13):
n = 1 ==> 12^n = 12^1 = 12 (mod 13)
n = 2 ==> 12^n = 12^2 = 144 = 14 = 1 (mod 13)
Therefore, N = ord_13(12) = 2, so 12 is NOT a primitive root mod 13.
So, all of the primitive roots mod 13 are in the following set: {2, 6, 7, 11}.
2 is a primitive root mod 17 <===> ord_17(2) = phi(17) = 16 <===> 2^16 = 1 (mod 17),
so we list the powers of 2^n (mod 17):
n = 1 ==> 2^n = 2^1 = 2 (mod 17)
n = 2 ==> 2^n = 2^2 = 4 (mod 17)
n = 4 ==> 2^n = 2^4 = 16 = -1 (mod 17)
n = 8 ==> 2^n = 2^8 = (2^4)^2 = (-1)^2 = 1 (mod 17)
Therefore, N = ord_17(2) = 4, so 2 is NOT a primitive root mod 17.
3 is a primitive root mod 17 <===> ord_17(3) = phi(17) = 16 <===> 3^16 = 1 (mod 17),
so we list the powers of 3^n (mod 17):
n = 1 ==> 3^n = 3^1 = 3 (mod 17)
n = 2 ==> 3^n = 3^2 = 9 (mod 17)
n = 3 ==> 3^n = 3^3 = 27 = 10 (mod 17)
n = 4 ==> 3^n = 3^4 = 10*3 = 30 = 13 (mod 17)
n = 8 ==> 3^n = 3^8 = (3^4)^2 = 13^2 = 169 = -1 (mod 17)
n = 16 ==> 3^n = 3^16 = (3^8)^2 = (-1)^2 = 1 (mod 17)
Therefore, N = ord_17(3) = 16, so 3 is a primitive root mod 17.
4 is a primitive root mod 17 <===> ord_17(4) = phi(17) = 16 <===> 4^16 = 1 (mod 17),
so we list the powers of 4^n (mod 17):
n = 1 ==> 4^n = 4^1 = 4 (mod 17)
n = 2 ==> 4^n = 4^2 = 16 = -1 (mod 17)
n = 4 ==> 4^n = 4^4 = (4^2)^2 = (-1)^2 = 1 (mod 17)
Therefore, N = ord_17(4) = 4, so 4 is NOT a primitive root mod 17.
5 is a primitive root mod 17 <===> ord_17(5) = phi(17) = 16 <===> 5^16 = 1 (mod 17),
so we list the powers of 5^n (mod 17):
n = 1 ==> 5^n = 5^1 = 5 (mod 17)
n = 2 ==> 5^n = 5^2 = 25 = 8 (mod 17)
n = 4 ==> 5^n = 5^4 = (5^2)^2 = 8^2 = 64 = 13 (mod 17)
n = 8 ==> 5^n = 5^8 = (5^4)^2 = 13^2 = 169 = -1 (mod 17)
n = 16 ==> 5^n = 5^16 = (5^8)^2 = (-1)^2 = 1 (mod 17)
Therefore, N = ord_17(5) = 16, so 5 is a primitive root mod 17.
6 is a primitive root mod 17 <===> ord_17(6) = phi(17) = 16 <===> 6^16 = 1 (mod 17),
so we list the powers of 6^n (mod 17):
n = 1 ==> 6^n = 6^1 = 6 (mod 17)
n = 2 ==> 6^n = 6^2 = 36 = 2 (mod 17)
n = 3 ==> 6^n = 6^3 = 2*6 = 12 = -5 (mod 17)
n = 4 ==> 6^n = 6^4 = -5*6 = -30 = 4 (mod 17)
n = 8 ==> 6^n = 6^8 = (6^4)^2 = 4^2 = 16 = -1 (mod 17)
n = 16 ==> 6^n = 6^16 = (6^8)^2 = (-1)^2 = 1 (mod 17)
Therefore, N = ord_17(6) = 16, so 6 is a primitive root mod 17.
7 is a primitive root mod 17 <===> ord_17(7) = phi(17) = 16 <===> 7^16 = 1 (mod 17),
so we list the powers of 7^n (mod 17):
n = 1 ==> 7^n = 7^1 = 7 (mod 17)
n = 2 ==> 7^n = 7^2 = 49 = -2 (mod 17)
n = 3 ==> 7^n = 7^3 = -2*7 = -14 = 3 (mod 17)
n = 4 ==> 7^n = 7^4 = 3*7 = 21 = 4 (mod 17)
n = 8 ==> 7^n = 7^8 = (7^4)^2 = 4^2 = 16 = -1 (mod 17)
n = 16 ==> 7^n = 7^16 = (7^8)^2 = (-1)^2 = 1 (mod 17)
Therefore, N = ord_17(7) = 16, so 7 is a primitive root mod 17.
8 is a primitive root mod 17 <===> ord_17(8) = phi(17) = 16 <===> 8^16 = 1 (mod 17),
so we list the powers of 8^n (mod 17):
n = 1 ==> 8^n = 8^1 = 8 (mod 17)
n = 2 ==> 8^n = 8^2 = 64 = -4 (mod 17)
n = 4 ==> 8^n = 8^4 = (8^2)^2 = (-4)^2 = 16 = -1 (mod 17)
n = 8 ==> 8^n = 8^8 = (8^4)^2 = (-1)^2 = 1 (mod 17)
Therefore, N = ord_17(8) = 8, so 8 is NOT a primitive root mod 17.
9 is a primitive root mod 17 <===> ord_17(9) = phi(17) = 16 <===> 9^16 = 1 (mod 17),
so we list the powers of 9^n (mod 17):
n = 1 ==> 9^n = 9^1 = 9 (mod 17)
n = 2 ==> 9^n = 9^2 = 81 = -4 (mod 17)
n = 4 ==> 9^n = 9^4 = (9^2)^2 = (-4)^2 = 16 = -1 (mod 17)
n = 8 ==> 9^n = 9^8 = (9^4)^2 = (-1)^2 = 1 (mod 17)
Therefore, N = ord_17(9) = 8, so 9 is NOT a primitive root mod 17.
10 is a primitive root mod 17 <===> ord_17(10) = phi(17) = 16 <===> 10^16 = 1 (mod 17),
so we list the powers of 10^n (mod 17):
n = 1 ==> 10^n = 10^1 = 10 (mod 17)
n = 2 ==> 10^n = 10^2 = 100 = 15 = -2 (mod 17)
n = 4 ==> 10^n = 10^4 = (10^2)^2 = (-2)^2 = 4 (mod 17)
n = 8 ==> 10^n = 10^8 = (10^4)^2 = 4^2 = 16 = -1 (mod 17)
n = 16 ==> 10^n = 10^16 = (10^8)^2 = (-1)^2 = 1 (mod 17)
Therefore, N = ord_17(10) = 16, so 10 is a primitive root mod 17.
11 is a primitive root mod 17 <===> ord_17(11) = phi(17) = 16 <===> 11^16 = 1 (mod 17),
so we list the powers of 11^n (mod 17):
n = 1 ==> 11^n = 11^1 = 11 = -6 (mod 17)
n = 2 ==> 11^n = 11^2 = -6*11 = -66 = 2 (mod 17)
n = 3 ==> 11^n = 11^3 = 2*11 = 22 = 5 (mod 17)
n = 4 ==> 11^n = 11^4 = 5*11 = 55 = 4 (mod 17)
n = 8 ==> 11^n = 11^8 = (11^4)^2 = 4^2 = 16 = -1 (mod 17)
n = 16 ==> 11^n = 11^16 = (11^8)^2 = (-1)^2 = 1 (mod 17)
Therefore, N = ord_17(11) = 16, so 11 is a primitive root mod 17.
12 is a primitive root mod 17 <===> ord_17(12) = phi(17) = 16 <===> 12^16 = 1 (mod 17),
so we list the powers of 12^n (mod 17):
n = 1 ==> 12^n = 12^1 = 12 = -5 (mod 17)
n = 2 ==> 12^n = 12^2 = -5*12 = -60 = 8 (mod 17)
n = 3 ==> 12^n = 12^3 = 8*12 = 96 = 11 = -6 (mod 17)
n = 4 ==> 12^n = 12^4 = -6*12 = -72 = -4 (mod 17)
n = 8 ==> 12^n = 12^8 = (12^4)^2 = (-4)^2 = 16 = -1 (mod 17)
n = 16 ==> 12^n = 12^16 = (12^8)^2 = (-1)^2 = 1 (mod 17)
Therefore, N = ord_17(12) = 16, so 12 is a primitive root mod 17.
13 is a primitive root mod 17 <===> ord_17(13) = phi(17) = 16 <===> 13^16 = 1 (mod 17),
so we list the powers of 13^n (mod 17):
n = 1 ==> 13^n = 13^1 = 13 = -4 (mod 17)
n = 2 ==> 13^n = 13^2 = (13^1)^2 = (-4)^2 = 16 = -1 (mod 17)
n = 4 ==> 13^n = 13^4 = (13^2)^2 = (-1)^2 = 1 (mod 17)
Therefore, N = ord_17(13) = 4, so 13 is NOT a primitive root mod 17.
14 is a primitive root mod 17 <===> ord_17(14) = phi(17) = 16 <===> 14^16 = 1 (mod 17),
so we list the powers of 14^n (mod 17):
n = 1 ==> 14^n = 14^1 = 14 = -3 (mod 17)
n = 2 ==> 14^n = 14^2 = (14^1)^2 = (-3)^2 = 9 (mod 17)
n = 4 ==> 14^n = 14^4 = (14^2)^2 = 9^2 = 81 = -4 (mod 17)
n = 8 ==> 14^n = 14^8 = (14^4)^2 = (-4)^2 = 16 = -1 (mod 17)
n = 16 ==> 14^n = 14^16 = (14^8)^2 = (-1)^2 = 1 (mod 17)
Therefore, N = ord_17(14) = 16, so 14 is a primitive root mod 17.
15 is a primitive root mod 17 <===> ord_17(15) = phi(17) = 16 <===> 15^16 = 1 (mod 17),
so we list the powers of 15^n (mod 17):
n = 1 ==> 15^n = 15^1 = 15 = -2 (mod 17)
n = 2 ==> 15^n = 15^2 = (15^1)^2 = (-2)^2 = 4 (mod 17)
n = 4 ==> 15^n = 15^4 = (15^2)^2 = 4^2 = 16 = -1 (mod 17)
n = 8 ==> 15^n = 15^8 = (15^4)^2 = (-1)^2 = 1 (mod 17)
Therefore, N = ord_17(15) = 8, so 15 is NOT a primitive root mod 17.
16 is a primitive root mod 17 <===> ord_17(16) = phi(17) = 16 <===> 16^16 = 1 (mod 17),
so we list the powers of 16^n (mod 17):
n = 1 ==> 16^n = 16^1 = 16 = -1 (mod 17)
n = 2 ==> 16^n = 16^2 = (16^1)^2 = (-1)^2 = 1 (mod 17)
Therefore, N = ord_17(13) = 2, so 16 is NOT a primitive root mod 17.
So, all of the primitive roots mod 17 are in the following set: {3,5,6,7,10,11,12,14}.
# Show that there are no primitive roots mod 8 nor 15:
3 is a primitive root mod 8 <===> ord_8(3) = phi(8) = 4 <===> 3^4 = 1 (mod 8),
so we list the powers of 3^n (mod 8):
n = 1 ==> 3^n = 3^1 = 3 (mod 8)
n = 2 ==> 3^n = 3^2 = 9 = 1 (mod 8)
Therefore, N = ord_8(3) = 2, so 3 is NOT a primitive root mod 8.
5 is a primitive root mod 8 <===> ord_8(5) = phi(8) = 4 <===> 5^4 = 1 (mod 8),
so we list the powers of 5^n (mod 8):
n = 1 ==> 5^n = 5^1 = 5 (mod 8)
n = 2 ==> 5^n = 5^2 = 25 = 1 (mod 8)
Therefore, N = ord_8(5) = 2, so 5 is NOT a primitive root mod 8.
7 is a primitive root mod 8 <===> ord_8(7) = phi(8) = 4 <===> 7^4 = 1 (mod 8),
so we list the powers of 7^n (mod 8):
n = 1 ==> 7^n = 7^1 = 7 (mod 8)
n = 2 ==> 7^n = 7^2 = 49 = 1 (mod 8)
Therefore, N = ord_8(7) = 2, so 7 is NOT a primitive root mod 8.
So, there are no primitive roots mod 8.
2 is a primitive root mod 15 <===> ord_15(2) = phi(15) = 8 <===> 2^8 = 1 (mod 15),
so we list the powers of 2^n (mod 15):
n = 1 ==> 2^n = 2^1 = 2 (mod 15)
n = 2 ==> 2^n = 2^2 = 4 (mod 15)
n = 3 ==> 2^n = 2^3 = 8 (mod 15)
n = 4 ==> 2^n = 2^4 = 16 = 1 (mod 15)
Therefore, N = ord_15(3) = 4, so 2 is NOT a primitive root mod 15.
4 is a primitive root mod 15 <===> ord_15(4) = phi(15) = 8 <===> 4^8 = 1 (mod 15),
so we list the powers of 4^n (mod 15):
n = 1 ==> 4^n = 4^1 = 4 (mod 15)
n = 2 ==> 4^n = 4^2 = 16 = 1 (mod 15)
Therefore, N = ord_15(4) = 2, so 4 is NOT a primitive root mod 15.
7 is a primitive root mod 15 <===> ord_15(7) = phi(15) = 8 <===> 7^8 = 1 (mod 15),
so we list the powers of 7^n (mod 15):
n = 1 ==> 7^n = 7^1 = 7 (mod 15)
n = 2 ==> 7^n = 7^2 = 49 = 4 (mod 15)
n = 3 ==> 7^n = 7^3 = 4*7 = 28 = -2 (mod 15)
n = 4 ==> 7^n = 7^4 = -2*7 = -14 = 1 (mod 15)
Therefore, N = ord_15(7) = 4, so 7 is NOT a primitive root mod 15.
8 is a primitive root mod 15 <===> ord_15(8) = phi(15) = 8 <===> 8^8 = 1 (mod 15),
so we list the powers of 8^n (mod 15):
n = 1 ==> 8^n = 8^1 = 8 (mod 15)
n = 2 ==> 8^n = 8^2 = 64 = 4 (mod 15)
n = 3 ==> 8^n = 8^3 = 4*8 = 32 = 2 (mod 15)
n = 4 ==> 8^n = 8^4 = 2*8 = 16 = 1 (mod 15)
Therefore, N = ord_15(8) = 4, so 8 is NOT a primitive root mod 15.
11 is a primitive root mod 15 <===> ord_15(11) = phi(15) = 8 <===> 11^8 = 1 (mod 15),
so we list the powers of 11^n (mod 15):
n = 1 ==> 11^n = 11^1 = 11 (mod 15)
n = 2 ==> 11^n = 11^2 = 121 = 1 (mod 15)
Therefore, N = ord_15(11) = 2, so 11 is NOT a primitive root mod 15.
13 is a primitive root mod 15 <===> ord_15(13) = phi(15) = 8 <===> 13^8 = 1 (mod 15),
so we list the powers of 13^n (mod 15):
n = 1 ==> 13^n = 13^1 = 13 (mod 15)
n = 2 ==> 13^n = 13^2 = 169 = 4 (mod 15)
n = 3 ==> 13^n = 13^3 = 4*13 = 52 = 7 (mod 15)
n = 4 ==> 13^n = 13^4 = 7*13 = 91 = 1 (mod 15)
Therefore, N = ord_15(13) = 4, so 13 is NOT a primitive root mod 15.
14 is a primitive root mod 15 <===> ord_15(14) = phi(15) = 8 <===> 14^8 = 1 (mod 15),
so we list the powers of 14^n (mod 15):
n = 1 ==> 14^n = 14^1 = 14 (mod 15)
n = 2 ==> 14^n = 14^2 = 196 = 46 = 1 (mod 15)
Therefore, N = ord_15(14) = 2, so 14 is NOT a primitive root mod 15.
So, there are no primitive roots mod 15.
# Wilson's Theorem Warmups:
1! (mod 2) = 1 (mod 2) = -1 (mod 2)
2! (mod 3) = 2*1 (mod 3) = 2 (mod 3) = -1 (mod 3)
17 * [1,2,3,4,5,6,7,8,9,10] = [17,34,51,68,85,102,119,136,153,170]
16! (mod 17) = 1*2*3*4*5*6*7*8*9*10*11*12*13*14*15*16 (mod 17) 
    = 1*(2*9)*(3*6)*(4*13)*(5*7)*(8*15)*(10*12)*(11*14)*16 (mod 17)
    = 1*18*18*52*35*120*120*154*-1 (mod 17) = 1*1*1*1*1*1*1*1*-1 (mod 17) = -1 (mod 17)
14! (mod 15) = 1*2*3*4*5*6*7*8*9*10*11*12*13*14 (mod 15)
    = (1*3*5) * (2*4*6*7*8*9*10*11*12*13*14) (mod 15)
    = (15) * (2*4*6*7*8*9*10*11*12*13*14) (mod 15) = 0 (mod 15) =/= -1 (mod 15)
Show that 2*(p-3)! = -1 (mod p) is true for all primes p:
2*(p-3)! (mod p) = 2*(p-1)!*(p-2)⁻¹*(p-1)⁻¹ (mod p) = 2*(-1)*(p-2)⁻¹*(p-1)⁻¹ (mod p)
    = (-1)*(-2)*(p-1)*(p-2)⁻¹*(p-1)⁻¹ (mod p) = (-1)*(p-2)*(p-2)⁻¹ (mod p) = -1 (mod p)
### Primitive Roots Modulo n Warmups:
# Which has a primitive root out of {4,8,9,10,12,16,22,27,28,31,33}?:
n has a primitive root <==> n = 1, 2, 4, p^k, or 2*p^k for some odd prime p and k in N
so {4, 9, 22, 27, 31} have primitive roots and {8, 10, 12, 16, 28, 33} don't have P.R.s.
# Find a primitive root mod 9 = 3^2, 25 = 5^2, and 18 = 2*3^2:
2 is a primitive root mod 3 <==> ord_3(2) = phi(3) = 2 <==> 2^1 =/= 1 (mod 3) ==> yes
    since 2 is a primitive root mod 3, then a primitive root mod 9 = 3^2 is 2 + 1*3 = 5
5 is a primitive root mod 9 <==> ord_9(5) = phi(9) = 6 <==> 5^2 == -2 =/= 1 (mod 9) and 
    5^3 == -2 * 5 == -10 == -1 =/= 1 (mod 9) ==> yes
2 is a primitive root mod 5 <==> ord_5(2) = phi(5) = 4 <==> 2^2 = -1 =/= 1 (mod 5) ==> yes
    since 2 is a primitive root mod 5, then a primitive root mod 25 = 5^2 is 2 + 2*5 = 12
12 is a primitive root mod 25 <==> ord_25(12) = phi(25) = 20 <==> 12^2 == 144 == -6 =/= 1
    (mod 25) and 12^5 == 12^2 * 12^2 * 12 == -6 * -6 * 12 == -6 * -72 == -6 * 3 == -18
    == 7 =/= 1 (mod 25) ==> yes
since 5 is a primitive root mod 9, then a primitive root mod 18 = 2 * 3^2 is 5
5 is a primitive root mod 18 <==> ord_18(5) = phi(18) = 6 <==> 5^2 == 25 == 7 =/= 1 
    (mod 18) and 5^3 == 7 * 5 == 35 == -1 =/= 1 (mod 18) ==> yes
# Prove that ax² + bx + c = 0 and cy² + by + a = 0 have reciprocal roots:
Given ax² + bx + c = 0, a =/= 0, and c =/= 0 we have x = [ -b +- √(b² - 4ac) ] / 2a,
and given cy² + by + a = 0, c =/= 0, and a =/= 0 we have y = [ -b +- √(b² - 4ca) ] / 2c,
so now we have the following:
y = { [ -b +- √(b² - 4ca) ][ -b -+ √(b² - 4ca) ] } / { 2c [ -b -+ √(b² - 4ca) ] }
y = { [-b]² - [√(b² - 4ca)]² } / { 2c [ -b +- √(b² - 4ac) ] }
y = { b² - (b² - 4ca) } / { 2c [ -b +- √(b² - 4ac) ] }
y = { b² - b² + 4ca } / { 2c [ -b +- √(b² - 4ac) ] }
y = { 4ca } / { 2c [ -b +- √(b² - 4ac) ] } = 2a / [ -b +- √(b² - 4ac) ] = 1/x.
# Prove the cubic formula:
Given ax³ + bx² + cx + d = 0 and a =/= 0, we have the following:
x³ + bx²/a + cx/a + d/a = 0, so x³ + 3(b/3a)x² + 3(b/3a)²x + cx/a + d/a = 3(b/3a)²x,
so x³ + 3(b/3a)x² + 3(b/3a)²x + (b/3a)³ + cx/a + d/a = 3(b/3a)²x + (b/3a)³,
so (x + b/3a)³ + cx/a + c(b/3a)/a + d/a = (b/3a)² (3x + b/3a) + c(b/3a)/a,
so (x+b/3a)³+(c/a)(x+b/3a)+d/a+(b/3a)²(2b/3a)=(b/3a)²(3x+b/3a)+(b/3a)²(2b/3a)+(c/a)(b/3a),
so (x+b/3a)³+(c/a)(x+b/3a)+d/a+(b/3a)²(2b/3a)=(b/3a)²(3x+3b/3a)+(c/a)(b/3a),
so (x+b/3a)³+(c/a)(x+b/3a)-3(b/3a)²(x+b/3a)+d/a+(b/3a)²(2b/3a)-(c/a)(b/3a)=0,
so (x+b/3a)³ + [c/a-3(b/3a)²] (x+b/3a) + d/a + 2(b/3a)³ - (bc/3a²) = 0,
so y³ + Ay + B = 0, with y = x+b/3a, A = c/a-3(b/3a)², and B = d/a+2(b/3a)³-(bc/3a²)
y = u + v, so y³ = (u+v)³ =  u³ + 3u²v + 3uv² + v³ = u³ + v³ + 3uv(u+v) = u³ + v³ + 3uvy,
so y³ - (u³ + v³ + 3uvy) = 0, so y³  - (3uv)y - (u³ + v³) = 0 = y³ + Ay + B,
so A = -3uv and B = -(u³ + v³), so A³ = -27u³v³ and 27u³B = -27(u³)² - 27u³v³,
so 27u³B = -27(u³)² + A³, so 27(u³)² + 27B(u³) - A³ = 0, so now we have, from the
quadratic formula: u³ = { -(27B) +- ²√[(27B)² - 4*(27)*(-A³)] } / { 2*(27) },
so u³ = { -27B +- ²√[(27)²B² + 4*(27)²*A³/27] } / { 2*(27) },
so u³ = [ -B +- ²√(B² + 4*A³/27) ] / 2, so B = -([ -B +- ²√(B² + 4*A³/27) ]/2 + v³),
so v³ = -B - [ -B +- ²√(B² + 4*A³/27) ]/2, so u = ³√{[ -B +- ²√(B² + 4*A³/27) ] / 2}
and v = ³√{-B - [ -B +- ²√(B² + 4*A³/27) ]/2}, so y = u + v, which is the following:
y = ³√{[ -B +- ²√(B² + 4*A³/27) ] / 2} + ³√{-B - [ -B +- ²√(B² + 4*A³/27) ]/2}
so since y = x + b/3a, then we have x = y - b/3a, so:
x = ³√{[ -B +- ²√(B² + 4*A³/27) ] / 2} + ³√{-B - [ -B +- ²√(B² + 4*A³/27) ]/2} - b/3a
where A = c/a-3(b/3a)², and B = d/a+2(b/3a)³-(bc/3a²).
# Find all x, y, z in the real numbers (R) such that (x + y + z)² = x³ + y³ + z³:
First, we have the obvious solution of x = y = z = 0,
because (0 + 0 + 0)² = 0² = 0 = 0 + 0 + 0 = 0³ + 0³ + 0³;
second we have the obvious solution of x = -1, y = 1, z = 0,
because (-1 + 1 + 0)² = 0² = 0 = -1 + 1 + 0 = (-1)³ + 1³ + 0³
and permutations thereof by symmetry;
third we have the obvious solution of x = -1, y = 1, z = 1,
because (-1 + 1 + 1)² = 1² = 1 = -1 + 1 + 1 = (-1)³ + 1³ + 1³,
and permutations thereof by symmetry;
fourth we have the obvious solution of x = 1, y = 2, z = 3,
because (1 + 2 + 3)² = 6² = 36 = 1 + 8 + 27 = 1³ + 2³ + 3³,
and permutations thereof by symmetry;
fifth we have the obvious solution of x = 1, y = 2, z = 0,
because (1 + 2 + 0)² = 3² = 9 = 1 + 8 + 0 = 1³ + 2³ + 0³,
and permutations thereof by symmetry;
sixth we have the obvious solution of x = 1, y = 0, z = 0,
because (1 + 0 + 0)² = 1² = 1 = 1 + 0 + 0 = 1³ + 0³ + 0³,
and permutations thereof by symmetry; AND
seventh we have more generally (x+y)² + 2(x+y)z + z² = x³ + y³ + z³,
so x³ + y³ + z³ - (x+y)² - 2(x+y)z - z² = 0,
so z³ - z² - 2(x+y)z + (x³ + y³)* - (x+y)² = 0,
so z³ - z² - 2(x+y)z + (x+y)(x²-xy+y²)* - (x+y)² = 0,
so z³ - z² - 2(x+y)z + (x+y)(x²-xy+y²-(x+y)) = 0,
so z³ - z² - 2(x+y)z + (x+y)(x²-xy+y²-x-y) = 0,
using the cubic formula with the following we have:
a = 1, b = -1, c = -2(x+y), and d = (x+y)(x²-xy+y²-x-y)
z = ³√{q + ²√[q² + (r-p²)³]} + ³√{q² - ²√[q + (r-p²)³]} + p
p = -b/(3a),  q = p³ + (bc-3ad)/(6a²),  and  r = c/(3a)
p = -(-1)/(3*1) = 1/3,  q = (1/3)³ + (-1*-2(x+y)-3*1*d)/(6*1²), so
q = 1/27 + (2x+2y-3d)/6 = 2/54 + 9(2x+2y-3d)/54 = (2+18x+18y-27d)/54,
and  r = -2(x+y)/(3*1) = (-2x-2y)/3, so we have that:
z = ³√{(2+18x+18y-27d)/54 + ²√[(2+18x+18y-27d)²/54² + ((-2x-2y)/3-(1/3)²)³]} + ³√{(2+18x+18y-27d)²/54² - ²√[(2+18x+18y-27d)/54 + ((-2x-2y)/3-(1/3)²)³]} + (1/3),
so z = ³√{(2+18x+18y-27d)/54 + ²√[(2+18x+18y-27d)²/54² + (6x+6y+1)³/9³]} + ³√{(2+18x+18y-27d)²/54² - ²√[54*(2+18x+18y-27d)/54² - (2x+2y+1)³/9³]} + (1/3),
so z = ³√{(2+18x+18y-27d)/54 + ²√[(2+18x+18y-27d)²/54² + 4(6x+6y+1)³/54²]} + ³√{(2+18x+18y-27d)²/54² - ²√[54(2+18x+18y-27d)/54² - 4(2x+2y+1)³/54²]} + (1/3),
so z = ³√{(2+18x+18y-27d)+²√[(2+18x+18y-27d)²+4(6x+6y+1)³]}/(3*³√(2)) + ³√{(2+18x+18y-27d)²-54*²√[54(2+18x+18y-27d)-4(2x+2y+1)³]}/(9*³√(4)) + (1/3),
where d = (x+y)(x²-xy+y²-x-y).
*            x² - xy + y²
        -------------------------
(x + y) |   x³ +  0  + y³
          -(x³ + x²y)
           ----------
                 - x²y + y³
               -(- x²y - xy²)
                -------------
                         y³ + xy²
                       -(xy² + y³)
                        ----------
                               0
# Find all solutions:
(a) 9x == 5 (mod 25)
First, there is one (1) solution since gcd(9, 25) = 1 and 1 | 5.
Now we have the following to calculate via the Euclidean Algorithm:
25 = 2*9 + 7,   9 = 1*7 + 2,   and   7 = 3*2 + 1,   so
7 = 25 - 2*9,   2 = 9 - 1*7,   and   1 = 7 - 3*2,   so
2 = 9 - 1*(25 - 2*9)   and   1 = (25 - 2*9) - 3*2,   so
1 = (25 - 2*9) - 3*[9 - 1*(25 - 2*9)] = 25 - 2*9 - 3*9 + 3*(25 - 2*9)
1 = 25 - 2*9 - 3*9 + 3*25 - 6*9 = 4*25 - 11*9, so 5 = 20*25 - 55*9
so x == -55 (mod 25) == 20 (mod 25).
(b) 987x == 610 (mod 1597)
First, we have to calculate the gcd(987, 1597) via the Euclidean Algorithm:
1597 = 1*987 + 610,  987 = 1*610 + 377,  610 = 1*377 + 233,  377 = 1*233 + 144,
233 = 1*144 + 89,  144 = 1*89 + 55,  89 = 1*55 + 34,  55 = 1*34 + 21,  34 = 1*21 + 13,
21 = 1*13 + 8,  13 = 1*8 + 5,  8 = 1*5 + 3,  5 = 1*3 + 2,  3 = 1*2 + 1,   2 = 2*1
So, now we have that there is one (1) solution since gcd(987, 1597) = 1 and 1 | 610.
Next, we can see that 987x == -987 == 1597-987 == 610 (mod 1597),
so x must be == -1 == 1596 (mod 1597).
# Linear formula proof:
Given ax + b = 0 and a =/= 0, we have the following: x + b/a = 0, so x = - b/a.
# Quadratic formula proof:
Given ax² + bx + c = 0 and a =/= 0, we have the following:
x² + bx/a + c/a = 0, so x² + bx/a + (b/2a)² + c/a = (b/2a)²,
so x² + 2*x*(b/2a) + (b/2a)² = (bx/2a)² - c/a,
so (x + b/2a)² = (b/2a)² - c/a, so (x + b/2a)² = b²/4a² - 4ac/4a²,
so (x + b/2a)² = (b² - 4ac) / 4a², so x + b/2a = +- ²√(b² - 4ac) / ²√(4a²),
so x = -b / 2a +- √(b² - 4ac) / 2a = [ -b +- √(b² - 4ac) ] / 2a.
# Cubic formula proof:
*** See after the following quartic formula proof. ***
# Quartic formula proof:
Given ax⁴ + bx³ + cx² + dx + e = 0 = (Ax² + Bx + C)² - (Dx² + Ex + F)²,
we have the following:
(A²x⁴ + ABx³ + ACx² + ABx³ + B²x² + BCx + ACx² + BCx + C²) - 
    (D²x⁴ + DEx³ + DFx² + DEx³ + E²x² + EFx + DFx² + EFx + F²) = 0, so
(A²x⁴ + 2ABx³ + 2ACx² + B²x² + 2BCx + C²) - (D²x⁴ + 2DEx³ + 2DFx² + E²x² + 2EFx + F²) = 0,
so A²x⁴ - D²x⁴ + 2ABx³ - 2DEx³ + 2ACx² + B²x² + ACx² - 2DFx² - E²x² 
    + 2BCx - 2EFx + C² - F² = 0, so
(A² - D²) * x⁴ + (2AB - 2DE) * x³ + (2AC + B² - 2DF - E²) * x² 
    + (2BC - 2EF) * x + (C² - F²) = 0, so
we now have the following 5 equations between our given constants and our new constants:
a = A² - D²,  b = 2AB - 2DE,  c = 2AC - 2DF + B² - E²,  d = 2BC - 2EF,  and  e = C² - F².
So, now we can solve them for our new constants, namely A, B, C, D, E, and F:
a + D² = A²,  b + 2DE = 2AB,  c + 2DF = 2AC + B² - E²,  d + 2EF = 2BC,  and  e + F² = C²
√(a+D²) = A,  (b+2DE)/(2A) = B,  2DF = 2AC + B² - E² - c,  2EF = 2BC - d,  and  √(e+F²) = C
A=√(a+D²),  B=(b+2DE)/(2A),  D=(2AC+B²-E²-c)/(2F),  E=(2BC-d)/(2F),  and  C=√(e+F²)
A=√(a+D²),  B=(b+2DE)/(2A),  C=√(e+F²),  D=(2AC+B²-E²-c)/(2F),  and  E=(2BC-d)/(2F)
Right now, we have B and E in terms of each other, so let's plug in E into B:
B = ( b + 2D [(2BC-d) / (2F)] )  /  (2A), and then solve for B:
B = ( b + (D/F) * (2BC-d) )  /  (2A) = ( b + 2BCD/F - dD/F )  /  (2A)
2AB = b + 2BCD/F - dD/F, so 2AB - 2BCD/F = b - dD/F, so B * (2A - 2CD/F) = b - dD/F,
so B = (b - dD/F) / (2A - 2CD/F) = (bF - dD) / (2AF - 2CD), so now:
A=√(a+D²),  B=(bF-dD)/(2AF-2CD),  C=√(e+F²),  D=(2AC+B²-E²-c)/(2F),  and  E=(2BC-d)/(2F),
so now if we let F = 1, then we have the following:
A=√(a+D²),  B=(b*1-dD)/(2A*1-2CD),  C=√(e+1²),  D=(2AC+B²-E²-c)/(2*1), and E=(2BC-d)/(2*1),
so A=√(a+D²),  B=(b-dD)/(2A-2CD),  C=√(e+1),  D=(2AC+B²-E²-c)/2, and E=(2BC-d)/2.
Now that we have our new constants in terms of our given constants, we have the following:
(Ax² + Bx + C)² - (Dx² + Ex + F)² = 0
(Ax² + Bx + C)² - (Dx² + Ex + 1)² = 0
(Ax² + Bx + C)² = (Dx² + Ex + 1)²
Ax² + Bx + C = +-(Dx² + Ex + 1)
Ax² + Bx + C = +(Dx² + Ex + 1)   or   Ax² + Bx + C = -(Dx² + Ex + 1)
Ax² + Bx + C - Dx² - Ex - 1 = 0   or   Ax² + Bx + C + Dx² + Ex + 1 = 0
(A-D) * x² + (B-E) * x + (C-1) = 0   or   (A+D) * x² + (B+E) * x + (C+1) = 0.
Using the quadratic formula, we now have the following:
x = [ -(B-E) +- √( (B-E)² - 4*(A-D)*(C-1) ) ] / [ 2*(A-D) ]   or
    x = [ -(B+E) +- √( (B+E)² - 4*(A+D)*(C+1) ) ] / [ 2*(A+D) ].
# *** Cubic formula proof ***:
Given ax³ + bx² + cx + d = 0 = `b`x³ + `c`x² + `d`x + `e` = 
    0 + `b`x³ + `c`x² + `d`x + `e` = 0x⁴ + `b`x³ + `c`x² + `d`x + `e` = 
    `a`x⁴ + `b`x³ + `c`x² + `d`x + `e` = (Ax² + Bx + C)² - (Dx² + Ex + F)²,
a = 0, and b =/= 0, we have the following, as seen above, and more below:
`a` = A²-D²,  `b` = 2AB-2DE,  `c` = 2AC - 2DF + B²- E²,  `d` = 2BC-2EF,  and  `e` = C²-F²,
so, with F=1, A=√(`a`+D²), B=(`b`-`d`D)/(2A-2CD), C=√(`e`+1), D=(2AC+B²-E²-`c`)/2,
and E=(2BC-`d`)/2, so, with `a`=0, so A=√(0+D²), `b`=a, `c`=b, `d`=c, and `e`=d, we have:
A=√(D²), B=(a-cD)/(2A-2CD), C=√(d+1), D=(2AC+B²-E²-b)/2, and E=(2BC-c)/2
Using the quadratic formula yet again, like last time, we now have the following:
x = [ -(B-E) +- √( (B-E)² - 4*(A-D)*(C-1) ) ] / [ 2*(A-D) ]  or
x = [ -(B+E) +- √( (B+E)² - 4*(A+D)*(C+1) ) ] / [ 2*(A+D) ],
but this time we must be careful, since A-D or A+D is = to 0.
# Find all quadratic residues mod 13, 16, 17, and 23:
For 13, we have 6 quadratic residues:
1² ==  1 (mod 13),
2² ==  4 (mod 13),
3² ==  9 (mod 13),
4² == 16 (mod 13) ==  3 (mod 13),
5² == 25 (mod 13) == 12 (mod 13),
6² == 36 (mod 13) == 10 (mod 13),
so the quadratic residues mod 13 are 1, 3, 4, 9, 10, and 12.
For 16, we have 2 quadratic residues:
 1² ==      1 (mod 16),
 3² ==      9 (mod 16),
 5² ==     25 (mod 16) ==  9 (mod 16),
 7² ==     49 (mod 16) ==  1 (mod 16),
 9² == (-7)² (mod 16) == 49 (mod 16) == 1 (mod 16),
11² == (-5)² (mod 16) == 25 (mod 16) == 9 (mod 16),
13² == (-3)² (mod 16) ==  9 (mod 16),
15² == (-1)² (mod 16) ==  1 (mod 16),
so the quadratic residues mod 16 are 1 and 9.
For 17, we have 8 quadratic residues:
1² ==  1 (mod 17),
2² ==  4 (mod 17),
3² ==  9 (mod 17),
4² == 16 (mod 17),
5² == 25 (mod 17) ==  8 (mod 17),
6² == 36 (mod 17) ==  2 (mod 17),
7² == 49 (mod 17) == 15 (mod 17),
8² == 64 (mod 17) == 13 (mod 17),
so the quadratic residues mod 17 are 1, 2, 4, 8, 9, 13, 15, and 16.
For 23, we have 11 quadratic residues:
 1² ==   1 (mod 23),
 2² ==   4 (mod 23),
 3² ==   9 (mod 23),
 4² ==  16 (mod 23),
 5² ==  25 (mod 23) ==  2 (mod 23),
 6² ==  36 (mod 23) == 13 (mod 23),
 7² ==  49 (mod 23) ==  3 (mod 23),
 8² ==  64 (mod 23) == 18 (mod 23),
 9² ==  81 (mod 23) == 12 (mod 23),
10² == 100 (mod 23) ==  8 (mod 23),
11² == 121 (mod 23) ==  6 (mod 23),
so the quadratic residues mod 23 are 1, 2, 3, 4, 6, 8, 9, 12, 13
# Counting on a chessboard (derived here: youtube.com/watch?v=DIsW_6u7jrA):
rectangles = n² * (n+1)² / 4
squares = n * (n+1) * (2n+1) / 6
# Problem from the Sir Isaac Newton vs Bill Nye Epic Rap Battles of History video:
Given ∫ sec(y) dy for y from 0 to π/6 = ln(√[3]) * (?)^64, ? = 1, -1, i, -i, and more.
# Sum of roots rational, but product irrational:
Suppose that x1,x2,x3,x4 are the real roots of a polynomial with integer coefficients of degree 4, and x1+x2 is rational while x1x2 is irrational. Is it necessary that x1+x2 = x3+x4?
For example, the polynomial x4−8x3+18x2−8x−7 has roots
x1=1−√2, x2=3+√2, x3=1+√2,x4=3−√2.
It holds that x1+x2 is rational while x1x2 is irrational, and we have x1+x2=x3+x4
# Limit as n goes to infinity of:
sum as k goes from 1 to n of 1 - e ^ [1/(n+k)]
# Given that (x+1)² + a² = x² + b² = (x-1)² + c², where x, a, b, and c are
# all integers, prove that the gcd(a, c) is greater than or equal to 4:
Let a = dA and c = dC, where d = gcd(a, c), so gcd(A, C) = 1, and we get:
(x+1)² + (dA)² = x² + b² = (x-1)² + (dC)²
***Note that since (x+1)² and (x-1)² have the same parity,
then (dA)² and (dC)² also must have the same parity, and
since x² and (x+1)² have the opposite parity, then 
(dA)² and b² must also have the opposite parity.***
(x+1)² + d²A² = x² + b² = (x-1)² + d²C²
(x+1)² + d²A² = (x-1)² + d²C²
(x+1)² - (x-1)² = d²C² - d²A²
(x² + 2x + 1) - (x² - 2x + 1) = d² * (C² - A²)
x² + 2x + 1 - x² + 2x - 1 = d² * (C² - A²)
4x = d² * (C² - A²), and since we also have:
x² + 2x + 1 + d²A² = (x+1)² + d²A² = x² + b²,
then 2x + 1 + d²A² = b², then 4x + 2 + 2d²A² = 2b², so then:
d² * (C² - A²) + 2 + 2d²A² = 2b², so d² * (C² - A² + 2A²) + 2 =
2b²,so, now, given d* (A² + C²) + 2 = 2b², we still must show that d >= 4:
***see above***, and now we have (dA)² + (dC)² + 2 = 2b²,
where dA and dC have the same parity, so if d is odd, then 
either A and C are both even or both odd, but since gcd(A, C) = 1,
then A and C can't both be even, so they must both be odd.
Therefore, b² must be even, so b must be even, so let b = 2B,
d = 2D + 1, A = 2m + 1, and C = 2n + 1, so we now have the following:
([2D+1] * [2m+1])² + ([2D+1] * [2n+1])² + 2 = 2*(2B)²
(4Dm + 2D + 2m + 1)² + (4Dn + 2D + 2n  1)² + 2 = 2*4B²
(4Dm + 2*(D+m) + 1)² + (4Dn + 2*(D+n) + 1)² + 2 = 8B²
16D²m² + 4*(D+m)² + 1 + 2*4*2*Dm*(D+m) + 2*2*(D+m) + 2*4Dm + 
    16D²n² + 4*(D+n)² + 1 + 2*4*2*Dn*(D+n) + 2*2*(D+n) + 2*4Dn + 2 = 8B²
16D²m² + 4*(D+m)² + 16*Dm*(D+m) + 4*(D+m) + 8Dm + 
    16D²n² + 4*(D+n)² + 16*Dn*(D+n) + 4*(D+n) + 8Dn + 4 = 8B²
So, if we reduce both sides by mod 8, then we have the following:
4*(D+m)² + 4*(D+m) + 4*(D+n)² + 4*(D+n) + 4 == 0 (mod 8)
[2*(D+m)]² + 2*[2*(D+m)][1] + 1² + [2*(D+n)]² + 2*[2*(D+n)][1] + 1² + 2 == 8 (mod 8)
[2*(D+m) + 1]² + [2*(D+n) + 1]² == 6 (mod 8), but the only odd squares mod 8 are:
1² == 1, 3² == 9 == 1, 5² == 25 == 1, and 7² == 49 == 1, all (mod 8),
so we would have the congruence 2 == 6 (mod 8),
but that is clearly nonsense, so d cannot be odd.
Thus, d is even, so (dA)² + (dC)² + 2 = 2b², where d=2D,
and b is odd since dA is even, so b = 2B+1, and we have:
(2DA)² + (2DC)² + 2 = 2*(2B+1)²
4D²A² + 4D²C² + 2 = 2*(4B²+4B+1)
4D² * (A² + C²) + 2 = 8B² + 8B + 2
4D² * (A² + C²) = 8B² + 8B
D² * (A² + C²) = 2B² + 2B = 2B * (B+1),
but since gcd(A, C) = 1, then at least 1 of A and C must be odd,
so let A be the odd one, so A = 2m+1, and we have:
D² * ([2m+1]² + C²) = 2B * (B+1)
D² * (4m² + 4m + 1 + C²) = 2B * (B+1)
4 * D² * (m² + m) + D² * (1 + C²) = 2B * (B+1)
since B is odd or even, then B+1 is even or odd,
and, as a result, 2B * (B+1) == 0 (mod 4), 
so reducing the above equation mod 4, we get:
D² * (1 + C²) == 0 (mod 4), but C² can only be == 0 or 1 (mod 4),
so 1 + C² is == 1 or 2 (mod 4), so we now have either, so
D² or 2D² == 0 (mod 4), so if D is odd, then D² is == 1 (mod 4),
and 2D² == 2 (mod 4), so we would then have a contradiction,
so D must be even, so d = 2D must be == 0 (mod 4), 
so, we finally have, d = gcd(a,c) must be >= 4.
# i) Calculate gcd(n+1, n²-n+1) for n = 1, 2, 3, 4, and 5:
gcd(1+1, 1²-1+1) = gcd(2, 1-0) = gcd(2, 1) = 1
gcd(2+1, 2²-2+1) = gcd(3, 4-1) = gcd(3, 3) = 3
gcd(3+1, 3²-3+1) = gcd(4, 9-2) = gcd(4, 7) = 1
gcd(4+1, 4²-4+1) = gcd(5, 16-3) = gcd(5, 13) = 1
gcd(5+1, 5²-5+1) = gcd(6, 25-4) = gcd(6, 21) = 3
# ii) Show that gcd(n+1, n²ˆ’n+1) | [ n*(n+1) ˆ’ (n²ˆ’n+1) ]:n+1), so by definition d | (n+1) and d | (n²-n+1).
Next, that means that n+1 = d*x and n²-n+1 = d*y, for some whole numbers
x and y, so n*(n+1) ˆ’ (n²ˆ’n+1) = n*d*x - d*y = d * (n*x - y), so
by definition (d, aka) gcd(n+1, n²-n+1) | [ n*(n+1) ˆ’ (n²ˆ’n+1) ].
# iii) Show that any common divisor of n+1 and 2*nˆ’1 divides 3:
Let c = any common divisor of n+1 and 2*nˆ’1, so by definition n+1 = c*w and 
2*n-1 = c*z, for some whole numbers w and z. Next, note that:
3 = 2n + 2 - 2n + 1 = 2*(n+1) - (2n-1) = 2*c*w - c*z = c * (2*w-z),
so, by definition, yet again, c (any common divisor of n+1 and 2*nˆ’1) | 3.
# iv) Use parts (ii) and (iii) to show that gcd(n+1, n²ˆ’n+1) always = 1 or 3:
First, observe that d = gcd(n+1, n²-n+1) | [ n*(n+1) ˆ’ (n²ˆ’n+1) ].
Second, observe that n*(n+1) ˆ’ (n²ˆ’n+1) = n² + n - n² + n - 1 = 2n-1.
Third, observe that c = any common divisor of n+1 and 2*nˆ’1 | 3.
Forth, observe that d | 2n-1 by above and d | n+1 by definition,
so d is a common divisor of n+1 and 2*nˆ’1, so d | 3, but the only 
2 numbers that divide 3 are 1 and 3, so d = gcd(n+1, n²-n+1) always = 1 or 3.
# Prove that the ratio test is inconclusive when lim n->ˆž of |a_{n+1}/a_n|=1:
A convergent series with this property is the ˆ‘(-1)^n/n from n = 1 to ˆž, 
since the lim as n -> ˆž of | (-1)^(n+1)/(n+1) Ã· (-1)^(n)/n | = 
the lim as n -> ˆž of | (-1)^(n+1) * n Ã· [ (n+1) * (-1)^n ] | = 
the lim as n -> ˆž of | (-1)^(1) * n Ã· (n+1) | = 1.
A divergent series with this property is the ˆ‘(1/n) from n = 1 to ˆž, 
since the lim as n->ˆž of |1/(n+1)Ã·1/n| = the lim as n->ˆž of |n/(n+1)| = 1.
# Find all integers  x and y >= 0 such that 3x² = 5^y +2:
# Find all real values of x to fulfill the inequality sqrt(5x+6) > x-3:
# Given that (x+y)! >= (x!)*(y!) is true for all x ˆˆ N and y ˆˆ N 
# (integers >= 0), find all x and y such that the equality holds:
(x+y)! = (x!)*(y!) implies (x!)*(x+1)*...*(x+y) = (x!)*(y!), which,
in turn, implies (x+1)*(x+2)*...*(x+y) = y! = 1*2*...*y, so then we get
the following set of equations: x+1 = 1, x+2 = 2, ... , and x+y = y, so 
x must = 0 for any, and therefore all, of these to be true. This works 
for any y, so, also due to symmetry, our solutions are the following:
(x=0, y=0); (x=0, y>=1); & (x>=1, y=0).
# Find the domain and range of f(x,y) = (xy + y²) / (x² + y²) over
# the real numbers, and find the limit as (x,y) --> (0,0) of f(x,y):
The only way that f(x,y) is undefined is when both x and y are 0, since
that is the only way that the denominator, namely x² + y², is = 0. So,
the domain is (x,y) ˆˆ R² / (0,0); also known as all points in the x-y
plane (where both x and y are real numbers) except the origin. 
To find the range, let's first assume that y =/= 0, so that we 
can divide both the top and the bottom of our function f(x,y) 
by y² to get that f(x,y) = (xy + y²) / (x² + y²), so f(x,y) 
= (xy/y² + y²/y²) / (x²/y² + y²/y²) = ([x/y] + 1) / ([x/y]² + 1), 
so f(x,y) = (z + 1) / (z² + 1), where z = x/y, and since both 
x and y are real numbers, then z can be any real number.
Therefore, in order to find the range of f(x,y), we must then 
find z in terms of f and then find the domain of z(f) = z:
f = (z + 1) / (z² + 1), so (z² + 1) f = z + 1, fz² + f = z + 1, so 
fz² - z + f-1 = 0, so z = ( 1 +- ˆš[ 1 - 4*(f)*(f-1) ] ) / (2*f)
Therefore, for z to be defined, f must be such that:
f =/= 0 and 1 - 4f(f-1) >= 0, so 1 >= 4f(f-1), so 4f(f-1) <= 1, 
so f(f-1) <= 1/4, so f² - f <= 1/4, so f² - f - 1/4 <= 0,
so f is between ( 1 - ˆš[ 1 - 4*(1)*(-1/4) ] ) / (2*1) and 
( 1 + ˆš[ 1 - 4*(1)*(-1/4) ] ) / (2*1), so if we simplify this
we get that f is between ( 1 - ˆš[ 1 - (-1) ] ) / 2 and 
( 1 + ˆš[ 1 - (-1) ] ) / 2, so f is between (1 - ˆš2) / 2 
and (1 + ˆš2) / 2. This includes f = 0 since (1 - ˆš2) / 2 = 
- (ˆš2 - 1) / 2, which is < 0; (1 + ˆš2) / 2 = (ˆš2 + 1) / 2,
which is > 0; and f = f(z) = (z + 1) / (z² + 1) = ([x/y] + 1) 
/ ([x/y]² + 1) = f(x,y) = 0 when z = x/y = -1. So, the range 
of f(x,y) is all real numbers f ˆˆ [-(ˆš2-1)/2, (ˆš2+1)/2].
Since when y = x, f(x,y) = f(x,x) = ([x/x]+1) / ([x/x]²+1),
which = (1+1) / (1²+1) = 2 / (1+1) = 2/2 = 1; and when y = -x,
f(x,y) = f(x,-x) = ([x/-x]+1) / ([x/-x]²+1), which = (-1+1) / 
([-1]²+1) = 0 / (1+1) = 0/2 = 0; we can conclude that the 
limit as (x,y) goes to (0,0) of f(x,y) does not exist.
# Differentiate y=x^x by definition:

# Integral of sin(2*Ï€*ˆš(1-x²)):

# Integral of cos(2x-a-b) divided by cos(b-a) + cos(2x-a-b):

# Integral of c * ln[ ˆš(a²+y²+c²) + a divided by ˆš(y²+c²) ] dy from 0 to b:

# Let m, n be positive integers and let x ˆˆ [0, 1],
# so prove that (1 - x^n)^m + (1 - (1-x)^m)^n ‰¥ 1:

# Find all (a,b,c) which are natural numbers which satisfy both of these
# equations: [1] 1/a = 1/b + 1/c - 1/abc and [2] a² + b² = c²

# ˆ‘ tan(kt) / k for k = 1 to ˆž

# Find the integral of (e^x cosx)^1/2 dx

# Try this integration out: int from 0 to 1 ((x^a) - 1) / lnx dx

# Find the integral of tan^2(arcsin(x)) sin^2(arctan(x)) + 1:
tan^2(arcsin(x)) sin^2(arctan(x))
# Find the integral from -ˆž to +ˆž of (ˆš(x^4+1)-x^2):

# Show that there exists no function f such that f(f(x))=(x^2)-2:

# Show that there exists no function f such that f(f(x))+xf(x)=1:

# If a/(b-8)=18 then what will be a/b & if Ã /(ÃŸ+8)=18 than what will be Ã /ÃŸ?:

# Claim: 10 | [divides] (n^5 - n) for all [integers] n ˆˆ Z
Proof by simple induction:
    Base case:
        When n = 0, n^5 - n = 0^5 - 0 = 0 - 0 = 0, and a*0 = 0 for
        any number a, so a divides 0, so 10 | 0, so 10 | (n^5 - n).
    Induction hypothesis:
        Suppose that 10 | (k^5 - k) for some k ˆˆ Z >= 0, aka k^5 - k = 
        10*x for some x ˆˆ Z, and note the k+1 case:
        since (k+1)^5-(k+1) = k^5 + 5*k^4 + 10*k^3 + 10*k² + 5*k + 1 - k - 1
        = (k^5 - k) + 10 * (k^3 + k^2) + 5 * (k^4 + k)
        = 10 * x + 10 * (k^3 + k^2) + 5 * (k^4 + k)
        = 10 * (x + k^3 + k^2) + 5 * ([2*a + b]^4 + [2*a + b]),
        where a ˆˆ Z and b = 0 or 1 such that k = 2*a + b, so this
        = 10 * (x + k^3 + k^2) + 5 * ([2*a]^4 + 4*b*[2*a]^3 + \
          6*[b^2]*[2*a]² + 4*[b^3]*[2*a] + b^4 + 2*a + b),
        and since b = 0 or 1, then b^4 = 0^4 or 1^4 = 0 or 1 = b, so this
        = 10 * (x + k^3 + k^2) + 5 * (16*[a^4] + 32*b*[a^3] + \
          24*[b^2]*[a^2] + 8*[b^3]*a + b + 2*a + b)
        = 10 * (x + k^3 + k^2) + 5 * (16*[a^4] + 32*b*[a^3] + \
          24*[b^2]*[a^2] + 8*[b^3]*a + 2*b + 2*a)
        = 10 * (x + k^3 + k^2) + 5 * 2 * (8*[a^4] + 16*b*[a^3] + \
          12*[b^2]*[a^2] + 4*[b^3]*a + b + a)
        = 10 * (x + k^3 + k^2) + 10 * (8*[a^4] + 16*b*[a^3] + \
          12*[b^2]*[a^2] + 4*[b^3]*a + b + a)
        = 10 * (x + k^3 + k² + 8*[a^4] + 16*b*[a^3] + \
          12*[b^2]*[a^2] + 4*[b^3]*a + b + a),
        which is 10 * y, where y is (some integer) ˆˆ Z, so
        (k+1)^5 - (k+1) = 10 * y, so 10 | [(k+1)^5 - (k+1)].
Proof for all negative n ˆˆ Z <= 0:
    Let n = -k, where k >= 0, so for all n ˆˆ Z <= 0, we have:
    n^5-n = (-k)^5 - (-k) = (-1)^5*(k^5) - (-k) = -1*k^5 - (-k) = -(k^5 - k).
    Now, since we proved above that 10 | (k^5 - k) for any k >= 0, then
    n^5-n = -(k^5-k) = (-1)*(10)*w, for some integer w ˆˆ Z, which = 10*(-w),
    where -w is also an integer ˆˆ Z, so we have 10|(n^5-n) for all nˆˆZ <= 0.
Therefore, 10 | (n^5 - n) for all integers n ˆˆ Z: positive, negative, and 0.
# Nested radicals:
# Problem:
ˆš(x +- ˆš(y)) = ˆš(a) +- ˆš(b)
# Conditions:
(1) y =/= perfect square
(2) a, b, x, & y all ˆˆ Q+
(3) x² - y = perfect square > 0
# Solution:
a = [ x + ˆš(x² - y) ] / 2
b = [ x - ˆš(x² - y) ] / 2
# Example 1 (thumbnail of this video [youtube.com/watch?v=gHefYLH4ICQ]):
ˆš(69 + 4*ˆš(20)) = ˆš(69 + ˆš(320)) = ˆš(a) + ˆš(b)
We assume that (1) is satisfied; y = 320 is =/= per. sq., so (2)
is also satisfied; x² - y = 69² - 320 = 4761 - 320 = 4441 =/= 
per. sq. (but is > 0), so (3) is NOT satisfied, so we do NOT
have a solution.
# Example 2 (first example of this video [youtube.com/watch?v=gHefYLH4ICQ]):
ˆš(3 - 2*ˆš(2)) = ˆš(3 - ˆš(8)) = ˆš(a) - ˆš(b)
We assume that (1) is satisfied; y = 8 is =/= per. sq., so (2)
is also satisfied; x² - y = 3² - 8 = 9 - 8 = 1 = 1² = per. 
sq. > 0, so (3) is satisfied, so we DO have a solution:
a = [ x + ˆš(x² - y) ] / 2 = [ 3 + ˆš(1) ] / 2 = [ 3 + 1 ] / 2 = 4 / 2 = 2
& b = [ x - ˆš(x² - y) ] / 2 = [ 3 - ˆš(1) ] / 2 = [ 3 - 1 ] / 2 = 2 / 2 = 1,
so ˆš(3 - 2*ˆš(2)) = ˆš(2) - ˆš(1) = ˆš(2) - 1
# If addition is ***DEFINED*** as follows, then we have:
a + b == Re[(a+i)*(b-i)] = Re[ab-ai+bi-i^2] = Re[ab + (b-a)i - (-1)] = ab+1
2 + 2 == Re[(2+i) * (2-i)] = Re[4 - 2i + 2i - i^2] = Re[4 + 0i - (-1)] = 5
2 + 3 == Re[(2+i) * (3-i)] = Re[6 - 2i + 3i - i^2] = Re[6 + 1i - (-1)] = 7
# Let the 4 positive numbers be w, x, y, and z such that:
w*x=2,  x*y=2.4,  w*y=3,  x*z=4,  z*w=5,  y*z=6,  and  w*x*y*z=12.
# Therefore, we have the following:
w=2/x and w=3/y, so w^2=(2/x)*(3/y)=6/(x*y)=6.0/2.4=30/12=5/2=2.5;
so w=ˆš(2.5), x=2/w=ˆš(4)/ˆš(2.5)=ˆš(4.0/2.5)=ˆš(8/5)=ˆš(1.6),
y=2.4/x=2.4/ˆš(1.6)=2.4/ˆš(16*0.1)=2.4/[ˆš(16)*ˆš(0.1)]=2.4/[4*ˆš(0.1)],
so y=0.6/ˆš(0.1)=ˆš(0.36)/ˆš(0.1)=ˆš(0.36/0.1)=ˆš(0.36*10)=ˆš(3.6), and
z=4/x=ˆš(16)/ˆš(1.6)=ˆš(16/1.6)=ˆš(10*1.6/1.6)=ˆš(10);
so our full answer is: (w, x, y, z) = (ˆš[2.5], ˆš[1.6], ˆš[3.6], ˆš[10]);
or as multiples of ˆš[10]; (w, x, y, z) = ˆš[10] * (0.5, 0.4, 0.6, 1).
# Integral from 0 to Ï€/4 of 1/ln(tanx)  +  (1+tanx) / (1-tanx) dx:
# Integral from 1 to inf of arctan(x) / x² dx:
# Find all functions such that:
f(-x) = f(x-1)
# Integrate arctan(x) * arccos(x) from 0 to 1:
# Sequence question:
Given a_(n+2)=a_n + 1/a_(n+1), a_1=a_2=1, find a_2013:
# Calculation of an example of a 2x2 non-diagonalizable matrix exponential:
A = +1 +1  A² = +1 +1  +1 +1 = +0 +0
    -1 -1        -1 -1  -1 -1   +0 +0
e^A = ˆ‘(n=0 to ˆž of A^n /n!) = I/0! + A/1! + A^2/2! + ...
e^A = I/1 + A/1 + 0/2 + ... = I + A = +1 +0  +  +1 +1 = +2 +1
                                      +0 +1     -1 -1   -1 +0
P = +1 +1
    -1 +0
P^-1 = +0 -1
       +1 +1
D = P^-1 * A * P = +0 -1   +1 +1   +1 +1   =   +0 -1   +0 +1 = +0 +1
                   +1 +1   -1 -1   -1 +0       +1 +1   +0 -1   +0 +0
D² = +0  +1   +0 +1   =   +0 +0
      +0  +0   +0 +0       +0 +0
e^D = ˆ‘(n=0 to ˆž of D^n /n!) = I/0! + D/1! + D^2/2! + ...
e^D = I/1 + D/1 + D^2/2 + ... = +1 +0  +  +0 +1  +  +0 +0  + ...
                                +0 +1     +0 +0     +0 +0
e^D = +1 +1 so e^A = P e^D P^-1 = +1 +1   +1 +1   +0 -1
      +0 +1                       -1 +0   +0 +1   +1 +1
e^A = +1 +1   +1 +0  =  +2 +1
      -1 +0   +1 +1     -1 +0
# 11th root of unity:
z^11 = 1
A = (z^10 + z^8 + z^7 + z^6 + z^2)
B = (z + z^3 + z^4 + z^5 + z^9)
AB = 
# Algebra from geometry:
b = Ï€ / (2+ˆš2)^2
x = [2ab-a] / [2(b-1)] 
==> x = [Ï€-2ˆš2-3] a / [Ï€-4ˆš2-6]
r = [a-x] / [2+ˆš2]
==> r = [2+2ˆš2] a / [12+8ˆš2-Ï€]
# Area = x = 1 + Ï€/3 - ˆš(3) by geometry and x = 1 + Ï€/3 - ˆš(3) by calculus:
1 + x + 2y = Ï€/4 + Ï€/4, so A = x + 2y = Ï€/2 - 1 and
Leg of right triangle = a = ˆš(1² - (1/2)^2) = ˆš(1 - 1/4) = ˆš(3/4) = ˆš(3)/2
Since that triangle is equilaterial, then Î¸ = 60 deg = Ï€/3 rad.
B = x + 2y + z = (Ï€/3)*1/2 + (Ï€/3)*1/2 - (1*ˆš(3)/2)/2 = Ï€/3 - ˆš(3)/4,
so z = B - A = Ï€/3 - ˆš(3)/4 - (Ï€/2 - 1) = 2Ï€/6 - ˆš(3)/4 - 3Ï€/6 + 1
z = 1 - ˆš(3)/4 - Ï€/6, so C = x + 4y = 1 - 4z = 1 - 4 * (1 - ˆš(3)/4 - Ï€/6)
C = x + 4y = 1 - 4 + ˆš(3) + 4Ï€/6 = ˆš(3) + 2Ï€/3 - 3
x = 2 * (x + 2y) - (x + 4y) = 2A - C = 2 * (Ï€/2 - 1) - (ˆš(3) + 2Ï€/3 - 3)
x = Ï€ - 2 - ˆš(3) - 2Ï€/3 + 3 = 1 + 3Ï€/3 - ˆš(3) - 2Ï€/3 = 1 + Ï€/3 - ˆš(3)
# Elliptic equation:
Given x = a*cos(Î¸), y = b*sin(Î¸), 36x²y - 27y³ = 8, and 8x³ - 54xy² = 8,
prove (2x)² + (3y)² = (2^{7/6})² and y = 2*tan(Î¸)*x/3:
First, we have y = x*(y/x) = x*b*sin(Î¸)/{a*cos(Î¸)} =  b*tan(Î¸)*x/a, so
proving y = 2*tan(Î¸)*x/3 is equivalent to proving that b/a = 2/3.
Next, 
# Find all integers n for which x² - x + n divides x^13 + x + 90.
# Prove or disprove that are infinitely many primes p1 and p2 such as: 
p1 +(the sum of digits of p1) = p2  ex.: 13+(1+3)=17, 307 + (3+0+7)=317
# Integrate [Cos^-1x (ˆš1-x^2)]^-1 / Log(1+(sin(2xˆš1-x^2)/Ï€):
# Prove ˆ(k=0 to nˆ’1) sin(x+kÏ€/n) = sin(nx)/[2^(n-1)]
# Solve x^y + y^z = z^x for the integers:
# Solve   x"+a*x=b*cos(w*t+j)   x=x(t), a,b,w, and j are constants
# Find the integral of sin(x^2) as x goes from 0 to ˆž
# Find the integral of (x arcsec(x^2)/(x² ˆš(x^4 - 1))
# Integration of 1/[1+tan^(5)x]:
# Suggestion is from IMO 1997 short list.
# Do there exist functions f and g (both R -> R) such that:
# 1. f(g(x))=x² and g(f(x))=x^3 for all x in R ?
# 2. f(g(x))=x² and g(f(x))=x^4 for all x in R ?
# Homework: Choose three random real numbers X1, X2 and X3 
# from the interval [0;1], independently of each other. 
# 1. What is the probability that X1 is stricly bigger than X2 + X3? 
# 2. In general, what is the probability that the largest of the 
# three random numbers is strictly greater than the sum of the other two
# 3. Bonus (the source only gives the answer but not the whole explanation) : 
# for X1, X2... Xn chosen in the same conditions (n bigger or equal than 2),
# what is the probability that X1 > X2 + ... + Xn?
# How can you get 6 from 4 and 9?
fill up the 9
fill up the 4 with the 9
now you have 4 in the 4 and 5 in the 9
spill out the 4
fill up the 4 with the 9 again
now you have 4 in the 4 and 1 in the 9
spill out the 4 again
fill up the 4 with the 9 yet again
now you have 1 in the 4 and 0 in the 9
fill up the 9 again
fill up the 4 with the 9 yet again
now you have 4 in the 4 and 6 in the 9
and yay, we are finally done!
# For n ˆˆ N, when is f(n) = n´ - n³ + 3n² + 5 a perfect square?
First, if we let m = 2n² - n + 2, then we get:
m² = (2n² - n + 2)² = (2n² - n + 2) * (2n² - n + 2)
= 4n´ - 2n³ + 4n² - 2n³ + n² - 2n + 4n² - 2n + 4
= 4n´ - 4n³ + 9n² - 4n + 4
= (4n´ - 4n³ + 12n² + 20) + (-3n² - 4n - 16)
= 4 * (n´ - n³ + 3n² + 5) - (3n² + 4n + 16)
= 4*f(n) - g(n), so 4*f(n) = m² + g(n),
where g(n) = 3n² + 4n + 16, which is > 0 for all n >= 1,
so 4*f(n) is always greater than (>) the perfect square m².
(m+1)² = m² + 2m + 1 = (4n´ - 4n³ + 9n² - 4n + 4) + 2(2n² - n + 2) + 1
= 4n´ - 4n³ + 9n² - 4n + 4 + 4n² - 2n + 4 + 1 = 4n´ - 4n³ + 13n² - 6n + 9
= (4n´ - 4n³ + 12n² + 20) + (n² - 6n - 11)
= 4 * (n´ - n³ + 3n² + 5) + (n² - 6n - 11)
= 4*f(n) + h(n), so 4*f(n) = (m+1)² - h(n), where 
h(n) = n² - 6n - 11 = (n² - 6n - 16) + 5 = (n-8) * (n+2) + 5,
which is >= 5, which > 0, for all n >= 8, so 4*f(n) is 
less than (<) the perfect square (m+1)² for all n >= 8.
Therefore, 4*f(n) is never a perfect square for any and all n >= 8,
and it follows that f(n) is also never a perfect square for all n >= 8,
but we still need to check n = 1, 2, 3, 4, 5, 6, and 7:
For n = 1, we get f(1) = 1´ - 1³ + 3*1² + 5 = 1 - 1 + 3 + 5 = 8,
which is not a perfect square, so n = 1 is not a solution.
For n = 2, we get f(2) = 2´ - 2³ + 3*2² + 5 = 16 - 8 + 12 + 5 = 25,
which is a perfect square, so n = 2 is a solution.
For n = 3, we get f(3) = 3´ - 3³ + 3*3² + 5 = 81 - 27 + 27 + 5 = 86,
which is not a perfect square, so n = 3 is not a solution.
For n = 4, we get f(4) = 4´ - 4³ + 3*4² + 5 = 256 - 64 + 48 + 5 = 245,
which is not a perfect square, so n = 4 is not a solution.
For n = 5, we get f(5) = 5´ - 5³ + 3*5² + 5 = 625 - 125 + 75 + 5 = 580,
which is not a perfect square, so n = 5 is not a solution.
For n = 6, we get f(6) = 6´ - 6³ + 3*6² + 5 = 1296-  216 + 108 + 5 = 1193,
which is not a perfect square, so n = 6 is not a solution.
For n = 7, we get f(7) = 7´ - 7³ + 3*7² + 5 = 2401 - 343 + 147 + 5 = 2210,
which is not a perfect square, so n = 7 is not a solution.
Therefore, finally we can conclude that n = 2 is the only solution,
that is, it is the only n for which f(n) is a perfect square.
# If we define j such that j² = +1, but j ˆ‰ {-1, 1}, then we get:
(a+bj)*(c+dj) = ac+adj+bcj+bd*(j^2) = ac+(ad+bc)*j+bd*1 = (ac+bd)+(ad+bc)j
and
(a+bj) * (a-bj) = a² - abj + abj - (j^2)*(b^2) = a² - 1*b² = a² - b^2
# Let Î±,Î²ˆˆQ* & find all functions f from R->R s.t. f([x+y]/Î±)=[f(x)+f(y)]/Î²:
Note that for x=y=0: f(0)=f([0+0]/Î±)=[f(0)+f(0)]/Î²=2f(0)/Î²,
so f(0) must be 0, but also for x=t and y=-t:
f(0)=f([t+(-t)]/Î±)=[f(t)+f(-t)]/Î²=0, so f(-t)=-f(t) for all 
t ˆˆ R, so f is an odd function. Furthermore, for x=Î±t and y=0:
f(t)=f(Î±*t/Î±)=f([Î±*t+0]/Î±)=[f(Î±*t)+f(0)]/Î²=f(Î±*t)/Î²,
so ^^^f(Î±*t)=Î²*f(t)^^^ for all t ˆˆ R, and also for x=y=Î±*t:
2*f(Î±*t)/Î²=[f(Î±*t)+f(Î±*t)]/Î²=f([Î±*t+Î±*t]/Î±)=f(2*Î±*t/Î±)=f(2*t),
so 2*f(Î±*t)=Î²*f(2*t) for all t ˆˆ R, but with ^^^, we have:
2*Î²*f(t)=2*f(Î±*t)=Î²*f(2*t), so 2*f(t)=f(2*t) for all t ˆˆ R,
but t is just a dummy variable, so we can replace t with x:
2*f(x)=f(2*x) for all x ˆˆ R, but this implies that if we take
f(x)=its infinite series=ˆ‘(n>=1){c_(2*n+1)*x^(2*n+1)},[since
f(x) is odd (see above), all the even terms are 0], we have:
2*ˆ‘(n>=0){c_(2*n+1)*x^(2*n+1)}=2*c_1*x+2*c_3*x^3+... =
c_1*(2*x)+c_3*(2*x)^3+...=ˆ‘(n>=1){c_(2*n+1)*(2*x)^(2*n+1)},
so 2*c_1*x+2*c_3*x^3+... = 2*c_1*x+8*c_3*x^3+..., but
since 2=/=8, and in general 2=/=2^(2*n+1) for all n>=1, then
2*c_3*x^3=/=8*c_3*x^3 unless c_3=0, and in general
2*c_(2*n+1)*x^(2*n+1)=/=2^(2*n+1)*c_(2*n+1)*x^(2*n+1)
for all n>=1 unless c_(2*n+1)=0, but the 1st term works out,
since 2*c_1*x = 2*c_1*x for all c_1 ˆˆ R. Since c_1 is just
a dummy variable, then we can replace it by c, so we have:
f(x)=c*x, where c ˆˆ R, but we must find all c that work with
c * [x+y] / Î± = f([x+y]/Î±) = [f(x)+f(y)]/Î² = [c*x + c*y] / Î²,
so c * (x + y) / Î± = c * (x + y) / Î², so either Î± = Î², or c=0.
Therefore, all functions f from R to R that satify 
f([x+y]/Î±) = [f(x)+f(y)]/Î², are the following:
f(x) = c*x, with c ˆˆ R and Î±=Î², OR with c=0 and Î±=/=Î²
S = 1/(1*2)+1/(3*4)+...+1/(49*50)
T = 1/(51*100)+1/(52*99)+...+1/(100*51)
S/T = ???
log[-2](-5) = ln(-2) / ln(-5)
= [ln(2)+i(2m+1)Ï€] / [ln(5)+i(2n+1)Ï€] w/ m,n ˆˆ Z
= [ln(2)+i(2m+1)Ï€]*[ln(5)-i(2n+1)Ï€] / 
                [ln(5)+i(2n+1)Ï€]*[ln(5)-i(2n+1)Ï€]
= [ln(5)ln(2)+i(2m+1)ln(5)Ï€-i(2n+1)ln(2)Ï€+
    i^2(2m+1)(2n+1)Ï€^2]/[(ln(5))^2-i^2(2n+1)^2Ï€^2]
= [ln(5)ln(2)+i*Ï€*[(2m+1)ln(5)-(2n+1)ln(2)]-
          (2m+1)(2n+1)*Ï€^2]/[(ln(5))^2+(2n+1)^2Ï€^2]
=[ln(5)ln(2)-(2m+1)(2n+1)Ï€^2]/[ln(5)^2+[(2n+1)Ï€]^2]
+i*Ï€[(2m+1)ln(5)-(2n+1)ln(2)]/[ln(5)^2+[(2n+1)Ï€]^2]
However, with m and n both = 0, we have 2m+1 and
2n+1 both = 1, and the above
= [ln(5)ln(2)-Ï€^2] / [ln(5)^2+Ï€^2] + 
        i * Ï€ * [ln(5)-ln(2)] / [ln(5)^2+Ï€^2]
‰ˆ ˆ’0.702576321372 + 0.231030219689i
integral of {(e^x)(x-1)}/{x(x+e^x)} dx from 1 to 2
u = x(x+e^x) and du = (x+e^x+x(1+e^x)) dx
    du = (x+e^x+x+x*e^x) dx = (2x+(e^x)(x+1)) dx
    du = ((e^x)(x-1+2)+2x) dx
    du = ((e^x)(x-1)+2*e^x+2x) dx
    du = ((e^x)(x-1)+2*(e^x+x) dx,
    so line 1 above is equal to:
integral of {[(e^x)(x-1)+2*(e^x+x)]-2*(e^x+x)}/
    {x*(x+e^x)} dx from 1 to 2
integral of du/u from x=1 to x=2 - integral of 
    {2*(e^x+x)}/{x*(x+e^x)} dx from 1 to 2 = 
ln|u| from x=1 to x=2 - integral of 2/x from 1 to 2
= ln|x*(x+e^x)| - 2*ln|x| from x=1 to x=2, but we
can remove the absolute values since x ˆˆ [1,2] > 0,
so the above = ln(x^2+x*e^x) - ln(x^2) from 1 to 2
= ln({x^2+x*e^x}/{x^2}) from 1 to 2
= ln(1+[(e^x)/x]) from 1 to 2
= ln(1+[(e^2)/2]) - ln(1+[(e^1)/1])
= ln([2+e^2]/2) - ln(1+e)
= ln(2+e^2)-ln(1+e)-ln(2) ‰ˆ 0.23313589814371605
Let f: [0,1] --> |R be a function s. t. the following
hold: 1) It is non-decreasing, 2) f(x/3) = f(x)/2, & 
3) f(1-x) = 1-f(x), so, from repeated application 
of 2) above, we get: 4) f(x/3^n) = f(x) / 2^n, where 
n ˆˆ |N (with n >= 1). From 4) above, we get f(0) = 
f(0/3^n) = f(0)/2^n = 0. From 3) above, we get f(1) =
f(1-0) = 1-f(0) = 1-0 = 1. So, since f(1) = 1, we 
get: f(1/3^n) = f(1)/2^n = 1/2^n, and from 3) above, 
we get: 5) f(1-1/3^n) = 1-f(1/3^n) = 1-(1/2^n)
Now, if we take n to be = to 1, then f(1/3)=f(1/3^1)=
1/2^1=1/2=1-1/2=1-(1/2^1)=1-f(1/3^1)=f(1-1/3^1)=
f(1-1/3)=f(2/3), so 1/2 = f(1/3) <= f(x) <= f(2/3) = 
1/2 for all x ˆˆ [1/3,2/3], from 1) above, so 6) f(x)
= 1/2 for all x ˆˆ [1/3,2/3]. From 4) and 6) above, 
we have 7) f(x/3^(n-1)) = 0.5/2^(n-1) for all x ˆˆ 
[1/3,2/3] and all n ˆˆ |N (s. t. n >= 1). From 5) &
7) above, we have 8) f(1-x/3^(n-1)) = 1-0.5/2^(n-1)
for all x ˆˆ [1/3,2/3] and all n ˆˆ |N (s. t. n >= 1)
From 2), 3), and 6) above, we also have:
f((x+2)/3) = f(x/3+2/3) = f(1-1/3+x/3) = 
f(1-(1/3-x/3)) = 1-f(1/3-x/3) = 1-f((1-x)/3) =
1-f(1-x)/2 = 1-(1-f(x))/2 = 1 - (1/2 - f(x)/2) = 
1 - 1/2 + f(x)/2 = 1/2 + f(x)/2 = (1+f(x))/2
# Let x and y be integers such that x^3 = y^3 + 2x + 1:
Find all such ordered pairs of integers (x,y):
First, if y >= 0, then we have x^3 = y^3 + 2*y + 1, 
but if y <= 0, then x^3 = y^3 + 2*y + 1 implies that
-x^3 = -y^3 - 2*y - 1, so (-x)^3 = (-y)^3 + 2*(-y) 
- 1. So, both x and y have symmetry such that, 
with X=|x| & Y=|y|, X^3 = Y^3 + 2*Y +or- 1, which is 
strictly > Y^3, so X must be strictly > Y, 
since X^3 and Y^3 are the same increasing function, 
just with different variables, so let X = Y + Z, 
where Z is an integer strictly > 0, so that:
X^3 = (Y+Z)^3 = Y^3 + 2Y +or- 1
Y^3 + 3Y^2*Z + 3Y*Z² + Z^3 = Y^3 + 2Y +or- 1
3Y^2*Z + 3Y*Z² - 2Y + Z^3 -or+ 1 = 0
3Z*Y² + (3Z^2-2)*Y + (Z^3-or+1) = 0
Y={-(3Z^2-2)+or-ˆš[(3Z^2-2)^2-4*3Z*(Z^3-or+1)]}/{2*3Z}
Y = {(2-3Z^2)+or-ˆš[9Z^4-12Z^2+4+or-12Z-12Z^4]}/{6Z}
Y = {(2-3Z^2)+or-ˆš[-3Z^4-12Z^2+or-12Z+4]}/{6Z}, but 
now, since Y must be an integer, it cannot be a 
complex number, so the discriminant (D) must be >= 0,
& D = D+ or D- = -3*Z^4 - 12*Z² +or- 12*Z + 4 must 
be >= 0. If Z = 1, then D+ = -3*1^4 - 12*1² + 12*1
+ 4 = -3 - 12 + 12 + 4 = 1, which is >= 0, so we are
good there, but D- = -3*1^4 - 12*1² - 12*1 + 4 = 
-3 - 12 - 12 + 4 = -23, which is < 0, so Z can be = 1
for D+, but it cannot = 1 for D-. However, if Z >= 2,
then we have: The first term of D is -3*Z^4 <= -3*2^4 
= -3*(2^2)*(2^2) = -3*4*(2^2) = -12*Z^2, and the last 
term of D is 4 <= 2*2 = 2*Z, so the entire number D 
is such that D <= -12*Z² - 12*Z² +or- 12*Z + 2*Z, 
so D- <= -24*Z² - 10*Z <= D+ <= -24*Z² + 14*Z =
-2*Z*(12*Z-7) <= -2*2*(12*2-7) = -4*(24-7) = -4*17 =
-68 < 0 for all Z >= 2. Therefore, Z must NOT be >= 
2, so Z must be strictly < 2, so, since Z is an 
integer strictly > 0, then Z must = 1. Therefore, 
from the above, we have D = 1 and Z = 1, so
Y = {(2-3Z^2)+or-ˆšD}/{6Z} = {(2-3*1^2)+or-ˆš1}/{6*1}
Y = (2-3*1+or-1)/6 = (2-3+or-1)/6
Y = (-1+1)/6 or (-1-1)/6 = 0/6 or -2/6 = 0 or -1/3,
but -1/3 is NOT an integer >= 0, so Y must = 0,
so X = Y + Z = 0 + 1 = 1, but since X = |x| and 
Y = |y|, then x must = 1 and/or -1, and y must = 0.
If we plug the ordered pair (x,y) = (1,0) into our
original equation, then we have:
1 = 1^3 = x^3 ?=? y^3 + 2*y + 1 = 0^3 + 2*0 + 1
1 ?=? 0 + 0 + 1 = 1, so yes, (1,0) is a solution.
However, if we plug the ordered pair (x,y) = (-1,0) 
into our original equation, then we have:
-1 = (-1)^3 = x^3 ?=? y^3 + 2*y + 1 = 0^3 + 2*0 + 1
-1 ?=? 0 + 0 + 1 = 1, so NO, (-1,0) is NOT a solution.
In conclusion, the first, last, and ONLY solution to
this problem is (x,y) = (1,0).
Let s(n) denote the sum of the digits of a positive 
integer n in base 10. If s(m) = 20 and s(33m) = 120;
what is the value of s(3m)?
Assume that m = 11,111,111,111,111,111,111; since 
that is the longest number with no zeros; and whose 
digit sum is 20. So, 3m = 33,333,333,333,333,333,333
and from there it follows that: 33m = 11*(3m) = 
366,666,666,666,666,666,663; and the sum of the 
digits of this number is indeed 120; so the number 
above for 3m is correct; so the value of s(3m) is 60.
If a = c*r and b = c/r, then: __                 __
ab = c*r * c/r = c^2, so c = ˆšab, & r = a/c = a/ˆšab,
        _  _    _____
so r = ˆša/ˆšb = ˆš(a/b)
I = integral [ln(x)/(x^2+1)] dx from 0 to 1 = I(1)
= integral [ln(tx) / (x^2+1)] dx from 0 to 1 when
t is 1, so I'(t) = integral [x/(tx)/(x^2+1)] dx from
0 to 1 = integral [t/(x^2+1)] dx from 0 to 1 = 
t*arctan(x) from 0 to 1 = t*((Ï€/4)-0) = Ï€*t/4, so
I = I(1) = integral [I'(t)] dt when t is 1 =
integral [Ï€*t/4] dt when t is 1 = Ï€*t^2/8 + C
when t is 1 = Ï€*1^2/8 + C ‰ˆ Ï€/8 - 1.308664675876
Given f(a + b/2) >= f(a) + f(b/2) for any a and b > 0 
and f(x) is increasing, find f(x) and f(1):
First, notice the following:
with a=1/2 and b=1, f(1)=f(1/2+1/2)>=f(1/2)+f(1/2)=2*f(1/2), and
with a=1 and b=2, f(2)=f(1+2/2)>=f(1)+f(2/2)=f(1)+f(1)=2*f(1), 
so f(1)>=2*f(1/2) and f(2)>=2*f(1), so 2*f(1/2)<=f(1)<=f(2)/2.
Let's assume that f(x)=c*x+d, with c>0 to keep it increasing, so
2*(c*(1/2)+d)<=c*1+d<=(c*2+d)/2, so c+2d<=c+d<=c+d/2, so d must
be <= 0, so with -d = d`>=0, we have f(x)=c*x-d`, and f(1)=c-d`
exp(x)*exp(y)=sum(x^k/k! for k=0 to ˆž)*sum(y^m/m! for m=0 to ˆž)
=(1+x+x^2/2+x^3/6+x^4/24+...+x^k/k!+...)*
    (1+y+y^2/2+y^3/6+y^4/24+...+y^m/m!+...)
=(1*1+1*y+1*y^2/2+1*y^3/6+1*y^4/24+...+1*y^m/m!+...)+
(x*1+x*y+x*y^2/2+x*y^3/6+x*y^4/24+...+x*y^m/m!+...)+
(x^2*1/2+x^2*y/2+x^2*y^2/(2*2)+...+x^2*y^m/(2*m!)+...)+...+
(x^k*1/k!+x^k*y/k!+x^k*y^2/(k!*2)+...+x^k*y^m/(k!*m!)+...)+...
=sum(sum(x^k*y^m/(k!*m!) for k=0 to ˆž) for m=0 to ˆž)
exp(x+y)=sum((x+y)^k/k! for k=0 to ˆž)=1+(x+y)^1/1+(x+y)^2/2+
    (x+y)^3/6+(x+y)^4/24+...+(x+y)^k/k!+...
=1+x+y+x^2/2+2xy/2+y^2/2+x^3/6+3*x^2*y/6+3x*y^2/6+y^3/6+x^4/24+
    4*x^3*y/24+6*x^2*y^2/24+4x*y^3/24+y^4/24+...+(x+y)^k/k!+...
=[x^0*y^0/(1*1)+x^0*y^1/(1*1)+x^0*y^2/(1*2)+x^0*y^3/(1*6)+x^0*
    y^4/(1*24)+...+x^0*y^n/(0!*n!)+...]+[x^1*y^0/(1*1)+x^1*y^1/
    (1*1)+...+x^1*y^2/(1*2)+x^1*y^3/(1*6)+...+x^1*y^(n-1)/(1!*
    (n-1)!)+...]+[x^2*y^0/(2*1)+x^2*y^1/(2*1)+x^2*y^2/(2*2)+...+
    x^2*y^(n-2)/(2!*(n-2)!)+...]+[x^3*y^0/(6*1)+x^3*y^1/(6*1)+
    ...+x^n*y^(n-3)/(3!*(n-3)!)+...]+[...]+[x^k*y^0/(k!*1)+x^k*
    y^1/(k!*1)+x^k*y^2/(k!*2)+...+x^k*y^(n-k)/(k!*(n-k)!)+...]+
    [...], and 1/[k!*(n-k)!]=n!/[k!*(n-k)!]/n!=(n k)/n!, so 
exp(x+y)=sum(sum((n k)*x^k*y^(n-k)/n! for k=0 to ˆž) for n=k to ˆž)
exp(x+y)=sum(sum((n k)*x^k*y^(n-k)/n! for k=0 to ˆž) for n=k to ˆž)
=sum(sum([n!/(k!*(n-k)!)]*x^k*y^(n-k)/n! for k=0 to ˆž) for n=k to
ˆž)=sum(sum(x^k*y^(n-k)/[k!*(n-k)!] for k=0 to ˆž) for n=k to ˆž)
sum(sum(x^k*y^(n-k)/(k!*(n-k)!) for k=0 to ˆž) for n-k=0 to ˆž),
so note that if we just replace n-k with m, then the above =
sum(sum(x^k*y^m/(k!*m!) for k=0 to ˆž) for m=0 to ˆž)=exp(x)*exp(y)
Yes, this will work for complex numbers, but for matrices, x and
y both must be square matrices, since that is the only way that
we can multiply a matrix by itself. However, since in general 
matrices don't commute, meaning AB most of the time =/= BA, then
this identity [exp(A+B)=exp(A)*exp(B)] generally won't work for 
matrices, but it will work for matrices when A = z*B, where z is 
any complex number, and A and B are both matrices.
f(x+y) = a*e^[b*(x+y)] = a*e^[b*(x)] * a*e^[b*(y)] = f(x) * f(y),
so a = a² --> a = 0 or 1 and b = any complex number
(m+n)!=m!(m+1)(m+2)...(m+n-1)(m+n)>=m!*1*2*...*(n-1)*n=m!n!
Find the inverse matrix formula for a 2x2 matrix A w/ detA=/=0:
        [a b]                  [w x]
Let A = [c d], and find A^-1 = [y z] such that A*A^-1=A^-1*A=I:
So, we have the following, when det(A) is =/= 0:
[a b]   [w x]   [a*w+b*y a*x+b*z]   [1 0]
[c d] * [y z] = [c*w+d*y c*x+d*z] = [0 1], so:
a*w = 1 - b*y, a*x = -b*z, c*w = -d*y, and c*x = 1 - d*z, so
a*d*w = d - b*d*y = d + b*c*w --> a*d*w - b*c*w = d -->
w * (a*d - b*c) = w * det(A) = d, so w = d / det(A)
b*c*x = b - b*d*z = b + a*d*x --> -b = a*d*x - b*c*x = 
x * (a*d - b*c) = x * det(A) = -b, so x = -b / det(A)
c*w = c*d/det(A) = -d*y --> y = -c / det(A)
a*x = -a*b/det(A) = -b*z --> z = a / det(A), so:
       [w x]   [d -b]            [d -b]
A^-1 = [y z] = [-c a] / det(A) = [-c a] / (a*d - b*c)
            x² + 1                     1 + 1/x²              
integral ------------- dx=integral --------------- dx=integral 
         x^4 - x² + 1             x² - 1 + 1/x²             
[1-(-1/x^2)] dx          d(x - 1/x)/dx                     
---------------=integral---------------dx=arctan(x-1/x)+C1 
 x^2-2+1/x^2+1          (x - 1/x)² + 1                    
With y = x^2, x^4 - x² + 1 = y² - y + 1 = (y - y1) * (y - y2), 
where y1 = [-(-1) + ˆš((-1)² - 4 * 1 * 1)] / [2 * 1] = (1 + 
ˆš(1 - 4)) / 2 = (1 + ˆš(-3)) / 2 = (1 + i * ˆš3) / 2 
and y2 = (1 - i * ˆš3) / 2. Also, if a + b*i = (c + i*d)^2, then 
a + i*b = c² + 2*i*c*d + (i*d)² = (c^2-d^2) + i*(2*c*d), so 
a = c² - d^2, b = 2*c*d, d = b / (2*c), a = c^2-(b/2c)² = c² 
- b² / 4*c^2, a * c² = c^4 - b² / 4, c^4 - a*c² - b^2/4 = 0, 
(just taking the + result) c^2=[-(-a)+ˆš((-a)^2-4*1*(-b^2/4))]/
[2*1] = [a + ˆš(a² + b^2)] / 2, c = ˆš[a + ˆš(a² + b^2)] / ˆš2, d=
b / (2*ˆš[a + ˆš(a² + b^2)]/ˆš2) = b/(ˆš2 * ˆš[a + ˆš(a² + b^2)]),
c = t / ˆš2, and d = b / (t * ˆš2), where t = ˆš[a + ˆš(a² + b^2)],
so  ˆš(-1+i*ˆš3)=t/ˆš2+i*ˆš3/(t*ˆš2), where t=ˆš[-1+ˆš((-1)^2+(ˆš3)^2)]
= ˆš[-1+ˆš(1+3)] = ˆš(-1+ˆš4) = ˆš(-1+2) = ˆš1 = 1, so ˆš(-1+i*ˆš3) = 
1/ˆš2+i*ˆš3/(1*ˆš2)=(1+i*ˆš3)/ˆš2, ˆš(-1-i*ˆš3)=(1-i*ˆš3)/ˆš2, and:
            x² + 1         
integral ------------- dx = integral 
         x^4 - x² + 1      
                   x² + 1                            
--------------------------------------------------- dx = 
(x² - (1 + i * ˆš3) / 2) * (x² - (1 - i * ˆš3) / 2)      
          [(1+i*ˆš3)/2+1]/[(1+i*ˆš3)/2-(1-i*ˆš3)/2]   
integral (-------------------------------------- + 
                 x² + (- 1 - i * ˆš3) / 2          
                [(1-i*ˆš3)/2+1]/[(1-i*ˆš3)/2-(1+i*ˆš3)/2]       
                --------------------------------------) dx = 
                       x² + (- 1 + i * ˆš3) / 2              
          [(1+i*ˆš3)/2+1]/[i*ˆš3]   [(1-i*ˆš3)/2+1]/[-i*ˆš3]       
integral (--------------------- + ----------------------) dx = 
             x^2+(-1-i*ˆš3)/2      x² + (- 1 + i*ˆš3) / 2       
[(1+i*ˆš3)/2+1] * arctan[(x*ˆš2)/ˆš(-1-i*ˆš3)]   
------------------------------------------ - 
         i * ˆš3 * ˆš(-1-i*ˆš3)/ˆš2              
                  [(1-i*ˆš3)/2+1]*arctan[(x*ˆš2)/ˆš(-1+i*ˆš3)]   
                  ---------------------------------------- = 
                           i * ˆš3 * ˆš(-1+i*ˆš3)/ˆš2            
[(1+i*ˆš3)/2+1]*arctan[(x*ˆš2)/[(1-i*ˆš3)/ˆš2]]   
------------------------------------------- - 
            i*ˆš3*(1-i*ˆš3)/ˆš2/ˆš2               
             [(1-i*ˆš3)/2+1]*arctan[(x*ˆš2)/[(1+i*ˆš3)/ˆš2]]   
             ------------------------------------------- = 
                         i*ˆš3*(1+i*ˆš3)/ˆš2/ˆš2               
[(1+i*ˆš3)/2+1]*arctan[2*x/(1-i*ˆš3)]           
----------------------------------- - 
            i*ˆš3*(1-i*ˆš3)/2                   
                     [(1-i*ˆš3)/2+1]*arctan[2*x/(1+i*ˆš3)]   
                     ----------------------------------- = 
                                 i*ˆš3*(1+i*ˆš3)/2           
[(1+i*ˆš3)+2]*arctan[2*x/(1-i*ˆš3)]   
--------------------------------- - 
        i*ˆš3-(i*ˆš3)²               
                     [(1-i*ˆš3)+2]*arctan[2*x/(1+i*ˆš3)]   
                     --------------------------------- = 
                                  i*ˆš3+(i*ˆš3)²          
(3+i*ˆš3)*arctan[2*x/(1-i*ˆš3)]   (3-i*ˆš3)*arctan[2*x/(1+i*ˆš3)]   
----------------------------- - ----------------------------- = 
        i*ˆš3-(-3)                        i*ˆš3+(-3)              
(3+i*ˆš3)*arctan[2*x/(1-i*ˆš3)]   (3-i*ˆš3)*arctan[2*x/(1+i*ˆš3)]   
----------------------------- - ----------------------------- = 
        i*ˆš3+3                            i*ˆš3-3                
arctan[2*x*(1+i*ˆš3)/(1-i*ˆš3)*(1+i*ˆš3)] + arctan[2*x*/(1+i*ˆš3)] = 
arctan[2*x*(1+i*ˆš3)/(1^2+(ˆš3)^2)] + arctan[2*x*/(1+i*ˆš3)] = 
arctan[2*x*(1+i*ˆš3)/(1+3)] + arctan[2*x*/(1+i*ˆš3)] = 
arctan[2*x*(1+i*ˆš3)/4] + arctan[2*x*/(1+i*ˆš3)] = 
arctan[(1+i*ˆš3)*x/2] + arctan[2*x*/(1+i*ˆš3)] + C2***
if A = (1 + i*ˆš3) / 2 = cos(Ï€/3) + i*sin(Ï€/3) = e^(i*Ï€/3),
then *** is the following:
arctan(A*x) + arctan(x/A) + C2 ?=? arctan(x - 1/x) + C1
arctan(e^(i*Ï€/3)*x)+arctan(e^(-i*Ï€/3)*x)+C2?=?arctan(x-1/x)+C1
arctan(A*x) + arctan(x/A) = arctan[(A*x+x/A)/(1-x^2)] = 
arctan[x*(A+1/A)/(1-x^2)], with A+1/A = (1+i*ˆš3)/2 + 2/(1+i*ˆš3)=
(1+i*ˆš3)^2/2/(1+i*ˆš3) + 4/(1+i*ˆš3)/2 = 
[(1+2*i*ˆš3-3)+4]/[2*(1+i*ˆš3)] = (2*i*ˆš3+2)/[2*(1+i*ˆš3)] = 1, so
*** = arctan[x/(1-x^2)] + C2 ?=? arctan(x - 1/x) + C1
+/-Ï€/2 - arctan[(1-x^2)/x] + C2 ?=? arctan(x - 1/x) + C1
+/-Ï€/2 - arctan(1/x - x) + C2 ?=? arctan(x - 1/x) + C1
+/-Ï€/2 + arctan(x - 1/x) + C2 ?=? arctan(x - 1/x) + C1
The above is true for all C2 = C1 -/+ Ï€/2, - for all
x >= 0, but + for all x < 0.
USING THE 3-4-5 TRIANGLE:
integral{25/(3cosx+4sinx)^2}dx=integral{[5/(3cosx+4sinx)]^2}dx***
    |\
    | \
    |  \
    |   \
    |    \
    |     \         t = arctan(4/3), cos(t) = 3/5, and sin(t) = 4/5
 4  |      \  5
    |       \
    |        \
    |         \   
    |_         \
    |_|_______t_\
          3
*** = integral{1/[cos(t)cos(x)+sin(t)sin(x)]^2}dx
= integral{1/[cos(x)cos(t)+sin(x)sin(t)]^2}dx
= integral{1/cos^2(x-t)} = integral{sec^2(x-t)}dx
= tan(x-t) = tan(x-arctan(4/3)) + C1
USING TANGENT AND U-SUBSTITUTION:
integral{25/(3cosx+4sinx)^2}dx
= 25*integral{(1/cos^2(x))/[(3cosx+4sinx)/cosx]^2}dx
= 25*integral{[sec^2(x)]/(3+4tanx)^2}dx
u = 3+4tanx --> du = 4sec^2(x)dx --> sec^2(x)dx = du/4
= 25*integral{1/(u)^2}du/4 = (25/4)*(-1/u)
= -25/[4(3+4tanx)] + C2 = -25/[4(3+4tanx)] + 3/4 + C1 (see below)
USING COTANGENT AND U-SUBSTITUTION:
integral{25/(3cosx+4sinx)^2}dx
= 25*integral{(1/sin^2(x))/[(3cosx+4sinx)/sinx]^2}dx
= 25*integral{[csc^2(x)]/(3cotx+4)^2}dx
u = 3cotx+4 --> du = -3csc^2(x)dx --> csc^2(x)dx = du/(-3)
= 25*integral{1/(u)^2}du/(-3) = [25/(-3)]*(-1/u)
= 25/[3(3cotx+4)] + C3 = 25/[3(3cotx+4)] - 25/12 + C2 
= 25/[3(3cotx+4)] - 25/12 + 3/4 + C1
= 25/[3(3cotx+4)] - 4/3 + C1 (see below)
CHECK TO SEE IF ANSWERS 1 AND 2 ABOVE ARE OFF BY A CONSTANT:
tan(x-arctan(4/3)) + C1 = -25/[4(3+4tanx)] + C2
Since tan(x-y) = (tanx-tany) / (1+tanx*tany), then:
tan(x-arctan(4/3))
    = (tanx-tan(arctan(4/3)))/(1+tanx*tan(arctan(4/3)))
    = (tanx-4/3)/(1+tanx*4/3), and
(tanx-4/3)/(1+tanx*4/3) + C1 = -25/[4(3+4tanx)] + C2
(3tanx-4)/(3+tanx*4) + 25/[4(3+4tanx)] + C1 = C2
(12tanx - 16 + 25) / [4(3+4tanx)] + C1 = C2
(12tanx + 9) / [4(3+4tanx)] + C1 = C2
3 * (4tanx + 3) / [4(3+4tanx)] + C1 = C2
3/4 + C1 = C2 --> Yes, so we are good!
CHECK TO SEE IF ANSWERS 2 AND 3 ABOVE ARE OFF BY A CONSTANT:
-25/[4(3+4tanx)] + C2 = 25/[3(3cotx+4)] + C3
-25/[4(3+4tanx)] - 25/[3(3cotx+4)] = C3 - C2
1/[4(3+4tanx)] + 1/[3(3cotx+4)] = (C3 - C2) / -25
3/(3+4tanx) + 4/(3cotx+4) = 12 * -(C3 - C2) / 25
3/(3+4tanx) + 4tanx/(3cotx*tanx+4tanx) = 12 * (-C3 + C2) / 25
3/(3+4tanx) + 4tanx/(3+4tanx) = 12 * (C2 - C3) / 25
(3+4tanx)/(3+4tanx) = 12 * (C2 - C3) / 25
1 = 12 * (C2 - C3) / 25 --> C2 - C3 = 25/12
C2 = C3 + 25/12 --> C3 = C2 - 25/12 --> Yes, so we are good!
Prove that A² - TR(A)*A + DET(A) * I = 0 for any 2x2 matrix A:
[a b]   [a b]             [a b]                     [1 0]
      *       - (a + d) *       + (a * d - b * c) *      
[c d]   [c d]             [c d]                     [0 1]
  [a^2+bc ab+bd]   [a^2+ad ab+bd]   [ad-bc 0]   [0 0]
=                -                +           = 
  [ac+cd bc+d^2]   [ac+cd ad+d^2]   [0 ad-bc]   [0 0]
Solve A + B = AB:
A + B = AB --> 1 + B/A = B --> 1 = B - B/A --> 1 = B * (1 - 1/A)
^B in terms of A: B = 1 / (1 - 1/A)
A + B = AB --> A + B - AB = 0 --> A - AB = -B --> A * (1-B) = -B
A in terms of B: A = -B / (1 - B) = B / (B - 1) = 1 / (1 - 1/B)
^A in terms of B from B in terms of A:
B = 1 / (1 - 1/A) --> B * (1 - 1/A) = 1 --> A/B*B*(1-1/A)=1*A/B
A - 1 = A/B --> A - A/B = 1 --> A * (1 - 1/B) = 1
A in terms of B again: A = 1 / (1 - 1/B)
P = {product n=1 to ˆž} (-Ï€² * n^2) = 1? = e^S, where
S = ln P = {sum n=1 to ˆž} (ln(-Ï€² * n^2)) = 0?
S = {sum n=1 to ˆž} (2 * ln(i * Ï€ * n))
S = 2 * {sum n=1 to ˆž} (ln(i * Ï€ * n))
S = 2 * {sum n=1 to ˆž} (ln(i) + ln(Ï€ * n))
S = 2 * {sum n=1 to ˆž} (i * Ï€ / 2 + ln(Ï€ * n))
S = 2 * {sum n=1 to ˆž} (ln(Ï€ * n) + i * Ï€ / 2) = ˆž + ˆž * i, 
so P = e^(ˆž + ˆž * i) = ˆž * e^(ˆž * i) = ˆž * undefined = undefined
S = {sum n=1 to ˆž} (n) = 1 + 2 + 3 + 4 + 5 + . . .
S = (2 + 4 + 6 + 8 + 10 + . . .) + (1 + 3 + 5 + 7 + 9 + . . .)
S = 2 * (1 + 2 + 3 + 4 + 5 + . . .) + (0 + 2 + 4 + 6 + 8 + . . .) 
    + (1 + 1 + 1 + 1 + 1 + . . .) 
S = 2 * S + 2 * (0 + 1 + 2 + 3 + 4 + 5 + . . .)
    + (1 + 1 + 1 + 1 + 1 + . . .)
S = 2 * S + 2 * (1 + 2 + 3 + 4 + 5 + . . .)
    + (1 + 1 + 1 + 1 + 1 + . . .)
S = 2 * S + 2 * S + (1 + 1 + 1 + 1 + 1 + . . .)
S = 4 * S + (1 + 1 + 1 + 1 + 1 + . . .)
-3 * S = 1 + 1 + 1 + 1 + 1 + . . . = ˆž, so S = -ˆž / 3 = -ˆž
# Solution to {sum n=1 to ˆž} (n/2^n) is:
{sum n=1 to ˆž} (n/2^n) = {sum n=1 to ˆž} ({sum k=1 to n} (1/2^n))
= {sum n=1 to ˆž} ({sum k=1 to n} (1/2^n))
= {sum k=1 to ˆž} ({sum n=k to ˆž} (1/2^n))
= {sum k=1 to ˆž} (1/2^k) / (1 - 1/2)
= {sum k=1 to ˆž} (1/2^k) / (1/2) = {sum k=1 to ˆž} (2/2^k)
= {sum k=1 to ˆž} (1/2^(k-1)) = {sum k=0 to ˆž} (1/2)^k = 2
If y = x² - x - 1, then the zeros are:
x = (-[-1]+-ˆš[1-(-4)])/2 = (1+ˆš5)/2 or (1-ˆš5)/2 = phi or -1/phi.
If y = x² + ˆš5*x + 1 = 0, then the zeros are:
x = [-ˆš5+-ˆš(5-4)]/2 = -(1+ˆš5)/2 or (1-ˆš5)/2 = -phi or -1/phi.
# Number challenges:
(0 - 0) x 0 = 0              (5 - 5) x 5 = 0
(1 - 1) x 1 = 0              (6 - 6) x 6 = 0
(2 - 2) x 2 = 0              (7 - 7) x 7 = 0
(3 - 3) x 3 = 0              (8 - 8) x 8 = 0
(4 - 4) x 4 = 0              (9 - 9) x 9 = 0
             (10 - 10) x 10 = 0
0 + 0 + 0! = 1               (5 / 5) % 5 = 1
1 + 1 - 1 = 1                (6 / 6) % 6 = 1
(2 / 2) % 2 = 1              (7 / 7) % 7 = 1
(3 / 3) % 3 = 1              (8 / 8) % 8 = 1
(4 / 4) % 4 = 1              (9 / 9) % 9 = 1
             (10 / 10) % 10 = 1
(0! + 0!) / 0! = 2           (5 + 5) / 5 = 2
(1 + 1) / 1 = 2              (6 + 6) / 6 = 2
(2 + 2) / 2 = 2              (7 + 7) / 7 = 2
(3 + 3) / 3 = 2              (8 + 8) / 8 = 2
(4 + 4) / 4 = 2              (9 + 9) / 9 = 2
             (10 + 10) / 10 = 2
0! + 0! + 0! = 3             (5!! / 5) % 5 = 3
1 + 1 + 1 = 3                (6! / 6!!) % 6 = 3
2 + (2 / 2) = 3              7 - (7!!! / 7) = 3
3 + 3 - 3 = 3                ˆš[8 + (8 / 8)] = 3
4 - (4 / 4) = 3              ˆš(9) + 9 - 9 = 3
            ˆš[10 - (10 / 10)] = 3
(0! + 0!) << (0!) = 4        5 - (5 / 5) = 4
(1 + 1) << 1 = 4             6!! / (6 + 6) = 4
!2 + !2 + 2 = 4              (7!!! / 7) % 7 = 4
3 + (3 / 3) = 4              8 - ˆš(8 + 8) = 4
4 + 4 - 4 = 4                ˆš(9) + (9 / 9) = 4
           [(10)!! / 10] % 10 = 4
(0! || 0) >> 0! = 5          5 + 5 - 5 = 5
(1 || !1) >> 1 = 5           6 - (6 / 6) = 5
!2 + 2 + 2 = 5               (7!!! + 7) / 7 = 5
3 + (3! / 3) = 5             8 - ˆš[!ˆš(8 + 8)] = 5
4 + (4 / 4) = 5              9 - !ˆš(9) - !ˆš(9) = 5
            10 >> (10 / 10) = 5
(0! + 0! + 0!)! = 6          5 + (5 / 5) = 6
(1 + 1 + 1)! = 6             6 + 6 - 6 = 6
2 + 2 + 2 = 6                7 - (7 / 7) = 6
3! + 3 - 3 = 6               ˆš[8 + (8 / 8)]! = 6
4 + 4 - ˆš(4) = 6             [9 - ˆš(9)] % 9 = 6
            ˆš[10 - (10 / 10)]! = 6
ˆš(0! || 0)! // (0!) = 7      ˆš[!5 + ˆš(5 x 5)] = 7
ˆš(1 || !1)! // 1 = 7         6 + (6 / 6) = 7
(2 + !2)! + !2 = 7           7 + 7 - 7 = 7
3! + (3 / 3) = 7             8 - (8 / 8) = 7
!4 + ˆš(4) - 4 = 7            ˆš(9)! + (9 / 9) = 7
            ˆš(10)! // (10 / 10) = 7
~(0!) % (0! || 0) = 8        (5!! / 5) + 5 = 8
(~1) % (1 || !1) = 8         6!! / ˆš(6 x 6) = 8
(2 + !2)! + 2 = 8            7 + (7 / 7) = 8
3 + 3 + !3 = 8               8 + 8 - 8 = 8
!4 - (4 / 4) = 8             9 - (9 / 9) = 8
              ~(10 / 10) % 10 = 8
(0! || 0) - 0! = 9           5!!! - (5 / 5) = 9
(1 || !1) - 1 = 9            (6!! + 6) / 6 = 9
(2 + !2) ^ 2 = 9             ![(7!!! / 7) % 7] = 9
3 + 3 + 3 = 9                8 + (8 / 8) = 9
!4 + 4 - 4 = 9               9 + 9 - 9 = 9
             10 - (10 / 10) = 9
(0! || 0) - 0 = 10           5!!! + 5 - 5 = 10
1 || (1 - 1) = 10            (6!! + 6!!!!) / 6 = 10
!2 || (2 - 2) = 10           (7!!!! / 7) + 7 = 10
!3 x (3 + !3) = 10           8!!! / ˆš(8 x 8) = 10
!4 + (4 / 4) = 10            9 + (9 / 9) = 10
              10 + 10 - 10 = 10
                                 b          f(x)             b - a
Cool definite integral formula = | ------------------- dx = -------
                                 a f(a + b - x) + f(x)         2
Can you get 24 from 3, 3, 8, 8 only using + - x / ()?
Yes, the answer is 8 / (3 - (8 / 3)) = 24.
If q(Ï€) = a_n*Ï€^n + ... + a_3*Ï€^3 + a_2*Ï€² + a_1*Ï€ + 
a_0 = 0, and v(i) = i^(-n) + ... + i - 1 - i + 1
then Q(Ï€*i) = 0, where x = Ï€*i and Q(Ï€*i) = q(Ï€) [dot] v(i)
= i^(-n)*a_n*x^n + ... + i*a_3*x^3 - a_2*x² - i*a_1*x + a_0.
divisor = d1 (or d3 or d7 or d9) x 9(or 3 or 7 or 1) = M9
divi number = m = (M9 + 1) / 10 = M + 1
dividend = D = 10t + q, so mq + t = multiple of d1 # (or d3 or d7 or d9)?
HTTRACK = offline browser for children
# Kitboga scam-baiting joke card code:
D035-Y0UR-M0MK-N0WU-5C4M
