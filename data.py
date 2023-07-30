from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

# DataFrame to store library data
library_df = pd.DataFrame(columns=["Date of Issue", "Name of Book", "Name of Issuer", "Date on which Due", "Date of Return"])

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/library', methods=['GET', 'POST'])
def library():
    if request.method == 'POST':
        date_of_issue = request.form['date_of_issue']
        book_name = request.form['book_name']
        issuer_name = request.form['issuer_name']
        date_due = request.form['date_due']
        date_of_return = request.form['date_of_return']

        global library_df
        library_df = library_df.append({
            "Date of Issue": date_of_issue,
            "Name of Book": book_name,
            "Name of Issuer": issuer_name,
            "Date on which Due": date_due,
            "Date of Return": date_of_return
        }, ignore_index=True)

    return render_template('library.html', library_data=library_df.to_dict('records'))

if __name__ == '__main__':
    app.run(debug=True)
