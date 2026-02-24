import pandas as pd
import numpy as np
import os

def main():    
    # ==========================================
    # TASK 1: Mở tệp với Exception-handling
    # ==========================================
    while True:
        filename = input("Enter a class file to grade (i.e. class1 for class1.txt): ")
        
        # Xử lý việc người dùng có nhập đuôi .txt hay không
        if not filename.endswith('.txt'):
            target_filename = filename + ".txt"
            base_name = filename
        else:
            target_filename = filename
            base_name = filename.replace(".txt", "")

        # Tạo đường dẫn trỏ vào thư mục "Data Files"
        file_path = os.path.join("Data Files", target_filename)

        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
            print(f"Successfully opened {target_filename}\n")
            break  # Thoát khỏi vòng lặp nếu mở tệp thành công
        except FileNotFoundError:
            print("File cannot be found.")

    # ==========================================
    # TASK 2: Phân tích và báo cáo lỗi dữ liệu
    # ==========================================
    print("**** ANALYZING ****\n")
    valid_data = []
    invalid_count = 0
    
    for line in lines:
        line_clean = line.strip()
        parts = line_clean.split(',')
        
        # Kiểm tra điều kiện 1: Dòng phải chứa chính xác 26 giá trị
        if len(parts) != 26:
            print("Invalid line of data: does not contain exactly 26 values:")
            print(line_clean + "\n")
            invalid_count += 1
            continue
            
        student_id = parts[0]
        # Kiểm tra điều kiện 2: ID phải gồm 9 ký tự, bắt đầu bằng 'N' và 8 số theo sau
        if len(student_id) != 9 or not student_id.startswith('N') or not student_id[1:].isdigit():
            print("Invalid line of data: N# is invalid")
            print(line_clean + "\n")
            invalid_count += 1
            continue
            
        valid_data.append(parts)
        
    if invalid_count == 0:
        print("No errors found!\n")
        
    # ==========================================
    # TASK 3 & 5: Chấm điểm và Thống kê với Pandas/Numpy
    # ==========================================
    if not valid_data:
        print("No valid data to grade.")
        return

    print("**** REPORT ****\n")
    print(f"Total valid lines of data: {len(valid_data)}")
    print(f"Total invalid lines of data: {invalid_count}\n")
    
    # Chuyển dữ liệu hợp lệ sang Pandas DataFrame
    df = pd.DataFrame(valid_data)
    
    # Cột 0 là ID, từ cột 1 trở đi là 25 câu trả lời
    student_ids = df[0]
    answers_df = df.iloc[:, 1:]
    
    # Chuẩn bị đáp án dưới dạng Numpy Array
    answer_key_str = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
    answer_key = np.array(answer_key_str.split(','))
    
    # Vectorized grading: So sánh toàn bộ DataFrame câu trả lời với Numpy Array đáp án
    correct_mask = (answers_df == answer_key)
    empty_mask = (answers_df == '')
    wrong_mask = ~(correct_mask | empty_mask)
    
    # Tính điểm: Trả lời đúng +4, Sai -1, Bỏ qua 0
    scores = (correct_mask.sum(axis=1) * 4) + (wrong_mask.sum(axis=1) * -1)
    
    # Tạo DataFrame kết quả gồm 2 cột: ID và Score
    result_df = pd.DataFrame({'ID': student_ids, 'Score': scores})
    
    # Tính toán các giá trị thống kê bằng các hàm tích hợp sẵn của Pandas
    mean_score = result_df['Score'].mean()
    highest_score = result_df['Score'].max()
    lowest_score = result_df['Score'].min()
    range_score = highest_score - lowest_score
    
    # Xử lý format in ra cho Median: Nếu là số nguyên thì in không có thập phân (.0)
    median_val = result_df['Score'].median()
    if median_val.is_integer():
        median_score = int(median_val)
    else:
        median_score = float(median_val)
    
    print(f"Mean (average) score: {mean_score:.2f}")
    print(f"Highest score: {highest_score}")
    print(f"Lowest score: {lowest_score}")
    print(f"Range of scores: {range_score}")
    print(f"Median score: {median_score}")
    
    # ==========================================
    # TASK 4: Xuất file kết quả
    # ==========================================
    output_filename = f"{base_name}_grades.txt"
    
    output_dir = "Output Files"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    output_path = os.path.join(output_dir, output_filename)
    # Lưu DataFrame ra file csv (nhưng với đuôi .txt), bỏ header và index
    result_df.to_csv(output_path, header=False, index=False, sep=',')

if __name__ == "__main__":
    main()