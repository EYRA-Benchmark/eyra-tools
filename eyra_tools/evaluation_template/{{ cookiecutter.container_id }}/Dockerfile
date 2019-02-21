FROM {{ cookiecutter.docker_base_image }}

RUN mkdir -p /opt/evaluation /input /output

WORKDIR /opt/evaluation

COPY requirements.txt /opt/evaluation/
RUN python -m pip install -r requirements.txt

ADD evaluation_src /opt/evaluation/

ENTRYPOINT "python" "-m" "evaluation"
