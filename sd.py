import streamlit as st
import requests
import random
import pandas as pd


bot_token = st.secrets['bot_token']
chat_id = st.secrets['chat_id']

st.title("Şiir Mesaj Uygulaması")

def send_telegram_message(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, params=params)
    return response.json()

def throw_random_poem():
    df = pd.read_csv("Antoloji Popüler Şiirler.csv")
    size = df.shape[0]
    id = random.choice([*range(size)])
    return df.iloc[id]["sair_adi"], df.iloc[id]["baslik"],df.iloc[id]["siir"]

def throw_random_poem_love():
    df = pd.read_csv("antoloji aşk şiirleri.csv")
    size = df.shape[0]
    id = random.choice([*range(size)])
    return df.iloc[id]["sair_adi"], df.iloc[id]["baslik"],df.iloc[id]["siir"]


if st.button("Popüler Şiirlerden gönder"):
    şiir1 = throw_random_poem()
    mesaj = f"""
{şiir1[0]} - {şiir1[1]}

{şiir1[2]}
"""

    send_telegram_message(bot_token, chat_id, mesaj)

if st.button("Aşk şiiri gönder"):
    şiir1 = throw_random_poem()
    mesaj = f"""
    {şiir1[0]} - {şiir1[1]}

    {şiir1[2]}
    """
    send_telegram_message(bot_token, chat_id, mesaj)