from src.models.country import Country


def get_country_details(country_name):
    try:
        country = Country.query.filter_by(name=country_name).first()
        if country:
            country_details = {column.name: getattr(country, column.name)
                               for column in country.__table__.columns if column.name != 'country'}
            return country_details
        else:
            return {'error': 'Country not found'}, 404
    except Exception as e:
        return {'error': str(e)}, 500
