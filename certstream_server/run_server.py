import config
import subprocess
from subprocess import DEVNULL

# To run the server locally
def run_server():
    try:
        # Whether we want to see the server logs in the terminal or not, we have to pass different arguments to subprocess.Popen()
        if config.PRINT_SERVER_LOGS:
            server_proc = subprocess.Popen([f'{config.PATH_TO_SERVER}'], cwd='../certstream_server')
        else:
            server_proc = subprocess.Popen([f'{config.PATH_TO_SERVER}'], stdout=DEVNULL, stderr=DEVNULL, cwd='../certstream_server')
        return server_proc
    except FileNotFoundError as exception_instance:
        print("Error trying to run the server: file not found. Double check config.PATH_TO_SERVER and config.SERVER_NAME")
        print(exception_instance)
        raise FileNotFoundError
    except Exception as exception_instance:
        print(f"Other server error: {exception_instance}")
