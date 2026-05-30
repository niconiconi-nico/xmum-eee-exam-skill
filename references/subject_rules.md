# Subject Rules

## Mathematics

For calculus, linear algebra, differential equations, and related math courses:

- Preserve definitions, theorem conditions, notation, and assumptions.
- Separate concept, theorem, formula, method, and example.
- For proofs or derivations, follow the teacher's depth. Add missing intermediate explanation only when needed for clarity.
- State when a theorem or formula can be used.
- Highlight common mistakes such as missing conditions, sign errors, wrong domain, invalid cancellation, or confusing necessary and sufficient conditions.

Recommended sections:

- Definitions / 定义
- Theorems and conditions / 定理与条件
- Methods / 方法
- Worked examples / 例题
- Common mistakes / 易错点

## Probability and statistics

Prioritize:

- Random variables, distributions, PMF/PDF/CDF, expectation, variance, covariance.
- Conditional probability, Bayes' theorem, independence, joint and marginal distributions.
- Estimation, hypothesis testing, confidence intervals, Markov chains, or stochastic processes if present.
- Conditions for using each distribution or theorem.

For each distribution, use:

| Distribution | Parameters | PMF/PDF | Mean | Variance | When to use |
| --- | --- | --- | --- | --- | --- |

For examples, explicitly identify:

- What is random?
- What is known?
- What is being asked?
- Which distribution or theorem applies?
- Why that method applies.

## Signals and systems

Prioritize:

- Signal classification: continuous/discrete, periodic/aperiodic, energy/power.
- System properties: linearity, time invariance, causality, stability, memory.
- Convolution and impulse response.
- Fourier series, Fourier transform, Laplace transform, Z-transform.
- Transfer functions, poles/zeros, ROC, frequency response, filtering.

For transforms, use:

| Transform | Definition | Key properties | ROC/conditions | Common use |
| --- | --- | --- | --- | --- |

For problem solutions, include:

- Identify domain: time, frequency, s-domain, or z-domain.
- Choose property or transform pair.
- Show algebra at the teacher's depth.
- Interpret the result physically when useful.

## Electronic devices

Prioritize:

- Energy band diagram and carrier movement.
- Device structure and operation.
- I-V characteristics and operating regions.
- Threshold voltage, depletion/inversion, recombination/generation, drift/diffusion when relevant.
- Applications and limitations.

For each device, use:

| Device | Structure | Operation principle | I-V behavior | Key equations | Applications |
| --- | --- | --- | --- | --- | --- |

If adding a helper diagram, mark it as:

`补充：讲义中没有，作为辅助理解。`

## Embedded systems

Prioritize:

- Hardware connections and pin mapping.
- Register configuration.
- Interrupts, timers, ADC/DAC, UART/SPI/I2C, PWM when present.
- Code logic and control flow.
- Debug steps and common hardware/software failure points.

For labs, use:

| Component | Role | Connection/config | Code responsibility | Debug check |
| --- | --- | --- | --- | --- |

Explain code in terms of behavior, not line-by-line unless requested.

## FPGA and digital design

Prioritize:

- Combinational vs sequential logic.
- FSM states, transitions, outputs.
- Clocking, reset, timing, setup/hold, constraints.
- Verilog/VHDL module purpose and signal roles.
- Simulation waveform interpretation.

For each module:

| Module | Inputs | Outputs | Internal signals | Behavior | Timing notes |
| --- | --- | --- | --- | --- | --- |

For timing/debug:

- Identify clock domain.
- Check reset behavior.
- Check signal width and signedness.
- Check blocking/non-blocking assignment issues.
- Check constraints and simulation/testbench coverage.
