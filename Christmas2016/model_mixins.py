class AuthorMixin():

    def author(self):
        name = self.user.first_name
        if name == 'Brian':
            name += ' ' + self.user.last_name
        return name

