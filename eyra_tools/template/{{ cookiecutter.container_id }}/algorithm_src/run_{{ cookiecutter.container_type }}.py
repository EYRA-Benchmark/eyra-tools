from algorithm import my_algorithm

class {{cookiecutter.container_type.capitalize()}}(object):
    def run(self):
        """This is boilerplate. Delete the contents of this method and put your
        own algorithm code here. Please do not change the class name
        ({{ cookiecutter.container_type.capitalize() }}) or the method name (run).
        """
        my_algorithm("/input/example_input_data.txt",
                     "/output/example_output_data.txt")


# Please do not change anything below
if __name__ == "__main__":
    {{cookiecutter.container_type.capitalize()}}().run()
