# FastAPI boilerplate

My web API boilerplate code based on FastAPI ready to be deployed to k8s.

## Setup

1. create venv
   ```
   $ python3 -m venv env
   ```
2. activate venv
   ```
   $ source env/bin/activate
   ```
3. install dependencies
   ```
   $ pip install -r requirements.txt
   ```

## Development

1. activate venv
   ```
   $ source env/bin/activate
   ```
2. start uvicorn
   ```
   $ uvicorn app.main:app --reload
   ```

## Deployment

1. build docker image
   ```
   $ sudo docker build -t k8s:32000/fastapi-helloworld:latest .
   ```
2. push docker image
   ```
   $ sudo docker push k8s:32000/fastapi-helloworld
   ```
3. update k8s resources
   ```
   $ kubectl apply -f resources.yaml
   ```
