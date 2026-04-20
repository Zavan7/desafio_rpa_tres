from playwright.sync_api import Page
import logging

logger = logging.getLogger(__name__)


class InitialPage:
    def __init__(
        self,
        page: Page,
        url: str,
        selector_page: str,
        timeout=4000
    ):
        self.page = page
        self.url = url
        self.selector_page = selector_page
        self.timeout = timeout

    def practice_page(self) -> bool:

        '''
        Iniciamos acessando a página inicial do desafio, onde iremos
        localizar e interagir com o elemento que dá início ao fluxo
        (ex: botão ou link para próxima etapa)

        Fluxo:
        - Acessa a URL informada
        - Aguarda o elemento da página estar disponível
        - Valida se o elemento está habilitado para interação
        - Realiza o clique no elemento
        - Registra logs de cada etapa do processo

        Retorno:
        - True: navegação e clique realizados com sucesso
        - False: erro ao acessar a página, elemento não encontrado
                 ou elemento desabilitado
        '''

        try:
            logger.info(
                "Acessando página",
                extra={"url": self.url}
            )

            self.page.goto(self.url)

            self.page.wait_for_selector(
                self.selector_page,
                timeout=self.timeout
            )

            button = self.page.locator(self.selector_page)

            if not button.is_enabled():
                logger.warning(
                    "Botão encontrado, mas desabilitado",
                    extra={"selector": self.selector_page}
                )
                return False

            button.click()

            logger.info(
                "Click realizado com sucesso",
                extra={"selector": self.selector_page}
            )

            return True

        except Exception:
            logger.error(
                "Erro ao acessar a página do desafio",
                exc_info=True,
                extra={
                    "url": self.url,
                    "selector": self.selector_page
                }
            )
            return False