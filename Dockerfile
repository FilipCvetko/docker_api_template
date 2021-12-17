FROM python:3.8

WORKDIR /workdir

COPY ./requirements.txt /workdir/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /workdir/requirements.txt

# Only include data which is absolutely necessary, scripts however are lightweight and not a problem.
ADD ./data /workdir/data
ADD ./src /workdir/src

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "5000"]