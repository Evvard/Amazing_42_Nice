def main() -> None:
    try:
        int("s")
        print("ok")
    except ValueError:
        print("error")


main()
