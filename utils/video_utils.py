import cv2

def read_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []                                 # Basicamente vou ler o video e transforma-lo numa lista de frames
    while True:
        ret, frame = cap.read()                 # vai lopar enquanto o video estiver a dar
        if not ret:
            break
        frames.append(frame)  
    return frames

def save_video(output_video_frames, output_video_path):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_path, fourcc, 24, (output_video_frames[0].shape[1], output_video_frames[0].shape[0]))
    for frame in output_video_frames:           # Vou gravar o video num tipo de ficheiro de video 
        out.write(frame)
    out.release()