import face_recognition
import cv2

# Initialize lists to store known faces and their names
known_face_encodings = []
known_face_names = []

# Add known faces and their names
def add_known_face(image_path, name):
    known_face_image = face_recognition.load_image_file(image_path)
    face_encodings = face_recognition.face_encodings(known_face_image)
    if len(face_encodings) > 0:
        known_face_encodings.append(face_encodings[0])
        known_face_names.append(name)
    else:
        print(f"Failed to detect a face in the image: {image_path}")

# Add known faces with error handling
add_known_face("WIN_20231102_21_49_53_Pro.jpg", "hello rishi")
#add_known_face("known_face2.jpg", "Known Person 2")
#add_known_face("known_face3.jpg", "Known Person 3")

# Open the video capture device (0 is usually the default camera)
video_capture = cv2.VideoCapture(0)

while True:
    # Capture a single frame
    ret, frame = video_capture.read()

    # Find all the faces and face encodings in the current frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    face_names = []
    for face_encoding in face_encodings:
        # Check if the face matches any known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        face_names.append(name)

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Draw a rectangle around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Label the face
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Exit the program if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture device and close OpenCV windows
video_capture.release()
cv2.destroyAllWindows()
