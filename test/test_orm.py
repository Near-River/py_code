#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" create a simple orm frame: """

__author__ = 'Nate River'


class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(64)')


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'int')


class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            print('Found class model')
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaClass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)   # v instance of Field
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

    def __init__(self, **kw):
        super(User,self).__init__(**kw)
        for k, v in kw.items():
            setattr(self, k, v)

    def __str__(self):
        return 'Id: %s Name: %s Email: %s Password: %s' % (self.id, self.name, self.email, self.password)


if __name__ == '__main__':
    u = User(id=101, name='Admin', email='admin@server.com', password='admin')
    u.save()
    # print('model mappings: ', u.__mappings__)
    # print(u)
