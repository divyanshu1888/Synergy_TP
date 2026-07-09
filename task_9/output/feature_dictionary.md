\# Feature Dictionary



\## rolling\_average\_signal

\- \*\*Formula:\*\* Rolling mean of `signal`, window size 3, computed within each domain+condition group, ordered by `time\_step`.

\- \*\*Applies to:\*\* All domains where time\_step/order is meaningful.

\- \*\*Required columns:\*\* domain, condition, time\_step, signal

\- \*\*Invalid when:\*\* Rows are unordered, or the window would cross into an unrelated condition/domain.

\- \*\*Why useful for ML:\*\* Smooths replicate-to-replicate noise, giving a less jittery input feature.



\## normalized\_signal

\- \*\*Formula:\*\* signal / baseline\_signal

\- \*\*Applies to:\*\* All domains with a valid, non-zero baseline\_signal.

\- \*\*Required columns:\*\* signal, baseline\_signal

\- \*\*Invalid when:\*\* baseline\_signal is missing or zero.

\- \*\*Why useful for ML:\*\* Puts readings on a comparable relative scale across baselines/batches instead of raw instrument scale.



\## power\_w

\- \*\*Formula:\*\* voltage\_v \* current\_a

\- \*\*Applies to:\*\* Electronics only.

\- \*\*Required columns:\*\* voltage\_v, current\_a, domain

\- \*\*Invalid when:\*\* Domain is not Electronics, or voltage/current are missing.

\- \*\*Why useful for ML:\*\* A physically meaningful derived quantity that often relates more directly to performance/failure than voltage or current alone.



\## error\_percent

\- \*\*Formula:\*\* ((signal - expected\_signal) / expected\_signal) \* 100

\- \*\*Applies to:\*\* All domains with a valid, non-zero expected\_signal.

\- \*\*Required columns:\*\* signal, expected\_signal

\- \*\*Invalid when:\*\* expected\_signal is missing or zero.

\- \*\*Why useful for ML:\*\* Directly quantifies calibration accuracy; large values flag unreliable readings.



\## stress\_ratio

\- \*\*Formula:\*\* stress\_mpa / reference\_stress\_mpa

\- \*\*Applies to:\*\* Mechanical only.

\- \*\*Required columns:\*\* stress\_mpa, reference\_stress\_mpa, domain

\- \*\*Invalid when:\*\* Domain is not Mechanical, or reference\_stress\_mpa is missing/zero.

\- \*\*Why useful for ML:\*\* Normalizes measured stress against a rated value, more informative than raw stress alone.



\## stability\_flag

\- \*\*Formula:\*\* Derived from coefficient\_of\_variation per replicate group - stable if CV ≤ 0.05, moderate if 0.05 < CV ≤ 0.15, unstable if CV > 0.15.

\- \*\*Applies to:\*\* All replicate groups.

\- \*\*Required columns:\*\* coefficient\_of\_variation (from replicate\_summary)

\- \*\*Invalid when:\*\* CV cannot be computed (fewer than 2 valid replicates).

\- \*\*Why useful for ML:\*\* Lets downstream steps distinguish trustworthy measurements from noisy ones.



\## ml\_ready

\- \*\*Formula:\*\* Boolean - True only if signal, expected\_signal (non-zero), input\_value, domain, and condition are all present, and the row's replicate group has stability\_flag == "stable".

\- \*\*Applies to:\*\* All domains.

\- \*\*Required columns:\*\* all of the above, plus merged stability\_flag.

\- \*\*Invalid when:\*\* Any required value is missing, or the group is moderate/unstable.

\- \*\*Why useful for ML:\*\* A single filter column to select complete, reliably-measured rows for training.

