# DEFAULT CONFIG
# CREATE A config.py FILE TO OVERRIDE SPECIFIC CONFIG VALUES

import os
from urllib import parse

# GERERAL
ARENA_CLIENT_ID = "aiarenaclient_000"
API_TOKEN = "???"
ROUNDS_PER_RUN = 5
SHUT_DOWN_AFTER_RUN = True
RUN_REPLAY_CHECK = True
USE_PID_CHECK = False
DEBUG_MODE = True

# PATHS AND FILES
TEMP_PATH = "/tmp/aiarena/"
LOCAL_PATH = os.path.dirname(__file__)
WORKING_DIRECTORY = LOCAL_PATH  # same for now
LOG_FILE = os.path.join(WORKING_DIRECTORY, "aiarena-client.log")
REPLAYS_DIRECTORY = os.path.join(WORKING_DIRECTORY, "replays")

# WEBSITE
BASE_WEBSITE_URL = "https://ai-arena.net"
API_MATCHES_URL = parse.urljoin(BASE_WEBSITE_URL, "/api/arenaclient/matches/")
API_RESULTS_URL = parse.urljoin(BASE_WEBSITE_URL, "/api/arenaclient/results/")

# STARCRAFT
SC2_HOME = "/home/aiarena/StarCraftII/"
SC2_BINARY = os.path.join(SC2_HOME, "Versions/Base75689/SC2_x64")

# SC2LADDERSERVER
SC2LADDERSERVER_PID_FILE = os.path.join(LOCAL_PATH, "laddermanager.pid")
SC2LADDERSERVER_PID_FILE_CREATION_TIMEOUT = 10
SC2LADDERSERVER_STDOUT_FILE = os.path.join(LOCAL_PATH, "sc2ladderserver_stdout.log")
SC2LADDERSERVER_STDERR_FILE = os.path.join(LOCAL_PATH, "sc2ladderserver_stderr.log")
SC2LADDERSERVER_BINARY = os.path.join(LOCAL_PATH, "Sc2LadderServer")
SC2LADDERSERVER_MATCHUP_LIST_FILE = os.path.join(LOCAL_PATH, "matchuplist")
SC2LADDERSERVER_LADDERBOTS_FILE = os.path.join(LOCAL_PATH, "LadderBots.json")
SC2LADDERSERVER_PLAYERIDS_FILE = os.path.join(LOCAL_PATH, "playerids")
SC2LADDERSERVER_RESULTS_FILE = os.path.join(LOCAL_PATH, "results.json")


# Override values with environment specific config
try:
    import config
except ImportError as e:
    if e.name == 'config':
        pass
    else:
        raise