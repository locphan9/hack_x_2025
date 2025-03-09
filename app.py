from flask import Flask, render_template, url_for, request
from scrape import get_book_cover_image
from prompt import query_graph, convert
import json
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        user_input = request.form.get("search_query")  # Get input from form
        result = query_graph(user_input)  # Pass to function x
        print(result)
        if result:
        
            structure_books = convert(result)
            books = json.loads(structure_books.replace('```json\n', '').replace('\n```', ''))
            books = books[:5]
            for book in books:
                book['cover'] = get_book_cover_image(book['url'])
    
            return render_template("index.html", books=books)  # Render result
        else:
            print(1)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)