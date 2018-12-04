from pyramid.testing import Configurator


def test_MpgOlacConfig(mocker):
    from clldlucl import MpgOlacConfig

    cfg = MpgOlacConfig()
    assert cfg.admin(None).role == 'Admin'
    assert 'shh' in cfg.description(mocker.MagicMock())['institution'].url


def test_includeme():
    from clldlucl import includeme

    includeme(Configurator(settings={'sqlalchemy.url': 'sqlite://'}))
