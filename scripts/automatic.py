import subprocess
import sys


if __name__ == '__main__':
    # Parameters
    n_list = [50, 100, 150, 200]
    c = 7

    for n in n_list:
        print(n)
        subprocess.call(['python', 'main.py', '-n', '{}'.format(n), '-c',  '{}'.format(c), '-a', 'sequential'],
                        stdout=sys.stdout)

        subprocess.call(['python', 'main.py', '-n', '{}'.format(n), '-c',  '{}'.format(c), '-a', 'parallel'],
                        stdout=sys.stdout)

        subprocess.call(['python', 'main.py', '-n', '{}'.format(n), '-c',  '{}'.format(c), '-a', 'parallelv1'],
                        stdout=sys.stdout)
        print('\n')
