# coding: utf-8

from django.conf import settings
from django.core.files import File
from django.core.files.storage import Storage
from django.utils.deconstruct import deconstructible
from django.utils.functional import LazyObject
from django.utils.six.moves.urllib.parse import urljoin

import requests

from lxml import html

@deconstructible
class ZimgImageStorage(Storage):
    def __init__(self):
        option = settings.ZIMG_OPTIONS
        self.base_url = option['BASE_URL']
        self.manage_url = option.get('MANAGE_URL', self.base_url)

    def _open(self, name, mode='rb'):
        r = requests.get(self.url(name))
        r.raise_for_status()
        return File(r.content, mode)

    def url(self, name):
        return urljoin(self.base_url, name)
        
    def save(self, name, content):
        files = {'file': content}
        r = requests.post(urljoin(self.manage_url, 'upload'), files=files)
        r.raise_for_status()
        element = html.document_fromstring(r.content)
        h1 = element.xpath('//h1')[0]
        name = h1.text.split()[1]
        return name


    def delete(self, name):
        assert name, "The name argument is not allowed to be empty."
        r = requests.get(urljoin(self.manage_url, 'admin'),
                         params={'md5': name, 't': 1})
        r.raise_for_status()

class ZimgStorage(LazyObject):
    def _setup(self):
        self._wrapped = ZimgImageStorage()

zimg_storage = ZimgStorage()
