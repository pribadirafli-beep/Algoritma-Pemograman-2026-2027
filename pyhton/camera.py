import cv2
import mediapipe as mp

# Mengaktifkan kamera laptop
kamera = cv2.VideoCapture(0)

# Menyiapkan sistem deteksi tangan
mp_tangan = mp.solutions.hands
mp_gambar = mp.solutions.drawing_utils

deteksi_tangan = mp_tangan.Hands(
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

print("Sistem deteksi tangan dimulai!")
print("Tekan tombol Q untuk keluar.")

while kamera.isOpened():
    berhasil, gambar = kamera.read()

    if not berhasil:
        print("Kamera tidak dapat dibuka!")
        break

    # Membalik gambar agar seperti bercermin
    gambar = cv2.flip(gambar, 1)

    # Mengubah format warna untuk MediaPipe
    gambar_rgb = cv2.cvtColor(
        gambar, cv2.COLOR_BGR2RGB
    )

    # Mendeteksi tangan
    hasil = deteksi_tangan.process(gambar_rgb)

    # Menggambar titik dan garis pada tangan
    if hasil.multi_hand_landmarks:
        for tangan in hasil.multi_hand_landmarks:
            mp_gambar.draw_landmarks(
                gambar,
                tangan,
                mp_tangan.HAND_CONNECTIONS
            )

        teks = "Tangan terdeteksi"
    else:
        teks = "Tangan tidak terdeteksi"

    # Menampilkan status pada layar
    cv2.putText(
        gambar,
        teks,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    # Menampilkan kamera
    cv2.imshow("Deteksi Gerakan Tangan", gambar)

    # Keluar jika tombol Q ditekan
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Menutup kamera dan jendela program
kamera.release()
deteksi_tangan.close()
cv2.destroyAllWindows()

print("Program selesai.")