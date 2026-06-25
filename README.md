# Commodity Price Signal Backtester

A quantitative backtesting framework for commodity futures (Crude Oil, Natural Gas, Corn) using Python, Pandas, NumPy, yfinance, and Matplotlib. 

This project is built from scratch entirely in Jupyter Notebooks and demonstrates two core algorithmic trading strategies:
1. **Momentum (Trend Following)**: Using moving average crossovers to ride market trends.
2. **Mean-Reversion**: Using statistical Z-scores (similar to Bollinger Bands) to identify overbought or oversold conditions.

## Features
- **Data Acquisition**: Fetches daily historical price and volume data using `yfinance`.
- **Signal Generation**: Derives momentum and mean-reversion signals.
- **Backtesting Engine**: Simulates trading based on generated signals.
- **Performance Analytics**: Calculates Sharpe ratio, maximum drawdown, and rolling volatility.
- **Visualization**: Plots equity curves, underwater drawdown charts, and risk metrics.
