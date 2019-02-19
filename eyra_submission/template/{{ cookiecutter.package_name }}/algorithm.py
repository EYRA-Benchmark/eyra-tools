import numpy as np


class {{ cookiecutter.package_name|capitalize }}(object):
    def run():
        with open("/input/data.txt", "r") as fpin, open("/output/data.txt", "w") as fpout:
            for l in fpin.readlines():
                try:
                    x, y = [float(i) for i in l.strip().split()]
                except ValueError:
                    continue
                fpout.write(f"{x} {y**2} {x*np.pi}\n")


if __name__ == "__main__":
    {{ cookiecutter.package_name|capitalize }}.run()
