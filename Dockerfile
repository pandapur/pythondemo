# only a comment to trigger build
FROM python
MAINTAINER Panda Pur
ADD main.py /home/main.py
CMD ["/home/main.py"]
ENTRYPOINT ["python"]
