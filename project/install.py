import os
from colorama import init, Fore

# initialize colours
init()

GREEN = Fore.GREEN
RED = Fore.RED
MAGENTA = Fore.MAGENTA
WHITE = Fore.WHITE


def intro():
    print(f"""{MAGENTA}
███████ ██    ██ ███████     ██ ███    ██ ███████ ████████  █████  ██      ██      ███████ ██████  
██       ██  ██  ██          ██ ████   ██ ██         ██    ██   ██ ██      ██      ██      ██   ██ 
█████     ████   ███████     ██ ██ ██  ██ ███████    ██    ███████ ██      ██      █████   ██████  
██         ██         ██     ██ ██  ██ ██      ██    ██    ██   ██ ██      ██      ██      ██   ██ 
██         ██    ███████     ██ ██   ████ ███████    ██    ██   ██ ███████ ███████ ███████ ██   ██ """)


def requirements():
    print(f"{GREEN}\nInstalling the project requirements...")
    command = "sudo apt install git python3-flask python3-flask-login python3-flask-sqlalchemy"
    try:
        os.system(command)
    except OSError as error:
        print(f"{RED}\nSomething went wrong with installing requirements! : {WHITE}{error}")


def get_project():
    print(f"{GREEN}\nDownloading project files...")
    command = "git clone https://github.com/YungYeno/corendon.git"
    try:
        os.system(command)
    except OSError as error:
        print(f"{RED}\nSomething went wrong with getting project files : {error}")


def moving_files():
    print(f"{GREEN}\nAdding files to the wsgi folder...")
    commands = ["sudo mv project /var/www/fys",
                "cd /var/www/fys",
                "sudo mkdir corendon",
                "cd project",
                "sudo mv app.py app.wsgi auth.py db.sqlite __init__.py models.py requirements.txt static templates /var/www/fys/wsgi",
                "sudo mv corendon.conf /etc/apache2/sites-available"]
    try:
        for command in commands:
            os.system(command)
    except OSError as error:
        print(f"{RED}\nSomething went wrong trying to move the files: {error}")


def permissions():
    print(f"{GREEN}\nSetting permissions...")
    commands = ["sudo chmod 755 -R /var/www/fys",
                "sudo chmod 663 /etc/apache2/sites-available/corendon.conf"]
    try:
        for command in commands:
            os.system(command)
    except OSError as error:
        print(f"{RED}\nSomething went wrong setting the permissions : {error}")


def outro():
    print(f"{GREEN}\nScript completed! {WHITE}Restart apache2 with {MAGENTA}'systemctl restart apache2'")


if __name__ == '__main__':
    intro()
    requirements()
    get_project()
    moving_files()
    permissions()
    outro()
