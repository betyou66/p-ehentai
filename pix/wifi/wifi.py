interface = self.wifi.interfaces()[0]    #使用索引序号0获取第一个无线网卡
interface.scan()
print('扫描WiFi中，请稍后………………')
time.sleep(1)
print('扫描完成！\n' + '*' * 50)
print('\n%s\t%s\t%s' % ('WiFi编号', 'WiFi信号', 'WiFi名称'))
wifiList = interface.scan_results()    #返回一个列表

wifiNewList = []
for w in wifiList:
    wifiNameAndSignal = (100 + w.signal, w.ssid.encode('raw_unicode_escape').decode('utf-8'))   #解决乱码问题并返回元组
    wifiNewList.append(wifiNameAndSignal)

wifi_signal_and_name_list = sorted(wifiNewList, key=lambda i: i[0], reverse=True)    # 按信号强度倒序

index = 0
while index < len(wifi_signal_and_name_list):
    print('%s\t\t\t%s\t\t\t%s' % (index, wifi_signal_and_name_list[index][0], wifi_signal_and_name_list[index][1]))
    index += 1
print('\n' + '*' * 50)