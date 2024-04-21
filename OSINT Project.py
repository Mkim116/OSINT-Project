import requests
import tkinter as tk
from tkinter import messagebox

class OSINTDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("OSINT Dashboard")
        
        # Create labels
        self.label_crypto = tk.Label(root, text="Cryptocurrency Data:")
        self.label_crypto.grid(row=0, column=0, padx=10, pady=10)
        
        # Create text area for cryptocurrency data
        self.text_crypto = tk.Text(root, width=40, height=10)
        self.text_crypto.grid(row=1, column=0, padx=10, pady=10)
        
        # Buttons to fetch data for each cryptocurrency
        self.button_fetch_bitcoin = tk.Button(root, text="Fetch Bitcoin Data", command=self.fetch_bitcoin_data)
        self.button_fetch_bitcoin.grid(row=2, column=0, padx=10, pady=5)
        self.button_fetch_ethereum = tk.Button(root, text="Fetch Ethereum Data", command=self.fetch_ethereum_data)
        self.button_fetch_ethereum.grid(row=3, column=0, padx=10, pady=5)
        self.button_fetch_dogecoin = tk.Button(root, text="Fetch Dogecoin Data", command=self.fetch_dogecoin_data)
        self.button_fetch_dogecoin.grid(row=4, column=0, padx=10, pady=5)
        self.button_fetch_binancecoin = tk.Button(root, text="Fetch Binance Coin Data", command=self.fetch_binancecoin_data)
        self.button_fetch_binancecoin.grid(row=5, column=0, padx=10, pady=5)
        
    def fetch_bitcoin_data(self):
        # Bitcoin API
        bitcoin_api = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
        try:
            response = requests.get(bitcoin_api)
            response.raise_for_status()  # Raise an error for non-200 status codes
            data = response.json()
            bitcoin_data = f"Bitcoin Data:\n{data}\n\n"
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Failed to fetch Bitcoin data: {e}")
            return
        
        self.text_crypto.delete(1.0, tk.END)  # Clear previous data
        self.text_crypto.insert(tk.END, bitcoin_data)
    
    def fetch_ethereum_data(self):
        # Ethereum API
        ethereum_api = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
        try:
            response = requests.get(ethereum_api)
            response.raise_for_status()  # Raise an error for non-200 status codes
            data = response.json()
            ethereum_data = f"Ethereum Data:\n{data}\n\n"
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Failed to fetch Ethereum data: {e}")
            return
        
        self.text_crypto.delete(1.0, tk.END)  # Clear previous data
        self.text_crypto.insert(tk.END, ethereum_data)

    def fetch_dogecoin_data(self):
        # Dogecoin API
        dogecoin_api = "https://api.coingecko.com/api/v3/simple/price?ids=dogecoin&vs_currencies=usd"
        try:
            response = requests.get(dogecoin_api)
            response.raise_for_status()  # Raise an error for non-200 status codes
            data = response.json()
            dogecoin_data = f"Dogecoin Data:\n{data}\n\n"
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Failed to fetch Dogecoin data: {e}")
            return
        
        self.text_crypto.delete(1.0, tk.END)  # Clear previous data
        self.text_crypto.insert(tk.END, dogecoin_data)

    def fetch_binancecoin_data(self):
        # Binance Coin API
        binancecoin_api = "https://api.coingecko.com/api/v3/simple/price?ids=binancecoin&vs_currencies=usd"
        try:
            response = requests.get(binancecoin_api)
            response.raise_for_status()  # Raise an error for non-200 status codes
            data = response.json()
            binancecoin_data = f"Binance Coin Data:\n{data}\n\n"
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Failed to fetch Binance Coin data: {e}")
            return
        
        self.text_crypto.delete(1.0, tk.END)  # Clear previous data
        self.text_crypto.insert(tk.END, binancecoin_data)

# Create GUI
root = tk.Tk()
app = OSINTDashboard(root)
root.mainloop()
