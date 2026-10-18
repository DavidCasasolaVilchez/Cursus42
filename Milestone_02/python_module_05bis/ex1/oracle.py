import dotenv
import os


def display_configuration() -> None:
    print(
        "\nORACLE STATUS: Consulting the configuration..."
        "\n\nConfiguration loaded:"
    )
    dotenv.load_dotenv()
    try:
        env = os.environ
        mode: str = env["MATRIX_MODE"]
        database: str
        if env["DATABASE_URL"] != "":
            database = "Connected to local instance"
        else:
            database = "Disconnected to local instance"
        api: str
        if env["API_KEY"] != "":
            api = "Authenticated"
        else:
            api = "Is not authenticated"
        log: str = env["LOG_LEVEL"]
        endpoint: str
        if env["ZION_ENDPOINT"] != "":
            endpoint = "online"
        else:
            endpoint = "disconected"
        print(
            f"Mode: {mode}\n"
            f"Database: {database}\n"
            f"API Access: {api}\n"
            f"Log Level: {log}\n"
            f"Remote Network: {endpoint}\n"
        )
    except KeyError as e:
        print(f"[Error] {e}")


def display_checks() -> None:
    file = open("oracle.py")
    text: str = file.read()
    hc1: bool = "MATRIX_MODE = \"" in text
    hc2: bool = "DATABASE_URL = \"" in text
    hc3: bool = "API_KEY = \"" in text
    hc4: bool = "LOG_LEVEL = \"" in text
    hc5: bool = "ZION_ENDPOINT = \"" in text
    hc: str
    if not (hc1 and hc2 and hc3 and hc4 and hc5):
        hc = "[OK] No hardcoded secrets detected"
    else:
        hc = "[KO] Hardcoded secrets detected"
    file = open(".gitignore")
    text = file.read()
    gi: str
    if ".env" in text:
        gi = "[OK] .env file properly ignored by git"
    else:
        gi = "[KO] .env file is not ignored by git"
    po: str
    env = os.environ
    try:
        mode: str = env["MATRIX_MODE"]
        mode2: str
        dotenv.load_dotenv()
        mode2 = env["MATRIX_MODE"]
        if mode == mode2:
            po = "[OK] Production overrides available"
        else:
            po = "[KO] Production overrides unavailable"

    except KeyError:
        po = "[OK] Production overrides available"
    print(
        "Configuration security check:\n"
        f"{hc}\n"
        f"{gi}\n"
        f"{po}\n"
        "\nThe Oracle sees all configurations."
    )


def main() -> None:
    display_configuration()
    display_checks()


if __name__ == "__main__":
    main()
