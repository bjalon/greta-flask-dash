from db.extensions import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(200))
    is_active = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    @classmethod
    def get_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        """
        {
            "id"="%s",
            "username"="%s",
            "email"="%s",
            "password"="%s",
            "is_active"="%s",
            "created_at"="%s",
            "updated_at"="%s",
        }
        """.format(
            self.id,
            self.username,
            self.email,
            self.password,
            self.is_active,
            self.created_at,
            self.updated_at,
        )
