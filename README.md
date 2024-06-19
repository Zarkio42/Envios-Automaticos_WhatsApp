# Envios-Automaticos_WhatsApp
Fiz essa automação para enviar artigos do meu blog no wordpress conforme eles vão sendo lançados via RSS_FEED.

### Existem dois arquivos: 
#### 1- ```automacao_envios.py```  que serve para monitorar os lançamentos futuros, fazendo uma varredura a cada 1 minuto (Ou o tempo que você determinar)
#### 2- ```envios_antigos.py```  que serve para enviar no whatsapp todos os artigos que já foram postados.

## Bibliotecas necessárias:

#### ```pip install feedparser```
#### ```pip install time```
#### ```pip install pywhatkit```
#### ```pip install pyautogui```
#### ```pip install pyperclip```
#### ```pip install re```
