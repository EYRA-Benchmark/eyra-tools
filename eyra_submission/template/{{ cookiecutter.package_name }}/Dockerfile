FROM {{ cookiecutter.docker_base_image }}

RUN mkdir -p /opt/evaluation /input /output

WORKDIR /opt/evaluation

COPY requirements.txt /opt/evaluation/
RUN python -m pip install -r requirements.txt

COPY evaluation.py /opt/evaluation/

ENTRYPOINT "python" "-m" "evaluation"
