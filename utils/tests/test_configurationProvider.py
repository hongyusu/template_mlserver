import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

default_path = os.path.join(__location__, 'config.ini')

os.environ.setdefault('CONFIG_FILE', default_path)

from utils import configurationProvider as cp



def test_get_configs_default_url():
    configurations = cp.get_configs()
    assert configurations.get('AI_SERVER_URL') == 'http://127.0.0.1:8030/'
    assert configurations.get('SENTIMENT_SERVER_URL') == 'http://127.0.0.1:8011/'
    assert configurations.get('DIALOGUE_SERVER_URL') == 'http://127.0.0.1:8012/'
    assert configurations.get('NLP_SERVER_URL') == 'http://127.0.0.1:8013/'
    assert configurations.get('EMBEDDING_SERVER_URL') == 'http://127.0.0.1:8014/'
    assert configurations.get('RETRIEVAL_SERVER_URL') == 'http://127.0.0.1:8015/'


def test_get_configs_docker_url():
    os.environ.setdefault('DJANGO_ENV','DOCKERTEST')
    configurations = cp.get_configs()
    assert configurations.get('AI_SERVER_URL') == 'http://10.0.0.30:8030/'
    assert configurations.get('SENTIMENT_SERVER_URL') == 'http://10.0.0.11:8011/'
    assert configurations.get('DIALOGUE_SERVER_URL') == 'http://10.0.0.12:8012/'
    assert configurations.get('NLP_SERVER_URL') == 'http://10.0.0.13:8013/'
    assert configurations.get('EMBEDDING_SERVER_URL') == 'http://10.0.0.14:8014/'
    assert configurations.get('RETRIEVAL_SERVER_URL') == 'http://10.0.0.15:8015/'


def test_get_configs_env():
    os.environ.setdefault('AI_SERVER_URL','http://10.11.11.30:8030/')
    os.environ.setdefault('SENTIMENT_SERVER_URL','http://10.11.11.11:8011/')
    os.environ.setdefault('DIALOGUE_SERVER_URL','http://10.11.11.12:8012/')
    os.environ.setdefault('NLP_SERVER_URL','http://10.11.11.13:8013/')
    os.environ.setdefault('EMBEDDING_SERVER_URL','http://10.11.11.14:8014/')
    os.environ.setdefault('RETRIEVAL_SERVER_URL','http://10.11.11.15:8015/')
    configurations = cp.get_configs()
    assert configurations.get('AI_SERVER_URL') == 'http://10.11.11.30:8030/'
    assert configurations.get('SENTIMENT_SERVER_URL') == 'http://10.11.11.11:8011/'
    assert configurations.get('DIALOGUE_SERVER_URL') == 'http://10.11.11.12:8012/'
    assert configurations.get('NLP_SERVER_URL') == 'http://10.11.11.13:8013/'
    assert configurations.get('EMBEDDING_SERVER_URL') == 'http://10.11.11.14:8014/'
    assert configurations.get('RETRIEVAL_SERVER_URL') == 'http://10.11.11.15:8015/'

def test_get_configs_file_dir():
    os.environ.clear()
    os.environ.setdefault('DJANGO_ENV','VM')
    configurations = cp.get_configs()
    assert configurations.get('VCA_DIR') == '/home/ai/Codes/vca/'
    assert configurations.get('FI_GREETINGS_LIST') == '/home/ai/Codes/vca/data//languageDetection/FI_greetings'

    os.environ.clear()
    os.environ.setdefault('DJANGO_ENV', 'DOCKERTEST')
    configurations = cp.get_configs()
    assert configurations.get('VCA_DIR') == '/vca/'
    assert configurations.get('FI_GREETINGS_LIST') == '/data//languageDetection/FI_greetings'

#def test_get_configs_file_env():
#    os.environ.clear()
#    os.environ.setdefault('DJANGO_ENV','TEST')
#    os.environ.setdefault('FI_GREETINGS_LIST','/Users/hongyusu/Codes/vca/data/languageDetection/FI_greetings')
#    configurations = cp.get_configs()
#
#    assert configurations.get('VCA_DIR') == '/Users/hongyusu/Codes/vca/'
#
#    assert configurations.get('FI_GREETINGS_LIST') == '/Users/hongyusu/Codes/vca/home/languageDetection/FI_greetings'
#
#    os.environ.clear()
#    os.environ.setdefault('DJANGO_ENV', 'DOCKERTEST')
#    os.environ.setdefault('FI_GREETINGS_LIST','/home/languageDetection/FI_greetings')
#
#    configurations = cp.get_configs()
#    assert configurations.get('VCA_DIR') == '/vca'
#
#    assert configurations.get('FI_GREETINGS_LIST') == '/home/languageDetection/FI_greetings'
#
#def test_get_configs_data_dir():
#    os.environ.clear()
#    os.environ.setdefault('DJANGO_ENV','LOCAL')
#    configurations = cp.get_configs()
#
#    assert configurations.get('VCA_DIR') == '/home/local'
#
#    assert configurations.get('PRETRAIN_VEC_ENGLISH') == '/home/local/data/embedding/raw/wiki/wiki.en.vec.test'
#    print configurations.get('PRETRAIN_VEC_ENGLISH')
#    os.environ.clear()
#    os.environ.setdefault('DJANGO_ENV', 'DOCKER')
#
#    configurations = cp.get_configs()
#    assert configurations.get('VCA_DIR') == '/vca'
#
#    assert configurations.get('PRETRAIN_VEC_ENGLISH') == '/vca/data/embedding/raw/wiki/wiki.en.vec.test'
#
#    os.environ.clear()
#    os.environ.setdefault('DJANGO_ENV', 'PRODUCTION')
#
#    configurations = cp.get_configs()
#    assert configurations.get('VCA_DIR') == '/vca'
#
#    assert configurations.get('PRETRAIN_VEC_ENGLISH') == '/vca/data/embedding/raw/wiki/wiki.en.vec'
#
#def test_get_configs_hyperparameter():
#    os.environ.clear()
#    os.environ.setdefault('DJANGO_ENV','PRODUCTION')
#    configurations = cp.get_configs()
#    NLG_VOCAB_SIZE = configurations.get('NLG_VOCAB_SIZE')
#    assert type(NLG_VOCAB_SIZE) is IntType
#    assert NLG_VOCAB_SIZE == 500
