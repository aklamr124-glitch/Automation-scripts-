import speedtest

st = speedtest.Speedtest()
download_speed = st.download() / 1_000_000  # Mbps
upload_speed = st.upload() / 1_000_000

print(f"⬇️ Download speed: {download_speed:.2f} Mbps")
print(f"⬆️ Upload speed: {upload_speed:.2f} Mbps")
