import app_config
import subprocess
import os
from subprocess import DEVNULL

# To run the server locally
def run_server():
    try:
        # Whether we want to see the server logs in the terminal or not, we have to pass different arguments to subprocess.Popen()
        if app_config.PRINT_SERVER_LOGS:
            server_proc = subprocess.Popen([f'./{app_config.SERVER_NAME}'], cwd=os.path.dirname(__file__))
        else:
            server_proc = subprocess.Popen([f'./{app_config.SERVER_NAME}'], stdout=DEVNULL, stderr=DEVNULL, cwd=os.path.dirname(__file__))
        return server_proc
    except FileNotFoundError as exception_instance:
        print("Error trying to run the server: file not found. Double check app_config.SERVER_NAME")
        print(exception_instance)
        raise FileNotFoundError
    except Exception as exception_instance:
        print(f"Other server error: {exception_instance}")
        raise
