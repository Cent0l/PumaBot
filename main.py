import socket
import json
import random
import time

server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'KoxPumaBot'
token = 'oauth:2vhl3vowajgi5ymf3xp7x4vj0vgvb8'
channel = '#toczkens'

with open('jokes.json', 'r', encoding='utf-8') as f:
    jokes = json.load(f)

sock = socket.socket()
sock.connect((server, port))
sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"NICK {nickname}\n".encode('utf-8'))
sock.send(f"JOIN {channel}\n".encode('utf-8'))

# Tylko jeden aktywny żart naraz
aktywny_zart = None

while True:
    resp = sock.recv(2048).decode('utf-8')

    if resp.startswith('PING'):
        sock.send("PONG :tmi.twitch.tv\n".encode('utf-8'))
        continue

    if 'PRIVMSG' in resp:
        username = resp.split('!')[0][1:]
        message = resp.split('PRIVMSG')[1].split(':', 1)[1].strip().lower()
        print(f"{username}: {message}")

        current_time = time.time()

        # Jeśli ktoś już rozpoczął żart — sprawdź timeout
        if aktywny_zart:
            if current_time - aktywny_zart['time'] > 20:
                aktywny_zart = None  # timeout — kasujemy

        # Komenda do uruchomienia żartu
        if message == "!puma":
            if not aktywny_zart:
                joke = random.choice(jokes)
                aktywny_zart = {
                    'user': username,
                    'joke': joke,
                    'time': current_time
                }
                sock.send(f"PRIVMSG {channel} :@{username} {joke['setup']}\n".encode('utf-8'))

        # Odpowiedź od osoby, która rozpoczęła żart
        elif aktywny_zart and username == aktywny_zart['user']:
            joke = aktywny_zart['joke']
            if current_time - aktywny_zart['time'] <= 20:
                if joke['expected'] in message:
                    sock.send(f"PRIVMSG {channel} :@{username} {joke['punchline']}\n".encode('utf-8'))
            aktywny_zart = None  # niezależnie od wyniku — kończymy
