# Test Grade Calculator

## Tổng quan dự án 

Dự án **Test Grade Calculator** là một chương trình Python được thiết kế để tự động hóa quá trình chấm điểm các bài thi trắc nghiệm. Chương trình đọc tệp dữ liệu chứa câu trả lời của học sinh, tiến hành làm sạch dữ liệu (loại bỏ các dòng không hợp lệ), chấm điểm dựa trên đáp án chuẩn và xuất báo cáo thống kê cũng như kết quả chi tiết của từng học sinh. 
---

## Cấu trúc thư mục 

Để chương trình hoạt động và đọc file chính xác, vui lòng đảm bảo thư mục dự án được sắp xếp như sau:
```
Test Grade Calculator/
│
├── Data Files/
│   ├── class1.txt
│   ├── class2.txt
│   └── ...
│
├── lastname_firstname_grade_the_exams.py
└── README.md
```
---

## Yêu cầu hệ thống 

- Hệ điều hành: Windows, macOS, hoặc Linux.

- Python: Phiên bản 3.7 trở lên.

- Thư viện yêu cầu: pandas, numpy.

**Hướng dẫn cài đặt thư viện**

Mở Terminal (trên macOS/Linux) hoặc Command Prompt / PowerShell (trên Windows) và chạy lệnh sau để cài đặt các thư viện cần thiết:
```bash
pip install pandas numpy
```

---

## Hướng dẫn chạy ứng dụng 

**Bước 1: Di chuyển vào thư mục dự án**

Mở Terminal / Command Prompt và sử dụng lệnh cd để điều hướng đến thư mục gốc chứa mã nguồn (Kĩ thuật lập trình/).
```bash
cd duong_dan_den_thu_muc/Test Grade Calculator
```

**Bước 2: Khởi chạy chương trình**

Gõ lệnh sau để chạy file Python (lưu ý thay đổi tên file sao cho khớp với tên file thực tế của bạn):
```bash
python lastname_firstname_grade_the_exams.py
```

**Bước 3: Nhập dữ liệu**

Khi chương trình hiện thông báo yêu cầu, hãy nhập tên file chứa dữ liệu lớp học bạn muốn chấm điểm. Bạn có thể nhập kèm đuôi .txt hoặc không. Ví dụ: class1 hoặc class1.txt
```
Enter a class file to grade (i.e. class1 for class1.txt): class1
```

**Bước 4: Xem báo cáo phân tích**

Chương trình sẽ hiển thị trực tiếp trên terminal: Quá trình quét lỗi (hiển thị chi tiết các dòng dữ liệu bị thiếu đáp án hoặc sai định dạng mã số học sinh). Tổng số dòng dữ liệu hợp lệ và không hợp lệ. Bảng thống kê điểm số của lớp (Điểm trung bình, Điểm cao nhất, Điểm thấp nhất, Miền giá trị, và Trung vị).

**Bước 5: Lấy file kết quả**

Kết quả điểm thi chi tiết của từng học sinh đã được tính toán xong sẽ được lưu tự động dưới định dạng .txt tại đường dẫn:
```
Output/[tên_file_gốc]_grades.txt
```

---

## Tiêu chí chấm điểm 

Chương trình tính điểm dựa trên nguyên tắc tiêu chuẩn sau:

- +4 điểm cho mỗi câu trả lời đúng.
- 0 điểm cho mỗi câu bỏ qua (không điền đáp án).
- -1 điểm cho mỗi câu trả lời sai.
