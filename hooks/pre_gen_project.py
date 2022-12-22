import os

project_name = "{{ cookiecutter.project_title  }}"

ERROR_COLOR   = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL     = "\x1b[0m"

print(f"{MESSAGE_COLOR}Let's do somthing awesome! ")
print(f"Creating {project_name} at {os.getcwd()}{RESET_ALL}")
