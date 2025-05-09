from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    subprocess.call(["/home/ec2-user/sync_repo.sh"])
    return "Pulled", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
