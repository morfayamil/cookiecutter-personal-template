import subprocess

ERROR_COLOR   = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL     = "\x1b[0m"

project_slug =  "{{ cookiecutter.project_slug }}"

git_init = str(input(
    "Would you like to initializea git repository? y/[N]: "
))

if git_init == '':
    git_init = "N"
if git_init in ["Yes", "yes", "Y", "y"]:
    print(f"{MESSAGE_COLOR} Initializing Git repository... \n {RESET_ALL}")
    subprocess.call(['git', 'init'])
    subprocess.call(['git', 'add', '*'])
    subprocess.call(['git', 'commit', '-m', 'Inicial commit'])
    
print(f"{MESSAGE_COLOR} Done! Create and have fun!{RESET_ALL}")



