import subprocess
import sys
from pathlib import Path


def run_servers():
    """
    Run both Django and local servers simultaneously
    """
    # Get the current directory
    current_dir = Path.cwd()
    picam_dir = current_dir / 'picam'

    try:
        # Start Django server in a separate process
        django_process = subprocess.Popen([sys.executable, 'manage.py', 'runserver', '5000'])

        # Start local server in a separate process
        local_server_process = subprocess.Popen([sys.executable, str(picam_dir / 'local_server.py')],
                                                cwd=str(picam_dir))

        # Wait for both processes
        django_process.wait()
        local_server_process.wait()

    except KeyboardInterrupt:
        print("\nShutting down servers...")
        django_process.terminate()
        local_server_process.terminate()
        django_process.wait()
        local_server_process.wait()
        print("Servers shut down successfully")


if __name__ == "__main__":
    run_servers()