import tensorflow as tf

#criação do grafo
grafo = tf.Graph()

'''
Uma tf.Session encapsula o ambiente onde as operações do grafo são executadas e os tensors são avaliados.
 Para isso a gente precisa definir qual o grafo que vai ser usado na sessão.
'''
#utilizando o grafo e inserindo os valores

'''
Para executar as operações você vai usar o método tf.Session.run(). 
Esse método executa um ‘passo’ da computação do grafo. 
Definimos o que queremos rodar através do argumento fetches. 
Ele pode ser um elemento do grafo, uma lista arbitrária, um dicionário, etc. No nosso caso vamos rodar um passo da nossa adição:
'''

with tf.Session(graph=grafo) as sessao:
    x = tf.constant([1,3,6]) 
    y = tf.constant([1,1,1])

#realizando as operações
    operacao = tf.add(x,y)
    resultado = sessao.run(fetches=operacao)
    print(resultado)