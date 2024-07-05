import turtle , random
import tkinter as tk
import tkinter.messagebox
# Turtle部分

screen = turtle.Screen()
screen.setup(width=600, height=400)  # 调整屏幕尺寸
p = turtle.Turtle()
screen.title('图书-仓库一')
nums = random.randint(10000,70000)
book = [{'title': '呐喊', 'donor': '张三', 'Borrowing?': 'no', 'Borrowing number': 'NH-ZS-1-001'},
        {'title': '失控', 'donor': '李四', 'Borrowing?': 'no', 'Borrowing number': 'SK-LS-1-002'},
        {'title': '天才与疯子', 'donor': '王五', 'Borrowing?': 'no', 'Borrowing number': 'TC-WW-1-003'},
        {'title': '狂人日记', 'donor': '赵六', 'Borrowing?': 'no', 'Borrowing number': 'KR-ZL-1-004'},
        {'title': '管理员书籍', 'donor': 'Admin', 'Borrowing?': 'no', 'Borrowing number': 'GL-AD-A-001'}]
book1 = [{'title': '十万个为什么', 'press': '人民出版社', 'Borrowing?': 'no', 'Borrowing number': 'SW-RM-2-001'}]
# Tkinter部分
screen_2 = tk.Tk()
screen_2.title('图书管理系统')
screen_2.geometry('400x400')  # 调整 Tkinter 窗口尺寸
screen_3 = turtle.Screen()
screen_3.title('区域2')
# 添加PIN码输入框和提示标签
label_pin = tk.Label(screen_2, text='请输入管理员PIN码:')
label_pin.pack()

entry_pin = tk.Entry(screen_2, show='*')
entry_pin.pack()
p.hideturtle()

def draw_interface():
    p.penup()
    p.goto(-200, 150)  # 调整初始位置
    p.write(f"图书管理系统\t游客号{nums}", font=('Arial', 18, 'bold'))
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
    pin = entry_pin.get()

    # 验证PIN码
    if pin != '750108':
        label_result.config(text='管理员PIN码错误')
        return

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
                book1['Borrowing?'] = 'no'  # 修改借阅状态为未借阅
            else:
                label_result.config(text="借阅号错误或该书未被借阅")
            break
    else:
        label_result.config(text='找不到该书')


def exit_system():
    screen.bye()  # 关闭 Turtle 图形窗口
    screen_2.quit()  # 关闭 Tkinter 窗口
    screen_2.destroy()
draw_interface()
def Game_mods():
    Game_modifiers = tk.Tk()
    Game_modifiers.geometry('500x500')
    Game_modifiers.title('修改器')
    button_PIN = tk.Button(Game_modifiers, text='尝试请求')
    button_PIN.pack()

# 借阅界面的标题和输入框
label_title = tk.Label(screen_2, text='请输入要借阅的书名:')
label_title.pack()

entry_title = tk.Entry(screen_2)
entry_title.pack()

button_borrow = tk.Button(screen_2, text='借阅', command=borrow_book)
button_borrow.pack()

# 还书界面的输入框和按钮
label_number = tk.Label(screen_2, text='请输入要还的书名和借阅号:')
label_number.pack()

entry_number = tk.Entry(screen_2)
entry_number.pack()

button_return = tk.Button(screen_2, text='还书', command=return_book)
button_return.pack()

label_result = tk.Label(screen_2, text='')
label_result.pack()

button_exit = tk.Button(screen_2, text='退出系统', command= exit_system)
button_exit.pack()

button_game_mod = tk.Button(screen_2, text='启动修改器')

label_nums = tk.Label(screen_2, text='已下已废除（维修中，请使用修改器）')
label_nums.pack()

entry_nums = tk.Entry(screen_2)
entry_nums.pack()


def display_messagebox():
    tk.messagebox.showinfo(title='消息',
                           message=f"成功，PIN为750108,{nums}")
def on_button_press(event):
    if event.widget["state"] != "active":
        if entry_nums == nums:
            tk.Button(screen_2,text='OK', command=display_messagebox())
    else:
        tk.Button(screen_2,text='OK', command=display_messagebox())

# 创建一个按钮

# 绑定按钮的 <Button-1> 事件（默认为左键点击）

screen_2.mainloop()
'''
备份
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
                break
    else:
        label_result.config(text='找不到匹配的书籍或借阅号错误')

def exit_system():
    screen.bye()  # 关闭 Turtle 图形窗口
    screen_2.quit()  # 关闭 Tkinter 窗口
    screen_2.destroy()

# 添加界面元素
draw_interface()

# 添加借阅和还书的输入框和按钮
label_title = tk.Label(screen_2, text='请输入书名:')
label_title.pack()
entry_title = tk.Entry(screen_2)
entry_title.pack()

label_number = tk.Label(screen_2, text='请输入借阅号:')
label_number.pack()
entry_number = tk.Entry(screen_2)
entry_number.pack()

button_borrow = tk.Button(screen_2, text='借阅书籍', command=borrow_book)
button_borrow.pack()

button_return = tk.Button(screen_2, text='还书', command=return_book)
button_return.pack()

label_result = tk.Label(screen_2, text='')
label_result.pack()

button_exit = tk.Button(screen_2, text='退出系统', command=exit_system)
button_exit.pack()

screen.mainloop()  # 启动 Turtle 图形窗口的主事件循环

'''
'''
def display_messagebox():
    tk.messagebox.showinfo(title='消息',
                           message='成功，PIN为750108')
                           
'''
