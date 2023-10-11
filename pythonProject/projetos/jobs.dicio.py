
Ebook = {
    'variável': 'Um local na memória onde você pode armazenar dados.',
    'loop': 'Um controle de fluxo que permite executar um bloco de código repetidamente.',
    'função': 'Um bloco de código reutilizável que realiza uma tarefa específica.',
    'lista': 'Uma coleção ordenada de elementos.',
    'condicional': 'Uma estrutura de controle que permite executar código com base em uma condição.'
}


palavra = input('Digite uma palavra para buscar no glossário: ')


if palavra in Ebook:
    significado = Ebook [palavra]
    print(f'Significado de {palavra}: {significado}')
else:
    print(f'{palavra} não está no glossário.')


