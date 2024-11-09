FROM public.ecr.aws/lambda/python:3.12.2024.11.08.16

# COPY lamlib-0.1.0-py3-none-any.whl ${LAMBDA_TASK_ROOT}

RUN pip install "git+https://github.com/jonatronblah/lamlib.git@master"

COPY lambda_function.py ${LAMBDA_TASK_ROOT}

CMD [ "lambda_function.handler" ]

