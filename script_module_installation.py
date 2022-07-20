
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

x = input("Enter the module name(case-sensitive):")

if x in sys.modules:
    print(f"{x!r} already installed")
else:
    install(x)
    print(f"{x!r} installed successfully")

