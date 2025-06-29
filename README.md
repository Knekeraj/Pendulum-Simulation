# Physics Simulation: Numerical Solution vs. Small-Angle Approximation

## Project Overview

This project is a physics simulation developed in Python to visually and analytically demonstrate the limitations of the **small-angle approximation** (`sin(θ) ≈ θ`), a concept fundamental to introductory physics.

The program simultaneously models a simple pendulum's motion in two ways:
1.  **The Accurate Model (Numerical Solution):** This model numerically solves the full, non-linear differential equation of pendulum motion, which is accurate for all starting angles.
2.  **The Approximate Model:** This model uses the simplified equation derived from the small-angle approximation, which is only accurate for small initial angles.

The simulation serves as a powerful tool to visualize how and why the simplified model deviates from reality, especially at larger angles.

---

## Key Features

*   **Real-Time Dual Visualization:** Utilizes **Pygame** to animate two pendulums simultaneously—the accurate numerical solution (blue) and the small-angle approximation (orange)—allowing for a direct visual comparison of their divergence.
*   **Live Data Display:** The simulation window displays real-time data for both models, including time passed and the current angle, providing immediate quantitative feedback.
*   **Comparative Data Analysis:** At the end of the simulation, **Matplotlib** is used to generate a detailed graph that plots the trajectories of both models over time, clearly quantifying the error introduced by the approximation.
*   **Interactive Parameters:** The program is interactive, allowing the user to define the starting angle and friction coefficient to explore different physical scenarios.

---

## Technologies Used

*   **Language:** Python
*   **Libraries:**
    *   **Pygame:** For creating the real-time animation and graphics.
    *   **Matplotlib:** For generating the final data plot for analysis.
    *   **NumPy:** For handling numerical calculations and physics constants.

---

## How to Run

1.  **Ensure you have the required libraries installed:**
    ```bash
    pip install pygame matplotlib numpy
    ```
2.  **Run the script from your terminal:**
    ```bash
    python your_script_name.py
    ```
3.  **Enter the initial conditions** (simulation time, friction, starting angle) when prompted. The Pygame window will open and the dual-simulation will begin.
