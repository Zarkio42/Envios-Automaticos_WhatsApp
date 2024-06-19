import feedparser
import time
import pywhatkit
import pyautogui
import pyperclip
import re

# URL do feed RSS do seu blog
RSS_FEED_URL = "https://desbravandouniverso.com/todos-os-artigos/feed/"

# Link do grupo no WhatsApp
LINK_GRUPO_WHATSAPP = "INnSOErAp2NEn5qCrWxOXu"

# Arquivo para armazenar os links já enviados
log = "links_enviados.log"

def get_latest_post():
    feed = feedparser.parse(RSS_FEED_URL)
    return feed.entries[0] if feed.entries else None

def send_whatsapp_message(message):
    try:
        # Use o link do grupo e a mensagem para enviar no WhatsApp
        pywhatkit.sendwhatmsg_to_group_instantly(LINK_GRUPO_WHATSAPP, "") # Importante não ter uma mensagem entre as aspas para não bugar o whats
        time.sleep(10)  # Aguarde o WhatsApp Web abrir e focar no campo de texto

        pyperclip.copy(message)  # Copiar a mensagem para a área de transferência
        
        pyautogui.hotkey('ctrl', 'v') # Colar a mensagem no campo de texto

        time.sleep(10) 

        pyautogui.press('enter') # Pressione Enter para enviar

        print("Mensagem enviada com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")

def log_sent_link(link):
    with open(log, "a") as file:
        file.write(link + "\n")

def check_if_link_sent(link):
    try:
        with open(log, "r") as file:
            sent_links = file.readlines()
            return link.strip() + "\n" in sent_links
    except FileNotFoundError:
        return False

last_post = None

while True:
    latest_post = get_latest_post()
    if latest_post and (last_post is None or latest_post.link != last_post.link):
        last_post = latest_post
        url_tratada = re.sub(r'\?.*', '', latest_post.link)  # Tira tudo que vier depois do '?' na url
        
        if not check_if_link_sent(url_tratada):
            message = (
                "🚀 Você está por dentro das últimas novidades e tendências no mundo da tecnologia? "
                "Não perca tempo! Visite agora o meu blog e mergulhe em artigos informativos sobre inovação, gadgets, "
                "dicas de programação e muito mais!\n"
                f"\n👉 Novo Post {latest_post.title}\n{url_tratada}\n\n"
                "Fique por dentro do que há de mais atual e interessante no universo tech. "
                "Não deixe de conferir e compartilhar com seus amigos apaixonados por tecnologia! 💡📱"
            )
            send_whatsapp_message(message)
            log_sent_link(url_tratada)
        else:
            print(f"Link já enviado anteriormente: {url_tratada}")
    time.sleep(120)  # Verificar a cada 2 minutos
