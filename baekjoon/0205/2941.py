s = input()
cro_alpah = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = len(s)
for i in cro_alpah:
    if i in s:
        cnt_i = s.count(i)
        cnt -= (1 * cnt_i)
if 'dz=' in s:
    cnt_dz = s.count('dz=')
    cnt -= (1 * cnt_dz) # 원래는 -2 이지만 위에서 'z='에서 -1을 이미 해줬으므로 -1만 한다
print(cnt)