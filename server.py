# Import necessary libraries
import re
import torch
import litserve as ls
from transformers import AutoModelForCausalLM, AutoTokenizer


class ReaderLMAPI(ls.LitAPI):
    """
    ReaderLMAPI is a subclass of ls.LitAPI that provides methods for the HTML to Markdown conversion task.

    Methods:
        - setup(device): Initializes the model and tokenizer with the specified device.
        - decode_request(request): Extracts the HTML content from the incoming request.
        - predict(html_content): Generates a response based on the provided HTML content using the model.
        - encode_response(output): Encodes the generated response into a dictionary format.
    """

    def setup(self, device):
        """
        Sets up the model and tokenizer on the specified device.
        """
        # Load the model and tokenizer
        model_name = "jinaai/reader-lm-1.5b"
        self.model = (
            AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True)
            .eval()
            .to(device)
        )
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_name, trust_remote_code=True
        )

    def decode_request(self, request):
        """
        Decodes the input request to extract the HTML content.
        """
        # Extract the HTML content from the request
        return request["html_content"]

    def predict(self, html_content):
        """
        Generates a response based on the provided HTML content using the model.
        """
        # Prepare the input for the model
        messages = [{"role": "user", "content": html_content}]
        input_text = self.tokenizer.apply_chat_template(messages, tokenize=False)
        inputs = self.tokenizer.encode(input_text, return_tensors="pt").to(self.device)

        # Generate a response from the model
        with torch.no_grad():
            return self.model.generate(
                inputs,
                max_new_tokens=1024,
                temperature=0.7,
                do_sample=True,
                repetition_penalty=1.08,
            )

    def encode_response(self, outputs):
        """
        Encodes the given results into a dictionary format.
        """
        # Return the results in a dictionary format
        pattern = r"<\|im_start\|>assistant(.*?)<\|im_end\|>"
        response = re.findall(pattern, self.tokenizer.decode(outputs[0]), re.DOTALL)
        return {"response": response[0]}


if __name__ == "__main__":
    # Create an instance of the ReaderLMAPI and run the LitServer
    api = ReaderLMAPI()
    server = ls.LitServer(api, track_requests=True)
    server.run(port=8000)
