import requests

def get_image(num):
    """Get daily horoscope for a zodiac sign.
    Keyword arguments:
    sign:str - Zodiac sign
    day:str - Date in format (YYYY-MM-DD) OR TODAY OR TOMORROW OR YESTERDAY
    Return:dict - JSON data
    """
    url = "https://framex-dev.wadrid.net/api/video/Falcon%20Heavy%20Test%20Flight%20(Hosted%20Webcast)-wbSwFU6tY1c/frame/{num}/"
    return url