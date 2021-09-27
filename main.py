from discord_webhook import DiscordWebhook, DiscordEmbed
import datetime, time
import cv2
import os
from pathlib import Path
import json
# pip install opencv-contrib-python==3.4.8.29 ignore this
print("Welcome to Cat Detection 2000")
with open("config.json") as config_file:
    data = json.load(config_file)
webhookurl = data["discordwebhook"]
webhook = DiscordWebhook(url=webhookurl, username="Cat Detection 2000")
face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')

# capture from a camera, 0 = default cam, can change if you have more, eg 1, 2
cap = cv2.VideoCapture(0)

# loop runs if capturing has been initialized.
while 1:

    # reads frames from a camera
    ret, img = cap.read()

    # convert to gray scale of each frames
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detects faces of different sizes in the input image
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        # To draw a rectangle in a face
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        img_name = "latestcat.png"
        testifexist = Path(f"{img_name}")
        if testifexist.is_file():
            os.rename(f"{img_name}", f"pics/cat-{time.time()}.png")
        cv2.imwrite(img_name, img)
        print("{} saved!".format(img_name))
        with open(f"{img_name}", "rb") as f:
            webhook.add_file(file=f.read(), filename=f"catpic.png")
        embed = DiscordEmbed(title="Cat Detected", description=f"At: `{datetime.datetime.utcnow()}`", color='03b2f8')
        embed.set_image(url='attachment://catpic.png')
        webhook.add_embed(embed)
        response = webhook.execute()
        print("Sent to discord!")
        with open(__file__) as fo: # restart script to prevent duped picture sending
            source_code = fo.read()
            byte_code = compile(source_code, __file__, "exec")
            exec(byte_code)
            cv2.destroyAllWindows()
            quit()
    # Display an image in a window
    cv2.imshow("Cat Detection 2000 - ESC to quit", img)
    # Wait for Esc key to stop
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        print("Quitting...")
        break

# Shutdown camera
cap.release()
# Close correctly
cv2.destroyAllWindows()