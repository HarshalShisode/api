# YouTube Comments Search API

The YouTube Comments Search API is a RESTful web service that allows you to search for comments on YouTube videos based on various criteria. This API serves as a wrapper for the YouTube comment data, allowing you to filter comments by author name, date range, like and reply counts, and search text within comments.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Search Parameters](#search-parameters)
  - [Example Requests](#example-requests)
- [Response Format](#response-format)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- [Python](https://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/en/2.1.x/installation/) (Installed via pip)
- [Requests](https://docs.python-requests.org/en/latest/user/install/#install) (Installed via pip)

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/youtube-comments-search-api.git
   ```

2. Navigate to the project directory:

   ```bash
   cd youtube-comments-search-api
   ```

3. Install the required Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask application:

   ```bash
   python app.py
   ```

   The API should now be running at `http://localhost:5000`.

## Usage

### Search Parameters

You can search for comments using the following query parameters:

- `search_author`: Search by author name.
- `at_from` and `at_to`: Search by date range (format: "YYYY-MM-DD").
- `like_from` and `like_to`: Search by like count range.
- `reply_from` and `reply_to`: Search by reply count range.
- `search_text`: Search for comments containing specific text.

### Example Requests

#### Search for comments by author name and date range:

```http
GET http://localhost:5000/search?search_author=John&at_from=2023-01-01&at_to=2023-02-01
```

#### Search for comments with specific text:

```http
GET http://localhost:5000/search?search_text=economic
```

#### Combined search with multiple criteria:

```http
GET http://localhost:5000/search?search_author=John&at_from=2023-01-01&at_to=2023-02-01&like_from=5&like_to=10&reply_from=2&reply_to=5&search_text=economic
```

## Response Format

The API returns a JSON response in the following format:

```json
[
  {
    "at": "Wed, 25 Jan 2023 23:59:38 GMT",
    "author": "John Doe",
    "like": 7,
    "reply": 3,
    "text": "This is a great video about economics."
  },
  {
    "at": "Thu, 26 Jan 2023 12:30:15 GMT",
    "author": "Alice Smith",
    "like": 12,
    "reply": 2,
    "text": "I found this video very informative."
  }
  // ... (other comments)
]
```

## Error Handling

If an error occurs, the API will return an error response in the following format:

```json
{
  "error": "Description of the error."
}
```

## Contributing

If you would like to contribute to this project, please open an issue or create a pull request. We welcome contributions and feedback.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to customize this README.md to provide more specific information about your project and any additional features or usage guidelines.
