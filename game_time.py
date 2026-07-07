import time


class GameTime:
    def __init__(self):
        self.day = 1
        self.hour = 9
        self.minute = 33

        self.last_update = time.monotonic()
        self.was_night = False

    def is_daytime(self):
        return 8 <= self.hour < 22

    def is_night(self):
        return not self.is_daytime()

    def get_phase_name(self):
        if self.is_daytime():
            return "Tag"
        return "Nacht"

    def update(self):
        now = time.monotonic()
        real_seconds_passed = now - self.last_update
        self.last_update = now

        while real_seconds_passed > 0:
            if self.is_daytime():
                seconds_per_game_minute = (20 * 60) / (14 * 60)
                end_hour = 22
            else:
                seconds_per_game_minute = (5 * 60) / (10 * 60)
                end_hour = 8

            game_minutes_to_add = int(real_seconds_passed / seconds_per_game_minute)

            if game_minutes_to_add <= 0:
                break

            self.minute += game_minutes_to_add
            real_seconds_passed = 0

            while self.minute >= 60:
                self.minute -= 60
                self.hour += 1

            if self.hour >= 24:
                self.hour -= 24
                self.day += 1

    def just_entered_night(self):
        currently_night = self.is_night()

        if currently_night and not self.was_night:
            self.was_night = True
            return True

        if not currently_night:
            self.was_night = False

        return False

    def skip_night(self):
        if self.is_night():
            if self.hour >= 22:
                self.day += 1

            self.hour = 8
            self.minute = 0
            self.last_update = time.monotonic()
            self.was_night = False

    def display(self):
        return f"Tag {self.day} | {self.hour:02d}:{self.minute:02d} | {self.get_phase_name()}"