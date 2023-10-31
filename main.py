import time
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import tkinter as tk
import tkinter.ttk
import threading
import pyautogui
import sys
import pickle
import re





# Get webdriver
co = Options()
#새 창을 열어 크롬드라이버를 실행하지 않고, 디버거모드크롬에 엑세스해서 미리 켜져있는 크롬창으로 프로세스 진행.
co.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
driver = webdriver.Chrome(options=co)
driver.implicitly_wait(5)

# 매개변수로 url을 받고, current_url값이 전달인자url이랑 일치할 시 해당 탭으로 switch하는 함수.
# 켜져 있는 여러 탭중에서 특정 탭으로 switch할 때 사용.
def currentUrl(url):
    for window in driver.window_handles:
        driver.switch_to.window(window)
        time.sleep(1)
        if driver.current_url == url:
            driver.switch_to.window(window)
            break

def currentUrl_test(url):
    for window in driver.window_handles:
        driver.switch_to.window(window)
        time.sleep(1)

        if driver.current_url == url:
            driver.switch_to.window(window)
            break


#########################################################################################

# 프로그램 종료할 때, 프로토콜로 실행되는 함수
# GUI에 입력된 모든 인풋값을 values.pickle 파일에 저장 후 exit.
def save_values():
    values = {
        'center1': center_input.get(),
        'landing1': landing_input.get(),
        'centerTime1': centerTime_input.get(),
        'landingTime1': landingTime_input.get(),
        'centerSwitchTime1': centerSwitchTime_input.get(),
        'center2': center_input2.get(),
        'landing2': landing_input2.get(),
        'centerTime2': centerTime_input2.get(),
        'landingTime2': landingTime_input2.get(),
        'centerSwitchTime2': centerSwitchTime_input2.get()
    }
    with open("values.pickle", "wb") as file:
        pickle.dump(values, file)

    time.sleep(1)
    sys.exit()

# 위 save_values 함수를 통해 values.pickle 파일에 저장된 데이터를 가져와서 인풋값에 다시 띄우는 load 함수
def load_values():
    try:
        with open("values.pickle", "rb") as file:
            values = pickle.load(file)
            center_input.delete(0, 'end')
            center_input.insert('end', values['center1'])
            landing_input.delete(0, 'end')
            landing_input.insert('end', values['landing1'])
            centerTime_input.delete(0, 'end')
            centerTime_input.insert('end', values['centerTime1'])
            landingTime_input.delete(0, 'end')
            landingTime_input.insert('end', values['landingTime1'])
            centerSwitchTime_input.delete(0, 'end')
            centerSwitchTime_input.insert('end', values['centerSwitchTime1'])
            center_input2.delete(0, 'end')
            center_input2.insert('end', values['center2'])
            landing_input2.delete(0, 'end')
            landing_input2.insert('end', values['landing2'])
            centerTime_input2.delete(0, 'end')
            centerTime_input2.insert('end', values['centerTime2'])
            landingTime_input2.delete(0, 'end')
            landingTime_input2.insert('end', values['landingTime2'])
            centerSwitchTime_input2.delete(0, 'end')
            centerSwitchTime_input2.insert('end', values['centerSwitchTime2'])
    # 초기실행 상황과 같이 데이터값이 없는 경우에는 load 없이 pass
    except FileNotFoundError:
        pass

#########################################################################
#아래 세 함수(instaPopUp, firstAlertPopUp, secondAlertPopUp)는 팝업 관리를 위함.
#멀티쓰레드로 각기 실행됨.
def instaPopUp():
    while True:
        try:
            # pyautogui 이미지 서칭을 활용하여 뜨는 무작위하게 발생하는 팝업창을 수시로 제거.
            elm = pyautogui.locateOnScreen('Img/1.png', grayscale=True, confidence=.8)
            if elm is not None:
                time.sleep(0.2)
                pyautogui.click(elm)
        except Exception as e:
            time.sleep(1)
            print(f"An error occurred: {str(e)}")

def firstAlertPopUp():
    while True:
        try:
            elm = pyautogui.locateOnScreen('Img/2.png', grayscale=True, confidence=.8)
            if elm is not None:
                time.sleep(0.5)
                pyautogui.click(elm)
        except Exception as e:
            time.sleep(1)
            print(f"An error occurred: {str(e)}")

def secondAlertPopUp():
    while True:
        try:
            elm = pyautogui.locateOnScreen('Img/3.png', grayscale=True, confidence=.8)
            if elm is not None:
                time.sleep(0.6)
                pyautogui.click(elm)
        except Exception as e:
            time.sleep(1)
            print(f"An error occurred: {str(e)}")


#######################################################################
# GUI 인풋에 입력된 값을 프로그램 실행 초기에 모두 글로벌화해서 모든 함수에서 접근 가능하게 선언하는 함수.
def initial():
    #초기 입력값 세팅
    global center1
    global center1_chachacha
    global center1_term
    global center1_cha_term
    global center1_switch_term

    global center2
    global center2_chachacha
    global center2_term
    global center2_cha_term
    global center2_switch_term

    global center_list

    center1 = center_input.get()
    center1_chachacha = landing_input.get()
    center1_term = int(centerTime_input.get())
    center1_cha_term = int(landingTime_input.get())
    center1_switch_term = int(centerSwitchTime_input.get())

    center2 = center_input2.get()
    center2_chachacha = landing_input2.get()
    center2_term = int(centerTime_input2.get())
    center2_cha_term = int(landingTime_input2.get())
    center2_switch_term = int(centerSwitchTime_input2.get())

    center_list = [center1, center2]

    #센터 두 개 다 리프레쉬 후 시작
    currentUrl(center_list[1])
    driver.maximize_window()
    time.sleep(1)
    driver.refresh()
    time.sleep(1)
    currentUrl(center_list[0])
    driver.refresh()
    time.sleep(5)

    mainLoop(center1, center1_chachacha, center1_term, center1_cha_term)




################################################################################
#센터 활성화(포커싱) 변경
def centerSwitch():
    #현재 센터 이닛하기
    driver.refresh()
    time.sleep(5)

    #다른 센터로 넘어가기
    global another
    for c in center_list:
        if c != driver.current_url:
            another = c

    # 센터변경텀 / 센터변경 / 메인룹 실행
    if another == center1:
        time.sleep(center1_switch_term)
        currentUrl(another)
        mainLoop(center1, center1_chachacha, center1_term, center1_cha_term)
    else:
        time.sleep(center2_switch_term)
        currentUrl(another)
        mainLoop(center2, center2_chachacha, center2_term, center2_cha_term)


    time.sleep(1)

##############################################################################

#메인룹
def mainLoop(center, chachacha, term, term2):
    progressbar.start(10)

    # 읽지 않음 클릭
    notRead_btn = driver.find_element(By.XPATH, "//*[contains(text(),'읽지 않음')]")
    driver.execute_script("arguments[0].click()", notRead_btn)
    time.sleep(term)

    # 추가된 날짜 리버스
    reverse_date = driver.find_element(By.XPATH, "//*[contains(text(),'추가된 날짜')]")
    driver.execute_script("arguments[0].click()", reverse_date)
    time.sleep(term)

    while True:
        blues = driver.find_elements(By.CLASS_NAME, '_893a')
        if len(blues) > 0:
            blues[0].click()
            time.sleep(term)

            # 고객정보 긁어 오기
            carType = driver.find_element(By.XPATH, "//*[contains(text(),'원하는 차종')]")
            car = carType.find_element(By.XPATH, '../div/div').text
            phone = carType.find_element(By.XPATH, '../../div[2]/div[2]/div').text
            re_phone = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z\s]", "", phone)
            time.sleep(term)

            # 등록 사이트 포커싱
            currentUrl_test(chachacha)
            time.sleep(2)

            # 등록 사이트 프로세스
            car_input = driver.find_element(By.XPATH, '//*[@id="speed_wrap"]/dl/dd[1]/input')
            car_input.send_keys(car)
            time.sleep(1)
            phone_input = driver.find_element(By.XPATH, '//*[@id="phone_num"]')
            phone_input.send_keys(re_phone)
            time.sleep(1)

            #프롬프트에 정보 띄우기 및 써밋
            print(f'차종: {car}\n'
                  f'전화번호: {phone}\n'
                  )
            phone_input.submit()
            time.sleep(term2)

            # 확인하기
            alert = driver.switch_to.alert
            alert.accept()
            time.sleep(1)

            #다시 센터 포커싱
            currentUrl(center)
            time.sleep(2)

            #센터 스위칭하기
            centerSwitch()


        else:
            yellows = driver.find_elements(By.CLASS_NAME, '_3b62')
            yellows_amount = len(yellows)
            if yellows_amount > 0:
                # 다음 페이지
                next_page = driver.find_element(By.XPATH, "//*[contains(text(),'다음')]")
                driver.execute_script("arguments[0].click()", next_page)
                time.sleep(term)

                yellows = driver.find_elements(By.CLASS_NAME, '_3b62')
                yellows_amount_check = len(yellows)
                if yellows_amount == yellows_amount_check and yellows_amount_check != 20:
                    # 센터 스위칭하기
                    centerSwitch()
            else:
                # 센터 스위칭하기
                centerSwitch()

########################################################################################

def mainThread():
    # 초기세팅 후에 mainLoop 실행
    t2 = threading.Thread(target=initial)
    t2.start()

    # 인스타 팝업 돌리기
    t3 = threading.Thread(target=instaPopUp)
    t3.start()

    # 1차경고무시 돌리기
    if CheckVar1.get() == 1:
        t4 = threading.Thread(target=firstAlertPopUp)
        t4.start()

    # 2차경고무시 돌리기
    if CheckVar2.get() == 1:
        t5 = threading.Thread(target=secondAlertPopUp)
        t5.start()




t1 = threading.Thread(target=mainThread)



##########################################################################################
#tkinter setting

#tkinter 활용해서 프로그램 GUI 만드는 코드
root = tk.Tk()
root.title('오토비즈니스')

frame1 = tk.Label(root)
frame1.pack(side='top')

frame2 = tk.Label(root)
frame2.pack(side='top', pady=(20, 0))

frame3 = tk.Label(root)
frame3.pack(side='top', pady=(20, 0))


# start stop 버튼 메인 쓰레드 실행
btn1 = tk.Button(frame3, text='Start', command=t1.start)
btn1.pack(pady=(20, 0), side='left')

# btn2 = tk.Button(frame3, text='Stop', command=t1.raise_exception)
# btn2.pack(pady=(20, 0), padx=(20,0) ,side='left')


CheckVar1= tk.IntVar()
CheckVar2= tk.IntVar()

c1 =tk.Checkbutton(root,text="1차경고무시",variable=CheckVar1)
c2 =tk.Checkbutton(root,text="2차경고무시",variable=CheckVar2)

c2.pack(side='right')
c1.pack(side='right')



frame1_frame1 = tk.Label(frame1)
frame1_frame1.pack(side='left')

frame1_frame2 = tk.Label(frame1)
frame1_frame2.pack(side='left', padx=(10, 0))

frame1_frame3 = tk.Label(frame1)
frame1_frame3.pack(side='left', padx=(20, 0))

frame1_frame4 = tk.Label(frame1)
frame1_frame4.pack(side='left', padx=(20, 0))

frame1_frame5 = tk.Label(frame1)
frame1_frame5.pack(side='left', padx=(20, 0))

frame1_frame6 = tk.Label(frame1)
frame1_frame6.pack(side='left', padx=(20, 0))

frame2_frame1 = tk.Label(frame2)
frame2_frame1.pack(side='left')

frame2_frame2 = tk.Label(frame2)
frame2_frame2.pack(side='left', padx=(10, 0))

frame2_frame3 = tk.Label(frame2)
frame2_frame3.pack(side='left', padx=(20, 0))

frame2_frame4 = tk.Label(frame2)
frame2_frame4.pack(side='left', padx=(20, 0))

frame2_frame5 = tk.Label(frame2)
frame2_frame5.pack(side='left', padx=(20, 0))

frame2_frame6 = tk.Label(frame2)
frame2_frame6.pack(side='left', padx=(20, 0))





number = tk.Button(frame1_frame1, text="1", background='#c6c6c6')
number.pack(pady=(20, 0), )

center_text = tk.Label(frame1_frame2, text="잠재고객센터URL")
center_text.pack(side='top')

center_input = tk.Entry(frame1_frame2, justify='center')
center_input.pack(side='top')

landing_text = tk.Label(frame1_frame3, text="랜딩페이지URL")
landing_text.pack(side='top')

landing_input = tk.Entry(frame1_frame3, justify='center')
landing_input.pack(side='top')

centerTime_text = tk.Label(frame1_frame4, text="잠재고객센터 시간(초)")
centerTime_text.pack(side='top')

centerTime_input = tk.Entry(frame1_frame4, justify='center')
centerTime_input.pack(side='top')

landingTime_text = tk.Label(frame1_frame5, text="랜딩페이지 시간(초)")
landingTime_text.pack(side='top')

landingTime_input = tk.Entry(frame1_frame5, justify='center')
landingTime_input.pack(side='top')

centerSwitchTime_text = tk.Label(frame1_frame6, text="센터변경 시간(초)")
centerSwitchTime_text.pack(side='top')

centerSwitchTime_input = tk.Entry(frame1_frame6, justify='center')
centerSwitchTime_input.pack(side='top')





number = tk.Button(frame2_frame1, text="2", background='#c6c6c6')
number.pack(pady=(20, 0), )

center_text2 = tk.Label(frame2_frame2, text="잠재고객센터URL")
center_text2.pack(side='top')

center_input2 = tk.Entry(frame2_frame2, justify='center')
center_input2.pack(side='top')

landing_text2 = tk.Label(frame2_frame3, text="랜딩페이지URL")
landing_text2.pack(side='top')

landing_input2 = tk.Entry(frame2_frame3, justify='center')
landing_input2.pack(side='top')

centerTime_text2 = tk.Label(frame2_frame4, text="잠재고객센터 시간(초)")
centerTime_text2.pack(side='top')

centerTime_input2 = tk.Entry(frame2_frame4, justify='center')
centerTime_input2.pack(side='top')

landingTime_text2 = tk.Label(frame2_frame5, text="랜딩페이지 시간(초)")
landingTime_text2.pack(side='top')

landingTime_input2 = tk.Entry(frame2_frame5, justify='center')
landingTime_input2.pack(side='top')

centerSwitchTime_text2 = tk.Label(frame2_frame6, text="센터변경 시간(초)")
centerSwitchTime_text2.pack(side='top')

centerSwitchTime_input2 = tk.Entry(frame2_frame6, justify='center')
centerSwitchTime_input2.pack(side='top')


progressbar = tkinter.ttk.Progressbar(root, maximum=100, mode="indeterminate")
progressbar.pack(padx=(190,0), pady=(10,0))

# 벨류 로딩 및 끌 때 저장
load_values()
root.protocol("WM_DELETE_WINDOW", save_values)
root.mainloop()




