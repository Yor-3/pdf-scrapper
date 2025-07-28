# Adobe Hackathon 2025 - Round 1A Submission

This project extracts a structured outline (Title, H1, H2, H3) from PDF documents.

## Project Structure

-   `main.py`: The main Python script for processing PDFs.
-   `Dockerfile`: Defines the container environment for the application.
-   `requirements.txt`: Lists the necessary Python dependencies.
-   `/input`: Directory for input PDF files (mounted via Docker).
-   `/output`: Directory for the resulting JSON files (mounted via Docker).

## My Approach

The solution uses a rule-based method to identify document structure based on text properties.

1.  **PDF Parsing**: The script iterates through each PDF in the `/app/input` directory. It uses the `PyMuPDF` (fitz) library to parse each page and extract text blocks along with their metadata (text content, font size, page number).
2.  **Title Extraction**: It assumes the text with the largest font size in the entire document is the **Title**.
3.  **Heading Detection**: Headings (H1, H2, H3) are identified based on font size thresholds:
    * **H1**: Font size >= 18
    * **H2**: Font size >= 14
    * **H3**: Font size >= 12
4.  [cite_start]**JSON Output**: The extracted title and outline are formatted into a JSON structure as specified in the challenge requirements [cite: 46] and saved to the `/app/output` directory.

[cite_start]This approach is lightweight, fast, and works offline without requiring large models, meeting all performance constraints[cite: 1, 82].

## Libraries Used

-   **PyMuPDF**: For robust and efficient PDF text and metadata extraction.

## How to Build and Run

The solution is designed to be run inside a Docker container.

1.  **Build the Docker image:**
    The image will be built using the following command:
    ```bash
    docker build --platform linux/amd64 -t mysolutionname:somerandomidentifier .
    ```

2.  **Run the container:**
    After building, the solution is executed with this command, which maps local `input` and `output` folders to the container:
    ```bash
    docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none mysolutionname:somerandomidentifier
    ```
    The container will automatically process all PDFs found in `/app/input` and place the corresponding JSON files in `/app/output`[cite: 72].

1. python -m venv venv-name

2. source venv-name/bin/activate

3. pip install -r "requirements.txt"

4. 
docker build -t pdf-outline-extractor:submission1 .
rememeber to change name everytime u create a new one

5. 
docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  --network none \
  pdf-outline-extractor:submission1
