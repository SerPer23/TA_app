import yfinance as yf
import pandas as pd
import time

def prices_stock(ticker, start, end, interval, retries=3, wait_seconds=10):
    for i in range(retries):
        try:
            data = yf.download(tickers=ticker, start=start, end=end, interval=interval)
            if not data.empty:
                return data
            else:
                print(f"Intento {i+1}: DataFrame vacío. Esperando {wait_seconds} segundos antes de reintentar...")
        except Exception as e:
            print(f"Intento {i+1}: Error al descargar datos: {e}")
        time.sleep(wait_seconds)
    print("No se pudo obtener datos después de varios intentos.")
    return pd.DataFrame()  # Devuelve vacío si falla todo

# Llamada a la función
df = prices_stock("AAPL", "2024-01-01", "2024-05-01", "1d")
print(df.head())


