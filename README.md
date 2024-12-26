# ReaderLM LitServe

[![Open In Studio](https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/app-2/studio-badge.svg)](https://lightning.ai/sitammeur/studios/readerlm-litserve)

[Jina.ai](https://jina.ai/) has introduced [Reader-LM](https://huggingface.co/collections/jinaai/jina-reader-lm-670628bfe0d782685cb53416), specialized small language models inspired by "Jina Reader" designed for converting raw, noisy HTML from the open web into clean markdown. The resulting reader-lm models outperform larger LLMs in this specific task, offering a cost-effective and multilingual solution. This project demonstrates the use of the Reader-LM model for converting HTML content to Markdown content served using LitServe, an easy-to-use, flexible serving engine for AI models built on FastAPI.

## Project Structure

The project is structured as follows:

- `server.py`: The file containing the main code for the web server.
- `client.py`: The file containing the code for client-side requests.
- `LICENSE`: The license file for the project.
- `README.md`: The README file that contains information about the project.
- `assets`: The folder containing screenshots for working on the application.
- `.gitignore`: The file containing the list of files and directories to be ignored by Git.

## Tech Stack

- Python (for the programming language)
- PyTorch (for the deep learning framework)
- Hugging Face Transformers Library (for the model)
- LitServe (for the serving engine)

## Getting Started

To get started with this project, follow the steps below:

1. Run the server: `python server.py`
2. Upon running the server successfully, you will see uvicorn running on port 8000.
3. Open a new terminal window.
4. Run the client: `python client.py`

Now, you can see the output of the model based on the HTML content. The model will convert the HTML content to Markdown content.

## Usage

The project can be used to serve the Reader-LM model using LitServe. Here, the model is used to convert HTML content to Markdown content. This suggests potential applications in web scraping, content repurposing, and accessibility improvements.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please raise an issue to discuss the changes you want to make. Once the changes are approved, you can create a pull request.

## License

This project is licensed under the [Apache-2.0 License](LICENSE).

## Contact

If you have any questions or suggestions about the project, feel free to contact me on my GitHub profile.

Happy coding! 🚀
