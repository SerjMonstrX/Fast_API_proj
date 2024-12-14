from fastapi import FastAPI

app = FastAPI()


@app.get("/hotels/")
def get_hotels(
        location,
        date_from,
        date_to,
        stars,
        has_spa,
):
    return date_from, date_to

# import requests
#
# r = requests.get("http://127.0.0.1:8000/hotels/1",
#                  params={"date_from": "today", "date_to":"now"})
