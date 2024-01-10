From amazonlinux:latest 

RUN yum install -y python3.11 python3-pip zip 

workdir /app 

copy . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN zip -r mylambdafunction.zip * 

CMD ["bash"]