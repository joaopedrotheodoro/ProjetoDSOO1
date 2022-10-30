from view.tela_abstrata import TelaAbstrata

class TelaRegistro(TelaAbstrata):

    def ler_opcao(self, mensagem: str = "", inteiros_validos: [] = None):
        while True:
            valor_lido = input(mensagem)
            try:
                inteiro = int(valor_lido)
                if inteiros_validos and inteiro not in inteiros_validos:
                    raise ValueError
                return inteiro
            except ValueError: 
                print("Selecione uma opcao valida")


    def tela_opcoes(self):
        print("____REGISTRO____")
        print("1 - Histórico do Player")
        print("2 - Limpar Histórico")
        print("3 - Criar Playlist")
        print("0 - Voltar")
        opcao = self.ler_opcao("Escolha a opcao: ", [0, 1, 2, 3])
        print()
        return opcao

    def nome_playlist(self):
        nome = input("Nome da Playlist: ")
        return nome

    def escolher_musica(self):
        posicao = int(input("Escolha uma música: "))
        return posicao     

    def mostra_musica(self, index, dados_musica):
        print(index, "-", "MÚSICA:", dados_musica["nome"], "-", "ARTISTA:", dados_musica["artista"])

    def mostra_musica_adicionada(self, msg, musica, mensagem, playlist):
        print(msg, musica, mensagem, playlist)    

    def continuar(self):
        print("1 - Continuar")
        print("0 - Salvar e Sair")
        retorno = input("Escolha a Opção: ")
        return retorno    
  