import os
import logging
from datetime import datetime, UTC
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

from db.mongo import MongoDB
from pages.initial_page import InitialPage
from pages.start_challenge import StartChallenge
from pages.login_faill import LoginFaillChallenge
from validators.validator import Validation
from config.log import setup_logging


load_dotenv()

setup_logging()
logger = logging.getLogger(__name__)

LOGIN_USER = os.getenv('USERNAME')
PASSWORD_USER = os.getenv('PASSWORD')

mongo = MongoDB()


def second_challenge():
    """
    Orquestra a execução do fluxo de automação de teste de login utilizando
    Playwright, incluindo navegação, tentativa de autenticação inválida,
    validação da mensagem de erro e persistência do resultado no MongoDB.

    Configurações:
    - Define a URL da aplicação alvo
    - Configura os seletores necessários para navegação e interação
    - Carrega credenciais a partir de variáveis de ambiente
    - Inicializa integração com MongoDB via camada de persistência

    Fluxo de execução:
    1. Inicializa o navegador e cria uma nova página
    2. Acessa a página inicial do desafio
    3. Navega até a página de login
    4. Executa tentativa de login com credenciais inválidas
    5. Valida a exibição da mensagem de erro esperada
    6. Registra logs em cada etapa do processo
    7. Consolida os dados da execução (status, duração, erro, etc.)
    8. Persiste o resultado na collection "executions" no MongoDB
    9. Finaliza o navegador

    Tratamento de erros:
    - Exceções são capturadas e registradas com stack trace
    - O status da execução é definido como "Error" em caso de falha
    - A mensagem e o erro são armazenados no resultado final
    - A persistência do resultado é garantida no bloco "finally"

    Persistência:
    - Os dados da execução são armazenados como documento no MongoDB
    - Campos principais: start_date, end_date, duration, status, message, error
    - Datas são registradas em UTC (timezone-aware)

    Retorno:
    - None: função orquestradora sem retorno explícito
    - O resultado da execução é persistido no banco de dados
    """

    result = {
        'start_date': None,
        'end_date': None,
        'duration': None,
        'status': 'Running',
        'message': None,
        'error': None
    }

    start_date = datetime.now(UTC)

    url = 'https://practicetestautomation.com/'
    selector_challenge_one = '#menu-item-20'
    test_login_page = 'a[href*="practice-test-login"]'
    locator_login = '#username'
    locator_password = '#password'
    submit_button = '#submit'
    msg_validator = '#error'

    logger.info('Iniciando execução do desafio')

    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()

        try:
            initial_page = InitialPage(page, url, selector_challenge_one)
            result_initial = initial_page.practice_page()

            if not result_initial:
                raise Exception('Falha ao acessar página inicial')

            page_challenge = StartChallenge(
                page,
                test_login_page,
                locator_login,
                locator_password,
                submit_button
            )
            page_challenge.login_page()

            login_fail_challenge = LoginFaillChallenge(
                page,
                locator_login,
                locator_password,
                submit_button
            )

            login_fail_challenge.login_fail_challenge(
                LOGIN_USER,
                PASSWORD_USER
            )

            final_validation = Validation(page, msg_validator)
            final_validation.final_validation()

            result['status'] = 'Success'
            result['message'] = 'Sucesso ao validar login como falho'

        except Exception as e:
            logger.error('Erro crítico na execução do fluxo', exc_info=True)

            result['status'] = 'Error'
            result['error'] = str(e)
            result['message'] = 'Erro na execução da automação'

        finally:
            browser.close()
            logger.info('Execução finalizada')

            end_date = datetime.now(UTC)
            duration = (end_date - start_date).total_seconds()

            result['start_date'] = start_date
            result['end_date'] = end_date
            result['duration'] = duration

            try:
                mongo.insert(result)
                logger.info('Resultado salvo no MongoDB')
            except Exception:
                logger.error('Erro ao salvar no MongoDB', exc_info=True)


if __name__ == '__main__':
    second_challenge()