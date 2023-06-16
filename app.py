from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world!'

if __name__ == '__main__':
    app.run()

@app.route('/project-zomboid/create-server')
def create_project_zomboid_server():
    subprocess.call(['project-zomboid/create-server.sh'])
    return 'Project Zomboid server creation script executed.'

@app.route('/minecraft/restart-server')
def restart_minecraft_server():
    subprocess.call(['minecraft/restart-server.sh'])
    return 'Minecraft server restart script executed.'

