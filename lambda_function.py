import logging
import pandas

# Fälle pro Landkreis (Anzahl, Inzidenz, 7-Tagesinzidenz, Todesfälle)
# https://www.apps.nlga.niedersachsen.de/corona/download.php?csv-file
# Fälle pro Geschlecht und Altersgruppe (Fälle, Inzidenz, Fälle 7-Tage, 7-Tages-Inzienz, Todesfälle, Todesfälle Inzidenz)
# https://www.apps.nlga.niedersachsen.de/corona/download.php?csv_alter-file
# Fälle pro Tag (Fälle, Todesfälle)
# https://www.apps.nlga.niedersachsen.de/corona/download.php?csv_tag-file
# Fälle pro Meldewoche und Altersgruppe
# https://www.apps.nlga.niedersachsen.de/corona/download.php?csv_woche_alter-file
# Fälle pro Tag und Landkreis (Anzahl, 7-Tagesinzidenz)
# https://www.apps.nlga.niedersachsen.de/corona/download.php?csv_tag_region-file


def lambda_handler(event, context):
    """
    Accepts an action and a number, performs the specified action on the number,
    and returns the result.
    :param event: The event dict that contains the parameters sent when the function
                  is invoked.
    :param context: The context in which the function is called.
    :return: The result of the specified action.
    """

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    logger.info(f'Event: {event}')

    logger.info(f'Looking for GKZ in event')
    
    gkz = int(event['queryStringParameters']['GKZ'])

    logger.info('Getting data')
    df = pandas.read_csv('https://www.apps.nlga.niedersachsen.de/corona/download.php?csv_tag_region-file',
                         delimiter=";",
                         header=0,
                         dayfirst=True,
                         parse_dates=[0],
                         usecols=['Meldedatum', 'GKZ',
                                  '7-Tagesinzidenz pro 100.000 Einwohner']
                         )

    logger.info(f'Parsing for GKZ: {gkz}')

    df = df.query(f'GKZ == {gkz}').set_index(
        'Meldedatum').drop(['GKZ'], axis=1).sort_index().tail(8)

    df = df.tz_localize('Europe/Berlin')
    return df.to_json(orient='index', date_format='iso')
