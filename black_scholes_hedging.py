import numpy as np
import math
import warnings

class BlackScholes:
    """
    A scikit-learn-style class for Black-Scholes option pricing and delta calculations.
    
    Parameters
    ----------
    S : float
        Current stock price.
    K : float
        Strike price.
    T : float
        Time to expiration (in years).
    r : float
        Risk-free interest rate (annualized).
    sigma : float
        Volatility (annualized).
    D : float, optional
        Dividend yield (annualized). Default is 0.0.
    
    Methods
    -------
    compute_d1_d2()
        Compute d1 and d2 parameters.
    norm_cdf_approx(x)
        Approximate standard normal CDF using the provided polynomial.
    call_price()
        Compute the Black-Scholes call option price per share.
    call_delta()
        Compute the call option delta per share.
    """
    
    def __init__(self, S, K, T, r, sigma, D=0.0):
        self.S = float(S)
        self.K = float(K)
        self.T = float(T)
        self.r = float(r)
        self.sigma = float(sigma)
        self.D = float(D)
        
        # Input validation
        if any(param <= 0 for param in [S, K, T, sigma]):
            raise ValueError("S, K, T, and sigma must be positive.")
        if r < 0 or D < 0:
            raise ValueError("r and D must be non-negative.")
    
    def compute_d1_d2(self):
        """Compute d1 and d2 parameters for Black-Scholes."""
        log_term = math.log(self.S / self.K)
        drift = (self.r - self.D + 0.5 * self.sigma**2) * self.T
        denominator = self.sigma * math.sqrt(self.T)
        d1 = (log_term + drift) / denominator
        d2 = d1 - self.sigma * math.sqrt(self.T)
        return d1, d2
    
    def norm_cdf_approx(self, x):
        """
        Approximate standard normal CDF using the provided polynomial for 0 < x <= 1.
        For x < 0, use Phi(-x) = 1 - Phi(x). Warn if x > 1.
        
        Parameters
        ----------
        x : float
            Input value for CDF.
        
        Returns
        -------
        float
            Approximated CDF value.
        """
        if x < 0:
            return 1 - self.norm_cdf_approx(-x)
        if x > 1:
            warnings.warn(f"CDF input x={x} > 1; using polynomial approximation.")
        c = 1 / math.sqrt(2 * math.pi)
        poly = x - (x**3) / 6 + (x**5) / 40 - (x**7) / 336 + (x**9) / 3456
        return 0.5 + c * poly
    
    def call_price(self):
        """Compute Black-Scholes call option price per share."""
        d1, d2 = self.compute_d1_d2()
        phi_d1 = self.norm_cdf_approx(d1)
        phi_d2 = self.norm_cdf_approx(d2)
        term1 = self.S * math.exp(-self.D * self.T) * phi_d1
        term2 = self.K * math.exp(-self.r * self.T) * phi_d2
        return term1 - term2
    
    def call_delta(self):
        """Compute call option delta per share."""
        d1, _ = self.compute_d1_d2()
        phi_d1 = self.norm_cdf_approx(d1)
        return math.exp(-self.D * self.T) * phi_d1

def delta_hedge_simulation():
    """
    Simulate delta hedging for a European call option over two days.
    
    Returns
    -------
    dict
        Results for initial pricing, hedging strategy, and two-day simulation.
    """
    # Initial parameters
    S0 = 35.0  # Initial stock price
    K = 33.0   # Strike price
    T0 = 180 / 365  # Initial time to expiration (years)
    r = 0.05   # Risk-free rate
    sigma = 0.25  # Volatility
    D = 0.02   # Dividend yield
    N = 1000   # Number of shares underlying the option
    
    # Day 0: Initial pricing and delta
    bs_day0 = BlackScholes(S=S0, K=K, T=T0, r=r, sigma=sigma, D=D)
    call_price_day0 = bs_day0.call_price() * N
    delta_day0 = bs_day0.call_delta() * N
    
    # Day 0: Hedging strategy
    shares_day0 = delta_day0
    cost_day0 = shares_day0 * S0
    premium = call_price_day0
    borrowing_day0 = cost_day0 - premium  # Borrow if positive
    
    # Day 1: Stock price rises to 35.50
    S1 = 35.50
    T1 = (180 - 1) / 365
    bs_day1 = BlackScholes(S=S1, K=K, T=T1, r=r, sigma=sigma, D=D)
    call_price_day1 = bs_day1.call_price() * N
    delta_day1 = bs_day1.call_delta() * N
    # Rebalancing
    shares_to_buy_day1 = delta_day1 - shares_day0
    cost_day1 = shares_to_buy_day1 * S1
    # Portfolio value
    debt_day1 = borrowing_day0 * math.exp(r * 1 / 365)
    portfolio_value_day1 = (shares_day0 * S1) - call_price_day1 - debt_day1
    profit_day1 = portfolio_value_day1  # Initial portfolio value is 0
    
    # Day 2: Stock price falls to 34.80
    S2 = 34.80
    T2 = (180 - 2) / 365
    # Assume rebalanced at end of day 1
    current_shares = delta_day1
    current_debt = debt_day1 + cost_day1
    bs_day2 = BlackScholes(S=S2, K=K, T=T2, r=r, sigma=sigma, D=D)
    call_price_day2 = bs_day2.call_price() * N
    delta_day2 = bs_day2.call_delta() * N
    # Rebalancing
    shares_to_adjust_day2 = delta_day2 - current_shares
    cost_day2 = shares_to_adjust_day2 * S2
    # Portfolio value
    debt_day2 = current_debt * math.exp(r * 1 / 365)
    portfolio_value_day2 = (current_shares * S2) - call_price_day2 - debt_day2
    profit_day2 = portfolio_value_day2
    
    # Compile results
    results = {
        'initial': {
            'call_price': call_price_day0,
            'delta': delta_day0
        },
        'hedge_setup': {
            'shares': shares_day0,
            'borrowing': borrowing_day0
        },
        'day1': {
            'profit': profit_day1,
            'rebalancing_cost': cost_day1
        },
        'day2': {
            'profit': profit_day2,
            'rebalancing_cost': cost_day2
        }
    }
    return results

def main():
    """Execute the delta hedging simulation and display results."""
    results = delta_hedge_simulation()
    
    print("Black-Scholes Delta Hedging Simulation Results")
    print("=============================================")
    print(f"Initial Setup:")
    print(f"  Call Option Value (1000 shares): ${results['initial']['call_price']:.2f}")
    print(f"  Delta (1000 shares): {results['initial']['delta']:.3f} shares")
    print(f"Hedging Strategy:")
    print(f"  Shares Purchased: {results['hedge_setup']['shares']:.3f}")
    print(f"  Amount Borrowed: ${results['hedge_setup']['borrowing']:.2f}")
    print(f"Day 1 (Stock Price = $35.50):")
    print(f"  Profit/Loss: ${results['day1']['profit']:.2f}")
    print(f"  Rebalancing Cost: ${results['day1']['rebalancing_cost']:.2f}")
    print(f"Day 2 (Stock Price = $34.80):")
    print(f"  Profit/Loss: ${results['day2']['profit']:.2f}")
    print(f"  Rebalancing Cost: ${results['day2']['rebalancing_cost']:.2f}")

if __name__ == "__main__":
    main()