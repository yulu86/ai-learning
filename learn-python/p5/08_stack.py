browsing_session = []

def forward(page):
    browsing_session.append(page)
    print("Now", browsing_session)

def backward():
    last = browsing_session.pop()
    print("now", last, browsing_session)
    # 判断列表为空
    if not browsing_session:
      print("Disabled")
    else:
      print("rediect", browsing_session[-1])

forward(1)
forward(2)
forward(3)

backward()
backward()
backward()
