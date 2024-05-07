from io import BytesIO

from flask import render_template
from PIL import Image
from requests import get

from . import app
from .models import Order, UserType


@app.route('/')
def index():
    orders_all = Order.select()
    return render_template('index.html', orders=orders_all)


def gen_image(id, name):
    param = {'seed': name}
    req = get('https://api.dicebear.com/8.x/adventurer-neutral/png', params=param)
    avatar_file_like = BytesIO(req.content)
    avatar = Image.open(avatar_file_like)
    avatar.save(f'app/static/images/{id}.png', format='PNG')
    return f'{id}.png'


def check_list(seq):
    for item in seq:
        if item.image is None:
            item.image = gen_image(item.id, item.name)
            item.save()


@app.route('/in')
def get_in():
    in_user = [item for item in UserType.select().where(UserType.name == 'Заказчик')][0]
    in1 = in_user.users
    check_list(in1)
    return render_template('in.html', in_list=in1)


@app.route('/out')
def get_out():
    out_user = [item for item in UserType.select().where(UserType.name == 'Исполнитель')][0]
    out1 = out_user.users
    check_list(out1)
    return render_template('out.html', out_list=out1)
