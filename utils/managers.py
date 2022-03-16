import pathlib


PREVIOUS_RECEIVED = 0


def check_folder(folder_path):
    """Create folder if it's not exists."""
    pathlib.Path(folder_path).mkdir(parents=True, exist_ok=True)


def check_file(filename):
    try:
        file = open(filename, 'x')
        file.close()
    except FileExistsError as err:
        print(f"{filename} exists!")


def update(progressbar, current_received):
    global PREVIOUS_RECEIVED
    diff = current_received - PREVIOUS_RECEIVED
    progressbar.update(diff)
    PREVIOUS_RECEIVED = current_received
