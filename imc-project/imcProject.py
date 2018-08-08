import imc_funcoes

#As funções desta model estão armazenadas na model imc_funcoes, por isso foi importada.

print("* by: thiagolago; exercício para teste e aprendizado                    *")
print("*************************************************************************")
print("*                                                                       *")
print("*                      ÍNDICE DE MASSA CORPORAL                         *")
print("*                                                                       *")
print("*************************************************************************")
print("Programa para calcular IMC masculino e feminino.")
print("\n")

validacao_sexo = False
while validacao_sexo == False:
    #O .lower() serve para executar a ação indepentede da letra maiúscula ou minúscula.
    sexo = input('Digite o seu sexo. "M" para masculino ou "F" para feminino: ').lower()
    if sexo != 'm' and sexo != 'f':
        print('Sexo inválido. Digite M ou F.')
    else:
        validacao_sexo = True
        print('\n')

validacao_peso = False
while validacao_peso == False:
    peso = input('Digite o peso (ex: 68.5): ')
    try:
        peso = float(peso)
        if peso <= 0 or peso > 350:
            print('Peso inválido. O número não pode ser menor ou igual a zero e deve ser inferior a 350.')
        else:
            validacao_peso = True
            print('\n')
    except:
        print('Peso inválido. Use apenas números e separe os decimais por ponto (ex:70.5).')

validacao_altura = False
while validacao_altura == False:
    altura = input('Digite a altura em metros (ex. 1.70): ')
    try:
        altura = float(altura)
        if altura <= 0 or altura > 3:
            print('Altura inválida. O número não pode ser menor ou igual a zero e deve ser inferior a 3 metros.')
        else:
            validacao_altura = True
            print('\n')
    except:
        print('Altura inválida. Use apenas números e separe os decimais por ponto (ex: 1.80).')

#Está importando da model imc_funcoes
v_imc = str(imc_funcoes.imc(peso,altura))
c_imc = imc_funcoes.classificacao_imc(sexo,peso,altura)

print('O seu IMC é:',v_imc[0:5])
print('Classificação:',c_imc)
print('\n')
print("********************************************")
print("*        Tabela IMC Feminino               *")
print("*                                          *")
print("*      IMC         |      Categoria        *")
print("* ___________________________________      *")
print("* Abaixo de 19.1       Abaixo do peso      *")
print("* 19.1 a 25.8          Peso Ideal          *")
print("* 25.9 a 27.3          Pouco acima do peso *")
print("* 27.4 a 32.3          Acima do Peso       *")
print("* 32.4 acima           Obesidade           *")
print("*                                          *")
print("********************************************")
print('\n')
print("********************************************")
print("*        Tabela IMC Masculino              *")
print("*                                          *")
print("*      IMC         |      Categoria        *")
print("* ___________________________________      *")
print("* Abaixo de 20.7       Abaixo do peso      *")
print("* 20.7 a 26.4          Peso Ideal          *")
print("* 26.5 a 27.8          Pouco acima do peso *")
print("* 27.9 a 31.1          Acima do Peso       *")
print("* 31.2 acima           Obesidade           *")
print("*                                          *")
print("********************************************")