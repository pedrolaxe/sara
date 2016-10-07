#!/usr/bin/python
# -*- coding: utf-8 -*-
# Name: SARA
# Version: 0.7.3b
# Author: Pedro Laxe
# Date: 06/10/2016

import time
import os
import sys
from gtts import gTTS

version = "0.7.3 beta"

def falar(audiostd):
    print audiostd
    tts = gTTS(text=audiostd, lang='pt-br')
    tts.save("tmpsara.mp3")
    os.system("mpg321 -q tmpsara.mp3")

def savedbfile(dbdata):
    dbfile = open("database.sara", "w")
    dbdata = str(dbdata)
    dbfile.write(dbdata)
    dbfile.close()

def sara(data):
    dicionario = []
    with open("database.sara", "r") as f:
        dicfile = eval(f.read())
        for key in dicfile:
            if key in data:
                falar(dicfile[key])

    if "aprender" in data:
        falar("Gosto de Aprender coisas novas!")
        pergunta = str(raw_input("Pergunta: "))
        resposta = str(raw_input("Resposta: "))
        if pergunta != "" and resposta != "":
            dicfile.update({pergunta: resposta})
            savedbfile(dicfile)
            falar("Salvei no meu banco de dados!")
            falar("Reinicie para ver as mudanças.")

    if "versao" in data or "version" in data:
          falar("Estou na versão "+version)
    if "sair" in data or "close" in data:
        falar("Até a Próxima meu senhor!")
        os.system("rm -rf tmpsara.mp3")
        sys.exit()

# inicializa a SARA
time.sleep(2)
falar("Olá, como você está?")
while 1:
    data = str(raw_input("Digite: "))
    sara(data)
