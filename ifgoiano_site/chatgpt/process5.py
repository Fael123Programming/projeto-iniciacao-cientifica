import os, pandas
from classify2 import SOURCE_PATH, TARGET_PATH



if __name__ == '__main__':
    files = os.listdir(TARGET_PATH)
    for f in files[:len(files) - 1]:
        df = pandas.read_csv(os.path.join(TARGET_PATH, f))