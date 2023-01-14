# MPS - MT5-Margin-Calculator

This program provides a graphical user interface (GUI) for calculating the margin required, profit, and stop loss values of a trading strategy when using the MetaTrader 5 (MT5) terminal.

## Installation

1. Download and install the MetaTrader 5 terminal from the official website (https://www.metaquotes.net/en/metatrader5).
2. Install the `mt5` package using pip:
```
pip install mt5
```
3. Clone or download this repository to your local machine.
4. Install the required Python packages by running the command `pip install -r requirements.txt` in the root folder of the project.
5. Run the command `python app.py` in the root folder of the project to start the GUI.

## Usage

1. Open the program by running the command `python app.py` in the root folder of the project.
2. Input the relevant information, such as the currency pair, trade size, and stop loss in pips or in %.
3. Press the "Calculate" button to see the margin required, profit, and stop loss values for the specified strategy.
4. Adjust the input values as desired and recalculate as needed.

## Note

- The program uses the `mt5` package to communicate with the MT5 terminal, which is not an official API provided by Meta quotes. The package might be subject to change in the future.
- This program is provided as-is and the developer(s) of this program will not be held responsible for any damages or losses that may occur as a result of using this program.
- Always test the program in a demo account before using it in a live account.
- The program assumes that the user has basic understanding of margin trading, leverage, and risk management.
- The program uses the information provided by the user, it does not guarantee the accuracy of the results.
