FROM ubuntu:latest
LABEL authors="samreen"

# Install Python and Pip (The engine and the wrench)
RUN apt-get update && apt-get install -y python3 python3-pip

# Set the work area
WORKDIR /app

# The "Safety Override" - This is where your previous build likely failed
RUN pip3 install flask --break-system-packages

# Copy your code into the box
COPY app.py .

# Tell the factory how to start
ENV FLASK_APP=app.py
ENTRYPOINT ["python3", "-m", "flask", "run", "--host=0.0.0.0"]