# Correlation Limitations



## Does signal increase or decrease with input value?

Depends on domain - Biochem goes up with concentration, Electronics goes down as load increases (voltage sag), Mechanical goes up with load (more deflection).



## Which domain shows the strongest signal-input relationship?

Biochem, r = 0.999, R² = 0.999. Very clean.



## Which domain shows the weakest or noisiest relationship?

Mechanical (signal vs load), R² = 0.968 - the lowest of the five. Makes sense given that outlier reading in the high_load group.



## Does high correlation prove causation?

No. It just means two things move together - could easily be a third factor, or coincidence, especially with this little data.



## Can correlation be trusted with small sample size?

Not really. Each domain only has 3 unique input levels (9 points total). One weird reading can swing the whole fit.



## Can correlation miss nonlinear relationships?

Yes - Pearson only picks up straight-line relationships. A real curved relationship could show a weak correlation even if the variables are clearly linked.



## How can outliers affect correlation?

They drag the slope/intercept toward themselves and inflate error. M009 is a good example - it's why Mechanical has the worst fit of the three.



## How can temperature, load, material type, or experimental condition act as confounding variables?

In Electronics, temperature climbs right along with load (35°C → 50°C) at the same time signal drops. Can't tell from this data alone whether it's the load or the heat causing the drop - they're moving together.



## Why should mixed-domain correlation be avoided?

Biochem, Electronics, and Mechanical are measuring completely different things on different scales (absorbance, volts, mm). Correlating across domains would just be comparing apples to oranges - the number wouldn't mean anything real.

