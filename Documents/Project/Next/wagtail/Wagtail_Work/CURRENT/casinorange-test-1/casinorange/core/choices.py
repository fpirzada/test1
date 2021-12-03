from django.db import models


class ColumnSizeChoices(models.TextChoices):
    FULL = "FULL", "Full width"
    HALF = "HALF", "1/2 width"
    THIRD = "THIRD", "1/3 width"
