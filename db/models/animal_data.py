from db.extensions import db


class AnimalData(db.Model):
    __tablename__ = 'animal'
    id = db.Column(db.Integer, primary_key=True)
    animal = db.Column(db.String(80), nullable=False, unique=True)
    file = db.Column(db.String(200), nullable=False, unique=True)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return 'AnimalData{"id"="' + str(self.id) + '", "animal"="' + self.animal + '", "file"="' + self.file + '"}'
