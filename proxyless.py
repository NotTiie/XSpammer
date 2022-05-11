import subprocess, colorama
from numpy.random.mtrand import hypergeometric
import base64
import requests, sys, time, discord_webhook
from discord_webhook import DiscordEmbed, DiscordWebhook
import string, threading, random, json, os, pyfiglet
from colorama import Fore
from time import sleep
import re, http.client, ctypes, sys, threading, json, random, sys, re, threading, time, os
from concurrent.futures import ThreadPoolExecutor, thread
import websocket
import socket
from colorama import *
from colorama import Fore
from colorama import init, Fore, Back, Style
import emoji as ej
from pypresence import Presence
import pyfade
import time, getpass, json, discum
from json import loads
from time import sleep
from json import dumps
from websocket import WebSocket
from concurrent.futures import ThreadPoolExecutor
from pymongo import MongoClient
http.client._is_legal_header_name = re.compile(b'[^\\s][^:\\r\\n]*').fullmatch
pool_sema = threading.Semaphore(value=30)
tokens = open('tokens.txt', 'r').read().splitlines()
start_time = time.time()

# Ignore this
def log_msg(message):
    try:
        requests.post('http://127.0.0.1:5000/log', data={'log': message})
    except:
        pass

# Ignore this
def log(message):
    threading.Thread(target=log_msg, args=(message,)).start()

def send_message(token, channel_id, text, antispam):
    og_text = text
    request = requests.Session()
    headers = {'Authorization':token, 
     'Content-Type':'application/json', 
     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
    if antispam:
        text += ' | ' + ''.join(random.choices((string.ascii_lowercase + string.digits), k=10))
    payload = {'content':text, 
     'tts':False}
    src = request.post(f"https://canary.discordapp.com/api/v6/channels/{channel_id}/messages", headers=headers, json=payload, timeout=10)
    if src.status_code == 429:
        try:
            ratelimit = json.loads(src.content)
            kig(colorama.Fore.RED + '[-] Ratelimit for ' + str(float(ratelimit['retry_after'] / 1000)) + ' seconds! [' + token + ']')
        except Exception as e:
            try:
                while True:
                    log(colorama.Fore.RED + f"[-] Discord propably CloudFlare banned this IP. Use a VPN. Error: {str(e)} [{token}]")
            finally:
                e = None
                del e

        if src.status_code == 200:
            log(colorama.Fore.WHITE + '[+] Message sent! [' + token + ']')
        else:
            log(colorama.Fore.RED + f"[-] Discord propably API, or CloudFlare banned this IP. Use a VPN. Error: {src.text} [{token}]")
        return src

def emojisend_message(token, channel_id, text):
    request = requests.Session()
    headers = {'Authorization':token, 
     'Content-Type':'application/json', 
     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
    if 5 > 5:
        text += ' | ' + ''.join(random.choices((string.ascii_lowercase + string.digits), k=10))
    payload = {'content':text, 
     'tts':False}
    src = request.post(f"https://canary.discordapp.com/api/v6/channels/{channel_id}/messages", headers=headers, json=payload, timeout=10)
    if src.status_code == 429:
        try:
            ratelimit = json.loads(src.content)
            log(colorama.Fore.RED + '[-] Ratelimit for ' + str(float(ratelimit['retry_after'] / 1000)) + ' seconds! [' + token + ']')
        except Exception as e:
            try:
                log(colorama.Fore.RED + f"[-] Discord propably CloudFlare banned this IP. Use a VPN. Error: {str(e)} [{token}]")
            finally:
                e = None
                del e

        if src.status_code == 200:
            log(colorama.Fore.WHITE + '[+] Message sent! [' + token + ']')
        else:
            log(colorama.Fore.RED + f"[-] Discord propably API, or CloudFlare banned this IP. Use a VPN. Error: {src.text} [{token}]")
        return src


def online(token, game):
    ws = websocket.WebSocket()
    status = 'online'
    ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')
    hello = json.loads(ws.recv())
    heartbeat_interval = hello['d']['heartbeat_interval']
    gamejson = {'name':game, 
     'type':0}
    auth = {'op':2, 
     'd':{'token':token, 
      'properties':{'$os':sys.platform, 
       '$browser':'RTB', 
       '$device':f"{sys.platform} Device"}, 
      'presence':{'game':gamejson, 
       'status':status, 
       'since':0, 
       'afk':False}}, 
     's':None, 
     't':None}
    ws.send(json.dumps(auth))
    log(colorama.Fore.WHITE + '[+] Set status as: ' + game + ' [' + token + ']')
    ack = {'op':1, 
     'd':None}
    while 1:
        time.sleep(heartbeat_interval / 1000)
        try:
            ws.send(json.dumps(ack))
        except Exception as e:
            try:
                break
            finally:
                e = None
                del e

def nickname():
    s=u''
    for i in range(random.randint(1, 32)):
        s=s+chr(random.randint(0x4E00, 0x9FA5))
    return s


def set_mping(msg):
    print(msg)


def spam(tokens, channel_id, text, antispam, delay, amount):
    for x in range(int(amount)):
        token = random.choice(tokens)
        threading.Thread(target=send_message, args=(token, channel_id, text, antispam)).start()
        sleep(delay)

def emojispam(tokens, channel_id, text, delay, amount):
    for x in range(int(amount)):
        token = random.choice(tokens)
        if 5 > 5:
            pass
        else:
            threading.Thread(target=emojisend_message, args=(token, channel_id, text)).start()
            sleep(delay)


def fastspam(token, channel_id, text, antispam, amount):
    og_text = text
    request = requests.Session()
    headers = {'Authorization':token, 
     'Content-Type':'application/json', 
     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
    for x in range(int(amount)):
        if 5 > 5:
            pass
        else:
            if antispam:
                text += ' | ' + ''.join(random.choices((string.ascii_lowercase + string.digits), k=10))
            payload = {'content':text, 
             'tts':False}
            src = request.post(f"https://canary.discordapp.com/api/v6/channels/{channel_id}/messages", headers=headers, json=payload, timeout=10)
        if src.status_code == 429:
            try:
                ratelimit = json.loads(src.content)
                time.sleep(float(ratelimit['retry_after'] / 1000))
            except:
                pass

        else:
            if src.status_code == 401:
                break
            else:
                if src.status_code == 404:
                    break
                else:
                    if src.status_code == 403:
                        break

def emojifastspam(token, channel_id, text, amount):
    og_text = text
    request = requests.Session()
    headers = {'Authorization':token, 
     'Content-Type':'application/json', 
     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
    for x in range(int(amount)):
        if 5 > 5:
            pass
        else:
            payload = {'content':text, 
             'tts':False}
            src = request.post(f"https://canary.discordapp.com/api/v6/channels/{channel_id}/messages", headers=headers, json=payload, timeout=10)
        if src.status_code == 429:
            try:
                ratelimit = json.loads(src.content)
                time.sleep(float(ratelimit['retry_after'] / 1000))
            except:
                pass

        else:
            if src.status_code == 401:
                break
            else:
                if src.status_code == 404:
                    break
                else:
                    if src.status_code == 403:
                        break

def replyspammer(token, channel_id, message_id, text, amount):
    og_text = text
    request = requests.Session()
    headers = {'Authorization':token, 
     'Content-Type':'application/json', 
     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
    for x in range(int(amount)):
        if 5 > 5:
            pass
        else:
            payload = {'content':text, 
             'tts':False}
            payload['message_reference'] = {
                "channel_id": channel_id,
                "message_id": message_id
            }
            src = request.post(f"https://canary.discordapp.com/api/v6/channels/{channel_id}/messages", headers=headers, json=payload, timeout=10)
        if src.status_code == 429:
            try:
                ratelimit = json.loads(src.content)
                time.sleep(float(ratelimit['retry_after'] / 1000))
            except:
                pass

        else:
            if src.status_code == 401:
                pass
            else:
                if src.status_code == 404:
                    pass
                else:
                    if src.status_code == 403:
                        pass

def nickchanger(token, guild_Id):
     pool_sema.acquire()
     try:
          try:
               headers = {
               'authority':'canary.discord.com', 
               'method':'PATCH', 
               'path':'/api/v9/users/@me', 
               'scheme':'https', 
               'accept':'*/*', 
               'accept-encoding':'gzip, deflate, br', 
               'accept-language':'en-US', 
               'authorization':token, 
               'content-length':'124', 
               'content-type':'application/json', 
               'origin':'https://canary.discord.com', 
               'sec-fetch-dest':'empty', 
               'sec-fetch-mode':'cors', 
               'sec-fetch-site':'same-origin', 
               'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.616 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36', 
               'x-debug-options':'bugReporterEnabled', 
               'x-super-properties':'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MTYiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjQ1OCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5ODgyMywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0='
               }
               nick = requests.patch(f'https://canary.discordapp.com/api/v6/guilds/{guild_Id}/members/@me', headers=headers, json={'nick': str(nickname())})
          except Exception as e:
               try:
                log(e)
               finally:
                    e = None
                    del e

     finally:
          pool_sema.release()


def customnickchanger(token, guild_Id, custom):
     pool_sema.acquire()
     try:
          try:
               headers = {
               'authority':'canary.discord.com', 
               'method':'PATCH', 
               'path':'/api/v9/users/@me', 
               'scheme':'https', 
               'accept':'*/*', 
               'accept-encoding':'gzip, deflate, br', 
               'accept-language':'en-US', 
               'authorization':token, 
               'content-length':'124', 
               'content-type':'application/json', 
               'origin':'https://canary.discord.com', 
               'sec-fetch-dest':'empty', 
               'sec-fetch-mode':'cors', 
               'sec-fetch-site':'same-origin', 
               'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.616 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36', 
               'x-debug-options':'bugReporterEnabled', 
               'x-super-properties':'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MTYiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjQ1OCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5ODgyMywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0='
               }
               nick = requests.patch(f'https://canary.discordapp.com/api/v6/guilds/{guild_Id}/members/@me', headers=headers, json={'nick': custom})
          except Exception as e:
               try:
                log(e)
               finally:
                    e = None
                    del e

     finally:
          pool_sema.release()

def join(invite, token):
    pool_sema.acquire()
    try:
        try:
            headers = {':authority':'canary.discord.com', 
             ':method':'POST', 
             ':path':'/api/v9/invites/' + invite, 
             ':scheme':'https', 
             'accept':'*/*', 
             'accept-encoding':'gzip, deflate, br', 
             'accept-language':'en-US', 
             'authorization':token, 
             'content-length':'0', 
             'Cookie':f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US", 
             'origin':'https://canary.discord.com', 
             'sec-fetch-dest':'empty', 
             'sec-fetch-mode':'cors', 
             'sec-fetch-site':'same-origin', 
             'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.600 Chrome/91.0.4472.106 Electron/13.1.4 Safari/537.36          ', 
             'x-context-properties':'eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==      ', 
             'x-debug-options':'bugReporterEnabled', 
             'x-super-properties':'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0='}
            a = requests.post(('https://discordapp.com/api/v9/invites/' + invite), headers=headers)
            if a.status_code == 200:
                log(colorama.Fore.WHITE + '[+] Joined a server with ' + invite + '! [' + token + ']')
            else:
                log(colorama.Fore.RED + f"[-] Discord propably API banned this IP. Use a VPN. Error: {a.text} [{token}]")
        except Exception as e:
            try:
                log(colorama.Fore.RED + f"[-] Discord propably CloudFlare banned this IP. Use a VPN. Error: {str(e)} [{token}]")
            finally:
                e = None
                del e

    finally:
        pool_sema.release()


def set_bio(token, bio):
    pool_sema.acquire()
    try:
        try:
            headers = {':authority':'canary.discord.com', 
             ':method':'PATCH', 
             ':path':'/api/v9/users/@me', 
             ':scheme':'https', 
             'accept':'*/*', 
             'accept-encoding':'gzip, deflate, br', 
             'accept-language':'en-US', 
             'authorization':token, 
             'content-length':'124', 
             'content-type':'application/json', 
             'Cookie':f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US", 
             'origin':'https://canary.discord.com', 
             'sec-fetch-dest':'empty', 
             'sec-fetch-mode':'cors', 
             'sec-fetch-site':'same-origin', 
             'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.616 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36', 
             'x-debug-options':'bugReporterEnabled', 
             'x-super-properties':'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MTYiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjQ1OCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5ODgyMywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0='}
            a = requests.patch('https://canary.discord.com/api/v9/users/@me', headers=headers, json={'bio': bio})
            if a.status_code == 200:
                log(colorama.Fore.WHITE + '[+] Set bio to: ' + bio + '! [' + token + ']')
            else:
                log(colorama.Fore.RED + f"[-] Discord propably API banned this IP. Use a VPN. Error: {a.text} [{token}]")
        except Exception as e:
            try:
                log(colorama.Fore.RED + f"[-] Discord propably CloudFlare banned this IP. Use a VPN. Error: {str(e)} [{token}]")
            finally:
                e = None
                del e

    finally:
        pool_sema.release()


def leave(guild_id, token):
    pool_sema.acquire()
    try:
        try:
            data = {'lurking': False}
            headers = {':authority':'canary.discord.com', 
             ':method':'DELETE', 
             ':path':'/api/v9/users/@me/guilds/' + guild_id, 
             ':scheme':'https', 
             'accept':'*/*', 
             'accept-encoding':'gzip, deflate, br', 
             'accept-language':'en-GB', 
             'authorization':token, 
             'content-length':'17', 
             'content-type':'application/json', 
             'Cookie':f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US", 
             'origin':'https://canary.discord.com', 
             'sec-fetch-dest':'empty', 
             'sec-fetch-mode':'cors', 
             'sec-fetch-site':'same-origin', 
             'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.40 Chrome/91.0.4472.164 Electron/13.2.2 Safari/537.36', 
             'x-debug-options':'bugReporterEnabled', 
             'x-super-properties':'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC40MCIsIm9zX3ZlcnNpb24iOiIxMC4wLjIyMDAwIiwib3NfYXJjaCI6Ing2NCIsInN5c3RlbV9sb2NhbGUiOiJzayIsImNsaWVudF9idWlsZF9udW1iZXIiOjk2MzU1LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=='}
            a = requests.delete(('https://canary.discord.com/api/v9/users/@me/guilds/' + str(guild_id)), json=data, headers=headers)
            if a.status_code == 204:
                log(colorama.Fore.WHITE + '[+] Left ' + guild_id + '! [' + token + ']')
            else:
                log(colorama.Fore.RED + f"[-] Discord propably API banned this IP. Use a VPN. Error: {a.text} [{token}]")
        except Exception as e:
            try:
                log(colorama.Fore.RED + f"[-] Discord propably CloudFlare banned this IP. Use a VPN. Error: {str(e)} [{token}]")
            finally:
                e = None
                del e

    finally:
        pool_sema.release()


def get_headers(token):
    return {'Content-Type':'application/json', 
     'Accept':'*/*', 
     'Accept-Encoding':'gzip, deflate, br', 
     'Accept-Language':'en-US', 
     'Cookie':f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US", 
     'DNT':'1', 
     'origin':'https://discord.com', 
     'TE':'Trailers', 
     'X-Super-Properties':'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9', 
     'authorization':token, 
     'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}


def randstr(lenn):
    alpha = 'abcdefghijklmnopqrstuvwxyz0123456789'
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]

    return text

def run(token) :
    ws = WebSocket()
    ws.connect("wss://gateway.discord.gg/?v=8&encoding=json")
    hello = loads(ws.recv())
    heartbeat_interval = hello['d']['heartbeat_interval']
    ws.send(dumps({"op": 2,"d": {"token": token,"properties": {"$os": "windows","$browser": "Discord","$device": "desktop"}}}))
    ws.send(dumps({"op": 4,"d": {"guild_id": guild_id,"channel_id": chid,"self_mute": True,"self_deaf": True}}))
    ws.send(dumps({"op": 18,"d": {"type": "guild","guild_id": guild_id,"channel_id": chid,"preferred_region": "singapore"}}))
    while True:
        sleep(heartbeat_interval/1000)
        try:
            ws.send(dumps({"op": 1,"d": None}))
        except Exception:
            break

def scrape_channels(server, token):
    try:
        headers = {'Authorization':token, 
         'Content-Type':'application/json', 
         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        data = requests.get(f"https://canary.discord.com/api/v8/guilds/{server}/channels", headers=headers, timeout=10).json()
        channel_ids = []
        try:
            for channel in data:
                channel_ids.append(channel['id'])

        except:
            log(colorama.Fore.RED + f"[-] Discord propably API banned this IP. Use a VPN. Error: {data.text} [{token}]")

        return channel_ids
    except Exception as e:
        try:
            log(colorama.Fore.RED + f"[-] Discord propably CloudFlare banned this IP. Use a VPN. Error: {str(e)} [{token}]")
        finally:
            e = None
            del e


def multispammer(tokens, guild_id, text, antispam, delay, amount):
    og_text = text
    channels = scrape_channels(guild_id, random.choice(tokens))
    for channel in channels:
        threading.Thread(target=spam, args=(tokens, channel, text, antispam, delay, amount)).start()


def thread_spammer(channel_id, message, thread_name, token, amount):
    try:
        headers = {'accept':'*/*',  'accept-encoding':'gzip, deflate, br', 
         'accept-language':'en-GB', 
         'authorization':token, 
         'content-length':'90', 
         'content-type':'application/json', 
         'cookie':f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US", 
         'origin':'https://discord.com', 
         'sec-fetch-dest':'empty', 
         'sec-fetch-mode':'cors', 
         'sec-fetch-site':'same-origin', 
         'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36', 
         'x-debug-options':'bugReporterEnabled', 
         'x-super-properties':'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9'}
        for x in range(int(amount)):
            try:
                thread_name_new = thread_name + ' | ' + ''.join(random.choices((string.ascii_lowercase + string.digits), k=10))
                data = {'name':thread_name_new,  'type':'11',  'auto_archive_duration':'1440',  'location':'Thread Browser Toolbar'}
                out = requests.post(f"https://discord.com/api/v9/channels/{str(channel_id)}/threads", headers=headers, json=data)
                if out.status_code == 429:
                    try:
                        ratelimit = json.loads(out.content)
                        time.sleep(float(ratelimit['retry_after'] / 1000))
                    except:
                        pass

                else:
                    thread_id = out.json()['id']
                    log(colorama.Fore.WHITE + '[+] Thread ' + thread_name + ' created! [' + token + ']')
                    send_message(token, thread_id, message, False)
            except Exception as e:
                try:
                    pass
                finally:
                    e = None
                    del e

    except Exception as e:
        try:
            log(colorama.Fore.RED + f"[-] Discord propably CloudFlare banned this IP. Use a VPN. Error: {str(e)} [{token}]")
        finally:
            e = None
            del e


def reaction(channel_id, message_id, addorrem, emoji_original, token):
    pool_sema.acquire()
    try:
        try:
            headers = get_headers(token)
            emoji = ej.emojize(emoji_original, use_aliases=True)
            addorrem = addorrem.lower()
            if addorrem == 'add':
                a = requests.put(f"https://discordapp.com/api/v6/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me", headers=headers)
                if a.status_code == 204:
                    log(colorama.Fore.WHITE + f"[+] Reaction {emoji_original} added! [{token}]")
                else:
                    log(colorama.Fore.RED + f"[-] Discord propably API banned this IP. Use a VPN. Error: {a.text} [{token}]")
            elif addorrem == 'rem':
                a = requests.delete(f"https://discordapp.com/api/v6/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me", headers=headers)
                if a.status_code == 204:
                    log(colorama.Fore.WHITE + f"[+] Reaction {emoji_original} removed! [{token}]")
                else:
                    log(colorama.Fore.RED + f"[-] Discord propably API banned this IP. Use a VPN. Error: {a.text} [{token}]")
        except Exception as e:
            try:
                log(colorama.Fore.RED + f"[-] Discord propably CloudFlare banned this IP. Use a VPN. Error: {str(e)} [{token}]")
            finally:
                e = None
                del e

    finally:
        pool_sema.release()


def friender(token, user):
    pool_sema.acquire()
    try:
        try:
            user = user.split('#')
            headers = {'accept':'*/*', 
             'accept-encoding':'gzip, deflate, br', 
             'accept-language':'en-GB', 
             'authorization':token, 
             'content-length':'90', 
             'content-type':'application/json', 
             'cookie':f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US", 
             'origin':'https://discord.com', 
             'sec-fetch-dest':'empty', 
             'sec-fetch-mode':'cors', 
             'sec-fetch-site':'same-origin', 
             'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36', 
             'x-debug-options':'bugReporterEnabled', 
             'x-super-properties':'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9'}
            payload = {'username':user[0], 
             'discriminator':user[1]}
            src = requests.post('https://canary.discordapp.com/api/v6/users/@me/relationships', headers=headers, json=payload)
            if src.status_code == 204:
                log(colorama.Fore.WHITE + f"[+] Friend request sent to {user[0]}#{user[1]}! [{token}]")
            if src.status_code == 400:
                log(colorama.Fore.RED + f"[-] Couldnt send friend request to {user[0]}#{user[1]}! He propably has turned off friend requests. [{token}]")
            else:
                log(colorama.Fore.RED + f"[-] Discord propably API banned this IP. Use a VPN. Error: {src.text} [{token}]")
        except Exception as e:
            try:
                log(colorama.Fore.RED + f"[-] Discord propably CloudFlare banned this IP. Use a VPN. Error: {str(e)} [{token}]")
            finally:
                e = None
                del e

    finally:
        pool_sema.release()


def dmspammer(token, userid, text, amount):
    try:
        headers = {'accept':'*/*',  'accept-encoding':'gzip, deflate, br', 
         'accept-language':'en-GB', 
         'authorization':token, 
         'content-length':'90', 
         'content-type':'application/json', 
         'cookie':f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US", 
         'origin':'https://discord.com', 
         'sec-fetch-dest':'empty', 
         'sec-fetch-mode':'cors', 
         'sec-fetch-site':'same-origin', 
         'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36', 
         'x-debug-options':'bugReporterEnabled', 
         'x-super-properties':'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9'}
        payload = {'recipient_id': userid}
        src = requests.post('https://canary.discordapp.com/api/v6/users/@me/channels', headers=headers, json=payload, timeout=10)
        dm_json = json.loads(src.content)
        payload = {'content':text,  'tts':False}
        for x in range(int(amount)):
            src = requests.post(f"https://canary.discordapp.com/api/v6/channels/{dm_json['id']}/messages", headers=headers, json=payload, timeout=10)
            if src.status_code == 429:
                ratelimit = json.loads(src.content)
                time.sleep(float(ratelimit['retry_after'] / 1000))
            else:
                if src.status_code == 200:
                    log(colorama.Fore.WHITE + f"[+] DM sent to {user_id}! [{token}]")
                else:
                    if src.status_code == 200:
                        log(colorama.Fore.RED + f"[-] Couldnt send dm to {user_id}! He propably has closed DMs. [{token}]")
                    else:
                        log(colorama.Fore.RED + f"[-] Discord propably API banned this IP. Use a VPN. Error: {src.text} [{token}]")

    except Exception as e:
        try:
            log(colorama.Fore.RED + f"[-] Discord propably CloudFlare banned this IP. Use a VPN. Error: {str(e)} [{token}]")
        finally:
            e = None
            del e


def pfpchanger(token, img64):
    headers = {
            "Authorization":
            token,
            "accept":
            "*/*",
            "accept-language":
            "en-US",
            "connection":
            "keep-alive",
            "cookie":
            f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
            "DNT":
            "1",
            "origin":
            "https://discord.com",
            "sec-fetch-dest":
            "empty",
            "sec-fetch-mode":
            "cors",
            "sec-fetch-site":
            "same-origin",
            "referer":
            "https://discord.com/channels/@me",
            "TE":
            "Trailers",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
            "X-Super-Properties":
            "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
        }

    requests.patch('https://discord.com/api/v9/users/@me', headers=headers, json={"avatar": "data:image/png;base64," + img64})



def loading_animation():
    final_text = 'XSPAMMER'
    text = ''
    for character in final_text:
        ctypes.windll.kernel32.SetConsoleTitleW(text)
        text += character
        time.sleep(0.05)

    ctypes.windll.kernel32.SetConsoleTitleW(final_text)

def loading_print(final_text):
    text = ''
    for character in final_text:
        sys.stdout.write(character)
        time.sleep(0.025)


def scrape_members(guild_id, channel_id, token):
    open('members.txt', 'w').write('')
    os.system(f"XSpammerMPINGScraper.exe {token} {guild_id} {channel_id}")
    while True:
        members = open('members.txt').read()
        if len(members) == 0:
            continue
        break


def bypass_screening(invite_code, guild_id, token):
    pool_sema.acquire()
    try:
        try:
            member_verif_url = f"https://canary.discord.com/api/v9/guilds/{guild_id}/member-verification?with_guild=false&invite_code=" + invite_code
            headers = get_headers(token)
            out = requests.get(member_verif_url, headers=headers).json()
            log(str(out))
            data = {}
            data['version'] = out['version']
            data['form_fields'] = out['form_fields']
            data['form_fields'][0]['response'] = True
            final_verif_url = f"https://canary.discord.com/api/v9/guilds/{str(guild_id)}/requests/@me"
            requests.put(final_verif_url, headers=headers, json=data)
        except Exception as e:
            try:
                log(e)
            finally:
                e = None
                del e

    finally:
        pool_sema.release()


def report(token, channel_id, guild_id, message_id, reason):
    headers = get_headers(token)
    payload = {'channel_id':channel_id, 
     'guild_id':guild_id, 
     'message_id':message_id, 
     'reason':reason}
    while True:
        r = requests.post('https://discord.com/api/v6/report', headers=headers, json=payload)
        if r.status_code == 201:
            log(colorama.Fore.WHITE + '[+] Reported ' + message_id + '! [' + token + ']')
        else:
            if r.status_code == 401:
                log(colorama.Fore.RED + '[-] Token phonelocked! [' + token + ']')
                break
            else:
                log(str(r.content) + ' ' + str(r.status_code))


def hypesquad_changer(hypesquad, token):
    pool_sema.acquire()
    try:
        try:
            headers = {'Authorization':token, 
             'Content-Type':'application/json', 
             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
            if hypesquad == 'bravery':
                payload = {'house_id': 1}
            elif hypesquad == 'brilliance':
                payload = {'house_id': 2}
            elif hypesquad == 'balance':
                payload = {'house_id': 3}
            elif hypesquad == 'random':
                houses = [
                 1, 2, 3]
                payload = {'house_id': random.choice(houses)}
            else:
                houses = [
                 1, 2, 3]
                payload = {'house_id': random.choice(houses)}
            requests.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
        except Exception as e:
            try:
                log(e)
            finally:
                e = None
                del e

    finally:
        pool_sema.release()

menu = """                     
            :::    :::  ::::::::  :::::::::     :::     ::::    ::::  ::::    ::::  :::::::::: :::::::::  
            :+:    :+: :+:    :+: :+:    :+:  :+: :+:   +:+:+: :+:+:+ +:+:+: :+:+:+ :+:        :+:    :+: 
             +:+  +:+  +:+        +:+    +:+ +:+   +:+  +:+ +:+:+ +:+ +:+ +:+:+ +:+ +:+        +:+    +:+ 
              +#++:+   +#++:++#++ +#++:++#+ +#++:++#++: +#+  +:+  +#+ +#+  +:+  +#+ +#++:++#   +#++:++#:  
             +#+  +#+         +#+ +#+       +#+     +#+ +#+       +#+ +#+       +#+ +#+        +#+    +#+ 
            #+#    #+# #+#    #+# #+#       #+#     #+# #+#       #+# #+#       #+# #+#        #+#    #+# 
            ###    ###  ########  ###       ###     ### ###       ### ###       ### ########## ###    ###                                       

                            +══════════════════════════════╦════════════════════════════════+
                            |      [1] Joiner              |      [11] Member Screening     |
                            |      [2] Spammer             |      [12] Hypesquad Changer    |
                            |      [3] Leaver              |      [13] Multichannel Spammer |
                            |      [4] Reaction Spammer    |      [14] VC Spammer           |
                            |      [5] Thread Spammer      |      [15] Emoji Spammer        |
                            |      [6] Friend Spammer      |      [16] Token Checker        |
                            |      [7] DM Spammer          |      [17] Status Changer       |
                            |      [8] Nickname Changer    |      [18] Bio Changer          |
                            |      [9] PFP Changer         |      [19] Menu Colors          |
                            |      [10] Reply Spammer      |      [20] Exit                 | 
                            +══════════════════════════════╧════════════════════════════════+
"""

config = json.load(open("config.json", "r"))
menucolor = config["menucolor"]
if menucolor == "env":
  menucolor = os.environ["menucolor"]

os.system('cls')
threading.Thread(target=loading_animation).start()
print('Credits to vast for menu\n')
while True:
    if menucolor == "Red":
        print(pyfade.Fade.Horizontal(pyfade.Colors.white_to_red, menu))
        choice = input(pyfade.Fade.Horizontal(pyfade.Colors.red_to_white, f" \nroot@{getpass.getuser()}: "))
    elif menucolor == "Green":
        print(pyfade.Fade.Horizontal(pyfade.Colors.yellow_to_green, menu))
        choice = input(pyfade.Fade.Horizontal(pyfade.Colors.yellow_to_green, f" \nroot@{getpass.getuser()}: "))
    elif menucolor == "Blue":
        print(pyfade.Fade.Horizontal(pyfade.Colors.cyan_to_blue, menu))
        choice = input(pyfade.Fade.Horizontal(pyfade.Colors.cyan_to_blue, f" \nroot@{getpass.getuser()}: "))
    elif menucolor == "Orange":
        print(pyfade.Fade.Horizontal(pyfade.Colors.yellow_to_red, menu))
        choice = input(pyfade.Fade.Horizontal(pyfade.Colors.yellow_to_red, f" \nroot@{getpass.getuser()}: "))
    else:
        print(pyfade.Fade.Horizontal(pyfade.Colors.white_to_red, menu))
        choice = input(pyfade.Fade.Horizontal(pyfade.Colors.red_to_white, f" \nroot@{getpass.getuser()}: "))
    if choice == '1':
        loading_print(f"Invite: ")
        invite = input()
        invite = invite.replace('https://discord.gg/', '')
        invite = invite.replace('https://discord.com/invite/', '')
        invite = invite.replace('discord.gg/', '')
        tokens = open('tokens.txt', 'r').read().splitlines()
        for token in tokens:
            threading.Thread(target=join, args=(invite, token)).start()

    elif choice == '2':
        tokens = open('tokens.txt', 'r').read().splitlines()
        file = open("tokens.txt", "r")
        token_count = 0
        for line in file:
            if line != "\n":
                token_count += 1
        loading_print(f"Channel ID: ")
        channel_id = input()
        loading_print(f"Delay [100-150 recommended]: ")
        delay = input()
        loading_print(f"Message: ")
        msg = input()
        amount = input('Amount of messages: ')
        amount = int(amount)
        loading_print(f"Bypass AntiSpam [y/n]: ")
        antispam = input().lower()
        loading_print(f"EXTREME SPEED MODE? [y/n]: ")
        extreme_speed = input().lower()
        if extreme_speed == 'y':
            amount = int(amount/token_count)
            for token in tokens:
                threading.Thread(target=fastspam, args=(token, channel_id, msg, antispam, amount)).start()
        else:
            if antispam == 'y':
                antispam = True
            else:
                antispam = False
            delay = int(delay) / 1000
            threading.Thread(target=spam, args=(tokens, channel_id, msg, antispam, delay, amount)).start()


    elif choice == '3':
        tokens = open('tokens.txt', 'r').read().splitlines()
        loading_print(f"Guild ID: ")
        guild_id = input()
        for token in tokens:
            threading.Thread(target=leave, args=(guild_id, token)).start()

    elif choice == '4':
        tokens = open('tokens.txt', 'r').read().splitlines()
        loading_print(f"Channel ID: ")
        channel_id = input()
        loading_print(f"Message ID: ")
        message_id = input()
        loading_print(f"Add reaction, or remove? [add/rem] ")
        addorrem = input()
        loading_print(f"Emoji [example: :joy:]: ")
        emoji = input()
        for token in tokens:
            threading.Thread(target=reaction, args=(channel_id, message_id, addorrem, emoji, token)).start()

    elif choice == '5':
        tokens = open('tokens.txt', 'r').read().splitlines()
        loading_print(f"Channel ID: ")
        channel_id = input()
        loading_print(f"Thread name: ")
        thread_name = input()
        loading_print(f"Message: ")
        message = input()
        amount = input('Amount of threads for each token: ')
        for token in tokens:
            threading.Thread(target=thread_spammer, args=(channel_id, message, thread_name, token, amount)).start()

    elif choice == '6':
        tokens = open('tokens.txt', 'r').read().splitlines()
        loading_print(f"Discord Username + Discriminator [example: H0LLOW#2648]: ")
        user = input()
        for token in tokens:
            threading.Thread(target=friender, args=(token, user)).start()

    elif choice == '7':
        tokens = open('tokens.txt', 'r').read().splitlines()
        loading_print(f"User ID: ")
        user_id = input()
        loading_print(f"Message: ")
        message = input()
        amount = input('Amount of DMS: ')
        amount = int(amount)
        for token in tokens:
            threading.Thread(target=dmspammer, args=(token, user_id, message, amount)).start()

    elif choice == "8":
        tokens = open('tokens.txt', 'r').read().splitlines()
        guild_Id = input(f"Guild ID: ")
        custom = input('Custom nickname? [Y/N]: ')
        if custom == "Y":
            customname = input('Custom name: ')
            custom = customname
            for token in tokens:
                threading.Thread(target=customnickchanger, args=(token, guild_Id, custom)).start()
        else:
            for token in tokens:
                threading.Thread(target=nickchanger, args=(token, guild_Id)).start()

    elif choice == '9':
        img = input('Path to image (For example C:\\Users\\Alex\\Images\\Dog.png): ')
        with open(img, "rb") as image_file:
            base64image = base64.b64encode(image_file.read())
            base64image = base64image.decode('utf-8')
        img64 = base64image
        for token in tokens:
            threading.Thread(target=pfpchanger, args=(token, img64)).start()

    elif choice == '10':
        tokens = open('tokens.txt', 'r').read().splitlines()
        channel_id = input('Channel ID: ')
        message_id = input('Message ID: ')
        text = input('Message: ')
        amount = input('Amount of replies for each token: ')
        amount = int(amount)
        for token in tokens:
            threading.Thread(target=replyspammer, args=(token, channel_id, message_id, text, amount)).start()

    elif choice == '11':
        loading_print(f"Invite: ")
        invite = input()
        invite = invite.replace('https://discord.gg/', '')
        invite = invite.replace('https://discord.com/invite/', '')
        invite = invite.replace('discord.gg/', '')
        loading_print(f"Guild ID: ")
        guild_id = input()
        tokens = open('tokens.txt', 'r').read().splitlines()
        for token in tokens:
            threading.Thread(target=bypass_screening, args=(invite, guild_id, token)).start()

    elif choice == '12':
        print('\n| HYPESQUADS\n\n| Balance\n| Brilliance\n| Bravery\n| Random\n')
        loading_print(f"Hypesquad: ")
        hypesquad = input().lower()
        tokens = open('tokens.txt', 'r').read().splitlines()
        for token in tokens:
            threading.Thread(target=hypesquad_changer, args=(hypesquad, token)).start()

    elif choice == '13':
        tokens = open('tokens.txt', 'r').read().splitlines()
        guild_id = input('Guild ID: ')
        delay = input('Delay [100-150 recommended]: ')
        msg = input('Message: ')
        amount = input('Amount of messages: ')
        amount = int(amount)
        amount = amount/2
        amount = int(amount)
        antispam = input('Bypass AntiSpam [y/n]: ').lower()
        if antispam == 'y':
            antispam = True
        else:
            antispam = False
        delay = int(delay) / 1000
        threading.Thread(target=multispammer, args=(tokens, guild_id, msg, antispam, delay, amount)).start()
    elif choice == '14':
        tokens = open('tokens.txt', 'r').read().splitlines()
        guild_id = input("Guild ID: ")
        chid = input("Channel ID: ")
        executor = ThreadPoolExecutor(max_workers=int(1000000))
        for token in tokens:
            executor.submit(run, token)

    elif choice == '15':
        tokens = open('tokens.txt', 'r').read().splitlines()
        file = open("tokens.txt", "r")
        token_count = 0
        for line in file:
            if line != "\n":
                token_count += 1
        channel_id = input(f"Channel ID: ")
        msg = input('Message: ')
        delay = input('Delay [100-150 recommended]: ')
        amount = input('Amount of messages: ')
        amount = int(amount)
        extreme_speed = input(f"EXTREME SPEED MODE? [y/n]: ").lower()
        msg = msg.lower()
        msg = msg.replace(" ", "")
        with open('emojitext.txt', 'w') as f:
            for i in range(len(msg)):
                f.write(':regional_indicator_' + msg[i] + ': ')
        msg = open('emojitext.txt', 'r').read()
        if extreme_speed == 'y':
            amount = int(amount/token_count)
            for token in tokens:
                threading.Thread(target=emojifastspam, args=(token, channel_id, msg, amount)).start()
        else:
            delay = int(delay) / 1000
            threading.Thread(target=emojispam, args=(tokens, channel_id, msg, delay, amount)).start()

    elif choice == '16':
        tokens = ''
        with open('tokens.txt') as f:
            for line in f:
                token = line.strip('\n')
                headers = {'Content-Type':'application/json',  'authorization':token}
                url = 'https://discordapp.com/api/v6/users/@me/library'
                r = requests.get(url, headers=headers)
                if r.status_code == 200:
                    print(f"{Fore.WHITE}[+] " + token)
                    tokens += token + '\n'
                else:
                    print(f"{Fore.RED}[-] " + token)

        open('tokens.txt', 'w').write(tokens[:-1])
    elif choice == '17':
        tokens = open('tokens.txt', 'r').read().splitlines()
        loading_print(f"Message: ")
        text = input()
        for token in tokens:
            threading.Thread(target=online, args=(token.replace('\n', ''), text)).start()

    else:
        if choice == '18':
            tokens = open('tokens.txt', 'r').read().splitlines()
            loading_print(f"Bio: ")
            bio = input()
            for token in tokens:
                threading.Thread(target=set_bio, args=(token.replace('\n', ''), bio)).start()

        else:
            pass

        if choice == '19':
            color = input('Color [Red, Green, Blue, Orange]: ')
            print('Changing color..')
            with open('config.json', 'w') as f:
                f.write('''{
    "menucolor": "%s"
}''' % str(color))
            sleep(1)
            print('Color changed! Restart to apply.')
            sleep(2)

        if choice == '20':
            exit(0)
            quit(0)
    os.system('cls')
