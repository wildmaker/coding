# 居中打印字符串

# print "hello"

def display_text_in_box(SCREEN_WIDTH = 800,PADDING = 2):
    text = input("Enter your text:\n")
    box_length = (len(text)+PADDING*2 + 2)
    margin_left =(SCREEN_WIDTH-box_length)//2
    print(' '*margin_left + '*'*box_length)
    print(' '*margin_left + '*' + ' '*PADDING + text + ' '*PADDING + '*')
    print(' '*margin_left + '*'*box_length)

# print "hello"
