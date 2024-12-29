def load_params(file="params.ini"):

    global PARAMS
    PARAMS = {}

    try:
        with open(file, mode="r", errors="ignore") as f:
            lines = f.readlines()
            for line in lines:
                param = line.split("=")
                if len(params) == 2:
                    key, value = param[0].strip(), param[1].strip()
                    if key != "dest":
                        try:
                            value = eval(value)
                        except (SyntaxError, NameError):
                            print(f"Невозможно преобразовать значение {value} для параметра {key}.")
                    PARAMS[key] = value
                else:
                    print(f"Некорректная строка в параметрах")
    except FileNotFoundError:
        print(f"Файл {file} не найден!")
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        if not PARAMS:
            PARAMS = {"dest": "calc-history.log.txt"}
        return PARAMS

def write_log(*args, action=None, result=None, file='calc-history.log.txt'):
    
    error = None
    try:
        with open(file, mode="a", errors="ignore") as f:
            f.write(f"{action}: {args} = {result} \n")
    except PermissionError:
        print(f'Ошибка записи в файл {file}')
        file_new = file + '.txt'
        print(f'Попытка записать лог в файл с новым именем: {file_new}')
        try:
            with open(file_new, mode='a', errors='ignore') as backup_file:
                backup_file.write(f"{action}: {args} = {result} \n")
        except PermissionError as e:
            error = e
            print("Ошибка записи в резервный файл!")
    finally:
        if error:
            raise Exception(f"Ошибка записи в оба файла!\n{error}")


def calculate(*args, **kwargs):

    params = load_params(kwargs.get("params_file", "params.ini"))
    print(f"Параметры: {params}")

    result = sum(args)

    print(f"Результаты вычислений: {result}")

    try:
        write_log(*args, action='sum', result=result, file=PARAMS['dest'])
    except Exception as log_error:
        print(log_error)
        print(f"Данные для записи: {args} = {result}")
    finally:
        print("Вычисления завершены")

if __name__ == "__main__":
    try:
        PARAMS = {}
        calculate(1,2,3,4,5)
    except Exception as e:
        print(f"Критическая ошибка: {e}")