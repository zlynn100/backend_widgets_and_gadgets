FROM python:3.9.1-alpine3.13

WORKDIR /widgets_and_gadgets_site

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv ${VIRTUAL_ENV}
ENV PATH="${VIRTUAL_ENV}/bin:$PATH"

COPY . ./
RUN pip install -r requirements.txt
RUN pip install -e .

CMD ["python", "main.py"]