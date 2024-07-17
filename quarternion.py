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

        # ベクトルの定義
        vector = np.array([1, 0, 0])
        vector_arrow = Arrow3D(start=[0, 0, 0], end=vector, color=RED)

        self.add(vector_arrow)

        # 回転の定義（ここでは90度回転）
        angle = np.pi / 2  # 90 degrees
        quaternion = (np.cos(angle / 2), np.sin(angle / 2) * 0, np.sin(angle / 2) * 0, np.sin(angle / 2) * 1)  # Z軸周りの回転

        # アニメーション
        num_frames = 60
        for _ in range(num_frames):
            vector = rotate_vector_by_quaternion(vector, quaternion)
            new_vector_arrow = Arrow3D(start=[0, 0, 0], end=vector, color=RED)
            self.play(Transform(vector_arrow, new_vector_arrow), run_time=0.1)
            vector_arrow = new_vector_arrow

        self.wait()

if __name__ == "__main__":
    from manim import config
    config.media_width = "75%"
    config.quality = "low_quality"
    scene = QuaternionRotation()
    scene.render()