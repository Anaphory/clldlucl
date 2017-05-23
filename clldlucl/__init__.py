from pyramid.response import Response
## Adapted for LUCL use by Gereon Kaiping

from clld.interfaces import IOlacConfig
from clld.web.views.olac import OlacConfig, Participant, Institution


class MpgOlacConfig(OlacConfig):
    def admin(self, req):
        return Participant("Admin", 'Gereon Kaiping', 'g.a.kaiping@hum.leidenuniv.nl')

    def description(self, req):
        res = OlacConfig.description(self, req)
        res['institution'] = Institution(
            'Leiden University Centre for Linguistics',
            'http://hum.leiden.edu/lucl/',
            'Leiden, The Netherlands')
        return res


def includeme(config):
    config.include('clld.web.app')
    config.registry.registerUtility(MpgOlacConfig(), IOlacConfig)
    config.add_static_view('clldlucl-static', 'clldlucl:static')
    config.add_settings({'clld.publisher_logo': 'clldlucl:static/lucl.png'})

    config.add_route('google-site-verification', 'googlebbc8f4da1abdc58b.html')
    config.add_view(
        lambda r: Response('google-site-verification: googlebbc8f4da1abdc58b.html'),
        route_name='google-site-verification')
