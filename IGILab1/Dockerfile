FROM python:3.11

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBITECODE 1

RUN apt-get update

WORKDIR /home/valentin/Studing/IGI/IGILab1

COPY . .

CMD ["python3", "task1.py","task2.py","task3.py"]