'''
dunder significa double under
dunder são métodos com nome iniciado e terminado com double underline __

dunder name == __name__
dunder main == __main__

o dunder é usado em funções, atributos, propriedades internas da linguagem pra que eles não conflitem com os nomes criados por nós

em C o programa se inicia na função main()
int main(){

    return 0
}

em JAVA
public static vooid main(string[] args){

}

em pytho, quando executamos um arquivo .py, é atribuido o nome dele para a avariável __name__ o valor __main__
indicando que ele é o móduo de execução principal
'''


# print(__name__)


# import _017_funcoes

'''
para não printar todo o que não queremos no import devemoso colocar isso no módulo
só será executado quando ele for o arquivo principal(main)
aqui vai printar o primeiro teste que não está dentro de um if deste
o que está dentro só será printado quando o arquivo for executado diretamente
'''
# if __name__ == '__main__':
#     print('teste com if __main__ no arquivo _41_: ao importar, executa todo o arquivo, módulos devem ter apenas funções')

# _017_funcoes.hello_world()


print(__name__)


# dê uma olhada no arquivo _44_1 e veja o if
import _44_1_teste # o else não existe nesse if, foi colocado aqui só para demonstração
