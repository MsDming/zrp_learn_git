from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def register():  # put application's code here
    return render_template("register.html")


@app.route('/do/reg',methods=['post'])
def do_reg():
    print(request.form)
    return "注册成功"


if __name__ == '__main__':
    app.run()
