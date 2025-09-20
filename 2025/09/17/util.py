import readline

def ask_int(prompt: str, minimum: int | float, maximum: int | float, default: str = "", validators=[]) -> int:
    def hook():
        readline.insert_text(default.strip())
        readline.redisplay()
    readline.set_pre_input_hook(hook)
    while True:
        try:
            value = int(input(prompt).strip())
            if value < minimum or value > maximum:
                raise ValueError(f"{value} is not within range [{minimum}, {maximum}]")
            for validator in validators:
                validator(value)
            return value
        except ValueError as e:
            print(e)
        finally:
            readline.set_pre_input_hook(None)

def ask_num(prompt: str, default: str = "", validators=[]) -> float:
    def hook():
        readline.insert_text(default.strip())
        readline.redisplay()
    readline.set_pre_input_hook(hook)
    while True:
        try:
            value = float(input(prompt).strip())
            for validator in validators:
                validator(value)
            return value
        except ValueError as e:
            print(e)
        finally:
            readline.set_pre_input_hook(None)

def ask_row(prompt: str, num_cols: int, default: str = "", validators=[]) -> list[float]:
    def hook():
        readline.insert_text(default.strip())
        readline.redisplay()
    readline.set_pre_input_hook(hook)
    while True:
        try:
            row_str = input(prompt).strip()
            row = [float(n) for n in row_str.split(" ")]
            if len(row) != num_cols:
                raise ValueError(f"Length of input {len(row)} does not match number of columns {num_cols}")
            for validator in validators:
                validator(value)
            return row
        except ValueError as e:
            print(e)
        finally:
            readline.set_pre_input_hook(None)
            
def ask_bool(prompt: str, default: bool) -> bool:
    bool_str = input(prompt).lower()
    if bool_str in ["t", "true", "y", "yes"]:
        return True
    elif bool_str in ["f", "false", "n", "no"]:
        return False
    return default