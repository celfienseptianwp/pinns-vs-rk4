# $\text{Physics-Informed Neural Networks vs Runge-Kutta}$ 

This repository discusses a comparison between two physics-based modeling methods, namely *Physics-Informed Neural Networks* (PINNs) and the *fourth-order Runge–Kutta method* (RK4). To evaluate both methods, a *damped vibration system* is used as the case study, with the objective of analyzing the prediction accuracy of each method with respect to the exact solution.

## $\text{Background}$

Modeling physical systems can be performed using classical numerical approaches as well as machine learning–based approaches:

* *Fourth-Order Runge–Kutta* (RK4) is a numerical method commonly used to solve ordinary differential equations.
* *Physics-Informed Neural Networks* (PINNs) are neural network–based approaches that incorporate physical laws into the training process.

This repository aims to compare the performance of these two methods in modeling a damped vibration system.

## $\text{Methodology}$

A damped vibration system is a mechanical system in which oscillatory motion gradually decreases over time due to energy dissipation mechanisms such as friction or viscous damping. Unlike undamped systems that oscillate indefinitely, damped systems experience a reduction in amplitude until the motion eventually ceases.

* *Equation of Motion*: The equation of motion for a single-degree-of-freedom (SDOF) damped vibration system is given by:
$$ m \ddot{y}(t) + b \dot{y}(t) + k y(t) = 0 $$
* *Analytic Solution*: The analytic solution of damped vibration system for every position (y) is given by:
$$ y(t) = y_0 e^{-\gamma t} \cos{(\omega_d t)} $$

Where: 
### $\text{2. Physics-Informed Neural Networks (PINNs)}$

### $\text{3. 4th Order Runge-Kutta (RK4)}$

## $\text{Hasil dan Evaluasi}$

## $\text{Visualisasi Hasil}$
