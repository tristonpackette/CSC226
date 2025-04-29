from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

form_html = """
<!DOCTYPE html>
<html>
  <body>
    <h2>Submit a Message</h2>
    <form method="POST" action="/submit">
      Email: <input type="email" name="email" required><br><br>
      Message: <input type="text" name="message"><br><br>
      <input type="submit" value="Submit">
    </form>
    <p>See all messages at <a href="/messages">/messages</a></p>
  </body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    return render_template_string(form_html)

@app.route("/submit", methods=["POST"])
def submit():
    # TODO: Get form data from request.form
    email = request.form["email"]
    message = request.form["message"]

    # TODO: Save it to a file (append mode - make sure you are appending to the file, not overwriting the whole thing)
    with open("messages.txt", "a") as f:
        f.write(f"{email}: {message}\n")

    return redirect("/messages")

@app.route("/messages", methods=["GET"])
def messages():
 # TODO: Read file content and return as plain text or HTML
    try:
        with open("messages.txt", "r") as f:
            content = f.read()
    except FileNotFoundError:
        content = "No messages yet."

    return f"<h2>All Submitted Messages:</h2><pre>{content}</pre>"

if __name__ == "__main__":
    app.run(debug=True)
