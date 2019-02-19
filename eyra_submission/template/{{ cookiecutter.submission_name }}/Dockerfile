FROM {{ cookiecutter.docker_base_image }}

RUN mkdir -p /opt/algorithm /input /output

WORKDIR /opt/algorithm

COPY requirements.txt /opt/algorithm/
RUN python -m pip install -r requirements.txt

COPY algorithm_src/* /opt/algorithm/

ENTRYPOINT "python" "-m" "algorithm"
