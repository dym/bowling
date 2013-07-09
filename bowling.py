from collections import deque


class WrongOrderError(Exception):
    pass


class PointsList():

    points_list = []
    frames_list = []

    def __init__(self, points_list):
        self.points_list = points_list
        self.frames_list = self._gen_frames()

    def _gen_frames(self):
        frames_list = []
        i = 1
        cur_frame = []
        counter = 0
        point_iter = iter(self.points_list)
        while i < 10:
            p = point_iter.next()

            if p >= 0 and p <= 10:
                cur_frame.append(p)
            else:
                raise WrongOrderError('Points are wrong: {}'.format(p))

            if sum(cur_frame) > 10:
                raise WrongOrderError('Frame #{} is wrong: {}'.format(
                    i, cur_frame))

            if sum(cur_frame) == 10 or len(cur_frame) == 2:
                frames_list.append(cur_frame)
                cur_frame = []
                i += 1

        def frame10_wrong_size():
            raise WrongOrderError('Frame 10 ({}) has wrong size: {}'.format(
                cur_frame, len(cur_frame)))

        cur_frame = [p for p in point_iter]
        if len(cur_frame) == 2:
            if sum(cur_frame) < 10:
                frames_list.append(cur_frame)
            else:
                frame10_wrong_size()
        elif len(cur_frame) == 3:
            if cur_frame[0] == 10 or sum(cur_frame[0:2]) == 10:
                frames_list.append(cur_frame)
            else:
                frame10_wrong_size()
        else:
            frame10_wrong_size()

        return frames_list

    def count_points(self):
        count = 0
        i = 0
        for pf in self.frames_list:
            count += sum(pf)
            length = len(pf)
            i += length
            if sum(pf) == 10:
                if length == 1:
                    count += sum(self.points_list[i:i+2])
                elif length == 2:
                    count += self.points_list[i]
        return count


if __name__ == '__main__':
    pl = PointsList([10, 3, 7, 6, 1, 10, 10, 10, 2, 8, 9, 0, 7, 3, 10, 10, 10])
    print pl.count_points()
