###### tags: `Security Research`

# LiSa

## 基本介紹
- 前端
    - React native
- 後端
    - nginx
    - flask
    - mariadb
    - rabbitmq
輸出結果為一包 json 檔，在利用react jsx 來做渲染

## API

### upload file
/api/tasks/create/file
- Parameters:
- POST
    - file
    - pretty
- Return
`{'task_id': '9f8a6d07-2634-480f-9290-f6f6748ce4f6'}`


### List tasks
/api/tasks/`{finished | failed | pending}`
- GET
- Return
```
[
  {
    "date_done": "Wed, 10 Apr 2019 09:58:27 GMT",
    "status": "SUCCESS",
    "task_id": "8fd49755-fe4b-4ca1-b1a1-046676475d33",
    "result": {
      "filename": "malware.bin"
    }
  }
]
```
### Check task status
/api/tasks/view/`<task id>`
- GET
- Returns `SUCCESS | None`
```
{
  "status": "SUCCESS"
}
```

### Get report
/api/report/<task_id>
/api/pcap/<task_id>
/api/machinelog/<task_id>
/api/output/<task_id>
/api/https/<task_id>


## 檔案文件
- data: 放置靜態文件
    - blacklists
    - db
    - geolite2databases
    - storage: 存放所有樣本分析結果
- docker
    - api: 叫起 uwsgi container
    - nginx: 叫起 nginx container，負責處理前端網頁
    - tests: 測試用
    - worker: 叫起 worker container 負責後端處理，包含sandbox, flask API
- lisa
    - analysis: 檔案上傳後，執行的各種分析(動態分析、靜態分析、封包分析)
    - anti_anti_debug: 針對 mips 架構的 anti-ptrace 做修補
    - core: 分析時用到的工具
    - web_api: API 接口
- stap
    - 用來 hook system call
- tests
    - 用來做 unitest
- web_frontend
    - 前端頁面配置

## 修改部分

1. 更改 x86_64 images
    - 位置: lisa/images
    - 放置新版 wget 
2. 前端修改
    - 1: web_frontend/src/components/ReportNetwork.jsx
        - 新增下載 HTTPS 記錄檔按鈕
    - 2: web_frontend/src/components/ReportOverview.jsx
        - 新增 HTTPS 和 TCP 紀錄
    - 3: web_api/routes.py
        - 下載 HTTPS 記錄檔 API
3. 後端初始化設定
    - docker/worker/Dockerfile
        - 新增 iptables 和 mitmproxy
    - docker/worker/init.sh
        - 執行 iptable 規則
        - 開啟 mitmproxy
        - 下載設定 mitmproxy 憑證
4. 後端分析設定
    - lisa/core/qemu_guest.py
        - run_and_analyze: 將 /tmp/http_traffic 清空
        - extract_output: 將 /tmp/http_traffic 複製到 storage
    - lisa/analysis/network_analysis.py
        - 新增 analyze_https function 讀取 https 記錄檔，並寫進報告中
        - 修改 analyze_pcap function 將 TCP 連線資訊寫進報告中
    
