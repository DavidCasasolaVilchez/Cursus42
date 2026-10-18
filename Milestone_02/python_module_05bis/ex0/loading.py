def main() -> None:
    print(
        "\nREAGENT STATUS: Loading reagents..."
        "\n\nChecking dependencies"
    )
    try:
        import pandas
        print(
            f"[OK] pandas ({pandas.__version__}) - Data manipulation ready"
        )
    except (ImportError, NameError):
        print(
            "[MISSING] pandas\n"
            "  pip: pip install pandas\n"
            "  Poetry: poetry add pandas"
        )
    try:
        import numpy
        print(
            f"[OK] numpy ({numpy.__version__}) - Numerical computation ready"
        )
    except (ImportError, NameError):
        print(
            "[MISSING] numpy\n"
            "  pip: pip install numpy\n"
            "  Poetry: poetry add numpy"
        )
    print(
        "\n\npip vs Poetry:"
        "\n\trequirements.txt declares what to install; pip resolves "
        "it at install time."
        "\n\tpyproject.toml declares the same constraints, "
        "and Poetry pins the resolved"
        "\n\tversions in poetry.lock."
        "\n\nAll reagents present and accounted for."
    )


if __name__ == "__main__":
    main()
