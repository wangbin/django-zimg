=============
Django-zimg
=============

Django-zimg is a simple and stupid Django app to store image files to Zimg_.

.. _Zimg: http://zimg.buaa.us/

Quick Start
-----------

1. Add "zimg" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'zimg',
    )

2. Add ZIMG_OPTIONS in your settings.py::

    ZIMG_OPTIONS = {
        'BASE_URL' : 'http://172.23.5.233', 
        'MANAGE_URL': 'http://127.0.0.1:4869'
    }

   MAANGE_URL is used for upload/delete image, BASE_URL is used for display image.

3. In your models, set the storage to zimg_storage for ImageField::

     from django.db import models

     from zimg.storage import zimg_storage

     class Picture(models.Model):
         name = models.CharField(max_length=255)
         pic = models.ImageField(upload_to="images", storage=zimg_storage)

4. There is also a zimg tag could be used for image manipulation in template::

     {% load zimg %}
     <img src="{% zimg pic.pic.url w=300 h=300 g=1 x=0 y=0 r=45 q=85 f=jpeg %}" />

    Check `Zimg GuideBook`_ for the usage of each parameters.

.. _`Zimg GuideBook`: http://zimg.buaa.us/documents/guidebook/
