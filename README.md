# Black-Scholes Delta Hedging

Welcome to the Black-Scholes Delta Hedging project, a deep dive into option pricing and risk management in quantitative finance. This repository features a Python implementation that prices a European call option and simulates a delta-hedging strategy using the Black-Scholes model. Built with a scikit-learn-inspired BlackScholes class, the project combines rigorous mathematical derivations with modular, well-documented code, showcasing expertise in financial engineering and software development.

## Project Overview
In financial markets, options are powerful tools for managing risk and capturing opportunity. The Black-Scholes model provides a theoretical framework to price options and hedge their risks. This project explores:

* Option Pricing: Calculating the value of a European call option on 1000 shares with a custom polynomial approximation for the standard normal CDF.
* Delta Hedging: Simulating a dynamic hedging strategy over two days as the stock price fluctuates, balancing theoretical precision with practical execution.
* Implementation: A reusable BlackScholes class with methods for pricing and delta calculations, designed for clarity and extensibility.

## Key features:

A unique polynomial approximation for the standard normal CDF, ensuring precise calculations.
LaTeX derivations in a Jupyter Notebook, blending mathematical rigor with practical insights.
Clean, scikit-learn-style Python code with input validation and comprehensive docstrings.

This project is ideal for quantitative finance professionals, data scientists, and developers interested in financial modeling and risk management.

## Installation
To run the project, ensure you have Python 3.6+ and the required dependencies installed. \
pip install numpy

## Usage
### Jupyter Notebook

1. Clone the repository:git clone https://github.com/Amos-Anderson/black-scholes-hedging.git
cd black-scholes-hedging


2. Install Jupyter Notebook (if not already installed):pip install jupyter


3. Launch Jupyter Notebook:jupyter notebook


4. Open black_scholes_hedging.ipynb and run all cells to explore the derivations, code, and results.

5. Python Script

  - Run the standalone script:python black_scholes_hedging_corrected.py


  - The script outputs the option price, delta, hedging strategy, and two-day simulation results.

## Files

* black_scholes_hedging.ipynb: Jupyter Notebook with narrative, LaTeX derivations, and Python code.
* black_scholes_hedging_corrected.py: Standalone Python script for pricing and hedging simulation.

## Methodology
The project implements the Black-Scholes model for a European call option with the following parameters:

* Stock price: $35
* Strike price: $33
* Volatility: 25%
* Dividend yield: 2%
* Risk-free rate: 5%
* Time to expiration: 180 days
* Shares: 1000

## Key Components

1. Pricing: Computes the call option value using a custom polynomial approximation for the standard normal CDF, as specified:$$\Phi(x) = 0.5 + \frac{1}{\sqrt{2\pi}} \left( x - \frac{x^3}{6} + \frac{x^5}{40} - \frac{x^7}{336} + \frac{x^9}{3456} \right), \quad 0 < x \leq 1.$$
2. Delta Calculation: Determines the option’s delta to guide the hedging strategy.
3. Hedging Simulation: Simulates delta hedging over two days with stock prices of \$35.50 (Day 1) and $34.80 (Day 2), calculating profit/loss and rebalancing costs.

The BlackScholes class provides a modular interface for pricing, delta calculations, and future extensions (e.g., other Greeks or option types).

## Results
The simulation yields:

* Initial Setup:
  * Call Option Value (1000 shares): $3647.32
  * Delta (1000 shares): 686.895 shares


* Hedging Strategy:
  * Shares Purchased: 686.895
  * Amount Borrowed: $20,394.01


* Day 1 (Stock Price = $35.50):
  * Profit/Loss: -$99.21
  * Rebalancing Cost: $972.84


* Day 2 (Stock Price = $34.80):
  * Profit/Loss: -$145.97
  * Rebalancing Cost: -$1395.86

These results highlight the challenges of discrete hedging, where small losses arise from rebalancing and interest costs.

## Why This Project?
This project stands out for its:

- Mathematical Precision: Implements a custom CDF approximation, ensuring adherence to specific requirements.
- Code Quality: Features a scikit-learn-style class with input validation, docstrings, and warnings for robustness.
- Educational Value: Combines LaTeX derivations with code, making it accessible to both technical and learning audiences.
- Real-World Relevance: Demonstrates practical risk management techniques applicable to trading and portfolio management.

## Contributing
Contributions are welcome! If you have ideas for enhancements (e.g., additional Greeks, visualizations, or alternative hedging strategies), please:

1. Feel free to engage with the repository!
2. Create a feature branch (git checkout -b feature/new-feature).
3. Commit changes (git commit -m 'Add new feature').
4. Push to the branch (git push origin feature/new-feature).
5. Open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For questions or collaboration opportunities, connect with me on LinkedIn or open an issue on GitHub.

Author: Amos Anderson 

GitHub: Amos-Anderson 

Project Repository: black-scholes-hedging

