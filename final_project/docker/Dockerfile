FROM python:3.9.2-alpine
WORKDIR /home/app
RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip install Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development
EXPOSE 5000
COPY . .
CMD ["flask", "run"]