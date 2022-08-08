import argparse
import subprocess
import os

parser = argparse.ArgumentParser(description='Evaluate against testdata', formatter_class=argparse.RawDescriptionHelpFormatter, epilog='''
Detailed Usage:

Contestant's solution file: ./ans, the executable solution file which reads from stdin and writes to stdout
Testdata directory: ./tests/
''')
args = parser.parse_args()

TIMEOUT = 2  # time limit in seconds
groups = [5, 5, 10, 10, 7, 8, 15]  # tests (in cms format: xx-yy.in, xx-yy.sol)
mainres = []
for i in range(len(groups)):
    groupres = ''
    for j in range(groups[i]):
        with open(f'./result/{i+1}-{j+1}.in') as inf:
            result = None
            with open(f'./tmp.out', 'w') as ouf:
                proc = subprocess.Popen('./ans', stdin=inf, stdout=ouf)
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
                    with open(f'./result/{i+1}-{j+1}.sol') as ans:
                        if ans.read().split() == ouf.read().split():
                            result = 'P'
                        else:
                            result = '-'
        groupres += result
    mainres.append(groupres)
print('[' + ']['.join(mainres) + ']')
os.remove('./tmp.out')
