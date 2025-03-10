from flask import Flask, render_template, url_for, request
from scrape import get_book_cover_image
from prompt import query_graph, convert, schemas
import json
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    
    result = None
    if request.method == "POST":
        status = False
        user_input = request.form.get("search_query")  # Get input from form
        user_input += f'contain in description, or title, or genre in graph dataset G with schema {schemas}'
        result = query_graph(user_input)  # Pass to function x
        
        if result:
            structure_books = convert(result)
            print(structure_books)
            filtered_structure_books = structure_books.replace('```json\n', '').replace('\n```', '')
            books = json.loads(filtered_structure_books)
            print(f"Books: {books}")
            books = books[:5]
            for book in books:
                book['cover'] = get_book_cover_image(book['url'])
            status = True
        return render_template("index.html", books=books,status=status)  # Render result
        
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
