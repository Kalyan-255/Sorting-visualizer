import pygame as pg
import random
import time
import sys
pg.init()
sys.setrecursionlimit(1000000)
#global swap_count
swap_count=0
def bubble_sort():
    for i in range(len(a)-1):
        for j in range(0, len(a)-i-1):
            if (a[j] > a[j+1]):
                swap(j, j+1)
            show()


def selection_sort():
    for i in range(len(a)-1):
        m = i
        for j in range(i+1, len(a)):
            reset_col()
            if (a[m] > a[j]):
                m = j
            high_col(m)
            high_col(j)
            show()
        swap(i, m)


def merge_sort(l, r):
    if l < r:
        m = (l+r)//2
        merge_sort(l, m)
        merge_sort(m+1, r)
        merge(l, m, r)


def merge(l, m, r):
    reset_col()
    a1 = a[l:m+1]
    a2 = a[m+1:r+1]
    i, j, n1, n2 = 0, 0, len(a1), len(a2)
    c = l
    while i < n1 and j < n2:
        if a1[i] <= a2[j]:
            a[c] = a1[i]
            c, i, = c+1, i+1
        else:
            a[c] = a2[j]
            c, j, = c+1, j+1
        high_col(i)
        high_col(j)
        high_col(c)
        show()
        reset_col()
    while i < n1:
        a[c] = a1[i]
        c, i, = c+1, i+1
        high_col(i)
        show()
    while j < n2:
        a[c] = a2[j]
        c, j, = c+1, j+1
        high_col(j)
        show()


def heap_sort():
    for i in range(size//2-1, -1, -1):
        heapify(size, i)
    for j in range(size-1, 0, -1):
        reset_col()
        swap(0, j)
        show()
        heapify(j, 0)


def heapify(n, i):
    l = 2*i+1
    r = 2*i+2
    m = i
    if l < n and a[l] > a[m]:
        m = l
    if r < n and a[r] > a[m]:
        m = r
    if m != i:
        swap(m, i)
        show()
        heapify(n, m)


def swap(i, j):
    reset_col()
    t = a[i]
    a[i] = a[j]
    a[j] = t
    high_col(i)
    high_col(j)
    global swap_count
    swap_count += 1


def quick_sort(l, r):
    if l < r:
        q = quick(l, r)
        draw_sor()
        quick_sort(l, q-1)
        quick_sort(q+1, r)


def quick(l, r):
    pivot = a[r]
    i = l-1
    for k in range(l, r):
        show()
        if a[k] < pivot:
            i += 1
            swap(i, k)
    swap(i+1, r)
    return i+1


def reset_col():
    for i in range(len(a)):
        col_arr[i] = (255, 0, 0)


def high_col(i):
    col_arr[i] = (0, 255, 0)


def draw_sor():
    for i in range(len(a)):
        pg.draw.rect(dis, color_green, (i*width//len(a),
                                        10, width//(2*len(a)), 10*a[i]))


class button:
    def __init__(self, x, y, h, w, col, text, f_size):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.col = col
        self.text = text
        self.f_size = f_size

    def draw(self, dis):
        pg.draw.rect(dis, self.col, (self.x, self.y, self.h, self.w))
        if self.f_size == 1:
            text = font_small.render(self.text, 0, (0, 0, 0))
        else:
            text = font_big.render(self.text, 0, (0, 0, 0))
        dis.blit(text, (self.x-30+self.h//2, self.y+self.w//2))

    def over(self, pos):
        if pos[0] > self.x and pos[1] > self.y and pos[0] < self.h+self.x and pos[1] < self.w+self.y:
            self.col = (0, 255, 0)
            return 1
        else:
            self.col = (255, 0, 0)
            return 0


def show():
    dis.fill((255, 255, 255))
    for i in range(len(a)):
        pg.draw.rect(dis, col_arr[i], (i*width//len(a),
                                       10, width//(2*len(a)), 10*a[i]))
    text = font_big.render(
        "Time : "+str(round((time.time()-start), 3)), 0, (0, 0, 0))
    t1 = font_big.render("Swaps : "+str(swap_count), 0, (0, 0, 0))
    dis.blit(text, (width-400, height-20))
    dis.blit(t1, (width-200, height-20))
    #pg.time.delay(4)
    pg.display.update()


def rep_draw():
    b.draw(dis)
    b.over(pos)
    s.draw(dis)
    s.over(pos)
    m.draw(dis)
    m.over(pos)
    q.draw(dis)
    q.over(pos)
    h.draw(dis)
    h.over(pos)
    s1.draw(dis)
    s1.over(pos)
    s2.draw(dis)
    s2.over(pos)
    s3.draw(dis)
    s3.over(pos)
    s4.draw(dis)
    s4.over(pos)


font_big = pg.font.SysFont('', 30, True)
font_small = pg.font.SysFont('', 15, True)
width = 1000
height = 600
col = (255, 0, 0)
color_dark_blue = (0, 0, 30)
color_blue = (75, 122, 230)
color_light_blue = (105, 152, 255)
color_green = (75, 229, 137)
color_red = (229, 42, 60)
color_purple = (200, 0, 200)
a = []
col_arr = []
sorted_val = []
dis = pg.display.set_mode((width, height))
pg.display.set_caption("sort")
b = button(100, 10, width-20, 100, (255, 0, 0), "Bubble Sort", 2)
s = button(100, 120, width-20, 100, (255, 0, 0), "Selection Sort", 2)
m = button(100, 230, width-20, 100, (255, 0, 0), "Merge Sort", 2)
q = button(100, 340, width-20, 100, (255, 0, 0), "Quick Sort", 2)
h = button(100, 450, width-20, 100, (255, 0, 0), "Heap Sort", 2)
s1 = button(10, 10, 80, 50, color_purple, "Size:50", 1)
s2 = button(10, 70, 80, 50, color_purple, "Size:100", 1)
s3 = button(10, 130, 80, 50, color_purple, "Size:150", 1)
s4 = button(10, 190, 80, 50, color_purple, "Size:200", 1)
run = True
f = 0
size = 50
start = 0
while run:
    for event in pg.event.get():
        pos = pg.mouse.get_pos()
        if (event.type == pg.QUIT):
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_r:
                f,swap_count = 0,0
                a.clear()
                dis.fill((255, 255, 255))
        if f == 0:
            rep_draw()
        if pg.mouse.get_pressed()[0]:
            f = 1
            if s1.over(pos):
                size = 50
            elif s2.over(pos):
                size = 100
            elif s3.over(pos):
                size = 150
            elif s4.over(pos):
                size = 200
            else:
                for i in range(size):
                    a.append(random.randint(1, 40))
                for i in range(len(a)):
                    k = (255, 0, 0)
                    col_arr.append(k)
            if b.over(pos):
                start = time.time()
                bubble_sort()
                reset_col()
                draw_sor()
            elif s.over(pos):
                start = time.time()
                selection_sort()
                reset_col()
                draw_sor()
            elif m.over(pos):
                start = time.time()
                merge_sort(0, len(a)-1)
                reset_col()
                draw_sor()
            elif q.over(pos):
                start = time.time()
                quick_sort(0, len(a)-1)
                reset_col()
                draw_sor()
            elif h.over(pos):
                start = time.time()
                heap_sort()
                draw_sor()
        pg.display.update()
pg.quit()
