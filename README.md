# $\text{Physics-Informed Neural Networks vs Runge-Kutta}$ 

This repository discusses a comparison between two physics-based modeling methods, namely *Physics-Informed Neural Networks* (PINNs) and the *fourth-order Runge–Kutta method* (RK4). To evaluate both methods, a *damped vibration system* is used as the case study, with the objective of analyzing the prediction accuracy of each method with respect to the exact solution.

## $\text{Background}$

Modeling physical systems can be performed using classical numerical approaches as well as machine learning–based approaches:

* *Fourth-Order Runge–Kutta* (RK4) is a numerical method commonly used to solve ordinary differential equations.
* *Physics-Informed Neural Networks* (PINNs) are neural network–based approaches that incorporate physical laws into the training process.

This repository aims to compare the performance of these two methods in modeling a damped vibration system.

## $\text{Methodology}$

A damped vibration system is a mechanical system in which oscillatory motion gradually decreases over time due to energy dissipation mechanisms such as friction or viscous damping. Unlike undamped systems that oscillate indefinitely, damped systems experience a reduction in amplitude until the motion eventually ceases.

### $\text{1. Physics-Informed Neural Networks (PINNs)}$

* The neural network is trained by considering the governing differential equations of the system and Initial and/or boundary conditions,
* The loss function includes the residuals of the physical equations,
* Used to predict the system response over time.

### $\text{2. 4th Order Runge-Kutta (RK4)}$

* An explicit fourth-order numerical method,
* Used as a deterministic approach to solve ordinary differential equations,
* The results are compared with the exact solution.

## $\text{Results and Evaluation}$

The evaluation is performed using the *Mean Squared Error (MSE)* with respect to the exact solution.

| Method |   MSE (%)  |
|--------|------------|
| PINNs  |  *0.1636*  |
| RK4    |  *0.1453*  |

Based on these results RK4 produces a slightly lower error compared to PINNs and PINNs still demonstrate competitive performance despite being a machine learning–based approach.