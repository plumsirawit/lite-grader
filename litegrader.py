import argparse
import subprocess
import os
import pathlib

parser = argparse.ArgumentParser(description='Evaluate against testdata', formatter_class=argparse.RawDescriptionHelpFormatter, epilog='''
Detailed Usage:

Contestant's solution file (ans): the executable solution file which reads from stdin and writes to stdout
Testdata directory (tests)
Time limit (TL)
''')
parser.add_argument(
    'ans', type=str, help='contestant\'s solution file')
parser.add_argument(
    'tests', type=str, help='path to testdata directory')
# tests (in cms format: xx-yy.in, xx-yy.sol)
parser.add_argument('TL', type=int, help='time limit in ms')
args = parser.parse_args()
ansfn = args.ans
testdir = args.tests

ans_path = pathlib.Path(ansfn).resolve(True)
tests_path = pathlib.Path(testdir).resolve(True)

groups = {}
for testfile in tests_path.glob('*.in'):
    sub, test = map(int, testfile.stem.split('-'))
    if sub not in groups:
        groups[sub] = set([test])
    else:
        groups[sub].add(test)

TIMEOUT = args.TL / 1000  # time limit in seconds
mainres = []
for sub, tests in sorted(groups.items()):
    groupres = ''
    for test in sorted(tests):
        print(f'Evaluating subtask {sub}, test {test}', end=': ')
        with (tests_path / f'{str(sub).zfill(2)}-{str(test).zfill(2)}.in').open() as inf:
            result = None
            with open(f'./tmp.out', 'w') as ouf:
                proc = subprocess.Popen(
                    ans_path.as_posix(), stdin=inf, stdout=ouf)
                try:
                    proc.wait(TIMEOUT)
                except subprocess.TimeoutExpired:
                    result = 'T'
                    proc.kill()
                pstatus = proc.poll()
                if pstatus is None:
                    result = 'T'
                    proc.kill()
                elif pstatus != 0 and result is None:
                    result = 'x'
            if result is None:
                with open(f'./tmp.out') as ouf:
                    with (tests_path / f'{str(sub).zfill(2)}-{str(test).zfill(2)}.sol').open() as ans:
                        if ans.read().split() == ouf.read().split():
                            result = 'P'
                        else:
                            result = '-'
        groupres += result
        print(result)
    mainres.append(groupres)
print('[' + ']['.join(mainres) + ']')
os.remove('./tmp.out')
