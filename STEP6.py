import subprocess
import sys

def uninstall_vlc():
    try:
        if sys.platform.startswith('win'):
            subprocess.run(["wmic", "product", "where", "name='VLC media player'", "call", "uninstall"], check=True)
            print("VLC has been uninstalled successfully.")
        elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
            # Uninstall VLC on Linux or macOS
            subprocess.run(["sudo", "apt-get", "remove", "--purge", "vlc"], check=True)
            print("VLC has been uninstalled successfully.")
        else:
            print("Unsupported operating system.")
    except subprocess.CalledProcessError as e:
        print(f"Error uninstalling VLC: {e}")

if __name__ == "__main__":
    uninstall_vlc()
