# Chemical Reactor Simulator

A Python-based interactive simulator for analyzing and comparing the performance of Continuous Stirred Tank Reactors (CSTRs) and Plug Flow Reactors (PFRs) using reaction engineering principles.

The simulator allows users to study reactor behavior under different operating conditions, compare reactor performance, perform basic economic analysis, generate engineering reports, and explore reactor design decisions through an intuitive Streamlit interface.

## Project Overview

This project was developed to bridge theoretical reaction engineering concepts with practical simulation and decision-making tools.

The simulator incorporates:
* Arrhenius kinetics
* CSTR modeling
* PFR modeling
* Reactor performance comparison
* Reactor design calculations
* Economic evaluation
* Automated reactor recommendation
* Interactive data visualization
* PDF report generation


## Objectives

* Understand the effect of temperature on reaction conversion.
* Compare CSTR and PFR performance under identical operating conditions.
* Analyze the effect of reactor volume on conversion.
* Determine reactor design requirements for target conversions.
* Perform preliminary economic evaluation of reactor operation.


## Features

### 1. Single Temperature Simulation

Evaluate reactor performance at a specified operating temperature.

Outputs include:

* Rate constant
* Conversion
* Reactor recommendation
* Economic metrics
* PDF report


### 2. Temperature Comparison

Analyze how conversion changes over a temperature range.

Provides:

* Interactive conversion vs temperature plots
* Comparison of CSTR and PFR performance
* Identification of favorable operating regions


### 3. Volume Comparison

Study the effect of reactor volume on conversion.

Provides:

* Interactive conversion vs volume plots
* Reactor efficiency comparison
* Design insights


### 4. Reactor Design Module

Determine operating conditions required to achieve a desired conversion.

Supports:

* Required temperature calculation
* Required reactor volume calculation


### 5. Economic Analysis

Estimate reactor profitability using user-defined economic parameters.

Calculates:

* Revenue
* Feed cost
* Profit
* Annual profit
* Capital cost
* Payback period


### 6. Reactor Recommendation Engine

Automatically recommends the most suitable reactor based on simulation results and provides engineering justification.


### 7. PDF Report Generation

Generate downloadable engineering reports containing:

* Input parameters
* Simulation results
* Economic analysis
* Reactor recommendation


## 🧪 Reaction Model

The simulator currently supports single irreversible reactions of the form:

[A ----> products]

with a generalized power-law rate expression:

[-r_A = k*(C_A^n)]

where:

* (r_A) = rate of disappearance of reactant A
* (k) = rate constant
* (C_A) = concentration of reactant A
* (n) = reaction order


## Arrhenius Kinetics

The temperature dependence of the rate constant is modeled using the Arrhenius equation:

[k = A*e^{-E_a/RT}]

where:

* (A) = frequency factor
* (E_a) = activation energy
* (R) = universal gas constant
* (T) = temperature


## Reactor Models

### Continuous Stirred Tank Reactor (CSTR)

Assumptions:

* Perfect mixing
* Uniform concentration throughout reactor
* Steady-state operation

Advantages:

* Easy temperature control
* Simple operation


### Plug Flow Reactor (PFR)

Assumptions:

* No axial mixing
* Concentration varies along reactor length
* Steady-state operation

Advantages:

* Higher conversion
* Better reactor volume utilization


## Technologies Used

* Python
* Streamlit
* Plotly
* NumPy


## Project Structure

Chemical-Reactor-Simulator/

│
├── app.py
|
├── kinetics.py
|
├── reactor_models.py
|
├── economics.py
|
├── graphs.py
|
├── reactor_info.py
|
├── reports.py
│
└── assets/

## 🚀 Installation

Clone the repository:

```bash
git clone <repository-url>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## Example Applications

The simulator framework can represent industrial processes involving single-reactant conversion systems, including:

* Hydrocarbon cracking
* Thermal decomposition reactions
* Isomerization reactions
* Pyrolysis processes
* Hydrogen peroxide decomposition
* Biomass conversion systems


## Future Scope

Potential future improvements:

* Multiple reactant systems (A + B → Products)
* Reversible reactions
* Non-isothermal reactor models
* Catalyst deactivation models
* Residence Time Distribution (RTD) analysis
* Optimization algorithms
* Process economics and sensitivity analysis
* Reactor networks


## Author

Dhananjay Srivastava

B.Tech Chemical Engineering
Malaviya National Institute of Technology (MNIT Jaipur)

## Disclaimer

This simulator is intended for educational and academic purposes. Industrial reactor design requires detailed kinetic studies, transport phenomena analysis, safety evaluation, and rigorous process simulation.
