# https://informatics.msk.ru/mod/statements/view.php?id=4535&chapterid=3753&__cf_chl_captcha_tk__=25a232a555a13383b25aa2c272ee9c38a6e48ee0-1613548754-0-AVE_7n4psP2th_hK7Y0Bm8Tf7dBOILROfSxVSFIjhEdlGrQb2HsfCc4KQwDD3LHs6_Ob-lwnK2VEx8_Scs2B0qW3UcQnJu482Ns5bZ_CI9chUOUMEbHGaw7pyKB7z-d2TqUS8TFJYmV8lrkc-aAiCAnettBnHqzE4oDNzsec1VlGztoW830A_GNPfeA8w9iIqpvJnCzjSQHf5Itjhh6-_VkjsRF-Fsb3upXLedYsJxUz2ti-Us4RUSMLg9Evz-lUhC6JGYMtDljUr8ioMQmcP7wjaAYSoLoD4eBiORldSm73Phc-J5HRXoFHwU6Wq12kIdl-Nodnjp8EzN1UxhgBHVTFf4P29BPiMEqNw_w20_Qn1pOGem60Y1GbJrpxKpEJkq4Bhn9olx7Z-OPxsd-rnlNOSiNwq2dMEmw6RawMV1OxywqwpdD-Z8vg1nN5f8AezO7tYONMnkL8BUgdmFBT-D_-AMkrpmOvcX0Lx5JYEcyBX36iUbZ7D_y6EBTcrANrBBFD3iuhhqe0rysMJnik0s90qQmbNyxzX2vqt2sbvvGxbMwwmC63uLFeVJrej29SEkKzbwIhcvfPLhXUwat4gopSQoUZl7hfDdTc3uYIxAq5xnuYfvAnK4jUWE4-Yw-4qAAwkcIxSGJB2quL1Agebps#1
n, m = input().split()
s1 = set()
s2 = set()
for i in range(int(n)):
    s1.add(int(input()))
for i in range(int(m)):
    s2.add(int(input()))
print(len(s1 & s2))
s3 = list(s1 & s2)
for i in range(len(s3)):
    print(s3[i],end = ' ')
print( ' ')
s3 = list(s1 - (s1 & s2))
print(len(s3))
for i in range(len(s3)):
    print(s3[i],end = ' ')
print(' ')
s3 = list(s2 - (s1 & s2))
print(len(s3))
for i in range(len(s3)):
    print(s3[i], end = ' ')
print (' ')