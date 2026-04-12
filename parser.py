from typing import Any, Dict, List
import time


def parse_type_value(value: Any) -> int | str | float:
    value = value.strip()
    if value.isdigit():
        return int(value)
    try:
        return float(value)
    except ValueError:
        return str(value)


def extraction_config(entry: str) -> Dict[str, Any]:
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
    except ValueError as e:
        raise ValueError(e)
    except Exception:
        raise FileNotFoundError("File Missing")
    return data


def config_validator(data: dict) -> Dict[str, Any]:
    config: Dict[str, Any] = {}

    try:
        width = data.get("WIDTH")
        value_w = int(width) if width is not None else 0
        if value_w <= 0 or value_w >= 100:
            raise ValueError
        config.update({"WIDTH": value_w})
    except (Exception):
        raise Exception("Probleme with WIDTH, min 0, max 100")

    try:
        height = data.get("HEIGHT")
        value_h = int(height) if height is not None else 0
        if value_h <= 0 or value_h >= 100:
            raise ValueError
        config.update({"HEIGHT": value_h})
    except (Exception):
        raise Exception("Probleme with HEIGHT, min 0, max 100")

    try:
        entry = data.get("ENTRY")
        value_str = str(entry).replace('.', ',')
        parts = value_str.split(',')
        value_en: List[int] = [int(parts[0]), int(parts[1])]
        if value_en[0] < 0 or value_en[0] > 100:
            raise ValueError("Out of range, error")
        if value_en[1] < 0 or value_en[1] > 100:
            raise ValueError("Out of range, error")
        if value_en[0] >= value_w or value_en[1] >= value_h:
            raise ValueError("Entry coordinates are out of maze bounds")
        config.update({"ENTRY": value_en})
    except (Exception) as e:
        raise Exception("Probleme with ENTRY value", e)

    try:
        exi_t = data.get("EXIT")
        value_str = str(exi_t).replace('.', ',')
        value_ex = value_str.split(',')
        value_exit: List[int] = [int(value_ex[0]), int(value_ex[1])]
        if value_exit[0] < 0 or value_exit[0] > 100:
            raise ValueError
        if value_exit[1] < 0 or value_exit[1] > 100:
            raise ValueError
        if value_exit[0] >= value_w:
            raise ValueError("Exit coordonate are bigger than Widht")
        if value_exit[1] >= value_h:
            raise ValueError("Exit coordonate are bigger than height")
        config.update({"EXIT": value_exit})
    except Exception as m:
        raise Exception(f"Probleme with EXIT value: {m}")

    if config["ENTRY"] == config["EXIT"]:
        raise Exception("Probleme with Entry because EXIT == ENTRY")

    try:
        perfect = data.get("PERFECT")
        if perfect == "TRUE":
            config.update({"PERFECT": True})
        elif perfect == "FALSE":
            config.update({"PERFECT": False})
        else:
            raise ValueError
    except (Exception):
        raise Exception("Problem with PERFECT flag, juste write FALSE or TRUE")

    try:
        algo = data.get("ALGORITHM")
        # a modifier en fonction de l'algo
        if algo == "bactracking":
            config.update({"ALGORITHM": algo})
        else:
            raise ValueError
    except (Exception):
        raise Exception("ALGORITHM")

    try:
        seed = data.get("SEED")
        if not seed:
            config.update({"SEED": time.time()})
        else:
            config.update({"SEED": seed})
    except (Exception):
        raise Exception("Probleme with SEED, please change value")

    try:
        output = data.get("OUTPUT_FILE")
        output = str(output)
        if output.endswith(".txt") and len(output) >= 5:
            if output == "config.txt":
                raise Exception("Probleme with OUTPUT FILE = FILE")
            config.update({"OUTPUT_FILE": output})
        else:
            raise ValueError
    except (Exception) as e:
        raise Exception(f"Probleme with OUTPUT_FILE {e}")

    return config
