from typing import Any, Optional, Dict
# version_correcte


def parse_type_value(value: Any) -> int | str | float:
    value = value.strip()
    if value.isdigit():
        return int(value)
    try:
        return float(value)
    except ValueError:
        return value


def extraction_config(entry: str) -> Optional[Dict[str, Any] | str]:
    try:
        if entry != "config.txt":
            raise FileNotFoundError
        data = dict({})
        with open(entry, 'r') as file:
            for line in file:
                if line.startswith("#"):
                    continue
                line = line.strip()
                if "=" in line:
                    key, value = line.split("=", 1)
                    data[key] = parse_type_value(value)
                else:
                    raise ValueError("INVALID VALUE IN CONFIG.TXT")
    except FileNotFoundError or PermissionError:
        raise FileNotFoundError("File Missing")
    return data


# en supposant que notre maze est une size entre 0 et 100
def config_validator(data: dict) -> Optional[Dict[str, Any] | str]:
    config = dict({})

    try:
        width = data.get("WIDTH")
        value_w = int(width)
        if value_w <= 0 or value_w >= 100:
            raise ValueError
        config.update({"WIDTH": value_w})
    except (Exception):
        return "Probleme with WIDTH, min 0, max 100"

    try:
        height = data.get("HEIGHT")
        value_h = int(height)
        if value_h <= 0 or value_h >= 100:
            raise ValueError
        config.update({"HEIGHT": value_h})
    except (Exception):
        return "Probleme with HEIGHT, min 0, max 100"

    try:
        entry = data.get("ENTRY")
        value_str = str(entry).replace('.', ',')
        value_en = value_str.split(',')
        value_en[0] = int(value_en[0])
        value_en[1] = int(value_en[1])
        if value_en[0] < 0 or value_en[0] > 100:
            raise ValueError
        if value_en[1] < 0 or value_en[1] > 100:
            raise ValueError
        config.update({"ENTRY": value_en})
    except (Exception):
        return "Probleme with ENTRY value"

    try:
        exi_t = data.get("EXIT")
        value_str = str(exi_t).replace('.', ',')
        value_ex = value_str.split(',')
        value_ex[0] = int(value_ex[0])
        value_ex[1] = int(value_ex[1])
        if value_ex[0] < 0 or value_ex[0] > 100:
            raise ValueError
        if value_ex[1] < 0 or value_ex[1] > 100:
            raise ValueError
        config.update({"EXIT": value_ex})
    except (Exception):
        return "Probleme with EXIT value "

    if config["ENTRY"] == config["EXIT"]:
        return "Probleme with Entry because EXIT == ENTRY"

    try:
        perfect = data.get("PERFECT")
        if perfect.upper() == "TRUE":
            config.update({"PERFECT": True})
        elif perfect.upper() == "FALSE":
            config.update({"PERFECT": False})
        else:
            raise ValueError
    except (Exception):
        return "Probleme with PERFECT flag, juste write FALSE or TRUE"

    try:
        algo = data.get("ALGORITHM")
        # a modifier en fonction de l'algo
        if algo == "?":
            config.update({"ALGORITHM": algo})
        # possinilite d'implementer un 2eme algo
        else:
            raise ValueError
    except (Exception):
        return "ALGORITHM"

    try:
        # Je ne sais pas le format des seeds donc a modifier plus tard
        seed = data.get("SEED")
        if not data:
            config.update({"SEED": "NOT_DATA"})
        else:
            config.update({"SEED": seed})
    except (Exception):
        return "Probleme with SEED, please change value"

    try:
        output = data.get("OUTPUT_FILE")
        output = str(output)
        if output.endswith(".txt") and len(output) >= 5:
            if output == "config.txt":
                return "Probleme with OUTPUT FILE = FILE"
            config.update({"OUTPUT_FILE": output})
        else:
            raise ValueError
    except (Exception):
        return "Probleme with OUTPUT_FILE"

    return config
