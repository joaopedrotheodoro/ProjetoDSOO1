from entidade.musica import Musica
from view.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaPlayer(TelaAbstrata):
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['5']:
            opcao = 5
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao



    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- PLAYER ----------', font=("Helvica", 25))],
        [sg.Text('Escolha sua opção', font=("Helvica", 15))],
        [sg.Radio('Pausar', "RD1", key='1')],
        [sg.Radio('Passar Música', "RD1", key='2')],
        [sg.Radio('Voltar Música', "RD1", key='3')],
        [sg.Radio('Curtir Música', "RD1", key='4')],
        [sg.Radio('Descurtir Música', "RD1", key='5')],
        [sg.Radio('Voltar', "RD1", key='0')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        
        self.__window = sg.Window('Player de Música').Layout(layout)

        #_---------------------------------------------------------------------------------------------------------------------------


    '''def player_opcoes(self):
        print("____PLAYER OPCÕES____")
        print("1 - Pausar")
        print("2 - Passar Música")
        print("3 - Voltar Música")
        print("4 - Curtir Música")
        print("5 - Descurtir Música")
        print("0 - Sair")
        opcao2 = self.ler_opcao("Escolha a opcao: ", [0, 1, 2, 3, 4, 5])
        print()
        return opcao2 '''

    def mostra_musica(self, dados_musica):
        string_todas_musicas = "" 
        for dado in dados_musica:
            string_todas_musicas = string_todas_musicas + "MÚSICA: " + dado["nome"] + '\n'
            string_todas_musicas = string_todas_musicas + "ARTISTA: " + str(dado["artista"]) + '\n'
            string_todas_musicas = string_todas_musicas + "GÊNERO: " + str(dado["genero"]) + '\n\n'
            string_todas_musicas = string_todas_musicas + "TEMPO: " + str(dado["tempo"]) + '\n\n' 

    #---------------------------------------------------------------------------------------------------------------------
    def escolhe_opcao(self):
        opcao = int(input("Escolha a Opção: "))
        return opcao

    def pausar_musica(self):
        #print("--------MÚSICA PAUSADA--------")
        [sg.Text('-------- MÚSICA PAUSADA ----------', font=("Helvica", 25))],
        [sg.Radio('CLIQUE PARA CONTINUAR', "RD1", key=any)],
        #input("CLIQUE PARA CONTINUAR: ")
        print()

    def dados_playlist(self, index, nome):
        print(index, "-", nome)
    #-------------------------------------------------------------------------------------------------------------------------

    def mostra_mensagem(self, msg):
            sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
