\# Feature Summary



\## Which features are general across all domains?

rolling\_average\_signal, normalized\_signal, error\_percent, stability\_flag, and ml\_ready - computed the same way regardless of domain, as long as their required columns are present.



\## Which features are domain-specific?

power\_w (Electronics only) and stress\_ratio (Mechanical only). Both are left blank outside their domain because the underlying columns don't apply there.



\## Which rows are not ML-ready and why?

B001–B003 (Biochem, low\_concentration) and M007–M009 (Mechanical, high\_load) - 6 of 27 rows. Both groups are flagged moderate rather than stable (CV = 0.0833 and 0.1005 respectively), so they fail the stability requirement even though no individual values are missing.



\## Which engineered feature is most useful for Electronics?

power\_w - the one feature unique to this domain, tying voltage and current into a single physically meaningful quantity.



\## Which engineered feature is most useful for Mechanical?

stress\_ratio - expresses how close a measured stress is to its rated limit, more informative for failure risk than raw stress\_mpa alone.



\## Which engineered feature is most useful for Biochem?

normalized\_signal - Biochem absorbance can drift with baseline/instrument conditions, so expressing signal relative to baseline makes readings more comparable.



\## Why should invalid domain features be left blank instead of forcing a value?

Forcing a value (e.g. 0 for power\_w on a Biochem row) creates a fake number that looks like a real measurement. A blank correctly signals "not applicable," while 0 could be misread as "measured and equal to zero."



\## How can feature engineering introduce misleading information?

Filling missing/invalid values with 0 can create fake patterns a model might learn as real; a rolling average can smooth over a genuine sudden change and hide it; and features derived from noisy replicate groups (like Mechanical high\_load) can propagate that unreliability downstream, making noise look like engineered signal.

