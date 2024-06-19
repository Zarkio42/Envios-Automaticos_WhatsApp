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
LOG_FILE = "links_enviados.log"

index = 0

def get_latest_post():
    global index
    feed = feedparser.parse(RSS_FEED_URL)
    if feed.entries:
        # Use o índice atual para obter o post
        if index < len(feed.entries):
            latest_post = feed.entries[index]
            index += 1
            return latest_post
        else:
            print("Todos os posts foram enviados.")
            return None
    return None

def send_whatsapp_message(message):
    try:
        time.sleep(2)
        pyperclip.copy(message)  # Copiar a mensagem para a área de transferência
        
        pyautogui.hotkey('ctrl', 'v')  # Colar a mensagem no campo de texto
        time.sleep(10)

        pyautogui.press('enter')  # Pressione Enter para enviar

        print("Mensagem enviada com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")

def log_sent_link(link):
    with open(LOG_FILE, "a") as file:
        file.write(link + "\n")

def check_if_link_sent(link):
    try:
        with open(LOG_FILE, "r") as file:
            sent_links = file.readlines()
            return link.strip() + "\n" in sent_links
    except FileNotFoundError:
        return False

def main():
    last_post = None
    feed = feedparser.parse(RSS_FEED_URL)
    pywhatkit.sendwhatmsg_to_group_instantly(LINK_GRUPO_WHATSAPP, "")
    time.sleep(15)  # Aguarde o WhatsApp Web abrir completamente

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
        time.sleep(10)  # Verificar a cada 10 segundos

if __name__ == "__main__":
    main()