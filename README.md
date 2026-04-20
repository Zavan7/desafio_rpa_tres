## 📌 Automação de Teste com Playwright

> ⚠️ **Disclaimer**
> Esta aplicação ainda está em desenvolvimento ativo e pode sofrer alterações significativas na estrutura, funcionalidades e implementação ao longo do tempo.

Este projeto implementa um fluxo de automação utilizando Playwright com Python, focado na validação de cenários de login com falha e verificação de mensagens exibidas na interface.

---

## 🎯 Objetivo

Validar o comportamento da aplicação ao realizar uma tentativa de login inválida, garantindo que:

- O fluxo de navegação ocorre corretamente  
- As interações com a UI são executadas com sucesso  
- A mensagem de erro esperada é exibida ao usuário  

---

## ⚙️ Estrutura do Projeto

O projeto segue uma separação clara de responsabilidades:

### 📁 pages/
- **InitialPage**: acessa a aplicação e inicia o desafio  
- **StartChallenge**: navega até a página de login  
- **LoginFaillChallenge**: executa o login com credenciais inválidas  

### 📁 validators/
- **Validation**: valida a presença de mensagens na tela  

### 📁 config/
- Configuração de logging estruturado  

### 📄 main (orquestrador)
- Controla o fluxo completo da automação  

---

## 🔄 Fluxo da Automação

1. Acessa a URL da aplicação  
2. Localiza e clica no elemento que inicia o desafio  
3. Navega até a página de login  
4. Preenche usuário e senha inválidos  
5. Executa a tentativa de login  
6. Valida se a mensagem de erro é exibida  
7. Registra logs detalhados de cada etapa  

---

## 📊 Logs e Observabilidade

O projeto utiliza logging estruturado para fornecer visibilidade completa da execução:

- `INFO`: etapas principais do fluxo  
- `DEBUG`: detalhes técnicos  
- `WARNING`: comportamentos inesperados  
- `ERROR`: falhas com stack trace  

---

## 🔐 Variáveis de Ambiente

As credenciais são carregadas via `.env`:

```env
USERNAME=CHANGE ME
PASSWORD=CHANGE ME

MONGO_URI=CHANGE ME
MONGO_DB=rCHANGE ME

USE_MONGO=CHANGE ME