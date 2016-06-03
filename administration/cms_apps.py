# -*- coding: utf-8 -*-

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

# from .menu import StaffSubMenu


class AdminApp(CMSApp):
    name = _('Administration')
    urls = ['administration.urls', ]
    app_name = 'Administration'
    # menus = [StaffSubMenu, ]

apphook_pool.register(AdminApp)
