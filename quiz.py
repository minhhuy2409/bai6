# Tạo danh sách các câu hỏi và đáp án
questions = [
    {
        "question": "Python được phát hành vào năm nào?",
        "options": {
            "A": "1991",
            "B": "1989",
            "C": "2000",
            "D": "1995"
        },
        "answer": "A"
    },
    {
        "question": "Ai là người tạo ra Python?",
        "options": {
            "A": "Guido van Rossum",
            "B": "Dennis Ritchie",
            "C": "James Gosling",
            "D": "Bjarne Stroustrup"
        },
        "answer": "A"
    },
    {
        "question": "Câu lệnh nào dùng để hiển thị dữ liệu ra màn hình trong Python?",
        "options": {
            "A": "print()",
            "B": "cout< <",
            "C": "System.out.printin()",
            "D": "echo"
        },
        "answer": "A"
    }
]

# Khởi tạo biến điểm
score = 0

# Hiển thị từng câu hỏi và cho người chơi nhập đáp án
for question in questions:
    print(question["question"])
    for option, value in question["options"].items():
        print(option + ".", value)
    answer = input("Nhập đáp án của bạn: ").upper()
    if answer == question["answer"]:
        score += 1

# In ra số điểm của người chơi
print("Số điểm của bạn là:", score)
