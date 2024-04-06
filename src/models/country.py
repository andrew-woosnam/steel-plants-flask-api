from database import db


class Country(db.Model):
    __tablename__ = 'iron_steel_production'
    name = db.Column('country', db.String(255), unique=True,
                     nullable=False, primary_key=True)
    total_plants = db.Column(db.Integer)
    electric = db.Column(db.Integer)
    electric_oxygen = db.Column(db.Integer)
    oxygen = db.Column(db.Integer)
    ironmaking_bf = db.Column(db.Integer)
    ironmaking_dri = db.Column(db.Integer)
    ironmaking_unknown = db.Column(db.Integer)
    integrated_bf = db.Column(db.Integer)
    integrated_bf_and_dri = db.Column(db.Integer)
    integrated_dri = db.Column(db.Integer)
    integrated_unknown = db.Column(db.Integer)
    unknown = db.Column(db.Integer)
    steelmaking_only = db.Column(db.Integer)
    ironmaking_only = db.Column(db.Integer)
    integrated_total = db.Column(db.Integer)
    other_total = db.Column(db.Integer)

    def to_dict(self):
        return {
            'name': self.name,
            'total_plants': self.total_plants,
            'electric': self.electric,
            'electric_oxygen': self.electric_oxygen,
            'oxygen': self.oxygen,
            'ironmaking_bf': self.ironmaking_bf,
            'ironmaking_dri': self.ironmaking_dri,
            'ironmaking_unknown': self.ironmaking_unknown,
            'integrated_bf': self.integrated_bf,
            'integrated_bf_and_dri': self.integrated_bf_and_dri,
            'integrated_dri': self.integrated_dri,
            'integrated_unknown': self.integrated_unknown,
            'unknown': self.unknown,
            'steelmaking_only': self.steelmaking_only,
            'ironmaking_only': self.ironmaking_only,
            'integrated_total': self.integrated_total,
            'other_total': self.other_total,
        }
