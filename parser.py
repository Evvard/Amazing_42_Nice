from typing import Any, Optional, Dict
from random import randint


def parse_type_value(value: Any) -> int | str | float:
    value = value.strip()
    if value.isdigit():
        return int(value)
    try:
        return float(value)
    except ValueError:
        return value


def extraction_config() -> dict:
    try:
        data = dict({})
        with open("config.txt", 'r') as file:
            for line in file:
                try:
                    line = line.strip()
                    if "=" in line:
                        key, value = line.split("=", 1)
                        data[key] = parse_type_value(value)
                    else:
                        raise ValueError
                except ValueError:
                    pass
    except FileNotFoundError or PermissionError:
        print("Missing file")
    return data


# en supposant que notre maze est une size entre 0 et 100
def config_validator(data: dict) -> Optional[Dict[str, Any] | str]:
    config = dict({})
    if "WIDTH" in config.keys():
        pass
    else:
        try:
            width = data.get("WIDTH")
            value_w = int(width)
            if value_w <= 0 or value_w >= 100:
                raise ValueError
            config.update({"WIDTH": value_w})
        except ValueError | KeyError | TypeError:
            return "WIDTH"

    if "HEIGHT" in config.keys():
        pass
    else:
        try:
            height = data.get("HEIGHT")
            value_h = int(height)
            if value_h <= 0 or value_h >= 100:
                raise ValueError
            config.update({"WIDTH": value_h})
        except ValueError | KeyError | TypeError:
            return "HEIGHT"

    if "ENTRY" in config.keys():
        pass
    else:
        try:
            entry = data.get("ENTRY")
            value_entry = float(entry)
            value_str = str(value_entry).replace('.', ',')
            [value_en] = value_str.split(',')
            value_en[0] = int(value_en[0])
            value_en[1] = int(value_en[1])
            if value_en[0] <= 0 or value_en[0] >= 100:
                raise ValueError
            if value_en[1] <= 0 or value_en[1] >= 100:
                raise ValueError
            config.update({"WIDTH": value_en})
        except ValueError | KeyError | TypeError:
            return "ENTRY"

    if "EXIT" in config.keys():
        pass
    else:
        try:
            exi_t = data.get("EXIT")
            value_exit = float(exi_t)
            value_str = str(value_exit).replace('.', ',')
            [value_ex] = value_str.split(',')
            value_ex[0] = int(value_ex[0])
            value_ex[1] = int(value_ex[1])
            if value_ex[0] <= 0 or value_ex[0] >= 100:
                raise ValueError
            if value_ex[1] <= 0 or value_ex[1] >= 100:
                raise ValueError
            config.update({"WIDTH": value_ex})
        except ValueError | KeyError | TypeError:
            return "ENTRY"

    if "PERFECT" in config.keys():
        pass
    else:
        try:
            perfect = data.get("PERFECT")
            if perfect.upper() == "TRUE":
                config.update({"PERFECT": True})
            elif perfect.upper() == "FALSE":
                config.update({"PERFECT": False})
            else:
                raise ValueError
        except ValueError | KeyError | TypeError:
            return "PERFECT"

    if config["ENTRY"] == config["EXIT"]:
        return "ENTRY==EXIT"
    return config
