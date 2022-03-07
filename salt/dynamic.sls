make_random_instance:
  random.make_instance:
    - name: yolofam
    - register: instance_uuid

make_tmp_file_for_instance_uuid:
  file.touch_reg:
    - registered:
        name: instance_uuid

