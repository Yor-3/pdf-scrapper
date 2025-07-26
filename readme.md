pip install -r "requirements.txt"

docker build -t pdf-outline-extractor:submission1 .
rememeber to change name everytime u create a new one

docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  --network none \
  pdf-outline-extractor:submission1
