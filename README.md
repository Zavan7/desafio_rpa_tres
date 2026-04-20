# RPA UV Tres

> ⚠️ **Aviso**
> Esta aplicação está em desenvolvimento ativo e pode sofrer alterações significativas na estrutura, funcionalidades e implementação ao longo do tempo.

Este projeto é uma automação RPA (Robotic Process Automation) desenvolvida em Python utilizando Playwright para testes automatizados de cenários de login com falha. O objetivo é validar o comportamento da aplicação web durante tentativas de login inválidas, garantindo que as mensagens de erro sejam exibidas corretamente.

## 🎯 Objetivos

- Automatizar o fluxo de navegação e interação com a interface web
- Validar cenários de falha no login
- Registrar logs detalhados para observabilidade
- Integrar com MongoDB para armazenamento de dados (opcional)

## ✨ Funcionalidades

- Navegação automatizada através de páginas web
- Preenchimento e submissão de formulários de login
- Validação de mensagens de erro na UI
- Logging estruturado com níveis de severidade
- Suporte opcional ao MongoDB para persistência de dados
- Configuração via variáveis de ambiente

## 📋 Pré-requisitos

- Python 3.14 ou superior
- MongoDB (opcional, se `USE_MONGO=true`)
- Navegador compatível com Playwright (Chrome, Firefox, etc.)

## 🚀 Instalação

1. Clone o repositório:
   ```bash
   git clone <url-do-repositorio>
   cd rpa-uv-tres
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   # ou se usar pyproject.toml
   pip install .
   ```

3. Instale os navegadores do Playwright:
   ```bash
   playwright install
   ```

## ⚙️ Configuração

1. Copie o arquivo de exemplo de variáveis de ambiente:
   ```bash
   cp env-exemple .env
   ```

2. Edite o arquivo `.env` com suas configurações:
   ```env
   USERNAME=seu_usuario
   PASSWORD=sua_senha

   # URI do MongoDB para ambiente local
   MONGO_URI_LOCAL=mongodb://localhost:27017

   # URI do MongoDB para ambiente Docker
   MONGO_URI_DOCKER=mongodb://mongo:27017

   MONGO_DB=nome_do_banco
   USE_MONGO=true  # ou false para desabilitar
   ENVIRONMENT=local  # ou docker
   ```

## 📖 Uso

Execute o script principal para iniciar a automação:

```bash
python main.py
```

O fluxo executará automaticamente:
1. Acesso à página inicial da aplicação
2. Início do desafio
3. Navegação para a página de login
4. Tentativa de login com credenciais inválidas
5. Validação da mensagem de erro
6. Registro de logs em `logs/`

## 📁 Estrutura do Projeto

```
rpa-uv-tres/
├── config/
│   └── log.py              # Configuração de logging
├── db/
│   └── mongo.py            # Classe para integração com MongoDB
├── downloads/              # Diretório para downloads
├── logs/                   # Arquivos de log gerados
├── pages/
│   ├── initial_page.py     # Página inicial e início do desafio
│   ├── login_faill.py      # Cenário de falha no login
│   └── start_challenge.py  # Navegação para o desafio
├── utils/
│   └── validators/
│       └── validator.py    # Validações de UI
├── env-exemple             # Exemplo de arquivo .env
├── main.py                 # Script principal (orquestrador)
├── pyproject.toml          # Configuração do projeto Python
└── README.md               # Este arquivo
```

## 🛠️ Tecnologias Utilizadas

- **Python 3.14+**: Linguagem principal
- **Playwright**: Automação de navegadores web
- **PyMongo**: Driver para MongoDB
- **python-dotenv**: Carregamento de variáveis de ambiente
- **python-json-logger**: Logging estruturado em JSON

## 📊 Logs e Observabilidade

O projeto utiliza logging estruturado para rastrear todas as operações:

- **INFO**: Etapas principais do fluxo
- **DEBUG**: Detalhes técnicos das operações
- **WARNING**: Comportamentos inesperados
- **ERROR**: Falhas críticas com stack trace

Os logs são salvos em `logs/` e podem ser visualizados em tempo real no console.

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.