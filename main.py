import websocket
import json
import pyfiglet
from termcolor import colored
from pyfiglet import Figlet


figlet = Figlet(font="standard")

pair = "xrpusdt"
hour_interval = "1h"
socket = f"wss://stream.binance.com:9443/ws/{pair}@kline_{hour_interval}"


def on_open(ws):
    print("Started")
    data = dict(
        method="SUBSCRIBE",
        params=[f"{pair}@kline_{hour_interval}"],
        id=1
    )
    ws.send(json.dumps(data))
    

def on_message(ws, message):
    message = json.loads(message)
    high_price = float(message["k"]["h"])
    price = float(message["k"]["c"])
    percent = 100 - (price * 100 / high_price)
    if percent >= 1:
        print(colored(f"Price is {percent}% lower than the high price", "red"))
    

def on_error(ws, error):
    print(error)
    
    
    
def run():
    wsa = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message, on_error=on_error)
    wsa.run_forever()
    

if __name__ == "__main__":
    print(colored(figlet.renderText("Binance"), "green"))
    print(colored("Made by @Dronikon (Деревянкин Никита)", "green"))
    run()