from django.core.exceptions import ValidationError
from django.utils import timezone

from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class MaxCurrentYearValidator:
    message = _("The year cannot be in the future.")
    code = "invalid_year"

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        current_year = timezone.now().year
        if value > current_year:
            raise ValidationError(self.message, code=self.code)
