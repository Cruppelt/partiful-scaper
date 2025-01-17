# /// script
# dependencies = [
#   "pydash",
#   "requests",
# ]
# ///


import argparse
import os

import requests
from pydash import get


def fetch_and_save_images(user_id: str, event_id: str, output_folder: str):
    os.makedirs(output_folder, exist_ok=True)

    response = requests.post(
        "https://api.partiful.com/getGuests",
        json={
            "data": {
                "params": {"eventId": event_id, "includeInvitedGuests": True},
                "paging": {"cursor": None, "maxResults": 500},
                "userId": user_id,
            }
        },
    )

    results = get(response.json(), "result.data", [])

    for idx, result in enumerate(results):
        url = get(result, "user.photo.url")
        if url:
            img_response = requests.get(url)
            if img_response.status_code == 200:
                file_path = os.path.join(output_folder, f"image_{idx}.jpg")
                with open(file_path, "wb") as file:
                    file.write(img_response.content)

    print(f"Images saved to {output_folder}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch and save images from Partiful event attendees.")
    parser.add_argument("userid", type=str, help="User ID for authentication.")
    parser.add_argument("eventid", type=str, help="Event ID to fetch guest list.")
    parser.add_argument("output_folder", type=str, nargs="?", default="partiful", help="Folder to save images (default: partiful).")

    args = parser.parse_args()
    fetch_and_save_images(args.userid, args.eventid, args.output_folder)
