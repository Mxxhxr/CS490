import requests

data = {
  "UCID": "mv398",
  "first_name": "Maahir",
  "last_name": "Vohra",
  "github_username": "Mxxhxr",
  "discord_username": "mxxhxr",
  "favorite_cartoon": "Cyberchase",
  "favorite_language": "TypeScript",
  "movie_or_game_or_book": "Interstellar",
}

# requests automatically converts data to a JSON & Sets the HTTP header to application/json
r = requests.post('https://student-info-api.netlify.app/.netlify/functions/submit_student_info', json=data)

print("Status Code: ", r.status_code)
print("Response: ", r.text)
