"""
Amatino API Python Bindings
Account (alpha) test
Author: hugh@amatino.io
"""

from amatino.amatino_alpha import AmatinoAlpha
from amatino.tests.alpha.alpha_test import AlphaTest

class AlphaCreateAccountTest(AlphaTest):
    """
    Assert that it is possible to create an accounr with an AmatinoAlpha
    instance
    """
    def __init__(self):
        super().__init__('Create accounts')

    def execute(self) -> None:
        try:
            amatinoAlpha = self.create_amatino_alpha()
        except Exception as error:
            hint = 'Failed to create AmatinoAlpha instance, error: '
            self.record_failure(hint + str(error))
            return
        try:
            entity = self.create_entity(amatinoAlpha)
        except Exception as error:
            hint = 'Failed to create entity, error: '
            self.record_failure(hint + str(error))
            return
        try:
            _ = self.create_accounts(amatinoAlpha, entity)
        except Exception as error:
            hint = 'Failed to create accounts, error: '
            self.record_failure(hint + str(error))
            return
        self.record_success()
        return
