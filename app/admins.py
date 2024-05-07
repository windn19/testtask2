from flask import redirect, url_for
from flask_admin import Admin, AdminIndexView, BaseView, expose
from flask_admin.contrib.peewee import ModelView

from . import app
from .models import User, UserType, Order


class IndexView(BaseView):
    @expose('/')
    def back_index(self):
        return redirect(url_for('index'))


class AdminIndex(AdminIndexView):
    @expose('/')
    def admin_index(self):
        users1 = User.select()
        orders1 = Order.select()
        return self.render('admin/admin_index.html', users=users1, orders=orders1)


admin = Admin(app, name='Новое-пиви', template_mode='bootstrap4', index_view=AdminIndex())
admin.add_view(ModelView(User, name='Пользователь'))
admin.add_view(ModelView(UserType, name='Тип пользователя'))
admin.add_view(ModelView(Order, name='Заказы'))
admin.add_view(IndexView(name='Сайт'))
