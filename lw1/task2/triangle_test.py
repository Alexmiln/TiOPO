import unittest
import subprocess


PROGRAM_PATH = '../task1/triangle.py'
RESULTS_PATH = 'Results/result.txt'
TESTS_PATH = 'Tests/tests.txt'


def run_process(process: str, args: str) -> str:
    output = subprocess.check_output(["py", process] + args.split())
    return output.decode("utf-8")

class MyTestCase(unittest.TestCase):

    def test(self):
        with open(RESULTS_PATH, encoding='utf-8', mode='w') as result:
            with open(TESTS_PATH, encoding='utf-8', mode='r') as file:
                lines = file.readlines()
                i = 0
                while i < len(lines):
                    test_line = lines[i].split(' || ')
                    input_case = test_line[0]
                    expect_result = test_line[1].rstrip('\r\n')
                    i += 1
                    output = run_process(PROGRAM_PATH, input_case).rstrip('\r\n')
                    print(f"{i}. Testing case: {input_case}")
                    if expect_result == output:
                        result.write('success\n')
                    else:
                        result.write('error\n')


if __name__ == '__main__':
    unittest.main()
    