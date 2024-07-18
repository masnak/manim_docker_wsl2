# manim -p -ql quarternion.py QuaternionRotation

from manim import *

class QuaternionRotation(ThreeDScene):
    def construct(self):
        # 四元数の定義
        def quaternion_multiply(q1, q2):
            w1, x1, y1, z1 = q1
            w2, x2, y2, z2 = q2
            w = w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2
            x = w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2
            y = w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2
            z = w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2
            return w, x, y, z

        def rotate_vector_by_quaternion(v, q):
            q_conjugate = (q[0], -q[1], -q[2], -q[3])
            v_as_quaternion = (0, v[0], v[1], v[2])
            return quaternion_multiply(quaternion_multiply(q, v_as_quaternion), q_conjugate)[1:]

        # 初期設定
        axis = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(axis)

        # 立方体の定義
        cube_positions = [np.array([2, 0, 0]), np.array([4, 0, 0]), np.array([5, 0, 0])]
        cubes = [Cube(side_length=1).move_to(pos) for pos in cube_positions]

        for cube in cubes:
            self.add(cube)

        # 各軸周りの回転四元数を定義
        angle = np.pi / 4  # 45 degrees

        # X軸周りの回転
        x_axis_rotation = (np.cos(angle / 2), np.sin(angle / 2), 0, 0)
        # Y軸周りの回転
        y_axis_rotation = (np.cos(angle / 2), 0, np.sin(angle / 2), 0)
        # Z軸周りの回転
        z_axis_rotation = (np.cos(angle / 2), 0, 0, np.sin(angle / 2))

        # アニメーション
        num_frames = 60
        rotations = [x_axis_rotation, y_axis_rotation, z_axis_rotation]
        for rotation in rotations:
            for _ in range(num_frames):
                for cube in cubes:
                    for face in cube.family_members_with_points():
                        face.apply_function(lambda p: rotate_vector_by_quaternion(p, rotation))
                self.wait(0.1)

        self.wait()

if __name__ == "__main__":
    from manim import config
    config.media_width = "75%"
    config.quality = "low_quality"
    scene = QuaternionRotation()
    scene.render()