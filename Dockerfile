FROM public.ecr.aws/lambda/python:3.7
RUN mkdir -p /app
ADD . /app/
WORKDIR /app
RUN pip install --upgrade pip &&\
    pip install --trusted-host pypi.python.org -r requirements.txt &&\
    python download_model.py
EXPOSE 8080
CMD ["main.py"]
ENTRYPOINT ["python"]
