from flake8_digit_separator import version


def test_const():
    assert version.NAME == 'flake8-digit-separator'
    assert isinstance(version.VERSION, str)
    assert version.AUTHOR == 'Timur Valiev'
    assert version.AUTHOR_EMAIL == 'cptchunk@yandex.ru'
    assert version.LICENSE == 'MIT'


def test_get_package_information():
    pkg_info = version.get_package_information()

    assert pkg_info == {
        'name': version.NAME,
        'version': version.VERSION,
        'author': version.AUTHOR,
        'author_email': version.AUTHOR_EMAIL,
        'license': version.LICENSE,
    }
