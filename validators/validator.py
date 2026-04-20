from playwright.sync_api import Page
import logging

logger = logging.getLogger(__name__)

class Validation:
    def __init__(self, page: Page, msg_locator: str):
        self.page = page
        self.msg_locator = msg_locator

    def final_validation(self):
        '''
        Realiza a validação final da automação, verificando se a mensagem
        esperada está visível na tela (ex: mensagem de erro ou sucesso)

        Recebe:
        - Page (objeto do Playwright)
        - Seletor (locator) da mensagem que deve ser validada

        Fluxo:
        - Localiza o elemento da mensagem através do locator informado
        - Verifica se o elemento está visível na página
        - Registra logs do resultado da validação

        Retorno:
        - True: mensagem encontrada e visível (validação concluída com sucesso)
        - False: mensagem não encontrada, não visível ou erro na execução
        '''
        try:
            assert self.page.locator(self.msg_locator).is_visible()

            logger.info(
                'Validação de erro feita com sucesso \n'
                f'Msg: {self.page.locator(self.msg_locator).inner_text()}'           
            )

        except Exception as e:
            logger.error(f'Erro para validar o erro de login {e}')