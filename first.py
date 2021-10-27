from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def root():
    return 'Hello World!'
    
@app.route('/mypage/<myname>')
def mypage(myname):
    return f'<h1>this is {myname} page</h1>'
    
@app.route('/pageone')
def mytemplate():
    student_list = [{'id': 1, 'name': 'saif', 'semester': 5},
                {'id': 2, 'name': 'anil', 'semester': 3}]
    return render_template('page1.html', students=student_list)
    
@app.route('/pagetwo')
def page2():
    return render_template('page2.html', title='page2')
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5555)