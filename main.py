import socket
import json
import random
import time
import re

server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'KoxPumaBot'
token = twojtoken
channel = '#twojkanal'

with open('jokes.json', 'r', encoding='utf-8') as f:
    jokes = json.load(f)

with open('oneliners.json', 'r', encoding='utf-8') as f:
    oneliners = json.load(f)

with open('yomama.json', 'r', encoding='utf-8') as f:
    yomamas = json.load(f)

sock = socket.socket()
sock.connect((server, port))
sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"NICK {nickname}\n".encode('utf-8'))
sock.send(f"JOIN {channel}\n".encode('utf-8'))

aktywny_zart = None
ostatni_oneliner = 0
ostatni_yomama = 0

def oczysc_tekst(tekst):
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

        # Timeout żartu !puma
        if aktywny_zart:
            if current_time - aktywny_zart['time'] > 20:
                aktywny_zart = None

        # Komenda do rozpoczęcia żartu !puma
        if message == "!puma":
            if not aktywny_zart:
                joke = random.choice(jokes)
                aktywny_zart = {
                    'user': username,
                    'joke': joke,
                    'time': current_time
                }
                sock.send(
                    f"PRIVMSG {channel} :@{username} {joke['setup']}\n".encode('utf-8'))

        # Odpowiedź do żartu !puma
        elif aktywny_zart and username == aktywny_zart['user']:
            joke = aktywny_zart['joke']
            if current_time - aktywny_zart['time'] <= 40:
                user_reply = oczysc_tekst(message)
                expected_clean = oczysc_tekst(joke['expected'])
                if expected_clean in user_reply:
                    sock.send(
                        f"PRIVMSG {channel} :@{username} {joke['punchline']}\n".encode('utf-8'))
            aktywny_zart = None

        # Komenda !zart - oneliner
        elif message == "!zart":
            if current_time - ostatni_oneliner >= 30:
                one = random.choice(oneliners)
                sock.send(f"PRIVMSG {channel} :{one}\n".encode('utf-8'))
                ostatni_oneliner = current_time

        # Komenda !twojastara - żart Twoja Stara
        elif message == "!twojastara":
            if current_time - ostatni_yomama >= 30:
                yomama = random.choice(yomamas)
                sock.send(f"PRIVMSG {channel} :{yomama}\n".encode('utf-8'))
                ostatni_yomama = current_time
