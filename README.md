# 麥塊轉蛋系統

## 簡介
+ 這是一個非插件也非模組的轉蛋系統，主要透過 Command Pipeline 的技巧建立而成，所以可以架設在無論是官方伺服器、SpigotMC 或 PaperMC 上
+ 預設會消耗玩家一顆綠寶石進行單抽，或者一個綠寶石磚進行十抽

## 系統需求
+ Ubuntu 20.04
    + 其他版本的 Linux 應該也適用
+ Python 3.6+

## 使用方法
+ 將執行伺服器的指令修改成 Pipeline 的形式
    ```
    tail -f /path/to/inn | java -jar server.jar | tee /path/to/out
    ```
+ 此時透過對 `/path/to/inn` 寫入指令字串就可以達到外部指令的效果
+ 而外部程式則可以透過讀取 `/path/to/out` 來做出反應
+ 將 `run.sh.template` 重新命名為 `run.sh`
+ 修改 `run.sh` 裡的 `OUT_PATH` 與 `INN_PATH` 並執行 `bash run.sh`
+ 透過修改 `rewards.json` 來建立自訂獎勵表
    + 推薦使用 [Give Command Generator](https://tinyurl.com/yzqjpef7) 或 [Potions Generator](https://tinyurl.com/yhtd9ly2)
+ 指令方塊的設定：
    + 單抽指令方塊組合：
        + 脈衝、無條件、需要紅石
            + `clear @p minecraft:emerald 0`
        + 連鎖、有條件、需要紅石
            + `say @p 戳了一下歐派!`
    + 十抽指令方塊組合：
        + 脈衝、無條件、需要紅石
            + `clear @p minecraft:emerald_block 0`
        + 連鎖、有條件、需要紅石
            + `say @p 戳了十下歐派!`

## 免費十抽
+ 設定記分板 `free` 跟 `one`
    + `/scoreboard objectives add free dummy`
    + `/scoreboard objectives add one dummy`
+ 設定一個 1 在 one 給任意使用者
    + `/scoreboard players set DemoUser one 1`
+ 將 `free.sh.template` 重新命名為 `free.sh`
+ 修改 `free.sh` 的內容，請務必使用絕對路徑
+ 使用 `crontab` 設定定時發送免費十抽給在線上的成員
    + `crontab -e` 開啟設定介面
    + 新增一行 `0,20,40 * * * * bash /path/to/free.sh`
        + 這樣會在每個小時的 20 分、40 分與整點的時候發送免費十抽
+ 指令方塊的設定：
    + 脈衝、無條件、需要紅石
        + `execute if score @p free matches 1.. run scoreboard players operation @p free -= DemoUser one`
    + 連鎖、有條件、需要紅石
        + `give @p minecraft:emerald_block`
    + 連鎖、有條件、需要紅石
        + `say @p 領取了免費十連抽!`

## 其他程式
+ `gen.py` 將複雜的 Give 指令轉成 JSON 格式
    + 修改 `name` 與 `item` 變數並執行
+ `format.py` 將 `rewards.json` 進行美化編排
