import yt_dlp

# Function to choose format based on user input
def download_video_or_audio(choice, video_url):
    if choice == 3:  # MP3 format (audio only)
        ydl_opts = {
            'format': 'bestaudio[ext=mp3]/bestaudio',  # Directly download the best audio in MP3 format
            'outtmpl': '%(title)s.%(ext)s',            # Output filename format
        }
        print("Downloading as MP3...")

    elif choice == 4:  # MP4 format (video)
        ydl_opts = {
            'format': 'best[height<=1080][ext=mp4]',  # Download the best video up to 1080p (MP4)
            'outtmpl': '%(title)s.%(ext)s',          # Output filename format
        }
        print("Downloading as MP4 (up to 1080p)...")

    else:
        print("Invalid choice. Please enter 3 for MP3 or 4 for MP4.")
        return

    # Download the video or audio
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

    print("Download completed!")

# Main function
def main():
    video_url = input("Enter the URL of the video: ")
    
    print("Choose the format to download:")
    print("3: Download MP3 (audio only)")
    print("4: Download MP4 (video up to 1080p)")

    choice = int(input("Enter your choice (3 or 4): "))

    # Download based on user choice
    download_video_or_audio(choice, video_url)

if __name__ == "__main__":
    main()
