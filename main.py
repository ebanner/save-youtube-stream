import os

from google.oauth2.credentials import Credentials
import googleapiclient.discovery

from dotenv import load_dotenv
load_dotenv()


credentials = Credentials.from_authorized_user_file(
    "tokens.json"
)

youtube = googleapiclient.discovery.build('youtube', 'v3', credentials=credentials)


if __name__ == '__main__':
    channel_id = os.environ['CHANNEL_ID']
    request = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        eventType="live",
        type="video"
    )
    response = request.execute()

    live_video_id = response["items"][0]['id']['videoId']
    print(live_video_id)

