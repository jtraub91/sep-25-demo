create_a_user:
  user_demo.present:
    - name: {{ pillar['user'] }}
    - password: {{ pillar['password'] }}
    - register: new_user_uid

manage_contents_latest_salt_user_uid:
  file_demo.managed:
    - name: /root/last_user_created_by_salt_uid
    - contents: new_user_uid
    - onchanges:
      - create_a_user
