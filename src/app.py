import tkinter as tk
from tkinter import ttk
from MT5functions import MT5
import MetaTrader5 as mt5

# Create the beggining of the interface
root = tk.Tk()
root.title('MPS software')
root.geometry('500x600')

# Functions
def initializa_MT5_terminal():
    init_text.set('connecting...')
    MT5.initialize()
    init_text.set('MT5 terminal connected!')

def pick_symbol(e):
    global symbol
    symbol = combo_2.get()

def calculate():
    calculate_text.set('loading...')
    volume = float(volume_entry.get())
    pct_change_profit = float(pct_profit_entry.get())
    pct_change_loss = float(pct_loss_entry.get())*-1
    global symbol
    symbol = str(symbol)

    point = mt5.symbol_info(symbol).point

    # Get entry price and calculate close price
    ask = mt5.symbol_info_tick(symbol).ask
    bid = mt5.symbol_info_tick(symbol).bid

    if p.get():
        price_close_profit = bid + pct_change_profit*point
        price_close_loss = ask - pct_change_loss*point
        
        # Calculate profit and loss
        profit = mt5.order_calc_profit(mt5.ORDER_TYPE_BUY, symbol, volume, bid, price_close_profit)
        loss =   mt5.order_calc_profit(mt5.ORDER_TYPE_BUY, symbol, volume, ask, price_close_loss)

        # Calculate distance in points
        point=mt5.symbol_info(symbol).point
        distance_profit = (price_close_profit - bid) / point
        distance_loss = (price_close_loss - ask) / point

        # Calculate margin for the volume
        margin = mt5.order_calc_margin(mt5.ORDER_TYPE_BUY, symbol, volume, ask)
        
        # Get minimum volume
        min_volume = mt5.symbol_info(symbol).volume_min

        # Add text to the text box
        text = f'{symbol} Margin for {volume} volume = £{margin}\nMinimum volume = {min_volume} lots\n Profit for {distance_profit} points = £{profit}\n Loss for {distance_loss} points = £{loss} \n\n\n\n\n'
        text_box.insert(1.0, text)

        print('--------------------------------------------------------------------------------------')
        print()
        print(f'{symbol} Margin for the volume {volume} lots is: £{margin}')
        print(f'Minimum volume = {min_volume} lots')
        print(f'Profit for {distance_profit} points= £{profit}')
        print(f'Loss for {distance_loss} points = £{loss}')
        print()

    else:
        price_close_profit = bid * (1 + pct_change_profit)
        price_close_loss = ask * (1 + pct_change_loss)

        # Calculate profit and loss
        profit = mt5.order_calc_profit(mt5.ORDER_TYPE_BUY, symbol, volume, bid, price_close_profit)
        loss =   mt5.order_calc_profit(mt5.ORDER_TYPE_BUY, symbol, volume, ask, price_close_loss)

        # Calculate distance in points
        point=mt5.symbol_info(symbol).point
        distance_profit = (price_close_profit - bid) / point
        distance_loss = (price_close_loss - ask) / point

        # Calculate margin for the volume
        margin = mt5.order_calc_margin(mt5.ORDER_TYPE_BUY, symbol, volume, ask)
        
        # Get minimum volume
        min_volume = mt5.symbol_info(symbol).volume_min

        # Add text to the text box
        text = f'{symbol} Margin for {volume} volume = £{margin}\nMinimum volume = {min_volume} lots\n Profit for {pct_change_profit*100}% change ({distance_profit} points) = £{profit}\n Loss for {pct_change_loss*100}% change ({distance_loss} points) = £{loss} \n\n\n\n\n'
        text_box.insert(1.0, text)

        print('--------------------------------------------------------------------------------------')
        print()
        print(f'{symbol} Margin for the volume {volume} lots is: £{margin}')
        print(f'Minimum volume = {min_volume} lots')
        print(f'Profit for a {pct_change_profit*100}% change ({distance_profit} points)= £{profit}')
        print(f'Loss for a {pct_change_loss*100}% change ({distance_loss} points) = £{loss}')
        print()

    calculate_text.set('Calculate')

def pick_market(e):
    if combo_1.get() == 'FTMO':
        combo_2.config(value=options_FTMO)
        combo_2.current(0)
    if combo_1.get() == 'Indices':
        combo_2.config(value=options_indices)
        combo_2.current(0)
    elif combo_1.get() == 'Future indices':
        combo_2.config(value=options_future_indices)
        combo_2.current(0)
    elif combo_1.get() == 'Forex':
        combo_2.config(value=options_forex)
        combo_2.current(0)
    elif combo_1.get() == 'Commodities':
        combo_2.config(value=options_commodities)
        combo_2.current(0)

# Instructions
instructions = tk.Label(root, text='Calculate Margin, Profit and Loss')
instructions.pack(pady=20)

# Initialize buttom
init_text = tk.StringVar()
init_btn = tk.Button(root, textvariable=init_text, command=lambda:initializa_MT5_terminal())
init_text.set('Connect to MT5 terminal...')
init_btn.pack()

# Dropdown menu information
markets = ['Select Market','FTMO','Indices','Future indices','Forex','Commodities']
options_FTMO = ['HK50.cash', 'GER40.cash','US30.cash', 'US100.cash', 'US500.cash']
options_indices = ['Select Symbol','HKInd', 'Ger40', 'UsaTec','UsaInd','Usa500','Ger40Mar23','UsaTecMar23','Bra50Feb23','MinDolJan23']
options_forex = ['Select Symbol','USDSEK','GBPUSD','EURUSD','USDBRL','USDCHF','USDJPY','EURGBP','CADJPY','CHFJPY','EURCAD','EURCHF','EURJPY','CADCHF','GBPCAD','GBPCHF','GBPJPY','USDCAD','AUDCAD','GBPAUD','USDSGD','GBPNZD','NZDCAD','NZDCHF','NZDJPY','NZDUSD','SGDJPY','EURHUF','USDZAR','USDHUF','USDMXN','USDNOK','USDPLN','USDRUB','USDSEK','USDTRY']
options_commodities=['Select Symbol','GOLD','SILVER', 'BrentJan23', 'NGasDec22']
options_future_indices=['Select Symbol','USDIndDec22','Ger40Mar23','Usa500Dec22','UsaTecMar23','UsaRusDec22','UsaIndDec22','Euro50Dec22','UK100Dec22','Jp225Dec22','Bra50Dec22','Neth25Dec22','GerTecDec22','USDIndDec22','MinDolDec22']

# Frame
my_frame = tk.Frame(root)
my_frame.pack(pady=20)

# Create drop box 1 / Select Market Type
combo_1 = ttk.Combobox(my_frame, values=markets)
combo_1.current(0)
combo_1.grid(row=0, column=0)

# bind the combbox
combo_1.bind('<<ComboboxSelected>>', pick_market)

# Create drop box 2 / Select Symbol
combo_2 = ttk.Combobox(my_frame, values=[' '])
combo_2.current(0)
combo_2.grid(row=0, column=1, padx=20)

# bind the combbox
combo_2.bind('<<ComboboxSelected>>', pick_symbol)

# Create volume input
volume_text = tk.Label(my_frame, text='Volume')
volume_text.grid(column=0, row=1, pady=10)

volume_entry = tk.Entry(my_frame, borderwidth=3)
volume_entry.grid(column=1, row=1)

# Create pct profit or points option

profit_option_text = tk.Label(my_frame, text='Use percentage or points?')
profit_option_text.grid(column=0, row=2, pady=10)

p = tk.BooleanVar()

tk.Radiobutton(my_frame, text="Percentage", variable=p, value=False).grid(column=1,row=2)
tk.Radiobutton(my_frame, text="Points", variable=p, value=True).grid(column=1,row=3)

# Create pct profit input
pct_profit_text = tk.Label(my_frame, text='Profit')
pct_profit_text.grid(column=0, row=4, pady=10)

pct_profit_entry = tk.Entry(my_frame, borderwidth=3)
pct_profit_entry.grid(column=1, row=4)

# Create pct loss input
pct_loss_text = tk.Label(my_frame, text='Loss')
pct_loss_text.grid(column=0, row=5, pady=10)

pct_loss_entry = tk.Entry(my_frame, borderwidth=3)
pct_loss_entry.grid(column=1, row=5)

# Calculate buttom
calculate_text = tk.StringVar()
calculate_btn = tk.Button(root, textvariable=calculate_text, command=lambda:calculate(), bg='white', fg='black', height=2, width=15)
calculate_text.set('Calculate')
calculate_btn.pack()

# Text box
text_box = tk.Text(root, height=6, width=50, padx=15, pady=15)
text_box.pack(pady=20)

root.mainloop()
