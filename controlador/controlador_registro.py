from view.tela_registro import TelaRegistro
from entidade.play_list import Playlist
from controlador.controlador_cadastro import musica0, musica1, musica2, musica3, musica4

class ControladorRegistro:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__play_list = [playlist1]
        self.__tela_registro = TelaRegistro()

    def abre_tela(self):
        lista_opcoes = {1: self.criar_playlist, 2: self.excluir_playlist, 
                        3: self.historico_player,4: self.limpar_lista, 
                        0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_registro.tela_opcoes()]()

    def historico_player(self):
        historico = self.__controlador_sistema.controlador_player.retorna_musicas()
        self.__tela_registro.mostra_mensagem("--------REGISTRO DO PLAYER--------")
        self.__tela_registro.quebra_linha()
        self.__tela_registro.mostra_mensagem("HISTÓRICO:")
        for index, item in enumerate(historico):
            self.__tela_registro.dados_musica(index, item)
        self.__tela_registro.quebra_linha() 

    def limpar_lista(self):
        self.__controlador_sistema.controlador_player.limpa_historico()
        self.__tela_registro.mostra_mensagem("HISTÓRICO EXCLUÍDO! \n")
        self.__tela_registro.quebra_linha()

    def criar_playlist(self):
        lista_posicoes = []
        nome_playlist = self.__tela_registro.nome_playlist()
        lista_musicas = self.__controlador_sistema.controlador_cadastro.retorna_objetos_musica()
        self.__tela_registro.mostra_mensagem("--------MONTAR PLAYLIST--------")
        self.__tela_registro.quebra_linha()
        self.__tela_registro.mostra_mensagem("Escolha as Músicas:")
        while True:
            self.__tela_registro.quebra_linha()
            for index, musica in enumerate(lista_musicas):
                self.__tela_registro.mostra_musica(index, {"nome": musica.nome, "artista": musica.artista})
            posicao = self.__tela_registro.escolher_musica()
            lista_posicoes.append(lista_musicas[posicao])    
            self.__tela_registro.quebra_linha()
            self.__tela_registro.mostra_musica_adicionada("Música -", lista_musicas[posicao].nome, "- Adicionada a Playlist -", nome_playlist)
            self.__tela_registro.quebra_linha()
            continuar = self.__tela_registro.continuar()
            if continuar == "0":
                self.__tela_registro.quebra_linha()
                self.__tela_registro.mostra_mensagem("PLAYLIST SALVA!")
                self.__tela_registro.quebra_linha()
                break
        playlist = Playlist(nome_playlist, lista_posicoes)
        self.__play_list.append(playlist)

    def excluir_playlist(self):
        self.__tela_registro.mostra_mensagem("--------EXCLUIR PLAYLIST--------")
        if len(self.__play_list) == 0:
                self.__tela_registro.mostra_mensagem("Você ainda não tem nenhuma playlist! \n")
        else:        
            for index, nome_playlist in enumerate(self.__play_list):
                self.__tela_registro.mostra_playlist(index, nome_playlist.nome)
            posicao = self.__tela_registro.escolher_musica()
            self.__play_list.pop(posicao)
            self.__tela_registro.mostra_mensagem("PLAYLIST EXCLUÍDA! \n")        

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def retorna_playlist(self):
        return self.__play_list

playlist1 = Playlist("Hinos do Rock", [musica0,musica1, musica2, musica3, musica4])        