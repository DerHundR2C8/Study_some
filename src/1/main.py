SUFFIXES = {'ci': ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB', 'YobaB'],
            'pr': ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB', 'YobiB']}


def human_size(byte_size: int, use_ci: bool = False):
    if byte_size < 0:
        raise ValueError('Введите адекватное число')
    index = 0
    suffixes = SUFFIXES['ci'] if use_ci else SUFFIXES['pr']
    multiple = 1000 if use_ci else 1024
    current_size = byte_size
    while current_size > multiple:
        if index >= len(suffixes) - 1:
            break
        current_size /= multiple
        index += 1
    return f'{current_size} {suffixes[index]}'


if __name__ == '__main__':
    byte1 = int(input('Введите кол-во байт'))
    print(human_size(byte1, use_ci=True))
    pass
