#Esta model armazena as funções que serão usadas na model imc


#A primeira função, a função imc, define o cálculo do imc em si

def imc(peso,altura):
    imc = peso / (altura*altura)
    return imc

#A segunda função, definirá as classificações do imc de acordo com o sexo da pessoa

#tabela com base no site http://indicedemassacorporal.com/imc-masculino.html

def classificacao_imc(sexo,peso,altura):
    valor_imc = imc(peso,altura)

    if sexo == 'm':
        if valor_imc < 20.7:
            return "Você está abaixo do peso."
        elif valor_imc >= 20.7 and valor_imc <= 26.4:
            return "Você está com um peso normal."
        elif valor_imc >= 26.5 and valor_imc <= 27.8:
            return "Você está um pouco acima do peso."
        elif valor_imc >= 27.9 and valor_imc <= 31.1:
            return "Você está acima do peso ideal."
        elif valor_imc >= 31.1:
            return "Você está com Obesidade. Se cuide!"
        else:
            return "Erro de cálculo. Tente novamente."

#tabela com base no site http://indicedemassacorporal.com/imc-feminino.html

    if sexo == 'f':
        if valor_imc < 19.1:
            return "Você está abaixo do peso."
        elif valor_imc >= 19.1 and valor_imc <= 25.8:
            return "Você está com um peso normal."
        elif valor_imc >= 25.9 and valor_imc <= 27.3:
            return "Você está um pouco acima do peso."
        elif valor_imc >= 27.4 and valor_imc <= 32.3:
            return "Você está acima do peso ideal."
        elif valor_imc >= 32.3:
            return "Você está com Obesidade. Se cuide!"
        else:
            return "Erro de cálculo. Tente novamente."