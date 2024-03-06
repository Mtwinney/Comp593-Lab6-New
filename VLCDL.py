import subprocess
import os
installer_path = r'C:/temp/vlc-3.0.17.4-win64.exe.sha256'
subprocess.run([installer_path, '/L=1033', '/S'], shell=True)
os.remove(installer_path)