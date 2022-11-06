import streamlit as st

def getAllbookstore():
	import requests
	url = 'https://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapJson&typeId=M' # 在這裡輸入目標 url
	headers = {"accept": "application/json"}
	response = requests.get(url, headers=headers)
	res = response.json()
	return res

def getCityOption(items):
	optionList = []
	for item in items:
		name = item['cityName'][0:3]
		if name not in optionList:
			optionList.append(name)
	return optionList

def getSpecificBookstore(items, city):
	specificBookstoreList =[]
	for item in items:
		name = item['cityName'][0:3]
		if city in name:
			specificBookstoreList.append(item)
		else:
			continue
	return specificBookstoreList

def getBookstoreInfo(items):
	expanderList = []
	for item in items:
		expander = st.expander(item['name'])
		expander.image(item['representImage'])
		expander.metric('hitRate', item['hitRate'])
		expander.subheader('Introduction')
		expander.write(item['intro'])
		expander.subheader('Open Time')
		expander.write(item['openTime'])
		expander.subheader('Email')
		expander.write(item['email'])
		expanderList.append(expander)
	return expanderList

def app():
  bookstoreList = getAllbookstore()# 呼叫 getAllBookstore 函式並將其賦值給變數 bookstoreList
  cityOption = getCityOption(bookstoreList)

  st.header('特色書店地圖')
  st.metric('Total bookstore',  len(bookstoreList)) # 將 118 替換成書店的數量
  city = st.selectbox('請選擇縣市', cityOption)
  specificBookstore = getSpecificBookstore(bookstoreList, city)
  num = len(specificBookstore)
  st.write(f'總共有{num}項結果', num)
  bookstoreInfo = getBookstoreInfo(specificBookstore)

if __name__ == '__main__':
	app()