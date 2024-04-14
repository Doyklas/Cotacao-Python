# importar o app, Builder (GUI)
#criar o aplicativo
#criar a funcao build
import kivy
from kivy.app import App
from kivy.lang import Builder
import requests

GUI = Builder.load_file("tela.kv")

class MeuApp(App):
    def build(self):
        return GUI
    def on_start(self):
        self.root.ids["1"].text = f"Dolar R$ {self.pegar_cotacao('USD')}"
        self.root.ids["2"].text = f"Euro R$ {self.pegar_cotacao('EUR')}"
        self.root.ids["3"].text = f"Bitcoin R$ {self.pegar_cotacao('BTC')}"
        self.root.ids["4"].text = f"Ethereum R$ {self.pegar_cotacao('ETH')}"
    def pegar_cotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        dicionario_req = requisicao.json()
        #pegando a cotacao da moeda no dicionario
        cotacao = dicionario_req[f"{moeda}BRL"]["bid"]
        
# Inicia o App de forma infinita
#MeuApp().run
if __name__ == '__main__':
    MeuApp().run()