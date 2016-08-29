from __future__ import unicode_literals

from django.db import models


class Image(models.Model):
    """
    Description: Model Description
    """
    img = models.ImageField(upload_to='uploads/%Y/%m/%d')

    @property
    def greyscale_path(self):
        return "{0}_greyscale.{1}".format(
            self.img.url.split(".")[0],
            self.img.url.split(".")[1]
        )

    @property
    def resize_path(self):
        return "{0}_resize.{1}".format(
            self.img.url.split(".")[0],
            self.img.url.split(".")[1]
        )
