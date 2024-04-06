FROM python:3.8
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV FLASK_APP="src/app.py"
CMD ["sh", "-c", "if [ \"$RUN_TESTS\" = \"true\" ] ; then pytest tests/; fi; flask run --host=0.0.0.0"]