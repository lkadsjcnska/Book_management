import turtle
import tkinter as tk

# Turtle部分
screen = turtle.Screen()
screen.setup(width=600, height=400)  # 调整屏幕尺寸
p = turtle.Turtle()

book = [{'title': '呐喊', 'donor': '张三', 'Borrowing?': 'no', 'Borrowing number': 'NH-ZS-1-001'},
        {'title': '失控', 'donor': '李四', 'Borrowing?': 'no', 'Borrowing number': 'SK-LS-1-002'},
        {'title': '天才与疯子', 'donor': '王五', 'Borrowing?': 'no', 'Borrowing number': 'TC-WW-1-003'},
        {'title': '狂人日记', 'donor': '赵六', 'Borrowing?': 'no', 'Borrowing number': 'KR-ZL-1-004'},
        {'title': '管理员书籍', 'donor': 'Admin', 'Borrowing?': 'no', 'Borrowing number': 'GL-AD-A-001'}]

# Tkinter部分
screen_2 = tk.Tk()
screen_2.title('图书管理系统')
screen_2.geometry('400x400')  # 调整 Tkinter 窗口尺寸

def draw_interface():
    p.penup()
    p.goto(-200, 150)  # 调整初始位置
    p.write('图书管理系统', font=('Arial', 18, 'bold'))
    p.goto(-200, 120)
    p.write('书名\t\t捐赠者\t\t可以借阅？\t借阅号', font=('Arial', 10, 'bold'))
    p.goto(-200, 100)
    for book1 in book:
        p.write(f"{book1['title']:20}\t"
                f"{book1['donor']:20}"
                f"{book1['Borrowing?']:25}"
                f"{book1['Borrowing number']:30}", font=('Arial', 10, 'normal'))
        p.goto(-200, p.ycor() - 20)  # 下一行位置

def borrow_book():
    title1 = entry_title.get()
    for book1 in book:
        if book1['title'] == title1:
            if book1['Borrowing?'] == 'no':
                label_result.config(text=f"成功借阅，借阅号为: {book1['Borrowing number']}")
                book1['Borrowing?'] = 'yes'  # 修改借阅状态
            else:
                label_result.config(text='该书已被借阅')
            break
    else:
        label_result.config(text='找不到该书')

def return_book():
    title1 = entry_title.get()
    numbers = entry_number.get()
    for book1 in book:
        if book1['title'] == title1:
            if book1['Borrowing?'] == 'yes' and book1['Borrowing number'] == numbers:
                label_result.config(text="成功还书，感谢您的使用")
                book1['Borrowing?'] = 'no'  # 修改借阅状态
            else:
                label_result.config(text='该书未被借阅')
            break
    else:
        label_result.config(text='找不到该书')

# 创建界面元素
label_title = tk.Label(screen_2, text="请输入书名：")
label_title.pack()

entry_title = tk.Entry(screen_2)
entry_title.pack()

label_number = tk.Label(screen_2, text="请输入借阅号：")
label_number.pack()

entry_number = tk.Entry(screen_2)
entry_number.pack()

button_borrow = tk.Button(screen_2, text="借书", command=borrow_book)
button_borrow.pack()

button_return = tk.Button(screen_2, text="还书", command=return_book)
button_return.pack()

label_result = tk.Label(screen_2, text="a")
label_result.pack()

# 在Turtle界面中显示图书信息
draw_interface()

# 启动Tkinter主循环
tk.mainloop()

# 关闭Turtle图形界面
screen.bye()
