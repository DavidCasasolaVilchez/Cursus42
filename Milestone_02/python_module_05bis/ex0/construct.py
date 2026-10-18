import sys
import os
import site


def display_sealing() -> None:
    labstatus: str = "LABORATORY STATUS: "
    currentpy: str = "Current Python: " + sys.executable
    venvironm: str = "Virtual Environment: "
    envpath: str
    reagent: str
    action: str
    if sys.prefix != sys.base_prefix:
        action = (
            "SUCCESS: You are working in an isolated environment!"
            "\nSafe to install reagents without affecting"
            "\nthe global system."
        )
        envpath = f"Environment Path: {sys.prefix}"
        labstatus += "The laboratory is sealed"
        venvironm += f"{os.path.basename(sys.exec_prefix)}"
        reagent = f"Reagent installation path:\n{site.getsitepackages()[0]}"
    else:
        action = (
            "To seal the laboratory, run:"
            "\npython3 -m venv lab_env"
            "\nsource lab_env/bin/activate # On Unix"
            "\nlab_env\\Scripts\\activate # On Windows"
        )
        envpath = (
            "\nWARNING: You are in the global environment!"
            "\nEvery reagent you install here leaks into the whole system"
        )
        labstatus += "You are working in the open"
        venvironm += "None detected"
        reagent = "Then run this program again."
    print(
        f"\n{labstatus}\n"
        f"\n{currentpy}"
        f"\n{venvironm}"
        f"\n{envpath}"
        f"\n\n{action}\n"
        f"\n{reagent}"
    )


def main() -> None:
    display_sealing()


if __name__ == "__main__":
    main()
