from settings import app_name, app_version
from app.cli import TerminalApp

def main():
    print(f"Welcome to {app_name}/{app_version}!")

    app = TerminalApp()
    app.run()


if __name__ == "__main__":
    main()
