# Dockerfile 

# Use an official lightweight Python image 

FROM python:3.12-slim 

 

# Set the working directory inside the container 

WORKDIR /scripts 



COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
# Copy the Python script into the container's working directory 

COPY /scripts/train.py .



# Specify the command to run when the container starts 

CMD ["python", "train.py"]