from enum import Enum
from colorama import Fore, Style


class FileType(Enum):
    INPUT = 1
    TEST = 2
    OTHER = 3


# region Print Functions with colors

def print_error(text):
    print_colored(text, Fore.RED)


def print_success(text):
    print_colored(text, Fore.GREEN)


def print_title(text):
    print_colored(text, Fore.BLUE)


def print_result(text):
    print_colored(text, Fore.YELLOW)


def print_debug(text):
    print_colored(text, Fore.LIGHTBLUE_EX)


def print_colored(text, color: Fore):
    print(color + str(text) + Style.RESET_ALL)

# endregion


# region File Read functions

def open_file(filename) -> str:
    with open(filename) as f:
        content = f.read()
    return content


def open_file_lines(filename) -> list[str]:
    with open(filename) as f:
        content = f.readlines()
    return [x.replace("\n", "") for x in content]


def open_file_str_array(filename) -> list[list[str]]:
    return [list(x) for x in open_file_lines(filename)]


def open_file_int_array(filename) -> list[int]:
    return [int(x) for x in open_file_lines(filename)]


def open_file_int_matrix(filename) -> list[list[int]]:
    return [[int(y) for y in x.strip()] for x in open_file_lines(filename)]


# endregion


class BaseClass:
    def __init__(self):
        pass

    # region Execution Functions

    def execute_internal(self, filepath) -> int:
        raise NotImplementedError('Method "executeInternal" not implemented.')

    def execute(self, filetype=FileType.INPUT, filename='') -> int:
        if filetype == FileType.OTHER and filename == '':
            raise Exception('File name not specified')

        if filetype == FileType.INPUT:
            filename = "input.txt"
        elif filetype == FileType.TEST:
            filename = "example.txt"

        complete_filename = f"../input_files/{filename}"

        print(f"Start Execution {filename}:")
        result = self.execute_internal(complete_filename)

        print(f"End Execution {filename}, result: ", end="")
        print_result(f"{result}")
        return result

    def test(self,
             expected_result: int,
             additional_test_filenames: list[str] = [],
             additional_test_expected_results: list[int] = []):

        print_title("Test:")
        main_test_result = self.execute(FileType.TEST)
        if main_test_result != expected_result:
            print_error("Main test failed")
        else:
            print_success("Main test succeeded")

        for cur_filename, cur_expected_value in zip(additional_test_filenames, additional_test_expected_results):
            cur_test_result = self.execute(FileType.OTHER, cur_filename)
            if cur_test_result != cur_expected_value:
                print_error(f"Test {cur_filename} failed")
            else:
                print_success(f"Test {cur_filename} succeeded")
        print_title("End test\n")
    # endregion
