\# Replicate Analysis



\## Which replicate group is most stable?

Electronics low\_load (10 ohm), CV = 0.0051. Barely any spread between the 3 readings.



\## Which replicate group is most noisy?

Mechanical high\_load (150 N), CV = 0.1005 - highest of all 9 groups.



\## Which group has the widest confidence interval?

Same group, Mechanical high\_load: \[1.41, 2.35]. About double the width of any other group.



\## Which group has the highest coefficient of variation?

Same group: Mechanical, high\_load, CV = 0.1005.



\## Why is mean alone not enough for judging reliability?

Two groups can have the exact same mean but totally different spread - one tight, one all over the place. The mean doesn't tell you which is which. You need std/CV to know how much to trust it.



\## Why does replicate count affect confidence interval width?

SE = std/√n, so more replicates = smaller SE = tighter interval. We only have 3 replicates per group here, so the CI is already pretty wide to begin with - small n means less certainty.



\## Which readings should be investigated before using the data for machine learning?

M009 (Mechanical, high\_load, rep 3) - signal came in at 2.10 vs an expected 1.75, a 20% miss. It's the reason the whole high\_load group got flagged moderate instead of stable. Worth re-checking before trusting that data point.

