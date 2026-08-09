# TCP Port Scanner

Um scanner de portas TCP básico desenvolvido em Python. 

Este projeto foi criado como parte dos meus estudos no 1º semestre de Defesa Cibernética, com o objetivo de entender na prática o funcionamento do protocolo TCP/IP e a manipulação de conexões de rede via código.

## Conceitos Aplicados

- **Sockets de Rede:** Uso da biblioteca nativa `socket` do Python para criar conexões (AF_INET, SOCK_STREAM).
- **Three-way Handshake (Básico):** Validação de portas abertas com base no retorno da tentativa de conexão.
- **Tratamento de Exceções:** Prevenção de quebras de execução durante falhas de rede ou interrupções de usuário.
- **Passagem de Argumentos:** Captura do IP alvo diretamente via linha de comando (CLI).

## Requisitos

- Python 3.x
- Nenhuma biblioteca externa é necessária.

## Como Usar

Clone o repositório e execute o script passando o endereço IP do alvo como argumento.

```bash
# Clone o repositório
git clone [https://github.com/ssaravitoria/port-scanner.git](https://github.com/ssaravitoria/port-scanner.git)

# Acesse a pasta
cd port-scanner

# Execute o script (Exemplo com localhost)
python3 scanner.py 127.0.0.1
