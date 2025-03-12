import os

from google.oauth2.credentials import Credentials
import googleapiclient.discovery

from dotenv import load_dotenv
load_dotenv()


credentials = Credentials.from_authorized_user_file(
    "tokens.json"
)

youtube = googleapiclient.discovery.build('youtube', 'v3', credentials=credentials)

def get_live_video_id():
    CHANNEL_ID = os.environ['CHANNEL_ID']

    request = youtube.search().list(
        part="snippet",
        channelId=CHANNEL_ID,
        eventType="live",
        type="video"
    )
    response = request.execute()

    print(response)

    live_video_id = response["items"][0]['id']['videoId']

    return live_video_id


def add_to_watch_next_playlist(live_video_id):
    WATCH_NEXT_PLAYLIST_ID = os.environ['WATCH_NEXT_PLAYLIST_ID']

    request = youtube.playlistItems().insert(
        part="snippet",
        body={
            "snippet": {
                "playlistId": WATCH_NEXT_PLAYLIST_ID,
                "position": 0,
                "resourceId": {
                "kind": "youtube#video",
                "videoId": live_video_id
                }   
            }   
        }
    )

    response = request.execute()
    print(response)
    return response


if __name__ == '__main__':
    live_video_id = get_live_video_id()
    add_to_watch_next_playlist(live_video_id)

