from googleapiclient.discovery import build
import APIKey

API_KEY = APIKey.youtube_apikey()
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
CHANNEL_ID = 'CHANNEL_ID'
channels = []
channel_dict = {}

print("YouTubeDataを起動しました")


def data_dict(name, subs):
    data = {}
    for s in range(len(name)):
        data[name[s]] = int(subs[s])

    return data


def youtube_channel_detail(channel_id, api_key):
    api_service_name = 'youtube'
    api_version = 'v3'
    youtube = build(api_service_name, api_version, developerKey=api_key)
    search_response = youtube.channels().list(
        part='snippet,statistics',
        id=channel_id,
    ).execute()

    return search_response['items']


def main(IDs, IDlist):
    for h in IDlist:
        data = youtube_channel_detail(h, API_KEY)
        for j in range(len(data)):
            channel_dict[IDs[data[j]['id']]] = int(data[j]['statistics']['subscriberCount'])

    return channel_dict
