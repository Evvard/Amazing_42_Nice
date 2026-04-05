from parser import extraction_config, config_validator
from sys import argv


def main() -> None:
    try:
        brut_data_from_config_txt = extraction_config(argv[1])
    except IndexError:
        print("Missig argument in argv")
        return

    if isinstance(brut_data_from_config_txt, str):
        print(brut_data_from_config_txt)
        return

    config = config_validator(brut_data_from_config_txt)

    if isinstance(config, str):
        print(f"EntryError: there is on error in config.txt : {config}")
        return

    print(config)
    # config ok



if __name__ == "__main__":
    main()
