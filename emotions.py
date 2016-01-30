NEUTRAL_FACE = "neutral"
HAPPY_FACE = "happy"
UNHAPPY_FACE = "unhappy"
ANGRY_FACE = "angry"
SURPRISED_FACE = "surprised"
FINGER = "finger"

def input_to_face(face):
  if face == 'h':
    face_type = HAPPY_FACE
  elif face == 'u':
    face_type = UNHAPPY_FACE
  elif face == 'a':
    face_type = ANGRY_FACE
  elif face == 's':
    face_type = SURPRISED_FACE
  elif face == 'finger':
    face_type = FINGER
  else:
    face_type = NEUTRAL_FACE
  return face_type
