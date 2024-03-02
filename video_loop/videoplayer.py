import keyboard
import tkvlc

def play_video(player, media):
    # You need to call "set_media()" to (re)load a video before playing it

    player.set_media(media)
    player.play()



def main():
    # Create a new VLC instance and media player:
    #
    # This could be done in one line using vlc.MediaPlayer()
    # that will create an instance behind the scene
    # but we will pass some parameters to the instance in future example codes

    instance = tkvlc.Instance()
    player = instance.media_player_new()
    player = tkvlc.MediaPlayer()
    #player.set_nsobject(obj)

    # Create libVLC objects representing the two videos
    video1 = tkvlc.Media("video1.mp4")
    video2 = tkvlc.Media("video2.mp4")

    # Start the player for the first time
    play_video(player, video1)
    current_video = video1

    while True:
        try:
            if keyboard.is_pressed('q'):
                if current_video == video1:
                    play_video(player, video2)
                    current_video = video2
                    print("spacekey")

                # Swap video if needed
                elif current_video == video2:
                    play_video(player, video1)
                current_video = video1
            # Loop video if playback is ended

            elif player.get_state() == vlc.State.Ended:
                play_video(player, current_video)
        except:
           break #break if any other key is Pressed

if __name__ == '__main__':
    main()
