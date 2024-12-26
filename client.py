import requests
from rich.console import Console
from rich.markdown import Markdown


def test_server(html_content):
    """
    Sends a POST request to the server with the given input html content and prints the server's response.

    Args:
        html_content (str): The html content to be sent to the server for prediction.

    Returns: None
    """
    # API endpoint URL for the server
    url = "http://127.0.0.1:8000/predict"

    # Send a POST request with the request payload
    payload = {"html_content": html_content}
    response = requests.post(url, json=payload)

    # Parse the response JSON data
    data = response.json()

    # Display the response in a formatted markdown format
    console = Console()
    markdown = Markdown(data['response'])
    console.print(markdown)


if __name__ == "__main__":
    # Sample input html content for testing. eg. "<html><body><h1>Hello, world!</h1></body></html>"
    html_content = """<div id="myDIV" class="header">
  <h2>My To Do List</h2>
  <input type="text" id="myInput" placeholder="Title...">
  <span onclick="newElement()" class="addBtn">Add</span>
</div>
<ul id="myUL">
  <li>Hit the gym</li>
  <li class="checked">Pay bills</li>
  <li>Meet George</li>
  <li>Buy eggs</li>
  <li>Read a book</li>
  <li>Organize office</li>
</ul>"""
    test_server(html_content)
