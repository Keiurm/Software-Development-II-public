import bpy, math, random


# 円柱の作成
def add_cylinder(location, rotation, resize, color, name):
    material = bpy.data.materials.new("Color")  # 材質データの作成
    material.diffuse_color = color  # 材質データの色（引数で受け取った値）
    bpy.ops.mesh.primitive_cylinder_add(location=(location), rotation=(rotation))
    bpy.ops.transform.resize(value=(resize))  # 平面を拡大
    bpy.ops.rigidbody.object_add(type="PASSIVE")  # 剛体をパッシブに設定
    bpy.context.object.data.materials.append(material)  # 材質の反映
    bpy.context.object.name = name
    return bpy.context.object


# 平面の作成
def add_plane(location, rotation, resize, color, name):
    material = bpy.data.materials.new("Color")  # 材質データの作成
    material.diffuse_color = color  # 材質データの色（引数で受け取った値）
    bpy.ops.mesh.primitive_plane_add(location=(location), rotation=(rotation))
    bpy.ops.transform.resize(value=(resize))  # 平面を拡大
    bpy.ops.rigidbody.object_add(type="PASSIVE")  # 剛体をパッシブに設定
    bpy.context.object.data.materials.append(material)  # 材質の反映
    bpy.context.object.name = name
    return bpy.context.object


# 照明の追加
def add_ceiling_light(location, color, energy, type, name):
    # 光源の設定
    bpy.ops.object.light_add(
        type=type,  # 光源の種類（POINT：点光源，SUN：平行光線，
        # SPOT：スポットライト，AREA：エリアライト）
        location=(location),  # 光源の位置
        rotation=(0, 0, -math.pi / 2),  # 光源の角度
        scale=(100, 10, 10),  # 光源の大きさ
    )
    bpy.context.object.data.energy = energy  # 光源の強さ（デフォルト値は 10）
    bpy.context.object.data.color = color  # 光源の色（赤，緑，青）
    bpy.context.object.name = name
    return bpy.context.object


# カメラの移動
def move_camera(
    current_location,
    current_rotation,
    current_frame,
    next_location,
    next_rotation,
    next_frame,
):
    obj = bpy.data.objects["camera"]  # アクティブなオブジェクトを取得
    scene.frame_set(current_frame)  # 現在のフレームを設定
    obj.location = current_location
    obj.rotation_euler = current_rotation
    obj.keyframe_insert(data_path="location")
    obj.keyframe_insert(data_path="rotation_euler")
    scene.frame_set(next_frame)  # 次のフレームを設定
    obj.location = next_location
    obj.rotation_euler = next_rotation
    obj.keyframe_insert(data_path="location")
    obj.keyframe_insert(data_path="rotation_euler")


def move_door(
    current_location,
    current_rotation,
    current_frame,
    next_location,
    next_rotation,
    next_frame,
):
    obj = bpy.data.objects["door"]  # アクティブなオブジェクトを取得
    scene.frame_set(current_frame)  # 現在のフレームを設定
    obj.location = current_location
    obj.rotation_euler = current_rotation
    obj.keyframe_insert(data_path="location")
    obj.keyframe_insert(data_path="rotation_euler")
    scene.frame_set(next_frame)  # 次のフレームを設定
    obj.location = next_location
    obj.rotation_euler = next_rotation
    obj.keyframe_insert(data_path="location")
    obj.keyframe_insert(data_path="rotation_euler")


def make_monkey(location, rotation, resize, color, name):
    material = bpy.data.materials.new("Color")  # 材質データの作成
    material.diffuse_color = color  # 材質データの色（引数で受け取った値）
    bpy.ops.mesh.primitive_monkey_add(location=(location), rotation=(rotation))
    bpy.ops.transform.resize(value=(resize))  # 平面を拡大
    bpy.ops.rigidbody.object_add(type="PASSIVE")  # 剛体をパッシブに設定
    bpy.context.object.data.materials.append(material)  # 材質の反映
    bpy.context.object.name = name
    return bpy.context.object


def move_monkey(
    current_location,
    current_rotation,
    current_frame,
    next_location,
    next_rotation,
    next_frame,
    object_name,
):
    # アクティブなオブジェクトを取得
    obj = bpy.data.objects[object_name]
    scene.frame_set(current_frame)  # 現在のフレームを設定
    obj.location = current_location
    obj.rotation_euler = current_rotation
    obj.keyframe_insert(data_path="location")
    obj.keyframe_insert(data_path="rotation_euler")
    scene.frame_set(next_frame)  # 次のフレームを設定
    obj.location = next_location
    obj.rotation_euler = next_rotation
    obj.keyframe_insert(data_path="location")
    obj.keyframe_insert(data_path="rotation_euler")


def change_monkey_color(
    current_color, current_frame, next_color, next_frame, object_name
):
    obj = bpy.data.objects[object_name]
    material = obj.material_slots[0].material
    scene.frame_set(current_frame)
    material.diffuse_color = current_color
    material.keyframe_insert(data_path="diffuse_color")
    scene.frame_set(next_frame)
    material.diffuse_color = next_color
    material.keyframe_insert(data_path="diffuse_color")


def change_light_color(
    current_color, current_frame, next_color, next_frame, object_name
):
    obj = bpy.data.objects[object_name]
    obj.data.color = current_color
    obj.data.keyframe_insert(data_path="color")
    scene.frame_set(next_frame)
    obj.data.color = next_color
    obj.data.keyframe_insert(data_path="color")


# 全てのオブジェクトを選択し、削除
bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete(True)


# レンダリングの設定
scene = bpy.context.scene  # シーンオブジェクトデータを変数 scene に代入
scene.render.engine = "CYCLES"  # レンダリングエンジンを Cycles に変更
scene.render.resolution_x = 1920  # レンダリング画像の X 方向の解像度
scene.render.resolution_y = 1080  # レンダリング画像の Y 方向の解像度
scene.render.resolution_percentage = 100  # レンダリングする画像サイズの百分率
scene.render.use_multiview = True  # レンダーのマルチビューをオンにする
scene.cycles.device = "GPU"  # GPU でレンダリングする
scene.cycles.samples = 128
scene.cycles.use_preview_denoising = True
scene.cycles.preview_samples = 300
scene.render.image_settings.views_format = "STEREO_3D"  # レンダーのビューフォーマットをステレオ 3D に設定
scene.render.image_settings.stereo_3d_format.display_mode = (
    "TOPBOTTOM"  # レンダーのビューフォーマットのステレオ 3D 設定
)
scene.frame_start = 0  # アニメーションの開始フレーム
scene.frame_end = 1500  # アニメーションの終了フレーム
# シーケンサーの設定(音声ファイルの再生)
if not scene.sequence_editor:  # ビデオシーケンスエディターがない場合
    scene.sequence_editor_create()  # ビデオシーケンスエディターを生成
bpy.ops.sequencer.select_all(action="SELECT")  # シーケンサーを全て選択
bpy.ops.sequencer.delete()  # 選択されたシーケンサーを削除

light_1 = add_ceiling_light((-40, -80, 42.5), (1, 1, 1), 3000, "AREA", "light_1")
light_2 = add_ceiling_light((75, -80, 42.5), (1, 1, 1), 3000, "AREA", "light_2")
light_3 = add_ceiling_light((75, 40, 42.5), (1, 1, 1), 3000, "AREA", "light_3")
light_4 = add_ceiling_light((45, 10, 42.5), (1, 1, 1), 3000, "AREA", "light_4")
light_5 = add_ceiling_light((5, -30, 42.5), (1, 1, 1), 3000, "AREA", "light_5")
light_6 = add_ceiling_light((-30, 30, 42.5), (1, 1, 1), 3000, "AREA", "light_6")

# 照明の点滅
scene.frame_set(690)
obj = bpy.data.objects["light_1"]
obj.data.energy = 3000
obj.data.keyframe_insert(data_path="energy")
scene.frame_set(695)
obj.data.energy = 0
obj.data.keyframe_insert(data_path="energy")
scene.frame_set(700)
obj.data.energy = 3000
obj.data.keyframe_insert(data_path="energy")

scene.frame_set(725)
obj.data.energy = 0
obj.data.keyframe_insert(data_path="energy")
scene.frame_set(730)
obj.data.energy = 3000
obj.data.keyframe_insert(data_path="energy")
scene.frame_set(735)
obj.data.energy = 0
obj.data.keyframe_insert(data_path="energy")
scene.frame_set(760)
obj.data.energy = 3000
obj.data.keyframe_insert(data_path="energy")

change_light_color(
    (1, 1, 1),
    795,
    (1, 0, 0),
    800,
    "light_1",
)
change_light_color(
    (1, 1, 1),
    795,
    (1, 0, 0),
    800,
    "light_2",
)
change_light_color(
    (1, 1, 1),
    795,
    (1, 0, 0),
    800,
    "light_3",
)
change_light_color(
    (1, 1, 1),
    795,
    (1, 0, 0),
    800,
    "light_4",
)
change_light_color(
    (1, 1, 1),
    795,
    (1, 0, 0),
    800,
    "light_5",
)
change_light_color(
    (1, 1, 1),
    795,
    (1, 0, 0),
    800,
    "light_6",
)


# カメラの設定
bpy.ops.object.camera_add(
    location=(0, 0, 17.5),
    rotation=(math.pi / 2, 0, math.pi / 2),
)
camera = bpy.context.object
camera.name = "camera"
camera.data.type = "PANO"  # カメラのレンズをパノラマ状に設定
camera.data.cycles.panorama_type = "EQUIRECTANGULAR"  # タイプを正距円筒図に設定
camera.data.clip_start = 0.1  # カメラのクリッピング開始位置
camera.data.clip_end = 10000  # カメラのクリッピング終了位置
camera.data.stereo.use_spherical_stereo = True  # カメラの立体視の球状ステレオを ON にする
# 目の間隔は要検討
# camera.data.stereo.interocular_distance = 0.1  # カメラの立体視の目の間隔
move_camera(
    (150, 0, 17.5),
    (math.radians(90), math.radians(0), math.radians(90)),
    0,
    (150, 0, 17.5),
    (math.radians(90), math.radians(0), math.radians(90)),
    192,
)
move_camera(
    (150, 0, 17.5),
    (math.radians(90), math.radians(0), math.radians(90)),
    192,
    (150, 0, 17.5),
    (math.radians(90), math.radians(0), math.radians(180)),
    264,
)
move_camera(
    (150, 0, 17.5),
    (math.radians(90), math.radians(0), math.radians(180)),
    264,
    (150, -75, 17.5),
    (math.radians(90), math.radians(0), math.radians(180)),
    384,
)
move_camera(
    (150, -75, 17.5),
    (math.radians(90), math.radians(0), math.radians(180)),
    384,
    (150, -75, 17.5),
    (math.radians(90), math.radians(0), math.radians(90)),
    432,
)


move_camera(
    (150, -70, 17.5),
    (math.radians(90), math.radians(0), math.radians(90)),
    432,
    (90, -75, 17.5),
    (math.radians(90), math.radians(0), math.radians(90)),
    504,
)
move_camera(
    (90, -75, 17.5),
    (math.radians(90), math.radians(0), math.radians(90)),
    504,
    (90, -75, 17.5),
    (math.radians(90), math.radians(0), math.radians(0)),
    552,
)
move_camera(
    (90, -75, 17.5),
    (math.radians(90), math.radians(0), math.radians(0)),
    552,
    (90, -75, 17.5),
    (math.radians(90), math.radians(0), math.radians(90)),
    588,
)
move_camera(
    (90, -75, 17.5),
    (math.radians(90), math.radians(0), math.radians(90)),
    588,
    (0, -75, 17.5),
    (math.radians(90), math.radians(0), math.radians(90)),
    684,
)
move_camera(
    (0, -75, 17.5),
    (math.radians(90), math.radians(0), math.radians(90)),
    684,
    (0, -75, 17.5),
    (math.radians(90), math.radians(0), math.radians(90)),
    879,
)

move_camera(
    (0, -75, 17.5),
    (math.radians(90), math.radians(0), math.radians(90)),
    879,
    (10, -75, 17.5),
    (math.radians(90), math.radians(0), math.radians(90)),
    927,
)
move_camera(
    (10, -75, 17.5),
    (math.radians(90), math.radians(0), math.radians(90)),
    879,
    (20, -75, 17.5),
    (math.radians(90), math.radians(0), math.radians(-90)),
    927,
)
move_camera(
    (20, -75, 17.5),
    (math.radians(90), math.radians(0), math.radians(-90)),
    927,
    (75, -75, 17.5),
    (math.radians(90), math.radians(0), math.radians(-90)),
    975,
)

move_camera(
    (75, -75, 17.5),
    (math.radians(90), math.radians(0), math.radians(-90)),
    975,
    (75, -75, 17.5),
    (math.radians(90), math.radians(0), math.radians(90)),
    999,
)
move_camera(
    (75, -75, 17.5),
    (math.radians(90), math.radians(0), math.radians(90)),
    999,
    (75, -75, 17.5),
    (math.radians(90), math.radians(0), math.radians(0)),
    1023,
)
move_camera(
    (75, -75, 17.5),
    (math.radians(90), math.radians(0), math.radians(0)),
    1023,
    (75, 80, 17.5),
    (math.radians(90), math.radians(0), math.radians(0)),
    1095,
)

move_camera(
    (75, 80, 17.5),
    (math.radians(90), math.radians(0), math.radians(0)),
    1095,
    (45, 80, 17.5),
    (math.radians(90), math.radians(0), math.radians(90)),
    1155,
)
move_camera(
    (45, 80, 17.5),
    (math.radians(90), math.radians(0), math.radians(90)),
    1155,
    (45, 80, 17.5),
    (math.radians(90), math.radians(0), math.radians(180)),
    1187,
)
move_camera(
    (45, 80, 17.5),
    (math.radians(90), math.radians(0), math.radians(180)),
    1187,
    (45, -40, 17.5),
    (math.radians(90), math.radians(0), math.radians(180)),
    1237,
)
move_camera(
    (45, -40, 17.5),
    (math.radians(90), math.radians(0), math.radians(180)),
    1237,
    (40, -40, 17.5),
    (math.radians(90), math.radians(0), math.radians(90)),
    1261,
)
move_camera(
    (40, -40, 17.5),
    (math.radians(90), math.radians(0), math.radians(90)),
    1261,
    (-30, -40, 17.5),
    (math.radians(90), math.radians(0), math.radians(90)),
    1285,
)
move_camera(
    (-30, -40, 17.5),
    (math.radians(90), math.radians(0), math.radians(90)),
    1285,
    (-30, -35, 17.5),
    (math.radians(90), math.radians(0), math.radians(0)),
    1309,
)

move_camera(
    (-30, -35, 17.5),
    (math.radians(90), math.radians(0), math.radians(0)),
    1309,
    (-30, 15, 17.5),
    (math.radians(90), math.radians(0), math.radians(0)),
    1333,
)

move_camera(
    (-30, 15, 17.5),
    (math.radians(90), math.radians(0), math.radians(0)),
    1333,
    (-30, 15, 17.5),
    (math.radians(90), math.radians(0), math.radians(180)),
    1387,
)


# 建物
# 床
floor = add_plane((0, 0, 0), (0, 0, 0), (100, 100, 1), (1, 1, 1, 0), "floor")
# 壁
right_wall = add_plane(
    (0, 100, 22.5), (math.pi / 2, 0, 0), (100, 1, 22.5), (0, 0, 0, 0), "right_wall"
)
left_wall = add_plane(
    (0, -100, 22.5), (math.pi / 2, 0, 0), (100, 1, 22.5), (0, 0, 0, 0), "left_wall"
)
# 向こうの壁
back_wall = add_plane(
    (-100, 0, 22.5),
    (0, math.pi / 2, 0),
    (1, 100, 22.5),
    (0, 0, 0, 1),
    "back_wall",
)
# 手前の壁
front_wall = add_plane(
    (100, 20, 22.5), (0, math.pi / 2, 0), (1, 80, 22.5), (0, 0, 0, 1), "front_wall"
)


# 仕切り壁1
wall_1 = add_plane(
    (-60, -25, 22.5), (0, math.pi / 2, 0), (1, 75, 22.5), (0, 0, 0, 0), "wall_1"
)

# 仕切り壁2
wall_2 = add_plane(
    (-20, 40, 22.5), (0, math.pi / 2, 0), (1, 60, 22.5), (0, 0, 0, 0), "wall_2"
)

# 仕切り壁3
wall_3 = add_plane(
    (0, -60, 22.5), (math.pi / 2, 0, 0), (60, 1, 22.5), (0, 0, 0, 0), "wall_3"
)

# 仕切り壁4
wall_4 = add_plane(
    (60, 5, 22.5), (0, math.pi / 2, 0), (1, 65, 22.5), (0, 0, 0, 0), "wall_4"
)

# 仕切り壁5
wall_5 = add_plane(
    (30, 40, 22.5), (0, math.pi / 2, 0), (1, 60, 22.5), (0, 0, 0, 0), "wall_5"
)

# 仕切り壁6
wall_6 = add_plane(
    (5, -20, 22.5), (math.pi / 2, 0, 0), (25, 1, 22.5), (0, 0, 0, 0), "wall_6"
)
# 天井
ceiling = add_plane((0, 0, 45), (0, 0, 0), (100, 100, 1), (0.1, 0.2, 0.2, 1), "ceiling")

# サルの追加
monkey_1 = make_monkey(
    (-40, -80, 12.5),
    (math.radians(0), math.radians(0), math.radians(90)),
    (11, 11, 11),
    (1, 0, 0, 1),
    "monkey_1",
)
move_monkey(
    (-40, -80, 12.5),
    (math.radians(0), math.radians(0), math.radians(90)),
    865,
    (67, -80, 12.5),
    (math.radians(0), math.radians(0), math.radians(90)),
    1050,
    "monkey_1",
)
move_monkey(
    (67, -80, 12.5),
    (math.radians(0), math.radians(0), math.radians(90)),
    1050,
    (75, 45, 12.5),
    (math.radians(0), math.radians(0), math.radians(180)),
    1080,
    "monkey_1",
)
move_monkey(
    (75, 45, 12.5),
    (math.radians(0), math.radians(0), math.radians(180)),
    1080,
    (75, 65, 12.5),
    (math.radians(0), math.radians(0), math.radians(180)),
    1110,
    "monkey_1",
)
move_monkey(
    (75, 65, 12.5),
    (math.radians(0), math.radians(0), math.radians(180)),
    1110,
    (75, 75, 12.5),
    (math.radians(0), math.radians(0), math.radians(270)),
    1120,
    "monkey_1",
)
move_monkey(
    (75, 75, 12.5),
    (math.radians(0), math.radians(0), math.radians(270)),
    1120,
    (65, 85, 12.5),
    (math.radians(0), math.radians(0), math.radians(270)),
    1145,
    "monkey_1",
)
move_monkey(
    (65, 85, 12.5),
    (math.radians(0), math.radians(0), math.radians(270)),
    1145,
    (55, 85, 12.5),
    (math.radians(0), math.radians(0), math.radians(270)),
    1190,
    "monkey_1",
)

move_monkey(
    (55, 85, 12.5),
    (math.radians(0), math.radians(0), math.radians(270)),
    1190,
    (50, 85, 12.5),
    (math.radians(0), math.radians(0), math.radians(0)),
    1200,
    "monkey_1",
)
move_monkey(
    (50, 85, 12.5),
    (math.radians(0), math.radians(0), math.radians(0)),
    1200,
    (50, -40, 12.5),
    (math.radians(0), math.radians(0), math.radians(0)),
    1350,
    "monkey_1",
)

move_monkey(
    (50, -40, 12.5),
    (math.radians(0), math.radians(0), math.radians(0)),
    1350,
    (50, -40, 12.5),
    (math.radians(0), math.radians(0), math.radians(-90)),
    1360,
    "monkey_1",
)

move_monkey(
    (50, -40, 12.5),
    (math.radians(0), math.radians(0), math.radians(-90)),
    1360,
    (-30, -40, 12.5),
    (math.radians(0), math.radians(0), math.radians(-90)),
    1395,
    "monkey_1",
)

move_monkey(
    (-30, -40, 12.5),
    (math.radians(0), math.radians(0), math.radians(-90)),
    1395,
    (-30, -40, 12.5),
    (math.radians(0), math.radians(0), math.radians(180)),
    1410,
    "monkey_1",
)
move_monkey(
    (-30, -40, 12.5),
    (math.radians(0), math.radians(0), math.radians(180)),
    1410,
    (-30, 15, 12.5),
    (math.radians(0), math.radians(0), math.radians(180)),
    1455,
    "monkey_1",
)

monkey_2 = make_monkey(
    (-80, 60, 12.5),
    (math.radians(0), math.radians(0), math.radians(0)),
    (11, 11, 11),
    (1, 0, 0, 1),
    "monkey_2",
)
move_monkey(
    (-80, 60, 12.5),
    (math.radians(0), math.radians(0), math.radians(0)),
    1310,
    (-40, 60, 12.5),
    (math.radians(0), math.radians(0), math.radians(0)),
    1350,
    "monkey_2",
)
move_monkey(
    (-40, 60, 12.5),
    (math.radians(0), math.radians(0), math.radians(0)),
    1410,
    (-30, -15, 12.5),
    (math.radians(0), math.radians(0), math.radians(0)),
    1455,
    "monkey_2",
)


# 庭
# 庭を囲む壁
garden_wall_1 = add_plane(
    (200, 0, 22.5), (0, math.pi / 2, 0), (1, 120, 22.5), (0, 0, 0, 1), "garden_wall_1"
)
garden_wall_2 = add_plane(
    (150, -120, 22.5), (math.pi / 2, 0, 0), (50, 1, 22.5), (0, 0, 0, 1), "garden_wall_2"
)
garden_wall_3 = add_plane(
    (150, 120, 22.5), (math.pi / 2, 0, 0), (50, 1, 22.5), (0, 0, 0, 1), "garden_wall_3"
)
graden_wall_4 = add_plane(
    (100, -110, 22.5), (0, math.pi / 2, 0), (1, 10, 22.5), (0, 0, 0, 1), "graden_wall_4"
)
garden_wall_5 = add_plane(
    (100, 110, 22.5), (0, math.pi / 2, 0), (1, 10, 22.5), (0, 0, 0, 1), "garden_wall_5"
)

# 床
garden_floor = add_plane(
    (150, 0, 0), (0, 0, 0), (50, 120, 1), (0.0160636, 0.8, 0.0370112, 1), "garden_floor"
)
bpy.ops.object.particle_system_add()  # パーティクルシステムを追加
particle_system = garden_floor.particle_systems[0]
particle_settings = particle_system.settings  # パーティクルの設定を取得
particle_settings.type = "HAIR"  # パーティクルの種類
particle_settings.count = 10000  # パーティクルの数
particle_settings.hair_length = 6.4  # パーティクルの長さ
particle_settings.brownian_factor = 0.65  # パーティクルの乱雑さ

material = bpy.data.materials.new(name="MyMaterial")  # マテリアルを作成
material.use_nodes = True  # ノードを使用する設定にする
# Principled BSDFノードを取得
principled_bsdf = material.node_tree.nodes.get("Principled BSDF")

# ベースカラーを設定
principled_bsdf.inputs["Base Color"].default_value = (0.0160636, 0.8, 0.0370112, 1)

# マテリアルをオブジェクトに割り当て
garden_floor.data.materials.append(material)

rain_1 = add_cylinder(
    (0, 0, 60), (0, 0, 0), (0.05, 0.05, 0.2), (1.0, 0.8, 0.8, 1.0), "rain_1"
)

# ドア
door = add_plane(
    (99, -20, 22.5), (0, math.pi / 2, 0), (1, 25, 22.5), (0, 0, 0, 0), "door"
)
move_door(
    (99, -30, 22.5),
    (0, math.pi / 2, 0),
    700,
    (99, -80, 22.5),
    (0, math.pi / 2, 0),
    805,
)


# 庭の天井
garden_ceiling = add_plane(
    (150, 0, 105),
    (0, 0, 0),
    (50, 120, 1),
    (0.5, 0.5, 0.5, 1),
    "garden_ceiling",
)
particle_system = bpy.context.object.modifiers.new("ParticleSystem", "PARTICLE_SYSTEM")

# パーティクル設定を取得
particle_settings = particle_system.particle_system.settings

# パーティクル設定を変更
particle_settings.render_type = "OBJECT"
particle_settings.instance_object = rain_1
particle_settings.particle_size = 1.02
particle_settings.count = 10000
particle_settings.lifetime = 500
particle_settings.frame_start = -100
particle_settings.frame_end = 580
particle_settings.mass = 1


# # シーケンサーの設定(音声ファイルの再生)
# if not scene.sequence_editor:  # ビデオシーケンスエディターがない場合
#     scene.sequence_editor_create()  # ビデオシーケンスエディターを生成
# # 音声ファイルのパス
# #sound_file_path = ここに音声ファイルのパスを入れる


# # 音声ストリップを追加
# sound_strip = bpy.context.scene.sequence_editor.sequences.new_sound(
#     "Sound", sound_file_path, start_frame, 1
# )


# # 音声の終了フレームを設定
# sound_strip.frame_final_end = end_frame

# シーケンサーの設定(音声ファイルの再生)
if not scene.sequence_editor:  # ビデオシーケンスエディターがない場合
    scene.sequence_editor_create()  # ビデオシーケンスエディターを生成


bpy.context.scene.render.image_settings.file_format = "FFMPEG"  # ファイル形式を設定
bpy.context.scene.render.ffmpeg.format = "MPEG4"  # コンテナの設定
bpy.context.scene.render.ffmpeg.audio_codec = "MP3"  # 音声追加用に MP3 に設定
bpy.context.scene.render.filepath = (
    "C:\\Users\\keisu\\Desktop\\Software-Development-II\\1219\\2245135_VR.mp4"
)
