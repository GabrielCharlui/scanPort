# scanPort

O Scanner é uma ferramenta de varredura de portas e análise de status de hosts ou endereços IP. Baseado na biblioteca Nmap, ele oferece três tipos de escaneamento:

- Scan do tipo SYN: Identifica portas abertas usando pacotes SYN, que são parte do processo de estabelecimento de conexão TCP.
- Scan do tipo UDP: Identifica portas abertas usando pacotes UDP, que são usados para comunicação sem conexão.
- Scan do tipo Intenso: Executa uma varredura mais detalhada e completa utilizando scripts Nmap.

O usuário insere o IP que deseja escanear e escolhe o tipo de varredura desejado. O programa então utiliza a biblioteca Nmap para realizar o escaneamento e retorna informações como:

- A versão do Nmap
- Detalhes do escaneamento
- Status do IP
- Portas abertas
