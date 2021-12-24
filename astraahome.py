import requests, os, sys, time, random, os.path, string, subprocess, pyperclip, pyautogui, urllib.request, random, threading, ctypes, base64, discord, json, datetime, shutil, aiohttp, asyncio
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

y = Fore.LIGHTYELLOW_EX
b = Fore.LIGHTBLUE_EX
w = Fore.LIGHTWHITE_EX

if os.name == "nt":
    os.system(f'title All Tools In One - Made by Astraa')

def Spinner():
	l = ['|', '/', '-', '\\']
	for i in l+l+l:
		sys.stdout.write(f"""\r{y}[{b}#{y}]{w} Loading... {i}""")
		sys.stdout.flush()
		time.sleep(0.2)

def discserver():
    print(f"""{y}------------------------------------------------------------------------------------------------------------------------\n{w}adev {b}|{w} https://dsc.gg/astraadev {b}|{w} https://dsc.gg/astraadev {b}|{w} https://dsc.gg/astraadev {b}|{w} https://dsc.gg/astraadev {b}|{w} https\n{y}------------------------------------------------------------------------------------------------------------------------\n""")

def astraahometitle():
    print(f"""\n\n                   {b}█████{y}╗ {b}███████{y}╗{b}████████{y}╗{b}██████{y}╗  {b}█████{y}╗  {b}█████{y}╗ {b}██{y}╗  {b}██{y}╗ {b}██████{y}╗ {b}███{y}╗   {b}███{y}╗{b}███████{y}╗""")
    print(f"""                  {b}██{y}╔══{b}██{y}╗{b}██{y}╔════╝╚══{b}██{y}╔══╝{b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}╗{b}██{y}║  {b}██{y}║{b}██{y}╔═══{b}██{y}╗{b}████{y}╗ {b}████{y}║{b}██{y}╔════╝""")
    print(f"""                  {b}███████{y}║{b}███████{y}╗   {b}██{y}║   {b}██████{y}╔╝{b}███████{y}║{b}███████{y}║{b}███████{y}║{b}██{y}║   {b}██{y}║{b}██{y}╔{b}████{y}╔{b}██{y}║{b}█████{y}╗  """)
    print(f"""                  {b}██{y}╔══{b}██{y}║╚════{b}██{y}║   {b}██{y}║   {b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}║{b}██{y}╔══{b}██{y}║{b}██{y}╔══{b}██{y}║{b}██{y}║   {b}██{y}║{b}██{y}║╚{b}██{y}╔╝{b}██{y}║{b}██{y}╔══╝  """)
    print(f"""                  {b}██{y}║  {b}██{y}║{b}███████{y}║   {b}██{y}║   {b}██{y}║  {b}██{y}║{b}██{y}║  {b}██{y}║{b}██{y}║  {b}██{y}║{b}██{y}║  {b}██{y}║╚{b}██████{y}╔╝{b}██{y}║ ╚═╝ {b}██{y}║{b}███████{y}╗""")
    print(f"""                  ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝\n""")
    discserver()
def selfbottitle():
    print(f"""\n\n                               {b}███████{y}╗{b}███████{y}╗{b}██{y}╗     {b}███████{y}╗    {b}██████{y}╗  {b}██████{y}╗ {b}████████{y}╗""")
    print(f"""                               {b}██{y}╔════╝{b}██{y}╔════╝{b}██{y}║     {b}██{y}╔════╝    {b}██{y}╔══{b}██{y}╗{b}██{y}╔═══{b}██{y}╗╚══{b}██{y}╔══╝""")
    print(f"""                               {b}███████{y}╗{b}█████{y}╗  {b}██{y}║     {b}█████{y}╗      {b}██████{y}╔╝{b}██{y}║   {b}██{y}║   {b}██{y}║   """)
    print(f"""                               ╚════{b}██{y}║{b}██{y}╔══╝  {b}██{y}║     {b}██{y}╔{y}══╝      {b}██{y}╔══{b}██{y}╗{b}██{y}║   {b}██{y}║   {b}██{y}║   """)
    print(f"""                               {b}███████{y}║{b}███████{y}╗{b}███████{y}╗{b}██{y}║         {b}██████{y}╔╝╚{b}██████{y}╔╝   {b}██{y}║   """)
    print(f"""                               ╚══════╝╚══════╝╚══════╝╚═╝         ╚═════╝  ╚═════╝    ╚═╝   \n""")
    discserver()
def rattitle():
    print(f"""\n\n                    {b}██████{y}╗ {b}██{y}╗{b}███████{y}╗ {b}██████{y}╗ {b}██████{y}╗ {b}██████{y}╗ {b}██████{y}╗     {b}██████{y}╗  {b}█████{y}╗ {b}████████{y}╗""")
    print(f"""                    {b}██{y}╔══{b}██{y}╗{b}██{y}║{b}██{y}╔════╝{b}██{y}╔════╝{b}██{y}╔═══{b}██{y}╗{b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}╗    {b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}╗╚══{b}██{y}╔══╝""")
    print(f"""                    {b}██{y}║  {b}██{y}║{b}██{y}║{b}███████{y}╗{b}██{y}║     {b}██{y}║   {b}██{y}║{b}██████{y}╔╝{b}██{y}║  {b}██{y}║    {b}██████{y}╔╝{b}███████{y}║   {b}██{y}║   """)
    print(f"""                    {b}██{y}║  {b}██{y}║{b}██{y}║╚════{b}██{y}║{b}██{y}║     {b}██{y}║   {b}██{y}║{b}██{y}╔══{b}██{y}╗{b}██{y}║  {b}██{y}║    {b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}║   {b}██{y}║   """)
    print(f"""                    {b}██████{y}╔╝{b}██{y}║{b}███████{y}║╚{b}██████{y}╗╚{b}██████{y}╔╝{b}██{y}║  {b}██{y}║{b}██████{y}╔╝    {b}██{y}║  {b}██{y}║{b}██{y}║  {b}██{y}║   {b}██{y}║   """)
    print(f"""                    ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   \n""")
    discserver()
def raidtitle():
    print(f"""\n\n                              {b}██████{y}╗  {b}█████{y}╗ {b}██{y}╗{b}██████{y}╗     {b}████████{y}╗ {b}██████{y}╗  {b}██████{y}╗ {b}██{y}╗     """)
    print(f"""                              {b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}╗{b}██{y}║{b}██{y}╔══{b}██{y}╗    ╚══{b}██{y}╔══╝{b}██{y}╔═══{b}██{y}╗{b}██{y}╔═══{b}██{y}╗{b}██{y}║     """)
    print(f"""                              {b}██████{y}╔╝{b}███████{y}║{b}██{y}║{b}██{y}║  {b}██{y}║       {b}██{y}║   {b}██{y}║   {b}██{y}║{b}██{y}║   {b}██{y}║{b}██{y}║     """)
    print(f"""                              {b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}║{b}██{y}║{b}██{y}║  {b}██{y}║       {b}██{y}║   {b}██{y}║   {b}██{y}║{b}██{y}║   {b}██{y}║{b}██{y}║     """)
    print(f"""                              {b}██{y}║  {b}██{y}║{b}██{y}║  {b}██{y}║{b}██{y}║{b}██████{y}╔╝       {b}██{y}║   ╚{b}██████{y}╔╝╚{b}██████{y}╔╝{b}███████{y}╗""")
    print(f"""                              ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═════╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝\n""")
    discserver()
def filegrabbertitle():
    print(f"""\n\n         {b}████████{y}╗ {b}██████{y}╗ {b}██{y}╗ {b}███{y}╗{b}███████{y}╗{b}███{y}╗   {b}██{y}╗     {b}██████{y}╗ {b}██████{y}╗  {b}█████{y}╗ {b}██████{y}╗ {b}██████{y}╗ {b}███████{y}╗{b}██████{y}╗ """)
    print(f"""         {y}╚══{b}██{y}╔══╝{b}██{y}╔═══{b}██{y}╗{b}██{y}║ {b}██{y}╔╝{b}██{y}╔════╝{b}████{y}╗  {b}██{y}║    {b}██{y}╔════╝ {b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}╗{b}██{y}╔════╝{b}██{y}╔══{b}██{y}╗""")
    print(f"""            {b}██{y}║   {b}██{y}║   {b}██{y}║{b}█████{y}╔╝ {b}█████{y}╗  {b}██{y}╔{b}██{y}╗ {b}██{y}║    {b}██{y}║  {b}███{y}╗{b}██████{y}╔╝{b}███████{y}║{b}██████{y}╔╝{b}██████{y}╔╝{b}█████{y}╗  {b}██████{y}╔╝""")
    print(f"""            {b}██{y}║   {b}██{y}║   {b}██{y}║{b}██{y}╔═{b}██{y}╗ {b}██{y}╔══╝  {b}██{y}║╚{b}██{y}╗{b}██{y}║    {b}██{y}║   {b}██{y}║{b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}║{b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}╗{b}██{y}╔══╝  {b}██{y}╔══{b}██{y}╗""")
    print(f"""            {b}██{y}║   ╚{b}██████{y}╔╝{b}██{y}║  {b}██{y}╗{b}███████{y}╗{b}██{y}║ ╚{b}████{y}║    ╚{b}██████{y}╔╝{b}██{y}║  {b}██{y}║{b}██{y}║  {b}██{y}║{b}██████{y}╔╝{b}██████{y}╔╝{b}███████{y}╗{b}██{y}║  {b}██{y}║""")
    print(f"""            ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝     ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝\n""")
    discserver()
def imagegrabbertitle():
    print(f"""\n\n                       {b}██{y}╗{b}███{y}╗   {b}███{y}╗ {b}█████{y}╗  {b}██████{y}╗ {b}███████{y}╗     {b}██████{y}╗ {b}██████{y}╗  {b}█████{y}╗ {b}██████{y}╗ """)
    print(f"""                       {b}██{y}║{b}████{y}╗ {b}████{y}║{b}██{y}╔══{b}██{y}╗{b}██{y}╔════╝ {b}██{y}╔════╝    {b}██{y}╔════╝ {b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}╗""")
    print(f"""                       {b}██{y}║{b}██{y}╔{b}████{y}╔{b}██{y}║{b}███████{y}║{b}██{y}║  {b}███{y}╗{b}█████{y}╗      {b}██{y}║  {b}███{y}╗{b}██████{y}╔╝{b}███████{y}║{b}██████{y}╔╝""")
    print(f"""                       {b}██{y}║{b}██{y}║╚{b}██{y}╔╝{b}██{y}║{b}██{y}╔══{b}██{y}║{b}██{y}║   {b}██{y}║{b}██{y}╔══╝      {b}██{y}║   {b}██{y}║{b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}║{b}██{y}╔══{b}██{y}╗""")
    print(f"""                       {b}██{y}║{b}██{y}║ ╚═╝ {b}██{y}║{b}██{y}║  {b}██{y}║╚{b}██████{y}╔╝{b}███████{y}╗    ╚{b}██████{y}╔╝{b}██{y}║  {b}██{y}║{b}██{y}║  {b}██{y}║{b}██████{y}╔╝""")
    print(f"""                       ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ \n""")
    discserver()
def fakeqrtitle():
    print(f"""\n\n                                   {b}███████{y}╗ {b}█████{y}╗ {b}██{y}╗  {b}██{y}╗{b}███████{y}╗     {b}██████{y}╗ {b}██████{y}╗ """)
    print(f"""                                   {b}██{y}╔════╝{b}██{y}╔══{b}██{y}╗{b}██{y}║ {b}██{y}╔╝{b}██{y}╔════╝    {b}██{y}╔═══{b}██{y}╗{b}██{y}╔══{b}██{y}╗""")
    print(f"""                                   {b}█████{y}╗  {b}███████{y}║{b}█████{y}╔╝ {b}█████{y}╗      {b}██{y}║   {b}██{y}║{b}██████{y}╔╝""")
    print(f"""                                   {b}██{y}╔══╝  {b}██{y}╔══{b}██{y}║{b}██{y}╔═{b}██{y}╗ {b}██{y}╔══╝      {b}██{y}║{b}▄▄ ██{y}║{b}██{y}╔══{b}██{y}╗""")
    print(f"""                                   {b}██{y}║     {b}██{y}║  {b}██{y}║{b}██{y}║  {b}██{y}╗{b}███████{y}╗    ╚{b}██████{y}╔╝{b}██{y}║  {b}██{y}║""")
    print(f"""                                   ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝     ╚══{b}▀▀{y}═╝ ╚═╝  ╚═╝\n""")
    discserver()
def ipgrabbertitle():
    print(f"""\n\n                                      {b}██{y}╗{b}██████{y}╗      {b}██████{y}╗ {b}██████{y}╗  {b}█████{y}╗ {b}██████{y}╗ """)
    print(f"""                                      {b}██{y}║{b}██{y}╔══{b}██{y}╗    {b}██{y}╔════╝ {b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}╗""")
    print(f"""                                      {b}██{y}║{b}██████{y}╔╝    {b}██{y}║  {b}███{y}╗{b}██████{y}╔╝{b}███████{y}║{b}██████{y}╔╝""")
    print(f"""                                      {b}██{y}║{b}██{y}╔═══╝     {b}██{y}║   {b}██{y}║{b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}║{b}██{y}╔══{b}██{y}╗""")
    print(f"""                                      {b}██{y}║{b}██{y}║         ╚{b}██████{y}╔╝{b}██{y}║  {b}██{y}║{b}██{y}║  {b}██{y}║{b}██████{y}╔╝""")
    print(f"""                                      ╚═╝╚═╝          ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ \n""")
    discserver()
def accountnukertitle():
    print(f"""\n\n                     {b}████████{y}╗ {b}██████{y}╗ {b}██{y}╗  {b}██{y}╗{b}███████{y}╗{b}███{y}╗   {b}██{y}╗{b}██████{y}╗  {b}█████{y}╗ {b}██████{y}╗ {b}███████{y}╗""")
    print(f"""                     {y}╚══{b}██{y}╔══╝{b}██{y}╔═══{b}██{y}╗{b}██{y}║ {b}██{y}╔╝{b}██{y}╔════╝{b}████{y}╗  {b}██{y}║{b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}╗{b}██{y}╔════╝""")
    print(f"""                        {b}██{y}║   {b}██{y}║   {b}██{y}║{b}█████{y}╔╝ {b}█████{y}╗  {b}██{y}╔{b}██{y}╗ {b}██{y}║{b}██████{y}╔╝{b}███████{y}║{b}██████{y}╔╝{b}█████{y}╗  """)
    print(f"""                        {b}██{y}║   {b}██{y}║   {b}██{y}║{b}██{y}╔═{b}██{y}╗ {b}██{y}╔══╝  {b}██{y}║╚{b}██{y}╗{b}██{y}║{b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}║{b}██{y}╔═══╝ {b}██{y}╔══╝  """)
    print(f"""                        {b}██{y}║   ╚{b}██████{y}╔╝{b}██{y}║  {b}██{y}╗{b}███████{y}╗{b}██{y}║ ╚{b}████{y}║{b}██{y}║  {b}██{y}║{b}██{y}║  {b}██{y}║{b}██{y}║     {b}███████{y}╗""")
    print(f"""                        ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝\n""")
    discserver()
def accountdisablertitle():
    print(f"""\n\n                                {b}██████{y}╗ {b}██{y}╗{b}███████{y}╗ {b}█████{y}╗ {b}██████{y}╗ {b}██{y}╗     {b}███████{y}╗{b}██████{y}╗ """)
    print(f"""                                {b}██{y}╔══{b}██{y}╗{b}██{y}║{b}██{y}╔════╝{b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}╗{b}██{y}║     {b}██{y}╔════╝{b}██{y}╔══{b}██{y}╗""")
    print(f"""                                {b}██{y}║  {b}██{y}║{b}██{y}║{b}███████{y}╗{b}███████{y}║{b}██████{y}╔╝{b}██{y}║     {b}█████{y}╗  {b}██████{y}╔╝""")
    print(f"""                                {b}██{y}║  {b}██{y}║{b}██{y}║╚════{b}██{y}║{b}██{y}╔══{b}██{y}║{b}██{y}╔══{b}██{y}╗{b}██{y}║     {b}██{y}╔══╝  {b}██{y}╔══{b}██{y}╗""")
    print(f"""                                {b}██████{y}╔╝{b}██{y}║{b}███████{y}║{b}██{y}║  {b}██{y}║{b}██████{y}╔╝{b}███████{y}╗{b}███████{y}╗{b}██{y}║  {b}██{y}║""")
    print(f"""                                ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝\n""")
    discserver()
def accountgentitle():
    print(f"""\n\n                        {b}████████{y}╗ {b}██████{y}╗ {b}██{y}╗  {b}██{y}╗{b}███████{y}╗{b}███{y}╗   {b}██{y}╗ {b}██████{y}╗ {b}███████{y}╗{b}███{y}╗   {b}██{y}╗""")
    print(f"""                        {y}╚══{b}██{y}╔══╝{b}██{y}╔═══{b}██{y}╗{b}██{y}║ {b}██{y}╔╝{b}██{y}╔════╝{b}████{y}╗  {b}██{y}║{b}██{y}╔════╝ {b}██{y}╔════╝{b}████{y}╗  {b}██{y}║""")
    print(f"""                           {b}██{y}║   {b}██{y}║   {b}██{y}║{b}█████{y}╔╝ {b}█████{y}╗  {b}██{y}╔{b}██{y}╗ {b}██{y}║{b}██{y}║  {b}███{y}╗{b}█████{y}╗  {b}██{y}╔{b}██{y}╗ {b}██{y}║""")
    print(f"""                          {b} ██{y}║   {b}██{y}║   {b}██{y}║{b}██{y}╔═{b}██{y}╗ {b}██{y}╔══╝  {b}██{y}║╚{b}██{y}╗{b}██{y}║{b}██{y}║   {b}██{y}║{b}██{y}╔══╝  {b}██{y}║╚{b}██{y}╗{b}██{y}║""")
    print(f"""                           {b}██{y}║   ╚{b}██████{y}╔╝{b}██{y}║  {b}██{y}╗{b}███████{y}╗{b}██{y}║ ╚{b}████{y}║╚{b}██████{y}╔╝{b}███████{y}╗{b}██{y}║ ╚{b}████{y}║""")
    print(f"""                           ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝\n""")
    discserver()
def settingscyclertitle():
    print(f"""\n\n                   {b}██████{y}╗{b}██{y}╗   {b}██{y}╗ {b}██████{y}╗{b}██{y}╗     {b}███████{y}╗    {b}████████{y}╗{b}██{y}╗  {b}██{y}╗{b}███████{y}╗{b}███{y}╗   {b}███{y}╗{b}███████{y}╗""")
    print(f"""                  {b}██{y}╔════╝╚{b}██{y}╗ {b}██{y}╔╝{b}██{y}╔════╝{b}██{y}║     {b}██{y}╔════╝    ╚══{b}██{y}╔══╝{b}██{y}║  {b}██{y}║{b}██{y}╔════╝{b}████{y}╗ {b}████{y}║{b}██{y}╔════╝""")
    print(f"""                  {b}██{y}║      ╚{b}████{y}╔╝ {b}██{y}║     {b}██{y}║     {b}█████{y}╗         {b}██{y}║   {b}███████{y}║{b}█████{y}╗  {b}██{y}╔{b}████{y}╔{b}██{y}║{b}█████{y}╗  """)
    print(f"""                  {b}██{y}║       ╚{b}██{y}╔╝  {b}██{y}║     {b}██{y}║     {b}██{y}╔══╝         {b}██{y}║   {b}██{y}╔══{b}██{y}║{b}██{y}╔══╝  {b}██{y}║╚{b}██{y}╔╝{b}██{y}║{b}██{y}╔══╝  """)
    print(f"""                  ╚{b}██████{y}╗   {b}██{y}║   ╚{b}██████{y}╗{b}███████{y}╗{b}███████{y}╗       {b}██{y}║   {b}██{y}║  {b}██{y}║{b}███████{y}╗{b}██{y}║ ╚═╝ {b}██{y}║{b}███████{y}╗""")
    print(f"""                   ╚═════╝   ╚═╝    ╚═════╝╚══════╝╚══════╝       ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚══════╝\n""")
    discserver()
def tokeninfotitle():
    print(f"""\n\n                        {b}████████{y}╗ {b}██████{y}╗ {b}██{y}╗  {b}██{y}╗{b}███████{y}╗{b}███{y}╗   {b}██{y}╗{b}██{y}╗{b}███{y}╗   {b}██{y}╗{b}███████{y}╗ {b}██████{y}╗ """)
    print(f"""                        {y}╚══{b}██{y}╔══╝{b}██{y}╔═══{b}██{y}╗{b}██{y}║ {b}██{y}╔╝{b}██{y}╔════╝{b}████{y}╗  {b}██{y}║{b}██{y}║{b}████{y}╗  {b}██{y}║{b}██{y}╔════╝{b}██{y}╔═══{b}██{y}╗""")
    print(f"""                           {b}██{y}║   {b}██{y}║   {b}██{y}║{b}█████{y}╔╝ {b}█████{y}╗  {b}██{y}╔{b}██{y}╗ {b}██{y}║{b}██{y}║{b}██{y}╔{b}██{y}╗ {b}██{y}║{b}█████{y}╗  {b}██{y}║   {b}██{y}║""")
    print(f"""                           {b}██{y}║   {b}██{y}║   {b}██{y}║{b}██{y}╔═{b}██{y}╗ {b}██{y}╔══╝  {b}██{y}║╚{b}██{y}╗{b}██{y}║{b}██{y}║{b}██{y}║╚{b}██{y}╗{b}██{y}║{b}██{y}╔══╝  {b}██{y}║   {b}██{y}║""")
    print(f"""                           {b}██{y}║   ╚{b}██████{y}╔╝{b}██{y}║  {b}██{y}╗{b}███████{y}╗{b}██{y}║ ╚{b}████{y}║{b}██{y}║{b}██{y}║ ╚{b}████{y}║{b}██{y}║     {y}╚{b}██████{y}╔╝""")
    print(f"""                           ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ \n""")
    discserver()
def autologintitle():
    print(f"""\n\n                         {b}█████{y}╗ {b}██{y}╗   {b}██{y}╗{b}████████{y}╗ {b}██████{y}╗ {b}██{y}╗      {b}██████{y}╗  {b}██████{y}╗ {b}██{y}╗{b}███{y}╗   {b}██{y}╗""")
    print(f"""                        {b}██{y}╔══{b}██{y}╗{b}██{y}║   {b}██{y}║╚══{b}██{y}╔══╝{b}██{y}╔═══{b}██{y}╗{b}██{y}║     {b}██{y}╔═══{b}██{y}╗{b}██{y}╔════╝ {b}██{y}║{b}████{y}╗  {b}██{y}║""")
    print(f"""                        {b}███████{y}║{b}██{y}║   {b}██{y}║   {b}██{y}║   {b}██{y}║   {b}██{y}║{b}██{y}║     {b}██{y}║   {b}██{y}║{b}██{y}║  {b}███{y}╗{b}██{y}║{b}██{y}╔{b}██{y}╗ {b}██{y}║""")
    print(f"""                        {b}██{y}╔══{b}██{y}║{b}██{y}║   {b}██{y}║   {b}██{y}║   {b}██{y}║   {b}██{y}║{b}██{y}║     {b}██{y}║   {b}██{y}║{b}██{y}║   {b}██{y}║{b}██{y}║{b}██{y}║╚{b}██{y}╗{b}██{y}║""")
    print(f"""                        {b}██{y}║  {b}██{y}║╚{b}██████{y}╔╝   {b}██{y}║   ╚{b}██████{y}╔╝{b}███████{y}╗╚{b}██████{y}╔╝╚{b}██████{y}╔╝{b}██{y}║{b}██{y}║ ╚{b}████{y}║""")
    print(f"""                        ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝\n""")
    discserver()
def cleardmtitle():
    print(f"""\n\n                              {b}██████{y}╗{b}██{y}╗     {b}███████{y}╗ {b}█████{y}╗ {b}██████{y}╗     {b}██████{y}╗ {b}███{y}╗   {b}███{y}╗""")
    print(f"""                             {b}██{y}╔════╝{b}██{y}║     {b}██{y}╔════╝{b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}╗    {b}██{y}╔══{b}██{y}╗{b}████{y}╗ {b}████{y}║""")
    print(f"""                             {b}██{y}║     {b}██{y}║     {b}█████{y}╗  {b}███████{y}║{b}██████{y}╔╝    {b}██{y}║  {b}██{y}║{b}██{y}╔{b}████{y}╔{b}██{y}║""")
    print(f"""                             {b}██{y}║     {b}██{y}║     {b}██{y}╔══╝  {b}██{y}╔══{b}██{y}║{b}██{y}╔══{b}██{y}╗    {b}██{y}║  {b}██{y}║{b}██{y}║╚{b}██{y}╔╝{b}██{y}║""")
    print(f"""                             ╚{b}██████{y}╗{b}███████{y}╗{b}███████{y}╗{b}██{y}║  {b}██{y}║{b}██{y}║  {b}██{y}║    {b}██████{y}╔╝{b}██{y}║ ╚═╝ {b}██{y}║""")
    print(f"""                              ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═════╝ ╚═╝     ╚═╝\n""")
    discserver()
def housechangertitle():
    print(f"""\n\n                         {b}██{y}╗  {b}██{y}╗{b}██{y}╗   {b}██{y}╗{b}██████{y}╗ {b}███████{y}╗{b}███████{y}╗ {b}██████{y}╗ {b}██{y}╗   {b}██{y}╗ {b}█████{y}╗ {b}██████{y}╗ """)
    print(f"""                         {b}██{y}║  {b}██{y}║╚{b}██{y}╗ {b}██{y}╔╝{b}██{y}╔══{b}██{y}╗{b}██{y}╔════╝{b}██{y}╔════╝{b}██{y}╔═══{b}██{y}╗{b}██{y}║   {b}██{y}║{b}██{y}╔══{b}██{y}{y}╗{b}██{y}╔══{b}██{y}╗""")
    print(f"""                         {b}███████{y}║ ╚{b}████{y}╔╝ {b}██████{y}╔╝{b}█████{y}╗  {b}███████{y}╗{b}██{y}║   {b}██{y}║{b}██{y}║   {b}██{y}║{b}███████{y}║{b}██{y}║  {b}██{y}║""")
    print(f"""                         {b}██{y}╔══{b}██{y}║  ╚{b}██{y}╔╝  {b}██{y}╔═══╝ {b}██{y}╔══╝  ╚════{b}██{y}║{b}██{y}║{b}▄▄ ██{y}║{b}██{y}║   {b}██{y}║{b}██{y}╔══{b}██{y}║{b}██{y}║  {b}██{y}║""")
    print(f"""                         {b}██{y}║  {b}██{y}║   {b}██{y}║   {b}██{y}║     {b}███████{y}╗{b}███████{y}║╚{b}██████{y}╔╝╚{b}██████{y}╔╝{b}██{y}║  {b}██{y}║{b}██████{y}╔╝""")
    print(f"""                         ╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚══════╝╚══════╝ ╚══{b}▀▀{y}═╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝\n""")
    discserver()
def statuechangertitle():
    print(f"""\n\n                                   {b}███████{y}╗{b}████████{y}╗ {b}█████{y}╗ {b}████████{y}╗{b}██{y}╗   {b}██{y}╗{b}███████{y}╗""")
    print(f"""                                   {b}██{y}╔════╝╚══{b}██{y}╔══╝{b}██{y}╔══{b}██{y}╗╚══{b}██{y}╔══╝{b}██{y}║   {b}██{y}║{b}██{y}╔════╝""")
    print(f"""                                   {b}███████{y}╗   {b}██{y}║   {b}███████{y}║   {b}██{y}║   {b}██{y}║   {b}██{y}║{b}█████{y}╗  """)
    print(f"""                                   ╚════{b}██{y}║   {b}██{y}║   {b}██{y}╔══{b}██{y}║   {b}██{y}║   {b}██{y}║   {b}██{y}║{b}██{y}╔══╝  """)
    print(f"""                                   {b}███████{y}║   {b}██{y}║   {b}██{y}║  {b}██{y}║   {b}██{y}║   ╚{b}██████{y}╔╝{b}███████{y}╗""")
    print(f"""                                   ╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝\n""")
    discserver()
def nitrogentitle():
    print(f"""\n\n                           {b}███{y}╗   {b}██{y}╗{b}██{y}╗{b}████████{y}╗{b}██████{y}╗  {b}██████{y}╗ {b} ██████{y}╗ {b}███████{y}╗{b}███{y}╗   {b}██{y}╗""")
    print(f"""                           {b}████{y}╗  {b}██{y}║{b}██{y}║╚══{b}██{y}╔══╝{b}██{y}╔══{b}██{y}╗{b}██{y}╔═══{b}██{y}╗{b}██{y}╔════╝ {b}██{y}╔════╝{b}████{y}╗  {b}██{y}║""")
    print(f"""                           {b}██{y}╔{b}██{y}╗ {b}██{y}║{b}██{y}║   {b}██{y}║   {b}██████{y}╔╝{b}██{y}║   {b}██{y}║{b}██{y}║  {b}███{y}╗{b}█████{y}╗  {b}██{y}╔{b}██{y}╗ {b}██{y}║""")
    print(f"""                           {b}██{y}║╚{b}██{y}╗{b}██{y}║{b}██{y}║   {b}██{y}║   {b}██{y}╔══{b}██{y}╗{b}██{y}║   {b}██{y}║{b}██{y}║   {b}██{y}║{b}██{y}╔══╝  {b}██{y}║╚{b}██{y}╗{b}██{y}║""")
    print(f"""                           {b}██{y}║ ╚{b}████{y}║{b}██{y}║   {b}██{y}║   {b}██{y}║  {b}██{y}║╚{b}██████{y}╔╝╚{b}██████{y}╔╝{b}███████{y}╗{b}██{y}║ ╚{b}████{y}║""")
    print(f"""                           ╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═══╝\n""")
    discserver()
def nitrosnipertitle():
    print(f"""\n\n                 {b}███{y}╗   {b}██{y}╗{b}██{y}╗{b}████████{y}╗{b}██████{y}╗  {b}██████{y}╗     {b}███████{y}╗{b}███{y}╗   {b}██{y}╗{b}██{y}╗{b}██████{y}╗ {b}███████{y}╗{b}██████{y}╗ """)
    print(f"""                 {b}████{y}╗  {b}██{y}║{b}██{y}║╚══{b}██{y}╔══╝{b}██{y}╔══{b}██{y}╗{b}██{y}╔═══{b}██{y}╗    {b}██{y}╔════╝{b}████{y}╗  {b}██{y}║{b}██{y}║{b}██{y}╔══{b}██{y}╗{b}██{y}╔════╝{b}██{y}╔══{b}██{y}╗""")
    print(f"""                 {b}██{y}╔{b}██{y}╗ {b}██{y}║{b}██{y}║   {b}██{y}║   {b}██████{y}╔╝{b}██{y}║   {b}██{y}║    {b}███████{y}╗{b}██{y}╔{b}██{y}╗ {b}██{y}║{b}██{y}║{b}██████{y}╔╝{b}█████{y}╗  {b}██████{y}╔╝""")
    print(f"""                 {b}██{y}║╚{b}██{y}╗{b}██{y}║{b}██{y}║   {b}██{y}║   {b}██{y}╔══{b}██{y}╗{b}██{y}║   {b}██{y}║    ╚════{b}██{y}║{b}██{y}║╚{b}██{y}╗{b}██{y}║{b}██{y}║{b}██{y}╔═══╝ {b}██{y}╔══╝  {b}██{y}╔══{b}██{y}╗""")
    print(f"""                 {b}██{y}║ ╚{b}████{y}║{b}██{y}║   {b}██{y}║   {b}██{y}║  {b}██{y}║╚{b}██████{y}╔╝    {b}███████{y}║{b}██{y}║ ╚{b}████{y}║{b}██{y}║{b}██{y}║     {b}███████{y}╗{b}██{y}║  {b}██{y}║""")
    print(f"""                 ╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝     ╚══════╝╚═╝  ╚═══╝╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝\n""")
    discserver()
def webhspamtitle():
    print(f"""\n\n            {b}██{y}╗    {b}██{y}╗{b}███████{y}╗{b}██████{y}╗ {b}██{y}╗  {b}██{y}╗ {b}██████{y}╗  {b}██████{y}╗{b} ██{y}╗  {b}██{y}╗    {b}███████{y}╗{b}██████{y}╗  {b}█████{y}╗ {b}███{y}╗   {b}███{y}╗""")
    print(f"""            {b}██{y}║    {b}██{y}║{b}██{y}╔════╝{b}██{y}╔══{b}██{y}╗{b}██{y}║  {b}██{y}║{b}██{y}╔═══{b}██{y}╗{b}██{y}╔═══{b}██{y}╗{b}██{y}║ {b}██{y}╔╝    {b}██{y}╔════╝{b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}╗{b}████{y}╗ {b}████{y}║""")
    print(f"""            {b}██{y}║ {b}█{y}╗ {b}██{y}║{b}█████{y}╗  {b}██████{y}╔╝{b}███████{y}║{b}██{y}║   {b}██{y}║{b}██{y}║   {b}██{y}║{b}█████{y}╔╝     {b}███████{y}╗{b}██████{y}╔╝{b}███████{y}║{b}██{y}╔{b}████{y}╔{b}██{y}║""")
    print(f"""           {b} ██{y}║{b}███{y}╗{b}██{y}║{b}██{y}╔══╝  {b}██{y}╔══{b}██{y}╗{b}██{y}╔══{b}██{y}║{b}██{y}║   {b}██{y}║{b}██{y}║   {b}██{y}║{b}██{y}╔═{b}██{y}╗     ╚════{b}██{y}║{b}██{y}╔═══╝ {b}██{y}╔══{b}██{y}║{b}██{y}║╚{b}██{y}╔╝{b}██{y}║""")
    print(f"""            {y}╚{b}███{y}╔{b}███{y}╔╝{b}███████{y}╗{b}██████{y}╔╝{b}██{y}║  {b}██{y}║╚{b}██████{y}╔╝╚{b}██████{y}╔╝{b}██{y}║  {b}██{y}╗    {b}███████{y}║{b}██{y}║     {b}██{y}║  {b}██{y}║{b}██{y}║ ╚═╝ {b}██{y}║""")
    print(f"""             ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝\n""")
    discserver()
def webhremovertitle():
    print(f"""\n\n                               {b}██████{y}╗ {b}███████{y}╗{b}███{y}╗   {b}███{y}╗ {b}██████{y}╗ {b}██{y}╗   {b}██{y}╗{b}███████{y}╗{b}██████{y}╗ """)
    print(f"""                               {b}██{y}╔══{b}██{y}╗{b}██{y}╔════╝{b}████{y}╗ {b}████{y}║{b}██{y}╔═══{b}██{y}╗{b}██{y}║   {b}██{y}║{b}██{y}╔════╝{b}██{y}╔══{b}██{y}╗""")
    print(f"""                               {b}██████{y}╔╝{b}█████{y}╗  {b}██{y}╔{b}████{y}╔{b}██{y}║{b}██{y}║   {b}██{y}║{b}██{y}║   {b}██{y}║{b}█████{y}╗  {b}██████{y}╔╝""")
    print(f"""                               {b}██{y}╔══{b}██{y}╗{b}██{y}╔══╝  {b}██{y}║╚{b}██{y}╔╝{b}██{y}║{b}██{y}║   {b}██{y}║╚{b}██{y}╗ {b}██{y}╔╝{b}██{y}╔══╝  {b}██{y}╔══{b}██{y}╗""")
    print(f"""                               {b}██{y}║  {b}██{y}║{b}███████{y}╗{b}██{y}║ ╚═╝ {b}██{y}║╚{b}██████{y}╔╝ ╚{b}████{y}╔╝ {b}███████{y}╗{b}██{y}║  {b}██{y}║""")
    print(f"""                               ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝\n""")
    discserver()                                                                                                      

def transition():
    os.system('cls' if os.name == 'nt' else 'clear')
    Spinner()
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    astraahometitle()
    print(f"""      {y}[{b}+{y}]{w} Main Options:           {y}[{b}+{y}]{w} Grabber Options:         {y}[{b}+{y}]{w} Token Options:             {y}[{b}+{y}]{w} Useful Options:
\n          {y}[{w}01{y}]{w} Self Bot               {y}[{w}06{y}]{w} File                    {y}[{w}10{y}]{w} Account Nuker            {y}[{w}16{y}]{w} Clear DM
\n          {y}[{w}02{y}]{w} RAT Tool               {y}[{w}07{y}]{w} Image                   {y}[{w}11{y}]{w} Account Disabler         {y}[{w}17{y}]{w} House Changer
\n          {y}[{w}03{y}]{w} Raid Tool              {y}[{w}08{y}]{w} QrCode                  {y}[{w}12{y}]{w} Account Generator        {y}[{w}18{y}]{w} Statue Changer
\n          {y}[{w}04{y}]{w} Server Nuker           {y}[{w}09{y}]{w} IP Grabber              {y}[{w}13{y}]{w} Settings Cycler
\n          {y}[{w}05{y}]{w} VideoCrash Maker                                    {y}[{w}14{y}]{w} Token Informations
\n                                                                   {y}[{w}15{y}]{w} AutoLogin                    
\n\t\t\t\t\t\t\t\t\t\t\t\t\t {y}[{b}>{y}]{w} Next Page""")
    global choice
    choice = input(f"""{y}[{b}#{y}]{w} Choice: """)

    if choice == '1' or choice == '01':
        transition()
        selfbottitle()
        print(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} This tool is under development, so it is not yet usable.", end="")
        input()
        main()
    elif choice == '2' or choice == '02':
        transition()
        exec(open('Additional_File/2_Rat/rat.py').read())
    elif choice == '3' or choice == '03':
        transition()
        raidtitle()
        print(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} This tool is under development, so it is not yet usable.", end="")
        input()
        main()
    elif choice == '4' or choice == '04':
        transition()
        script_name = 'Additional_File/4_ServerNuker/servernuker.py'
        cmd_line = [sys.executable, script_name]
        subprocess.check_call(cmd_line)
    elif choice == '5' or choice == '05':
        transition()
        subprocess.call([r'Additional_File\\5_VidCrashMaker\\crashvideomaker.bat'])
    elif choice == '6' or choice == '06':
        transition()
        exec(open('Additional_File/6_FileGrab/filegrabber.py').read())
    elif choice == '7' or choice == '07':
        transition()
        imagegrabbertitle()
        print(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} This tool is under development, so it is not yet usable.", end="")
        input()
        main()
    elif choice == '8' or choice == '08':
        transition()
        exec(open('Additional_File/8_TokenFakeQr/fakeqr.py').read())
    
    elif choice == '9' or choice == '09':
        transition()
        ipgrabbertitle()
        print(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} This tool is under development, so it is not yet usable.", end="")
        input()
        main()
    elif choice == '10':
        transition()
        exec(open('Additional_File/10_AccountNuker/accountnuker.py').read())
    elif choice == '11':
        transition()
        exec(open('Additional_File/11_AccountDisabler/accountdisabler.py').read())
    elif choice == '12':
        transition()
        accountgentitle()
        print(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} This tool is under development, so it is not yet usable.", end="")
        input()
        main()
    elif choice == '13':
        transition()
        exec(open('Additional_File/13_SettingsCycler/settingscycler.py').read())
    elif choice == '14':
        transition()
        exec(open('Additional_File/14_TokenInfo/tokeninfo.py').read())
    elif choice == '15':
        transition()
        exec(open('Additional_File/15_AutoLogin/autologin.py').read())     
    elif choice == '16':
        transition()
        exec(open('Additional_File/16_ClearDM/cleardm.py').read())
    elif choice == '17':
        transition()
        exec(open('Additional_File/17_HouseChanger/housechanger.py').read())
    elif choice == '18':
        transition()
        exec(open('Additional_File/18_StatueChanger/statuechanger.py').read())
    elif choice == '>':
        os.system('cls' if os.name == 'nt' else 'clear')
        astraahometitle()
        print(f"""      {y}[{b}+{y}]{w} Nitro Options:          {y}[{b}+{y}]{w} WebHooks Options:        {y}[{b}+{y}]{w} Other Options:
\n          {y}[{w}19{y}]{w} Generator              {y}[{w}21{y}]{w} Spammer                 {y}[{w}23{y}]{w} Credits
\n          {y}[{w}20{y}]{w} Sniper                 {y}[{w}22{y}]{w} Remover                 {y}[{w}24{y}]{w} Exit\n\n\n\n\n\n\n\n\n\n                                                                                                     {y}[{b}<{y}]{w} Previous Page""")
        choice = input(f"""{y}[{b}#{y}]{w} Choice: """)

        if choice == '19':
            transition()
            exec(open('Additional_File/19_NitroGen/nitrogen.py').read())
        elif choice == '20':
            transition()
            nitrosnipertitle()
            print(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} This tool is under development, so it is not yet usable.", end="")
            input()
            main()
        elif choice == '21':
            transition()
            exec(open('Additional_File/21_WebHSpam/webhspam.py').read())
        elif choice == '22':
            transition()
            exec(open('Additional_File/22_WebHRemover/webhremover.py').read())
        elif choice == '23':
            transition()
            astraahometitle()
            print(f"""                                            {y}[{b}+{y}]{w} Development Networks:\n\n                                                {y}[{w}#{y}]{w} GitHub:    @AstraaDev\n                                                {y}[{w}#{y}]{w} Server:    dsc.gg/astraaddev\n\n\n                                            {y}[{b}+{y}]{w} Other Network\n\n                                                {y}[{w}#{y}]{w} Twitter:   @AstraaDev\n                                                {y}[{w}#{y}]{w} Discord:   Astraa#1000\n                                                {y}[{w}#{y}]{w} Insta:     @astraaftn\n\n\n\n""")
            input(f"""{y}[{b}#{y}]{w} Press ENTER to exit""")
            sys.exit()
        elif choice == '24':
            transition()
            sys.exit()
        elif choice == '<':
            os.system('cls' if os.name == 'nt' else 'clear')
            main()    
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            main()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        main()

main()