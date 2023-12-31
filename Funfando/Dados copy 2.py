import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
from datetime import datetime, timedelta  # Importe o módulo datetime

from binance.client import Client

from API_Key import API_Key as key
from API_Key import API_Secrect as secret

print("Iniciando!")

# Importando as credenciais da API
API_Key = key
API_Secrect = secret

client = Client(API_Key, API_Secrect)

symbol = "BTCUSDT"

interval = Client.KLINE_INTERVAL_15MINUTE

csv_filename = '/home/otavio/Documentos/Programas/Pessoais/AutoAlert_for_Trade/Funfando/Dados.csv'

while True:
    try:
        # Calcular no atrás até a data atual
        end_date = datetime.now()
        start_date = end_date - timedelta(days=365)

        # Dados do Kline, faixa gráfica
        klines = client.get_historical_klines(symbol, interval, start_date.strftime("%d %b, %Y"), end_date.strftime("%d %b, %Y"))

        # DataFrame do Pandas
        columns = ["timestamp", "open", "high", "low", "close", "volume", "close_time", "quote_asset_volume",
                   "number_of_trades", "taker_buy_base_asset_volume", "taker_buy_quote_asset_volume", "ignore"]
        df = pd.DataFrame(klines, columns=columns)

        # Convertendo o timestamp
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

        df['close'] = df['close'].astype(float)

        # CSV para análise da IA
        df.to_csv(csv_filename, index=False)  # Usamos index=False para evitar adicionar números de linha extras

        # DataFrame
        print(df)

    except Exception as e:
        print("Erro ao obter os dados:", e)
        
        print("Rodando...")       
    # Delay
    time.sleep(900)