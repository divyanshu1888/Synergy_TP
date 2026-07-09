# Feature Dictionary



## rolling_average_signal

- **Formula:** Rolling mean of `signal`, window size 3, computed within each domain+condition group, ordered by `time_step`.

- **Applies to:** All domains where time_step/order is meaningful.

- **Required columns:** domain, condition, time_step, signal

- **Invalid when:** Rows are unordered, or the window would cross into an unrelated condition/domain.

- **Why useful for ML:** Smooths replicate-to-replicate noise, giving a less jittery input feature.



## normalized_signal

- **Formula:** signal / baseline_signal

- **Applies to:** All domains with a valid, non-zero baseline_signal.

- **Required columns:** signal, baseline_signal

- **Invalid when:** baseline_signal is missing or zero.

- **Why useful for ML:** Puts readings on a comparable relative scale across baselines/batches instead of raw instrument scale.



## power_w

- **Formula:** voltage_v * current_a

- **Applies to:** Electronics only.

- **Required columns:** voltage_v, current_a, domain

- **Invalid when:** Domain is not Electronics, or voltage/current are missing.

- **Why useful for ML:** A physically meaningful derived quantity that often relates more directly to performance/failure than voltage or current alone.



## error_percent

- **Formula:** ((signal - expected_signal) / expected_signal) * 100

- **Applies to:** All domains with a valid, non-zero expected_signal.

- **Required columns:** signal, expected_signal

- **Invalid when:** expected_signal is missing or zero.

- **Why useful for ML:** Directly quantifies calibration accuracy; large values flag unreliable readings.



## stress_ratio

- **Formula:** stress_mpa / reference_stress_mpa

- **Applies to:** Mechanical only.

- **Required columns:** stress_mpa, reference_stress_mpa, domain

- **Invalid when:** Domain is not Mechanical, or reference_stress_mpa is missing/zero.

- **Why useful for ML:** Normalizes measured stress against a rated value, more informative than raw stress alone.



## stability_flag

- **Formula:** Derived from coefficient_of_variation per replicate group - stable if CV ≤ 0.05, moderate if 0.05 < CV ≤ 0.15, unstable if CV > 0.15.

- **Applies to:** All replicate groups.

- **Required columns:** coefficient_of_variation (from replicate_summary)

- **Invalid when:** CV cannot be computed (fewer than 2 valid replicates).

- **Why useful for ML:** Lets downstream steps distinguish trustworthy measurements from noisy ones.



## ml_ready

- **Formula:** Boolean - True only if signal, expected_signal (non-zero), input_value, domain, and condition are all present, and the row's replicate group has stability_flag == "stable".

- **Applies to:** All domains.

- **Required columns:** all of the above, plus merged stability_flag.

- **Invalid when:** Any required value is missing, or the group is moderate/unstable.

- **Why useful for ML:** A single filter column to select complete, reliably-measured rows for training.

