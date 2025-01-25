"""
with this python program, you can check your exercise on your own

usage:
    python3 check.py <name_of_your_solution.py>

you can pass optional function_names, to only check specific functions

usage:
    python3 check.py <name_of_your_solution.py> -f function_name

PS: DO NOT MODIFY THIS FILE, OR THE CHECKS MAY NOT WORK CORRECTLY
    AND YOUR FINAL SUBMISSION WILL MAY NOT WORK AS YOU EXPECT!
"""

import sys
from argparse import ArgumentParser, Namespace
from dataclasses import dataclass
from enum import StrEnum
from importlib import import_module
from os import getcwd, listdir
from pathlib import Path
from shutil import rmtree
from typing import Any, Callable


def main():
    args = get_args()
    code_file = args.code_file
    functions = args.functions or [check.function_name for check in checks]

    if not code_file.exists():
        sys.exit(error(f"file '{bold(code_file.name)}' does not exist!"))

    try:
        module = import_module(
            code_file.stem, str(code_file.parent.absolute()))

        for function_name in functions:
            function = getattr(module, function_name, None)
            if not function:
                print(error(
                    f"function '{bold(function_name)}' does not exist in '{italic(code_file)}'\n"))
                continue

            check = next(
                filter(lambda x: x.function_name == function_name, checks))
            if not check:
                print(
                    error(f"no checks for function '{bold(function_name)}' available\n"))
                continue

            print(f"checks for {bold(check.function_name)}:")
            for validation in check.validations:
                try:
                    result = function(*validation.input)
                    assert validation.assert_fct(
                        result, validation.expected), f"expected: {validation.expected} ({class_name(validation.expected)}), got: {repr(result)} ({class_name(result)})"
                    info(function_name, validation.input,
                         validation.expected, MARK.OK, ok, parameter_max_length=validation.max_length_input_print)
                except AssertionError as e:
                    info(function_name, validation.input, e, MARK.ERR, warn,
                         parameter_max_length=validation.max_length_input_print)
                except Exception as e:
                    info(function_name, validation.input,
                         f'{class_name(e)} {line_nr(e)}: {e}', MARK.ERR, warn, parameter_max_length=validation.max_length_input_print)
            print()
    except ModuleNotFoundError as e:
        sys.exit(
            error(f"error on importing '{code_file}'\n{MARK.ERR} {warn(str(e))}"))
    except Exception as e:
        if args.verbose:
            raise e
        else:
            print(f"unexpected error occurred {e}", file=sys.stderr)
            sys.exit(f"if you want to see full stacktrace, use option '--verbose'")


def get_args() -> Namespace:
    parser = ArgumentParser(prog=sys.argv[0], description="this program will help you to check your exercise",
                            epilog="when you find any errors or stuck, please contact <harald.schwab2@fh-joanneum.at>")
    parser.add_argument('code_file', type=Path,
                        help='path to your code file, that should be checked')
    parser.add_argument('-f', '--function', metavar='function_name',
                        dest='functions', action='append', )

    return parser.parse_args()


class MARK(StrEnum):
    EMPTY = ''
    OK = f' [\u2713]'   # [✓]
    ERR = f' [\u2717]'  # [✗]


# https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797#colors--graphics-mode
class COLOR(StrEnum):
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    DEFAULT = '\033[39m'
    RESET = '\033[0m'


class FORMAT(StrEnum):
    BOLD = '\033[1m'
    RBOLD = '\033[22m'
    ITALIC = '\033[3m'
    RITALIC = '\033[23m'


def ok(s: str) -> str:
    """GREEN coloured string"""
    return f"{COLOR.GREEN}{s}{COLOR.DEFAULT}"


def error(s: str) -> str:
    """RED coloured string"""
    return f"{COLOR.RED}{s}{COLOR.DEFAULT}"


def warn(s: str) -> str:
    """YELLOW coloured string"""
    return f"{COLOR.YELLOW}{s}{COLOR.DEFAULT}"


def bold(s: str) -> str:
    """BOLD formatted string"""
    return f"{FORMAT.BOLD}{s}{FORMAT.RBOLD}"


def italic(s: str) -> str:
    """ITALIC formatted string"""
    return f"{FORMAT.ITALIC}{s}{FORMAT.RITALIC}"


def info(fn: str, input: list[Any], output: Any, mark: MARK, color=ok, parameter_max_length=-1):
    """helper to print formatted info about assertion"""
    if parameter_max_length == -1:
        def f(x: Any) -> str:
            return repr(x)
    else:
        def f(x: Any) -> str:
            r = repr(x)
            if len(r) - 5 > parameter_max_length:
                return r[0] + r[1:parameter_max_length-1] + '...' + r[-1]
            else:
                return r
    output = repr(output) if not isinstance(output, Exception) else str(output)
    print(
        color(f'{mark} {fn}({", ".join([f(x) for x in input])}) -> {output}'))


def class_name(o: Any) -> str:
    return type(o).__name__


def line_nr(e: Exception) -> str:
    tbo = e.__traceback__
    ln = 0
    if tbo:
        while tbo.tb_next:
            tbo = tbo.tb_next
        ln = tbo.tb_lineno
    return f'(line {ln})' if ln > 0 else ''


def cleanup(args: Namespace):
    cwd = Path(getcwd())
    code_path = args.code_file.parent
    try:
        for path in [cwd, code_path]:
            if '__pycache__' in listdir(path):
                rmtree(path.joinpath('__pycache__'))
    except:
        sys.exit('error on cleaning')


def assert_equal(actual: Any, expected: Any) -> bool:
    return actual == expected


def assert_float(actual: float, expected: float, threshold: float = 0.009) -> bool:
    return abs(actual - expected) <= threshold


@dataclass
class Validation:
    input: list[Any]
    expected: Any
    assert_fct: Callable[[Any, Any], bool] = assert_equal
    max_length_input_print: int = -1


@dataclass
class Check:
    function_name: str
    validations: list[Validation]


one = """I can't remember anything
Can't tell if this is true or dream
Deep down inside I feel to scream
This terrible silence stops me

Now that the war is through with me
I'm waking up, I cannot see
That there's not much left of me
Nothing is real but pain now

Hold my breath as I wish for death
Oh please, God, wake me

Back in the womb it's much too real
In pumps life that I must feel
But can't look forward to reveal
Look to the time when I'll live

Fed through the tube that sticks in me
Just like a wartime novelty
Tied to machines that make me be
Cut this life off from me

Hold my breath as I wish for death
Oh please, God, wake me

Now the world is gone, I'm just one
Oh God, help me
Hold my breath as I wish for death
Oh please, God, help me

Darkness
Imprisoning me
All that I see
Absolute horror
I cannot live
I cannot die
Trapped in myself
Body my holding cell

Landmine
Has taken my sight
Taken my speech
Taken my hearing
Taken my arms
Taken my legs
Taken my soul
Left me with life in hell
"""

barbara_streisand = """Barbra Streisand
Oo-oo who-oo-oo whooo-oo oo-oo
Oo-oo who-oo-oo whooo-oo oo-oo
Oo-oo who-oo-oo whooo-oo oo-oo
Barbra Streisand
Oo-oo who-oo-oo whooo-oo oo-oo
Oo-oo who-oo-oo whooo-oo oo-oo
Oo-oo who-oo-oo whooo-oo oo-oo
Oo-oo who-oo-oo whooo-oo
Barbra Streisand

Oo-oo who-oo-oo whooo-oo oo-oo
Oo-oo who-oo-oo whooo-oo oo-oo
Oo-oo who-oo-oo whooo-oo
Barbra Streisand
Oo-oo who-oo-oo whooo-oo oo-oo
Oo-oo who-oo-oo whooo-oo oo-oo
Oo-oo who-oo-oo whooo-oo oo-oo
Oo-oo who-oo-oo whooo-oo oo-oo
Oo-oo who-oo-oo whooo-oo oo-oo
Oo-oo who-oo-oo whooo-oo oo-oo
Oo-oo who-oo-oo whooo-oo oo-oo
Oo-oo who-oo-oo whooo-oo

Barbra Streisand
Oo-oo who-oo-oo whooo-oo oo-oo
Oo-oo who-oo-oo whooo-oo oo-oo
Oo-oo who-oo-oo whooo-oo oo-oo
Oo-oo who-oo-oo whooo-oo
Barbra Streisand
Oo-oo oo-oo oo-oo whooo-oo
Oo-oo who-oo-oo whooo-oo oo-oo
Oo-oo oo-oo oo-oo whooo-oo
Oo-oo who-oo-oo whooo-oo
Barbra Streisand
Oo-oo whooo-oo
Oo-oo whooo-oo oo-oo whooo-oo
Oo-oo whooo-oo
Barbra Streisand
Oo-oo who-oo-oo whooo-oo oo-oo
Oo-oo who-oo-oo whooo-oo oo-oo
Oo-oo who-oo-oo whooo-oo oo-oo"""

checks = [
    Check('remove_non_alpha', [
        Validation(["hello"], 'hello'),
        Validation(["world!"], 'world'),
        Validation(["Can't"], 'Cant'),
        Validation(['2nd'], 'nd'),
        Validation(['S0m€th!ng'], 'Smthng'),
        Validation(['3.14'], ''),
    ]),
    Check('extract_words', [
        Validation(["This isn't some Text. This is an example !"], [
                   "this", "isnt", "some", "text", "this", "is", "an", "example"]),
        Validation(['ar! 47 nogul 2nu\nHa[m @, oLA $ef'],
                   ['ar', 'nogul', 'nu', 'ham', 'ola', 'ef']),
        Validation(['Hello, World!'], ['hello', 'world']),
        Validation([''], []),
    ]),
    # Check('order_by_length', [
    #     Validation(["This is what I expect".split()],
    #                "I is This what expect".split()),
    #     Validation(["100 1 10 10000 1000".split()],
    #                "1 10 100 1000 10000".split()),
    #     Validation([["single"]], ["single"]),
    #     Validation([[]], []),
    # ]),
    Check('uniq', [
        Validation(["test this is this is some test".split()],
                   "test this is some".split()),
        Validation([list('abacbd')], list('abcd')),
        Validation(["hello world".split()], "hello world".split()),
        Validation([["single"]], ["single"]),
        Validation([[]], []),
    ]),
    Check('lengths', [
        Validation(["This is some test text for lengths".split()],
                   [4, 2, 4, 4, 4, 3, 7]),
        Validation([['hello', 'swd', '', '2023']], [5, 3, 4]),
        Validation([['']], []),
    ]),
    Check('min', [
        Validation([[7, 3, 8, 1, 5]], 1),
        Validation([[4, 2, 7, 3]], 2),
        Validation([[724, 93, 18, 432]], 18),
        Validation([[-2, 3, -5, 5]], 3),
        Validation([[-2, -5, -8]], 0),
        Validation([[]], 0),
    ]),
    Check('max', [
        Validation([[7, 3, 8, 1, 5]], 8),
        Validation([[4, 2, 7, 3]], 7),
        Validation([[724, 93, 18, 432]], 724),
        Validation([[-2, 3, -5, 5]], 5),
        Validation([[-2, -5, -8]], 0),
        Validation([[]], 0)
    ]),
    Check('counts', [
        Validation([[4, 1, 4, 2, 1]], [2, 1, 0, 2]),
        Validation([[5, 5, 5, 5]], [4]),
        Validation([[3, 7, 5]], [1, 0, 1, 0, 1]),
        Validation([[]], []),
    ]),
    Check('score', [
        Validation([one], 0.32, assert_float, 20),
        Validation([barbara_streisand], 0.17, assert_float, 20)
    ]),
]


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
    finally:
        cleanup(get_args())
