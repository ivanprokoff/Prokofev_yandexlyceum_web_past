from flask import Flask, url_for, request, render_template
from PIL import Image
import io

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def first():
    return render_template('main.html', title='Главная')


@app.route('/index')
def second():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    prom = ['<b>Человечество вырастает из детства.', 'Человечеству мала одна планета.',
            'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!',
            'Присоединяйся!</b>']
    return '</br>'.join(prom)


@app.route('/image_mars')
def image_mars():
    return f'''
                <!doctype html>
                    <html lang="en">
                        <head>
                            <meta charset="utf-8">
                            <title>Привет, Марс!</title>
                        </head>
                    <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/mars_img.png')}" 
                        alt="здесь должна была быть картинка, но не нашлась">
                        <p>Вот она какая, красная планета.</p>
                  </body>
                </html>
'''


@app.route('/promotion_image')
def promotion_image_mars():
    return f'''
                <!doctype html>
                    <html lang="en">
                        <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet" 
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="
                            {url_for('static', filename='css/style.css')}"/>
                            <title>Привет, Марс!</title>
                        </head>
                    <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/mars_img.png')}" 
               alt="здесь должна была быть картинка, но не нашлась">
                        <div class="alert alert-dark" role="alert">
                            <b>Человечество вырастает из детства.
                        </div>
                        <div class="alert alert-success" role="alert">
                            <b>Человечеству мала одна планета.
                        </div>
                        <div class="alert alert-dark" role="alert">
                            <b>Мы сделаем обитаемыми безжизненные пока планеты.
                        </div>
                        <div class="alert alert-warning" role="alert">
                            <b>И начнем с Марса!
                        </div>
                        <div class="alert alert-danger" role="alert">
                            <b>Присоединяйся!
                        </div>
                  </body>
                </html>
'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/form.css')}" />
                                <title>Отбор астронавтов</title>
                              </head>
                              <body>
                                <h1>Анкета претендента</h1>
                                <h2>На участие в миссии</h2>
                                <div>
                                    <form class="login_form" method="post">
                                        <input type="surname" class="form-control" id="surname" aria-describedby="emailHelp" placeholder="Введите фамилию" name="surname">
                                        <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
                                        </br>
                                        <input type="mail" class="form-control" id="mail" placeholder="Введите адрес почты" name="mail">
                                        <div class="form-group">
                                            <label for="classSelect">Какое у вас образование?</label>
                                            <select class="form-control" id="classSelect" name="class">
                                              <option>Начальное</option>
                                              <option>Основное общее</option>
                                              <option>Среднее общее</option>
                                              <option>Среднее профессиональное</option>
                                              <option>Высшее</option>
                                            </select>
                                         </div>
                                        </br>
                                        <div class="form-group">
                                            <label for="form-check">Кто вы по профессии?</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="profession" id="explorer" value="explorer">
                                              <label class="form-check-label" for="explorer">
                                                Инженер-исследователь
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="profession" id="pilot" value="pilot">
                                              <label class="form-check-label" for="pilot">
                                                Пилот
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="profession" id="builder" value="builder">
                                              <label class="form-check-label" for="builder">
                                                Строитель
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="profession" id="biolog" value="biolog">
                                              <label class="form-check-label" for="biolog">
                                                Экзобиолог
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="profession" id="doctor" value="doctor">
                                              <label class="form-check-label" for="doctor">
                                                Врач
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="profession" id="radio_protector" value="radio_protector">
                                              <label class="form-check-label" for="radio_protector">
                                                Инженер по радиальной защите
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="profession" id="operator" value="operator">
                                              <label class="form-check-label" for="operator">
                                                Оператор марсохода
                                              </label>
                                            </div>
                                        </div>
                                        </br>
                                        <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                            <div class="form-check">
                                                <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                                <label class="form-check-label" for="male">
                                                    Мужской
                                                </label>
                                            </div>
                                            <div class="form-check">
                                                <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                                <label class="form-check-label" for="female">
                                                    Женский
                                                </label>
                                            </div>
                                        </div>
                                        </br>
                                        <div class="form-group">
                                            <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                            <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                        </div>
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>
                                        </br>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                            <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                        </div>
                                        </br>
                                        <button type="submit" class="btn btn-primary">Записаться</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return render_template('choices.html', name=planet_name, title='Варианты выбора')


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return render_template('results.html', title='Результаты', nickname=nickname,
                           level=level, rating=rating)


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'GET':
        return render_template('load_photo.html', title='Ваше фото')
    elif request.method == 'POST':
        raw = request.files['file']
        f = raw.read()
        file = open('static/img/im.jpeg', 'wb')
        file.write(f)
        file.close()
        return render_template('loaded_photo.html', title='Ваше фото', photo='img/im.jpeg')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
