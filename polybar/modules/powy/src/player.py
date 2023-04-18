import subprocess


class Spotify:
    def execute_command(self, commands: list[str]) -> list[str]:
        get_output = subprocess.run(commands, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        decode_get_output = get_output.stdout.decode('UTF-8')
        return decode_get_output

    def get_song_metadata(self) -> dict:
        command = ['playerctl', 'metadata', '--player=spotify']
        get_output = self.execute_command(command)
        split_output = get_output.split('\n')
        if split_output[0] == 'No players found':
            return split_output[0].strip('\n')
        if split_output[-1] == '': 
            split_output.pop(-1)
        metadata_dict = {}
        for metadata in split_output:
            split_metadata = metadata.split(' ')
            split_metadata.pop(0)
            key = split_metadata[0].split(':')[-1]
            values = split_metadata[1:]
            add_whitespace = []
            for value in values:
                if value != '':
                    add_whitespace.append(value + ' ')

            value = ''.join(add_whitespace).strip(' ')
            metadata_dict.update({key: value})

        return metadata_dict

    def get_current_player_status(self) -> str:
        command = ['playerctl', 'status', '--player=spotify']
        get_output = self.execute_command(command)
        status = get_output.strip('\n').lower()
        if status == 'playing':
            return 'Now Playing'
        elif status == 'paused':
            return 'Paused'
        elif status == 'no players found':
            return 'Sleeping...'
        else:
            return 'Unknown'

    # Commands
    def play_song(self) -> None:
        command = ['playerctl', 'play', '--player=spotify']
        self.execute_command(command)

    def pause_song(self) -> None:
        command = ['playerctl', 'pause', '--player=spotify']
        self.execute_command(command)

    def toggle_play_pause(self) -> None:
        command = ['playerctl', 'play-pause', '--player=spotify']
        self.execute_command(command)

    def stop_song(self) -> None:
        command = ['playerctl', 'stop', '--player=spotify']
        self.execute_command(command)

    def play_next_song(self) -> None:
        command = ['playerctl', 'next', '--player=spotify']
        self.execute_command(command)

    def play_previous_song(self) -> None:
        command = ['playerctl', 'previous', '--player=spotify']
        self.execute_command(command)

    @staticmethod
    def truncate_text(text: str, char_count: int) -> str:
        if len(text) <= char_count:
            return text
        truncated_text = f'{text[:char_count]}...'
        return truncated_text

    def handle_args(self, arguments: str) -> str:
        _format = arguments.format
        space = arguments.space
        
        metadata = self.get_song_metadata()
        if 'Sleeping' in self.get_current_player_status():
            return 'Sleeping 鈴'
        valid_args = {
            'status': self.get_current_player_status(),
            'artist': metadata['artist'],
            'title': metadata['title'],
            'album': metadata['album'],
            'albumArtist': metadata['albumArtist'],
        }
        info: list[str] = _format.split(' ')
        for count, args in enumerate(info):
            for keys, values in valid_args.items():
                if args == keys:
                    info[count] = values

        display_str = ''.join(info).replace(space, ' ')
        return display_str