try:
    from setuptools import setup
except ImportError:
    from disutils.core import setup

config = {
    'description': 'Vault of Nool',
    'author': 'AAbdul272',
    'url': 'N/A',
    'download_url': 'N/A',
    'author_email': 'abdinurabdulrahman@outlook.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NOOL'],
    'scripts': [],
    'name': 'vault_of_nool',
}

setup(**config)
