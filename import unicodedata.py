import unicodedata

# Hàm để loại bỏ dấu từ chuỗi Unicode
def bo_dau(chuoi):
    return ''.join(c for c in unicodedata.normalize('NFD', chuoi)
                   if unicodedata.category(c) != 'Mn')

# Hàm để thêm một mục từ mới vào từ điển
def them_muc_tu(tu_dien, tu, loai_tu, nghia, vi_du):
    tu_khong_dau = bo_dau(tu.lower())
    if tu_khong_dau in tu_dien:
        tu_dien[tu_khong_dau].append((loai_tu, nghia, vi_du))
    else:
        tu_dien[tu_khong_dau] = [(loai_tu, nghia, vi_du)]

# Hàm để đọc từ điển từ tập tin
def doc_tu_dien(ten_tap_tin):
    tu_dien = {}
    with open(ten_tap_tin, 'r', encoding='utf-8') as file:
        tu = ''
        for line in file:
            line = line.strip()
            if '|' not in line:
                tu = line
                tu_dien[tu] = []
            else:
                loai_tu, nghia, vi_du = line.split('|')
                tu_dien[tu].append((loai_tu, nghia, vi_du))
    return tu_dien
# Hàm để in ra từ điển
def in_tu_dien(tu_dien):
    for tu, cac_nghia in sorted(tu_dien.items()):
        print(tu)
        for loai_tu, nghia, vi_du in cac_nghia:
            print(f"- {loai_tu}: {nghia}")
            print(f"  Ví dụ: {vi_du}")

# Hàm để lưu từ điển vào tập tin
def luu_tu_dien(tu_dien, ten_tap_tin):
    with open(ten_tap_tin, 'w') as file:
        for tu, cac_nghia in tu_dien.items():
            file.write(tu + '\n')
            for loai_tu, nghia, vi_du in cac_nghia:
                file.write(f"{loai_tu}|{nghia}|{vi_du}\n")

# Hàm để lưu từ điển vào tập tin
def luu_tu_dien(tu_dien, ten_tap_tin):
    with open(ten_tap_tin, 'w', encoding='utf-8') as file:
        for tu, cac_nghia in tu_dien.items():
            file.write(tu + '\n')
            for loai_tu, nghia, vi_du in cac_nghia:
                file.write(f"{loai_tu}|{nghia}|{vi_du}\n")


# Main function
def main():
    tu_dien = {}
    ten_tap_tin = "n21dcdt073_mang.txt"  # Thay mã sinh viên vào đây
    try:
        tu_dien = doc_tu_dien(ten_tap_tin)
    except FileNotFoundError:
        print("Không tìm thấy tập tin từ điển. Tạo mới từ điển.")

    while True:
        print("\nChương trình từ điển Anh-Anh")
        print("1. Thêm mục từ mới")
        print("2. Hiển thị từ điển")
        print("3. Lưu từ điển")
        print("4. Thoát")

        lua_chon = input("Nhập lựa chọn của bạn: ")

        if lua_chon == '1':
            tu = input("Nhập từ: ")
            loai_tu = input("Nhập loại từ: ")
            nghia = input("Nhập nghĩa: ")
            vi_du = input("Nhập ví dụ: ")
            them_muc_tu(tu_dien, tu, loai_tu, nghia, vi_du)
        elif lua_chon == '2':
            if tu_dien:
                in_tu_dien(tu_dien)
            else:
                print("Từ điển rỗng.")
        elif lua_chon == '3':
            luu_tu_dien(tu_dien, ten_tap_tin)
            print("Từ điển đã được lưu.")
        elif lua_chon == '4':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
