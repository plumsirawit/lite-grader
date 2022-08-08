# lite-grader
A **very** lightweight offline judge.

## Usage
Before using the `lite-grader`, prepare two things:
1. Your executable answer file (if you only have in C/C++, compile it first before using this tool).
2. Testset (testdata, tests, or whatever...), in the `xx-yy.in`, `xx-yy.sol` format where `xx` is the subtask number
(i.e. `01`, `02`, etc.) and `yy` is the testcase number in that subtask. Careful: you need to pad a zero for one digit number.
(use `01` instead of `1`)

Suppose your answer executable is at `ANSWER_PATH`, your testset directory is at `TESTS_PATH`, and the time limit for
each testcase is `TL` milliseconds, then you can run `python3 litegrader.py ANSWER_PATH TESTS_PATH TL` directly.

## Warning
This offline judge does not use any kind of sandbox. (the well-known `box` or `isolate` were planned to be used but I don't have enough time to do it, otherwise this won't be this such lightweight) Handle with care, do not use with dangerous executable if you don't know what you're doing. (i.e. with system commands such as shutdown, or something that mess with files)

The offline judge is provided as-is. It is intended to be used as a problemsetter's tool to test (initially) whether a wrong program produces correct output or a correct program produces wrong output, etc. The time limit is not strict, initial testing shows that sometimes running the same thing twice may get a `T` or a `P` randomly. Set the time limit accordingly with care.

## Final notes
I provide this tool because I'm too lazy to use [Polygon](https://polygon.codeforces.com/) as it requires a lot of care on preparation. The `lite-grader` is intended to be used with [lite-gen](https://github.com/plumsirawit/lite-gen), though not necessary.

Enjoy! Bug reports and feature requests are welcomed (in issues).
