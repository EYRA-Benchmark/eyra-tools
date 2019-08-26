# Add your imports here; numpy is only used as an example
import numpy as np

def my_algorithm(in_file, out_file):
    with open(in_file, "r") as fpin, open(out_file, "w") as fpout:
        for l in fpin.readlines():
            try:
                x, y = [float(i) for i in l.strip().split()]
            except ValueError:
                continue
            fpout.write("{} {} {}\n".format(x, y**2, x*np.pi))


if __name__ == "__main__":
    # Run the algorithm on your local copy of the data by typing:
    # python algorithm_src/algorithm.py
    my_algorithm('data/input/example_input_data.txt',
                 'data/output/example_output_data.txt')
