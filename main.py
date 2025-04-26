import socket
import json
import random
import time
import re  # ← do czyszczenia wiadomości z interpunkcji

server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'KoxPumaBot'
token = 'oauth:2vhl3vowajgi5ymf3xp7x4vj0vgvb8'
channel = '#twojkanal'

with open('jokes.json', 'r', encoding='utf-8') as f:
    jokes = json.load(f)

sock = socket.socket()
sock.connect((server, port))
sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"NICK {nickname}\n".encode('utf-8'))
sock.send(f"JOIN {channel}\n".encode('utf-8'))

aktywny_zart = None


def oczysc_tekst(tekst):
    # Usuwa interpunkcję i zamienia na małe litery
    return re.sub(r'[^a-zA-Z0-9ąćęłńóśźż\s]', '', tekst.lower())


while True:
    resp = sock.recv(2048).decode('utf-8')

    if resp.startswith('PING'):
        sock.send("PONG :tmi.twitch.tv\n".encode('utf-8'))
        continue

    if 'PRIVMSG' in resp:
        username = resp.split('!')[0][1:]
        message_raw = resp.split('PRIVMSG')[1].split(':', 1)[1].strip()
        message = message_raw.lower()
        print(f"{username}: {message_raw}")

        current_time = time.time()

        # Timeout
        if aktywny_zart:
            if current_time - aktywny_zart['time'] > 20:
                aktywny_zart = None

        # Komenda do rozpoczęcia żartu
        if message == "!puma":
            if not aktywny_zart:
                joke = random.choice(jokes)
                aktywny_zart = {
                    'user': username,
                    'joke': joke,
                    'time': current_time
                }
                sock.send(
                    f"PRIVMSG {channel} :@{username} {joke['setup']}\n".encode(
                        'utf-8'))

        # Odpowiedź od osoby, która rozpoczęła żart
        elif aktywny_zart and username == aktywny_zart['user']:
            joke = aktywny_zart['joke']
            if current_time - aktywny_zart['time'] <= 40:
                user_reply = oczysc_tekst(message)
                expected_clean = oczysc_tekst(joke['expected'])
                if expected_clean in user_reply:
                    sock.send(
                        f"PRIVMSG {channel} :@{username} {joke['punchline']}\n"
                        .encode('utf-8'))
            aktywny_zart = None
