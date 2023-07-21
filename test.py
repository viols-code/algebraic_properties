import subprocess
import sys

if __name__ == '__main__':
    # Parameters
    n_list = [50, 100, 150, 200]
    c = 7

    for n in n_list:
        print(n)
        subprocess.call(['python', 'sequential.py', '-n {}'.format(n), '-c {}'.format(c)], stdout=sys.stdout)

        subprocess.call(['python', 'parallelv1.py', '-n {}'.format(n), '-c {}'.format(c)], stdout=sys.stdout)

        subprocess.call(['python', 'parallel.py', '-n {}'.format(n), '-c {}'.format(c)], stdout=sys.stdout)
        print('\n')
