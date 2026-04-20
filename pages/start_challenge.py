from playwright.sync_api import Page
import logging

logger = logging.getLogger(__name__)


class StartChallenge:
    def __init__(
        self,
        page: Page,
        locator_challenge_two: str,
        user_selector: str,
        password_selector: str,
        button_selector: str,
        timeout: int = 4000
    ):
        self.page = page
        self.locator_challenge_two = locator_challenge_two
        self.user_selector = user_selector
        self.password_selector = password_selector
        self.button_selector = button_selector
        self.timeout = timeout

    def login_page(self) -> bool:

        '''
        Iniciamos na página principal do desafio, onde iremos navegar
        até a página de login (Test Login Page)

        A ideia aqui é garantir que o elemento que direciona ao desafio
        esteja visível e, em seguida, realizar o clique para navegação

        Recebe:
        - Page (objeto do Playwright)
        - Locator do desafio (elemento que contém/acessa o challenge)
        - Timeout para espera dos elementos

        Fluxo:
        - Aguarda o elemento do desafio estar visível
        - Realiza o clique no link "Test Login Page"
        - Confirma a navegação via logs

        Retorno:
        - True: navegação realizada com sucesso
        - False: erro ao acessar a página de login
        '''
        
        try:
            logger.info(
                "Acessando página de login do desafio",
                extra={"selector": self.locator_challenge_two}
            )

            self.page.wait_for_selector(
                self.locator_challenge_two,
                timeout=self.timeout
            )

            self.page.get_by_role('link', name='Test Login Page').click()

            logger.info("Navegação para Test Login Page realizada com sucesso")

            return True

        except Exception:
            logger.error(
                "Erro ao acessar Test Login Page",
                exc_info=True,
                extra={"selector": self.locator_challenge_two}
            )
            return False
