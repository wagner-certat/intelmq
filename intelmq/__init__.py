from .version import __version__
import os


DEFAULT_LOGGING_LEVEL = "INFO"

# directories
ROOT_DIR = os.environ.get('INTELMQ_ROOT_DIR', '/opt/intelmq/')
if ROOT_DIR in ('/', ''):
    ROOT_DIR_PRE = '/'
    ROOT_DIR_POST = 'intelmq/'
else:
    ROOT_DIR_PRE = ROOT_DIR
    ROOT_DIR_POST = ''

CONFIG_DIR = os.path.join(ROOT_DIR_PRE, "etc", ROOT_DIR_POST)
DEFAULT_LOGGING_PATH = os.path.join(ROOT_DIR_PRE, "var/log", ROOT_DIR_POST)
VAR_RUN_PATH = os.path.join(ROOT_DIR, "var/run", ROOT_DIR_POST)
VAR_STATE_PATH = os.path.join(ROOT_DIR, "var/lib/bots", ROOT_DIR_POST)

# file names
BOTS_FILE = os.path.join(CONFIG_DIR, "BOTS")
DEFAULTS_CONF_FILE = os.path.join(CONFIG_DIR, "defaults.conf")
HARMONIZATION_CONF_FILE = os.path.join(CONFIG_DIR, "harmonization.conf")
PIPELINE_CONF_FILE = os.path.join(CONFIG_DIR, "pipeline.conf")
RUNTIME_CONF_FILE = os.path.join(CONFIG_DIR, "runtime.conf")
