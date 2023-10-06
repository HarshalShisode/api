from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search_comments():
    # Parse query parameters
    search_author = request.args.get('search_author')
    at_from = request.args.get('at_from')
    at_to = request.args.get('at_to')
    like_from = request.args.get('like_from')
    like_to = request.args.get('like_to')
    reply_from = request.args.get('reply_from')
    reply_to = request.args.get('reply_to')
    search_text = request.args.get('search_text')

    # Construct and send request to the external API
    base_url = "https://app.ylytic.com/ylytic/test"
    query_params = {
        'search_author': search_author,
        'at_from': at_from,
        'at_to': at_to,
        'like_from': like_from,
        'like_to': like_to,
        'reply_from': reply_from,
        'reply_to': reply_to,
        'search_text': search_text,
    }

    response = requests.get(base_url, params=query_params)

    # Check if the request to the external API was successful
    if response.status_code == 200:
        # Process the JSON response
        comments = response.json().get("comments", [])
        
        # Filter comments based on search criteria
        filtered_comments = filter_comments(comments, search_author, at_from, at_to, like_from, like_to, reply_from, reply_to, search_text)

        # Return the filtered comments as JSON
        return jsonify(filtered_comments)
    else:
        # Handle the case where the external API returns an error
        return jsonify({"error": "External API error"}), response.status_code

def filter_comments(comments, search_author, at_from, at_to, like_from, like_to, reply_from, reply_to, search_text):
    filtered_comments = []
    for comment in comments:
        # Apply filtering conditions based on search criteria
        if (not search_author or search_author.lower() in comment["author"].lower()) \
           and (not at_from or comment["at"] >= at_from) \
           and (not at_to or comment["at"] <= at_to) \
           and (not like_from or comment["like"] >= like_from) \
           and (not like_to or comment["like"] <= like_to) \
           and (not reply_from or comment["reply"] >= reply_from) \
           and (not reply_to or comment["reply"] <= reply_to) \
           and (not search_text or search_text.lower() in comment["text"].lower()):
            filtered_comments.append(comment)
    
    return filtered_comments

if __name__ == "__main__":
    app.run()
