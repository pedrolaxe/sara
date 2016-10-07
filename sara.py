#!/usr/bin/python
# -*- coding: utf-8 -*-
# Name: Sara
# Version: 0.4a
# Author: Pedro Laxe
# Date: 06/10/2016
from time import ctime
import time
import os
import sys
from gtts import gTTS

version = "0.4 alpha"

def falar(audiostd):
    print audiostd
    tts = gTTS(text=audiostd, lang='pt-br')
    tts.save("tmpsara.mp3")
    os.system("mpg321 -q tmpsara.mp3")

def sara(data):
    dic = {
    "olá": "Oi Pedro",
    "oi": "Oi Pedro",
    "ola": "Oi Pedro",

    "estou bem": "fico feliz por estar bem!",
    "bem": "fico feliz por estar bem!",

    "sara": "Em que posso lhe servir meu senhor?",

    "piada": "O que é um Fúio?    é um buiáco na parede kkk"
    }
    for x in dic:
        if x in data:
            falar(dic[x])

    if "versao" in data or "version" in data:
          falar("Estou na versão "+version)
    if "sair" in data:
        falar("Até a Próxima meu senhor!")
        sys.exit()


# inicializa a sara
time.sleep(2)
falar("Olá Pedro, como você está?")
while 1:
    data = str(raw_input("Digite: "))
    sara(data)
