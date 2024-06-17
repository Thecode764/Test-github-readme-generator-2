# Github readme generator
import requests

# You name. for example my name is artin karimi (a iranian name)
name = "Artin karimi"

# Summary. For example a developer
summary = "A developer"

# Interested. For example web development
interested = "Web development"

# Working. I currently working on project
working_on = "Open source projects"

# Learning. What are you learning? django?
learning = "Django, React and wordpress"

# Email. How to reach me. enter you email
email = "artin962354@proton.me"

# Username. You github username
username = "Thecode764"

# Pronouns. Male or female?
pronouns = "Male"

# Fun fact about you
fun_fact = "I am github readme generator developers"

# What you are know?
know = "html,css,js,vim,vscode,git,c,php,python,go,bash,github,pycharm,flask,django,linux,neovim,bootstrap,tailwind,arch,debian,ubuntu,electron,dart,markdown,mint,figma,sublime,mysql,react,ruby,discord,powershell,wordpress"

# Discord id. You discord id
discord_id = "1125429179685548112"

# Wakatime username: You wakatime username. make sure you wakatime profile is public
wakatime = "Thecode764"

# Generate file
file = "README.md"

print("Generating ...")

url = f"https://api.github.com/users/{username}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    bio = data["bio"]
    public_repos = data["public_repos"]
    followers = data["followers"]
    following = data["following"]

out = f"""
<h1 align="center">{name}</h1>
<h3 align="center">{summary}</h3>

- 👋 Hi, I’m {name}


- 👀 I’m interested in **{interested}**

- ♾ I currently working on **{working_on}**

- 🌱 I’m currently learning **{learning}**

- 📫 How to reach me {email}

- 😄 Pronouns: {pronouns}

- 😎 Fun fact: {fun_fact}

- ℹ️ My Bio: | {bio} |

- 📂 I created {public_repos} public repositories

- 👤 My followers number is {followers}

- 👤 I follow {following} users

<h3 align="center">Tech stack</h3>
<img src="https://skillicons.dev/icons?i={know}">
<h3>Stats</h3>
<img src="https://github-readme-stats.vercel.app/api?username={username}&show_icons=true&theme=dracula">
<h3>Most used languages</h3>
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username={username}&theme=dracula&langs_count=300">
<h3>Others</h3>
<img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2F{username}%2F&count_bg=%23000&title_bg=%23171717&icon=github.svg&icon_color=%23FFFFFF&title=Visits&edge_flat=false">
<img src="https://img.shields.io/github/followers/{username}">
<h3>Discord status</h3>
<!--Join to lanyard server for this-->
<img src="https://lanyard.cnrad.dev/api/{discord_id}">
<h3>Trophy</h3>
<img src="https://github-profile-trophy.vercel.app/?username={username}&theme=dracula">
<img src="https://streak-stats.demolab.com/?user={username}&theme=dracula">
<h3>Activity graph</h3>
<img src="https://github-readme-activity-graph.vercel.app/graph/?username={username}&bg_color=000&color=fff&line=00E676&point=fff&hide_border=true">

<img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username={username}&theme=dark">

<img src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username={username}&theme=dark">

<img src="https://github-readme-stats.vercel.app/api/wakatime?username={username}&theme=dracula">
"""

write = open(file, "w+")

write.write(out)
