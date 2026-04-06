import logging
logger = logging.getLogger(__name__)

def transform_data(data):
    rows = []
    try:
        for feature in data['features']:
            properties = feature['properties']
            row = {
            'id': feature.get('id', None),
            'title': properties.get('title', None),
            'type': properties.get('type', None),
            'place': properties.get('place', None),
            }
            rows.append(row)

            if len(rows) == 100:
                yield rows
                rows = []
        if rows:
            yield rows
    except (KeyError, TypeError) as e:
        logger.error(f"Transform failed: {e}")