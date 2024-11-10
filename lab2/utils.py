def delete_prev_values():
    with open("../txtf/output.txt", 'w') as file:
        pass
delete_prev_values()


with open("../txtf/output.txt", 'w') as file:
    pass
def open_file(file_name):
    with (open(file_name, 'r') as file):
        lines = [line.strip() for line in file if line.strip()]
        if len(lines) >= 2:
            data_n = list(map(int, lines[0].split()))
            n, arr_n = data_n[0], data_n[1:]
            data_k = list(map(int, lines[1].split()))
            k = data_k[0]
            arr_k = data_k[1:] if len(data_k) > 1 else []
            return [n] + arr_n, [k] + arr_k



def write_file(arr, file_name, mode = 'w'):
    with open(file_name, mode) as file:
        if isinstance(arr, (str, int)):
            file.write(str(arr))
        elif isinstance(arr, list):
            if len(arr) > 0 and isinstance(arr[0], list):
                for r in arr:
                    file.write(" ".join(map(str, r)) + "\n")
            else:
                file.write(" ".join(map(str, arr)) + "\n")