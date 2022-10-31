from view.tela_abstrata import TelaAbstrata

class TelaInicial(TelaAbstrata):

    def tela_opcoes(self):
        print("____PlayerDeMusica____")
        print("Escolha uma opção")
        print("1 - Música")
        print("2 - Player")
        print("3 - Registro")
        print("0 - Sair")
        opcao = self.ler_opcao("Escolha a opcao: ", [0, 1, 2, 3])
        print()
        return opcao
