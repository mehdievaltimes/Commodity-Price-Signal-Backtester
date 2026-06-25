# Commodity Price Signal Backtester

A comprehensive quantitative backtesting framework built in Python for analyzing commodity futures. 

This project explores automated trading strategies on highly liquid futures markets (Crude Oil, Natural Gas, and Corn) using historical price action.

## Features
- **Automated Data Acquisition**: Fetches daily historical price data directly from Yahoo Finance (`yfinance`).
- **Momentum (Trend Following) Engine**: Capitalizes on market trends using Moving Average Crossovers.
- **Mean-Reversion Engine**: Capitalizes on overbought/oversold conditions using Z-Scores (Bollinger Band logic).
- **Realistic Backtesting**: Prevents look-ahead bias by shifting trading signals and models trading friction (slippage & commissions).
- **Performance Analytics**: Calculates critical quantitative metrics such as Annualized Sharpe Ratio, Maximum Drawdown, and Rolling Volatility.
- **Rich Visualizations**: Plots cumulative equity curves, underwater drawdown charts, and dynamic risk metrics.

---

## Mathematical Foundations

### 1. Momentum Strategy (Moving Average Crossover)
The momentum strategy assumes that an asset trending in one direction will continue to do so. We calculate a Fast Moving Average ($MA_{fast}$) and a Slow Moving Average ($MA_{slow}$).

- **Long Signal (+1)**: Generated when $MA_{fast} > MA_{slow}$.
- **Short Signal (-1)**: Generated when $MA_{fast} < MA_{slow}$.

### 2. Mean-Reversion Strategy (Z-Score)
The mean-reversion strategy assumes prices act like a rubber band and will revert to their historical average. We calculate the Z-Score of the current price relative to a rolling window.

$$ Z = \frac{Price_t - \mu_{rolling}}{\sigma_{rolling}} $$

- **Long Signal (+1)**: Generated when $Z < -2.0$ (Price is unusually low / Oversold).
- **Short Signal (-1)**: Generated when $Z > 2.0$ (Price is unusually high / Overbought).

### 3. Backtesting Logic
To simulate real trading without "seeing the future" (Look-ahead bias), a signal generated at the close of day $t$ is applied to the return of day $t+1$. 

$$ StrategyReturn_{t} = Signal_{t-1} \times AssetReturn_{t} $$
$$ Equity_T = \prod_{t=1}^{T} (1 + StrategyReturn_{t} - TransactionCosts_t) $$

---

## Project Structure

The entire framework is self-contained within `Commodity_Backtester.ipynb`. 
The notebook is structured modularly:
1. **Data Acquisition**: Fetching and cleaning data.
2. **Momentum Strategy**: Function logic and testing.
3. **Mean-Reversion Strategy**: Function logic and testing.
4. **Backtesting Engine**: Core simulation loop.
5. **Performance Analytics**: Risk/Reward math.
6. **Visualization**: Matplotlib charting.
7. **Transaction Costs**: Friction modeling.

---

## How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/mehdievaltimes/Commodity-Price-Signal-Backtester.git
   cd Commodity-Price-Signal-Backtester
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the Notebook**:
   ```bash
   jupyter notebook Commodity_Backtester.ipynb
   ```

5. **Run all cells** from top to bottom to see the data fetch, the signal generation, and the final equity curve plots!

---
*Built with Python, Pandas, NumPy, and Matplotlib.*
