from imutils.video import VideoStream
from pyzbar import pyzbar
import imutils
import cv2

print("Listening for QR codes...")
vs = VideoStream(src=0).start()

while True:
    frame = vs.read()
    frame = imutils.resize(frame, width=400)
    qrcodes = pyzbar.decode(frame)

    for qrcode in qrcodes:
        (x, y, w, h) = qrcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        barcodeData = qrcode.data.decode("utf-8")
        text = "{}".format(barcodeData) # TODO Parse json
        cv2.putText(frame, 'GOT IT', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        print("Processing:", text)
        # TODO Place in data store. composite key: competition, team num, match num (latest read overwrites)

    cv2.imshow("image", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

print("Exiting...")
cv2.destroyAllWindows()
vs.stop()
