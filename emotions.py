NEUTRAL_FACE = "emotion:neutral"
HAPPY_FACE = "emotion:happy"
UNHAPPY_FACE = "emotion:unhappy"
ANGRY_FACE = "emotion:angry"
SURPRISED_FACE = "emotion:surprised"
FINGER = "emotion:finger"

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
