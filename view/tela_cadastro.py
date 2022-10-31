from view.tela_abstrata import TelaAbstrata

class TelaCadastro(TelaAbstrata):

    def tela_opcoes(self):
        print("____MÚSICA____")
        print("Escolha a opção:")
        print("1 - Listar Música")
        print("2 - Cadastrar Música")
        print("3 - Alterar Música")
        print("4 - Excluir Música")
        print("0 - Retornar")
        opcao = self.ler_opcao("Escolha a opcao: ", [0, 1, 2, 3, 4])
        print()
        return opcao

    def pega_dados_musica(self):
        nome = input("Nome: ")
        artista = input("Artista: ")
        genero = input("Genero: ")
        tempo = input("Tempo: ")
        print()
        return {"nome": nome, "artista": artista, "genero": genero, "tempo": tempo}
 
    def mostra_musica(self, dados_musica):
        print("MÚSICA: ", dados_musica["nome"])
        print("ARTISTA: ", dados_musica["artista"])
        print("GENERO MUSICAL: ", dados_musica["genero"]) 
        print("TEMPO: ", dados_musica["tempo"])
        print()

    def mostra_nome_musica(self, nome):
        print("MÚSICA:", nome["nome"])
        print()    

    def exclui_musica(self):
        nome = input("NOME DA MÚSICA QUE DESEJA EXCLUIR: ")
        return nome

    def edita_musica(self):
        nome = input("NOME DA MÚSICA QUE DESEJA EDITAR: ")
        return nome
