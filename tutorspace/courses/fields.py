from django.db import models
from django_ckeditor_5.widgets import CKEditor5Widget

class RichTextField(models.TextField):
    """
    Campo di testo che usa CKEditor5 come widget,
    ma è un vero TextField lato DB, quindi compatibile con le migrazioni.
    """
    def __init__(self, *args, config_name="default", **kwargs):
        self.config_name = config_name
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'widget': CKEditor5Widget(config_name=self.config_name)
        }
        defaults.update(kwargs)
        return super().formfield(**defaults)