# https://readwise.io/api_deets

# If you want to check that a token is valid, just make a GET request to 
    # https://readwise.io/api/v2/auth/ with the above header. You should receive a 204 response. 
# Rate Limiting : The default base rate is 240 requests per minute but the Highlight LIST and Book LIST endpoints are restricted to 20 per minute. You can check Retry-After header in the 429 response to get the amount of seconds to wait for.

from secrets import secret_key
import requests

# requests.post(
#     url="https://readwise.io/api/v2/highlights/",
#     headers={"Authorization": f"Token {secret_key}"},
#     json={
#         "highlights": [{
#             "text": "Call me Ishmael",
#             "title": "Moby Dick",
#             "author": "Herman Melville",
#             "source_type": "book",
#             "location_type": "page",
#             "location": 3,
#             "highlighted_at": "2020-07-14T20:11:24+00:00",
#         }]
#     }
# )

message = requests.get(
    url='https://readwise.io/api/v2/auth/',
    headers={
        'Authorization': f'Token {secret_key}',
    },
    # json={    },
)

print(message)